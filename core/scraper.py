import requests
import time
from bs4 import BeautifulSoup
from core.mealie_client import MealieClient
from core.tandoor_client import TandoorClient


class RecipeScraper:
    """Recipe scraper that can be controlled and monitored"""

    def __init__(self, config: dict, site_list: list):
        """
        Initialize scraper with configuration and site list

        Args:
            config: Configuration dictionary
            site_list: List of site URLs to scrape
        """
        self.config = config
        self.site_list = site_list
        self.running = False

        # Progress tracking
        self.status = {
            "running": False,
            "progress": 0,
            "current_site": "",
            "total_imported": 0,
            "sites_completed": 0,
            "sites_total": len(site_list)
        }

        # HTTP headers
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

        # Initialize API clients
        self.mealie_client = None
        self.tandoor_client = None

        if self.config['mealie']['enabled']:
            self.mealie_client = MealieClient(
                self.config['mealie']['url'],
                self.config['mealie']['api_token']
            )

        if self.config['tandoor']['enabled']:
            self.tandoor_client = TandoorClient(
                self.config['tandoor']['url'],
                self.config['tandoor']['api_key']
            )

    def get_status(self) -> dict:
        """Get current scraper status"""
        return self.status.copy()

    def stop(self):
        """Stop the scraper gracefully"""
        print("[Scraper] Stop requested")
        self.running = False
        self.status["running"] = False

    def find_sitemap(self, base_url: str) -> str:
        """
        Find sitemap for a website

        Args:
            base_url: Base URL of the website

        Returns:
            Sitemap URL or None if not found
        """
        candidates = [
            f"{base_url}/post-sitemap.xml",
            f"{base_url}/sitemap_index.xml",
            f"{base_url}/sitemap.xml",
            f"{base_url}/sitemap_posts.xml",
        ]

        for url in candidates:
            try:
                r = requests.head(url, headers=self.headers, timeout=5)
                if r.status_code == 200:
                    return url
            except:
                pass

        return None

    def verify_is_recipe(self, url: str) -> bool:
        """
        Verify if a URL contains a recipe

        Args:
            url: URL to check

        Returns:
            True if URL contains a recipe, False otherwise
        """
        try:
            r = requests.get(url, headers=self.headers, timeout=10)
            if r.status_code != 200:
                return False

            # Check for Recipe schema
            if '"@type":"Recipe"' in r.text or '"@type": "Recipe"' in r.text:
                return True

            # Check for common recipe plugins
            soup = BeautifulSoup(r.content, "html.parser")
            if soup.find(
                class_=lambda x: x
                and (
                    "wp-recipe-maker" in x
                    or "tasty-recipes" in x
                    or "mv-create-card" in x
                )
            ):
                return True

            return False
        except:
            return False

    def parse_sitemap(self, sitemap_url: str, ignore_set: set) -> list:
        """
        Parse sitemap and return list of candidate URLs

        Args:
            sitemap_url: URL of the sitemap
            ignore_set: Set of URLs to ignore

        Returns:
            List of candidate URLs
        """
        print(f"   [Sitemap] Parsing: {sitemap_url}")
        new_candidates = []
        scan_depth = self.config['scraper']['scan_depth']

        try:
            r = requests.get(sitemap_url, headers=self.headers, timeout=15)
            soup = BeautifulSoup(r.content, "lxml-xml")

            # Handle Index Sitemaps (sitemaps inside sitemaps)
            if soup.find("sitemap"):
                for sm in soup.find_all("sitemap"):
                    loc = sm.find("loc").text
                    if len(new_candidates) >= scan_depth:
                        break
                    if "post" in loc:
                        new_candidates.extend(self.parse_sitemap(loc, ignore_set))

                # Fallback if no posts found but nested sitemaps exist
                if not new_candidates and soup.find("sitemap"):
                    return self.parse_sitemap(soup.find("sitemap").find("loc").text, ignore_set)

            # Handle Actual URLs
            for u in soup.find_all("url"):
                if len(new_candidates) >= scan_depth:
                    break
                loc = u.find("loc").text

                # Skip non-recipe pages
                if any(
                    x in loc
                    for x in [
                        "/about",
                        "/contact",
                        "/shop",
                        "/privacy",
                        "login",
                        "cart",
                        "roundup",
                    ]
                ):
                    continue

                # If URL is NOT in our ignore list
                if loc not in ignore_set:
                    new_candidates.append(loc)

        except Exception as e:
            print(f"   [Error] Parsing sitemap: {e}")

        return list(set(new_candidates))

    def run_scrape(self):
        """Main scraping logic"""
        self.running = True
        self.status["running"] = True
        self.status["total_imported"] = 0
        self.status["sites_completed"] = 0

        print(f"[Scraper] Starting: {len(self.site_list)} sites")
        print(f"[Scraper] Target: {self.config['scraper']['target_recipes_per_site']} recipes/site")
        print(f"[Scraper] Scan depth: {self.config['scraper']['scan_depth']}")
        print("-" * 60)

        # Load existing recipe URLs from enabled services
        existing_mealie = set()
        existing_tandoor = set()

        if self.mealie_client:
            existing_mealie = self.mealie_client.get_existing_urls()

        if self.tandoor_client:
            existing_tandoor = self.tandoor_client.get_existing_urls()

        # Combined existing URLs for initial filtering
        combined_existing = set()
        if self.config['mealie']['enabled'] and self.config['tandoor']['enabled']:
            combined_existing = existing_mealie.intersection(existing_tandoor)
        elif self.config['mealie']['enabled']:
            combined_existing = existing_mealie
        elif self.config['tandoor']['enabled']:
            combined_existing = existing_tandoor

        # Process each site
        for site_idx, site in enumerate(self.site_list):
            if not self.running:
                print("[Scraper] Stopped by user")
                break

            self.status["current_site"] = site
            self.status["progress"] = int((site_idx / len(self.site_list)) * 100)

            print(f"\n[Site {site_idx + 1}/{len(self.site_list)}] {site}")

            # Find sitemap
            sitemap = self.find_sitemap(site)
            if not sitemap:
                print("   [Skip] No sitemap found")
                self.status["sites_completed"] += 1
                continue

            # Parse sitemap
            targets = self.parse_sitemap(sitemap, combined_existing)
            if not targets:
                print("   [Skip] No new recipes found in recent posts")
                self.status["sites_completed"] += 1
                continue

            print(f"   [Found] {len(targets)} candidate URLs")
            print(f"   [Target] {self.config['scraper']['target_recipes_per_site']} recipes")

            imported_count = 0
            target_recipes = self.config['scraper']['target_recipes_per_site']

            # Check each candidate URL
            for url in targets:
                if not self.running:
                    break

                if imported_count >= target_recipes:
                    print("   [Done] Target reached")
                    break

                # Verify it's a recipe
                if not self.verify_is_recipe(url):
                    continue

                # Dry run mode
                if self.config['scraper']['dry_run']:
                    print(f"      [DRY RUN] Would import: {url}")
                    imported_count += 1
                    self.status["total_imported"] += 1
                    continue

                # Import to enabled services
                success_mealie = False
                success_tandoor = False

                # Try Mealie
                if self.mealie_client and url not in existing_mealie:
                    if self.mealie_client.import_recipe(url):
                        success_mealie = True
                        existing_mealie.add(url)

                # Try Tandoor
                if self.tandoor_client and url not in existing_tandoor:
                    if self.tandoor_client.import_recipe(url):
                        success_tandoor = True
                        existing_tandoor.add(url)

                # Output result
                if success_mealie or success_tandoor:
                    services = []
                    if success_mealie:
                        services.append("Mealie")
                    if success_tandoor:
                        services.append("Tandoor")

                    print(f"      [OK] Imported to {', '.join(services)}: {url}")
                    imported_count += 1
                    self.status["total_imported"] += 1

                    # Be polite - delay between imports
                    time.sleep(self.config['scraper']['delay_between_imports'])

            self.status["sites_completed"] += 1

        # Done
        self.running = False
        self.status["running"] = False
        self.status["progress"] = 100
        print("\n" + "=" * 60)
        print(f"[Scraper] Complete! Imported {self.status['total_imported']} recipes")
        print("=" * 60)
