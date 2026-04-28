import pytest

from SampleFramework.POM.login import LoginPage
from SampleFramework.POM.products import Products
from SampleFramework.util.config import BASE_URL, USERNAME, PASSWORD



@pytest.mark.smoketest
@pytest.mark.E2Etest
def test_login(browser_detail):
    driver = browser_detail
    # driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.get(BASE_URL)
    loginPage = LoginPage(driver)
    loginPage.login(USERNAME,PASSWORD)
    loginPage.home()
    loginPage.get_title()


@pytest.mark.E2Etest
def test_login_invalid_username_and_password(browser_detail):
    driver = browser_detail
    driver.get(BASE_URL)
    loginPage = LoginPage(driver)
    loginPage.login("invalidUser", "invalidPass")
    loginPage.assert_login_failed()


@pytest.mark.E2Etest
def test_login_invalid_username_valid_password(browser_detail):
    driver = browser_detail
    driver.get(BASE_URL)
    loginPage = LoginPage(driver)
    loginPage.login("invalidUser", PASSWORD)
    loginPage.assert_login_failed()


@pytest.mark.E2Etest
def test_login_valid_username_invalid_password(browser_detail):
    driver = browser_detail
    driver.get(BASE_URL)
    loginPage = LoginPage(driver)
    loginPage.login(USERNAME, "invalidPass")
    loginPage.assert_login_failed()


@pytest.mark.E2Etest
def test_checkout(browser_detail):
    driver = browser_detail
    products = Products(driver)
    products.go_to_url()
    products.get_title()
    products.print_products("Blackberry")
    checkoutsuccess = products.add_to_cart()
    checkoutsuccess.country_selection("India")
    checkoutsuccess.get_title()
    checkoutsuccess.purchase_confirm()



