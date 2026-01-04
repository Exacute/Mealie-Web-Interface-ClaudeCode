import requests


class MealieClient:
    """Client for interacting with Mealie API"""

    def __init__(self, url: str, api_token: str):
        """
        Initialize Mealie API client

        Args:
            url: Base URL of Mealie instance (e.g., http://192.168.1.79:9000)
            api_token: API token for authentication
        """
        self.url = url.rstrip('/')
        self.api_token = api_token
        self.headers = {"Authorization": f"Bearer {self.api_token}"}

    def test_connection(self) -> tuple:
        """
        Test API connection

        Returns:
            Tuple of (success: bool, message: str)
        """
        try:
            r = requests.get(
                f"{self.url}/api/recipes?page=1&perPage=1",
                headers=self.headers,
                timeout=10
            )
            if r.status_code == 200:
                return (True, "Connection successful")
            elif r.status_code == 401:
                return (False, "Authentication failed - check API token")
            else:
                return (False, f"Connection failed with status code {r.status_code}")
        except requests.exceptions.Timeout:
            return (False, "Connection timeout - check URL")
        except requests.exceptions.ConnectionError:
            return (False, "Connection refused - check URL and port")
        except Exception as e:
            return (False, f"Error: {str(e)}")

    def get_existing_urls(self) -> set:
        """
        Fetch all existing recipe URLs from Mealie

        Returns:
            Set of existing recipe URLs
        """
        print("[Mealie] Fetching existing recipes...")
        existing = set()
        page = 1

        try:
            # Check connection first
            r = requests.get(
                f"{self.url}/api/recipes?page=1&perPage=1",
                headers=self.headers,
                timeout=10
            )
            if r.status_code != 200:
                print(f"[Mealie] Connection failed with status {r.status_code}")
                return set()
        except Exception as e:
            print(f"[Mealie] Connection error: {e}")
            return set()

        print("[Mealie] Downloading recipe index...")
        while True:
            try:
                r = requests.get(
                    f"{self.url}/api/recipes?page={page}&perPage=1000",
                    headers=self.headers,
                    timeout=15,
                )
                if r.status_code != 200:
                    break

                items = r.json().get("items", [])
                if not items:
                    break

                for item in items:
                    if "orgURL" in item and item["orgURL"]:
                        existing.add(item["orgURL"])
                    if "originalURL" in item and item["originalURL"]:
                        existing.add(item["originalURL"])

                print(f"   ...scanned page {page} (Total: {len(existing)})", end="\r")
                page += 1
            except Exception as e:
                print(f"\n[Mealie] Error reading index: {e}")
                break

        print(f"\n[Mealie] Found {len(existing)} existing recipe URLs")
        return existing

    def import_recipe(self, url: str) -> bool:
        """
        Import a single recipe by URL

        Args:
            url: Recipe URL to import

        Returns:
            True if successful, False otherwise
        """
        endpoint = f"{self.url}/api/recipes/create/url"
        headers = {
            "Authorization": f"Bearer {self.api_token}",
            "Content-Type": "application/json",
        }

        try:
            r = requests.post(
                endpoint,
                json={"url": url},
                headers=headers,
                timeout=10
            )
            return r.status_code == 201
        except Exception as e:
            print(f"[Mealie] Error importing {url}: {e}")
            return False
