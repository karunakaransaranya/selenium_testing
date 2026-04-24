from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from SampleFramework.util.utilities import Util


class CheckoutSuccess(Util):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.country = (By.ID, "country")
        self.countrylist = (By.CSS_SELECTOR, "div.suggestions ul")
        self.teamsandcond = (By.ID, "checkbox2")
        self.chkbox = (By.CSS_SELECTOR, "label[for='checkbox2']")
        self.purchase = (By.CSS_SELECTOR, "input[value='Purchase']")
        self.successmsg = (By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible strong")
        self.confirmationmsg = (By.CSS_SELECTOR, "div.alert.alert-success.alert-dismissible")
        self.close = (By.CSS_SELECTOR, ".close")

    def country_selection(self,country_name):
        self.driver.find_element(*self.country).send_keys("in")
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "suggestions")))
        country = self.driver.find_elements(By.CSS_SELECTOR, "div.suggestions ul")
        for i in country:
            mycountry = i.find_element(By.CSS_SELECTOR, "li a").text
            print(i.find_element(By.CSS_SELECTOR, "li a").text)
            if mycountry == country_name:
                i.find_element(By.CSS_SELECTOR, "li a").click()
                break

    def purchase_confirm(self):
        assert self.driver.find_element(*self.teamsandcond).is_enabled()
        self.driver.find_element(*self.chkbox).click()
        assert self.driver.find_element(*self.teamsandcond).is_selected()
        assert self.driver.find_element(*self.chkbox).text == "I agree with the term & Conditions"
        self.driver.find_element(*self.purchase).click()
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.visibility_of_element_located(self.close))
        msg = self.driver.find_element(*self.successmsg).text
        print(msg)
        assert msg == "Success!"
        msg2 = self.driver.find_element(*self.confirmationmsg).text
        print(msg2)
        assert "Success! Thank you! Your order will be delivered in next few weeks :-)" in msg2
