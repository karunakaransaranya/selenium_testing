from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from SampleFramework.util.utilities import Util
from SampleFramework.util.config import USERNAME, PASSWORD, BASE_URL  # ✅ import BASE_URL

class LoginPage(Util):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.username = (By.ID, "username")
        self.password = (By.ID, "password")
        self.signInBtn = (By.ID, "signInBtn")
        self.error_msg = (By.CSS_SELECTOR, "div.alert.alert-danger")

    def go_to_url(self):                         # ✅ new method
        self.driver.get(BASE_URL)
        self.driver.implicitly_wait(10)

    def login(self, username, password):
        self.driver.find_element(*self.username).send_keys(username)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.signInBtn).click()
        self.driver.implicitly_wait(5)

    def home(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='/angularpractice/shop']")))
        self.driver.find_element(By.CSS_SELECTOR, "a[href='/angularpractice/shop']").click()
        print(self.driver.current_url)
        assert self.driver.current_url == "https://rahulshettyacademy.com/angularpractice/shop"

    def assert_login_failed(self):
        wait = WebDriverWait(self.driver, 10)
        error_element = wait.until(EC.visibility_of_element_located(self.error_msg))
        error_text = error_element.text
        assert "Incorrect" in error_text, f"Expected login error message but got: '{error_text}'"
        print(f"Login failed as expected. Error: {error_text}")

