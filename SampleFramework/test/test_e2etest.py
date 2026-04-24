import pytest

from SampleFramework.POM.login import LoginPage
from SampleFramework.POM.products import Products



@pytest.mark.smoketest
def test_login(browser_detail):
    driver = browser_detail
    # driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    loginPage = LoginPage(driver)
    loginPage.login("rahulshettyacademy","Learning@830$3mK2")
    loginPage.home()
    loginPage.get_title()

    # driver.find_element(By.CSS_SELECTOR,"a[href='/angularpractice/shop']").click()

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



