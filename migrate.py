#!/usr/bin/env python3
"""
Migration script to extract configuration and sites from mealie_dredger.py
and create config.json and sites.txt files.
"""

import json
import re
from pathlib import Path

# Paths
BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"
CONFIG_FILE = DATA_DIR / "config.json"
SITES_FILE = DATA_DIR / "sites.txt"
OLD_SCRIPT = BASE_DIR / "mealie_dredger.py"


def extract_config():
    """Extract configuration values from mealie_dredger.py"""
    config = {
        "mealie": {
            "enabled": True,
            "url": "",
            "api_token": ""
        },
        "tandoor": {
            "enabled": False,
            "url": "",
            "api_key": ""
        },
        "scraper": {
            "dry_run": False,
            "target_recipes_per_site": 50,
            "scan_depth": 1000,
            "delay_between_imports": 1.5
        },
        "active_site_list": "sites.txt"
    }

    if not OLD_SCRIPT.exists():
        print(f"Warning: {OLD_SCRIPT} not found. Using default config.")
        return config

    try:
        with open(OLD_SCRIPT, 'r', encoding='utf-8') as f:
            content = f.read()

        # Extract Mealie settings
        mealie_enabled_match = re.search(r'MEALIE_ENABLED\s*=\s*(True|False)', content)
        if mealie_enabled_match:
            config['mealie']['enabled'] = mealie_enabled_match.group(1) == 'True'

        mealie_url_match = re.search(r'MEALIE_URL\s*=\s*["\']([^"\']+)["\']', content)
        if mealie_url_match:
            config['mealie']['url'] = mealie_url_match.group(1)

        mealie_token_match = re.search(r'MEALIE_API_TOKEN\s*=\s*["\']([^"\']+)["\']', content)
        if mealie_token_match:
            config['mealie']['api_token'] = mealie_token_match.group(1)

        # Extract Tandoor settings
        tandoor_enabled_match = re.search(r'TANDOOR_ENABLED\s*=\s*(True|False)', content)
        if tandoor_enabled_match:
            config['tandoor']['enabled'] = tandoor_enabled_match.group(1) == 'True'

        tandoor_url_match = re.search(r'TANDOOR_URL\s*=\s*["\']([^"\']+)["\']', content)
        if tandoor_url_match:
            config['tandoor']['url'] = tandoor_url_match.group(1)

        tandoor_key_match = re.search(r'TANDOOR_API_KEY\s*=\s*["\']([^"\']+)["\']', content)
        if tandoor_key_match:
            config['tandoor']['api_key'] = tandoor_key_match.group(1)

        # Extract scraper settings
        dry_run_match = re.search(r'DRY_RUN\s*=\s*(True|False)', content)
        if dry_run_match:
            config['scraper']['dry_run'] = dry_run_match.group(1) == 'True'

        target_match = re.search(r'TARGET_RECIPES_PER_SITE\s*=\s*(\d+)', content)
        if target_match:
            config['scraper']['target_recipes_per_site'] = int(target_match.group(1))

        scan_depth_match = re.search(r'SCAN_DEPTH\s*=\s*(\d+)', content)
        if scan_depth_match:
            config['scraper']['scan_depth'] = int(scan_depth_match.group(1))

        print("[OK] Extracted configuration successfully")
        return config

    except Exception as e:
        print(f"Error extracting config: {e}")
        return config


def extract_sites():
    """Extract SITES list from mealie_dredger.py"""
    if not OLD_SCRIPT.exists():
        print(f"Warning: {OLD_SCRIPT} not found. Creating empty sites.txt")
        return []

    try:
        with open(OLD_SCRIPT, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        # Find SITES = [ ... ] block
        sites = []
        in_sites_block = False
        current_comment = ""

        for line in lines:
            line = line.strip()

            # Start of SITES block
            if line.startswith('SITES = ['):
                in_sites_block = True
                continue

            # End of SITES block
            if in_sites_block and line.startswith(']'):
                break

            if in_sites_block:
                # Check for category comment
                if line.startswith('#'):
                    current_comment = line
                    sites.append('')  # Add blank line before category
                    sites.append(current_comment)
                    continue

                # Extract URL from line like "https://www.example.com",
                url_match = re.search(r'["\']([^"\']+)["\']', line)
                if url_match:
                    url = url_match.group(1)
                    if url.startswith(('http://', 'https://')):
                        sites.append(url)

        print(f"[OK] Extracted {len([s for s in sites if s and not s.startswith('#')])} sites successfully")
        return sites

    except Exception as e:
        print(f"Error extracting sites: {e}")
        return []


def save_config(config):
    """Save configuration to config.json"""
    try:
        DATA_DIR.mkdir(parents=True, exist_ok=True)

        with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=2)

        print(f"[OK] Saved config to {CONFIG_FILE}")
        return True
    except Exception as e:
        print(f"Error saving config: {e}")
        return False


def save_sites(sites):
    """Save sites to sites.txt"""
    try:
        DATA_DIR.mkdir(parents=True, exist_ok=True)

        with open(SITES_FILE, 'w', encoding='utf-8') as f:
            for site in sites:
                f.write(f"{site}\n")

        print(f"[OK] Saved sites to {SITES_FILE}")
        return True
    except Exception as e:
        print(f"Error saving sites: {e}")
        return False


def create_example_lists(sites):
    """Create example category-based site lists"""
    if not sites:
        return

    try:
        # Parse sites by category
        current_category = None
        categorized_sites = {}

        for line in sites:
            line = line.strip()

            if not line:
                continue

            if line.startswith('#'):
                # Extract category name
                category = line.replace('#', '').strip()
                category = category.replace(' ', '_').replace('&', 'and').lower()
                current_category = category
                if current_category not in categorized_sites:
                    categorized_sites[current_category] = []
            elif current_category and line.startswith(('http://', 'https://')):
                categorized_sites[current_category].append(line)

        # Save category-based files
        for category, urls in categorized_sites.items():
            if urls:
                filename = DATA_DIR / f"sites_{category}.txt"
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(f"# {category.replace('_', ' ').upper()}\n")
                    for url in urls:
                        f.write(f"{url}\n")
                print(f"[OK] Created {filename.name} with {len(urls)} sites")

    except Exception as e:
        print(f"Error creating example lists: {e}")


def main():
    """Main migration function"""
    print("=" * 60)
    print("Mealie Recipe Dredger - Configuration Migration")
    print("=" * 60)
    print()

    # Extract config
    print("Extracting configuration...")
    config = extract_config()

    # Extract sites
    print("Extracting site list...")
    sites = extract_sites()

    # Save files
    print()
    print("Saving files...")
    save_config(config)
    save_sites(sites)

    # Create example lists
    print()
    print("Creating category-based site lists...")
    create_example_lists(sites)

    print()
    print("=" * 60)
    print("Migration complete!")
    print("=" * 60)
    print()
    print("Next steps:")
    print("1. Review data/config.json and update API tokens if needed")
    print("2. Review data/sites.txt and customize as needed")
    print("3. Check data/sites_*.txt for category-based lists")
    print("4. Run 'python app.py' to start the web interface")
    print()


if __name__ == "__main__":
    main()
