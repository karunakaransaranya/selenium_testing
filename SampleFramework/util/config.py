import os
from dotenv import load_dotenv

# Load .env file
load_dotenv(override=True)

BASE_URL = os.getenv("BASE_URL")
SHOP_URL = os.getenv("SHOP_URL")
USERNAME = os.getenv("APP_USERNAME")
PASSWORD = os.getenv("APP_PASSWORD")