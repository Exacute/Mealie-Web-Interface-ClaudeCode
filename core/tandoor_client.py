import requests


class TandoorClient:
    """Client for interacting with Tandoor API"""

    def __init__(self, url: str, api_key: str):
        """
        Initialize Tandoor API client

        Args:
            url: Base URL of Tandoor instance (e.g., http://192.168.1.80:8080)
            api_key: API key for authentication
        """
        self.url = url.rstrip('/')
        self.api_key = api_key
        self.headers = {"Authorization": f"Bearer {self.api_key}"}

    def test_connection(self) -> tuple:
        """
        Test API connection

        Returns:
            Tuple of (success: bool, message: str)
        """
        try:
            r = requests.get(
                f"{self.url}/api/recipe/?page=1&limit=1",
                headers=self.headers,
                timeout=10
            )
            if r.status_code == 200:
                return (True, "Connection successful")
            elif r.status_code == 401:
                return (False, "Authentication failed - check API key")
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
        Fetch all existing recipe URLs from Tandoor

        Returns:
            Set of existing recipe URLs
        """
        print("[Tandoor] Fetching existing recipes...")
        existing = set()
        page = 1

        while True:
            try:
                r = requests.get(
                    f"{self.url}/api/recipe/?page={page}&limit=100",
                    headers=self.headers,
                    timeout=10,
                )
                if r.status_code != 200:
                    if r.status_code == 401:
                        print("[Tandoor] Authentication failed")
                    else:
                        print(f"[Tandoor] Request failed with status {r.status_code}")
                    break

                data = r.json()
                results = data.get("results", [])
                if not results:
                    break

                for recipe in results:
                    if recipe.get("source"):
                        existing.add(recipe.get("source"))

                print(f"   ...scanned page {page} (Total: {len(existing)})", end="\r")

                if not data.get("next"):
                    break
                page += 1
            except Exception as e:
                print(f"\n[Tandoor] Error reading index: {e}")
                break

        print(f"\n[Tandoor] Found {len(existing)} existing recipe URLs")
        return existing

    def import_recipe(self, url: str) -> bool:
        """
        Import a single recipe by URL

        Args:
            url: Recipe URL to import

        Returns:
            True if successful, False otherwise
        """
        endpoint = f"{self.url}/api/recipe/from-url/"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

        try:
            r = requests.post(
                endpoint,
                json={"url": url},
                headers=headers,
                timeout=10
            )
            return r.status_code in [200, 201]
        except Exception as e:
            print(f"[Tandoor] Error importing {url}: {e}")
            return False
