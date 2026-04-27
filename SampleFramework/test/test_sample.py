import time

import pytest
from selenium import webdriver




def test_url(browser_detail):
    driver = browser_detail
    driver.get("https://www.google.com")
    print(driver.title)

