import requests
import logging
from pipeline.config import ConfigManager

# Configure basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class APIClient:
    """A simple wrapper for the fakestore API."""

    CONFIGMANAGER = ConfigManager()
    
    def __init__(self, base_url):
         self.base_url = APIClient.CONFIGMANAGER.get("API", "base_url")
         self.limit = int(APIClient.CONFIGMANAGER.get("PAGINATION", "pagination_limit"))

    def get_user(self, user_id: int) -> dict:
         """Fetches a single user by their ID."""
         endpoint = f"/users/{user_id}"
         url = self.base_url + endpoint

         logging.info(f"Fetching user from {url}")
         try:
             response = requests.get(url)
             response.raise_for_status() # Check for HTTP errors
             return response.json()
         except requests.exceptions.RequestException as e:
             logging.error(f"API request failed: {e}")
             # Return an empty dict or raise a custom exception
             return {}

    #function to fetch all users data from the API
    def get_all_users(self) -> dict:
         """Fetches all users by their ID."""
         endpoint = f"/users/"
         url = self.base_url + endpoint

         logging.info(f"Fetching user from {url}")
         try:
             response = requests.get(url)
             response.raise_for_status() # Check for HTTP errors
             return response.json()
         except requests.exceptions.RequestException as e:
             logging.error(f"API request failed: {e}")
             # Return an empty dict or raise a custom exception
             return {}
        

    def get_product(self, product_id: int) -> dict:
         """Fetches a single product by it's ID."""
         endpoint = f"/products/{product_id}"      
         url = self.base_url + endpoint

         logging.info(f"Fetching user from {url}")
         try:
            response = requests.get(url)
            response.raise_for_status()   # Check for HTTP errors
            return response.json()

         except requests.exceptions.RequestException as e:
             logging.error(f"API request failed: {e}")
             # Return an empty dict or raise a custom exception
             return {}

    def get_all_products(self) -> dict:
         """Fetches all products by their ID."""
         endpoint = f"/products/"
         url = self.base_url + endpoint

         logging.info(f"Fetching products from {url}")
         try:
             response = requests.get(url)
             response.raise_for_status() # Check for HTTP errors
             return response.json()
         except requests.exceptions.RequestException as e:
             logging.error(f"API request failed: {e}")
             # Return an empty dict or raise a custom exception
             return {}


         