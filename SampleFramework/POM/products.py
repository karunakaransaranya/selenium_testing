from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from SampleFramework.POM.checkout_success import CheckoutSuccess
from SampleFramework.util.utilities import Util


class Products(Util):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.shop = (By.CSS_SELECTOR, "a[href='/angularpractice/shop']")
        self.card = (By.CSS_SELECTOR, "div.card.h-100")
        self.cardtitle = (By.CSS_SELECTOR, ".card-body .card-title a")
        self.checkout = (By.CSS_SELECTOR, ".nav-link.btn.btn-primary")
        self.chkout = (By.CLASS_NAME, "btn.btn-success")


    def go_to_url(self):
        self.driver.get("https://rahulshettyacademy.com/angularpractice/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def print_products(self,product_name):
        self.driver.find_element(*self.shop).click()
        wait = WebDriverWait(self.driver, 5)
        wait.until(expected_conditions.visibility_of_element_located(self.card))
        links = self.driver.find_elements(*self.card)
        for i in links:
            print(i.find_element(By.CSS_SELECTOR, ".card-body .card-title a").text)
            itemname = i.find_element(By.CSS_SELECTOR, ".card-body .card-title a").text
            if itemname == product_name:
                i.find_element(By.CSS_SELECTOR, ".card-footer .btn.btn-info").click()
                break

    def add_to_cart(self):
        self.driver.find_element(*self.checkout).click()
        self.driver.find_element(*self.chkout).click()
        checkoutSuccess = CheckoutSuccess(self.driver)
        return checkoutSuccess