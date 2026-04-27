from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from SampleFramework.util.utilities import Util
from SampleFramework.util.config import USERNAME, PASSWORD

class LoginPage(Util):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.username = (By.ID, "username")
        self.password = (By.ID, "password")
        self.signInBtn = (By.ID, "signInBtn")

    def login(self,username,password):
        self.driver.find_element(*self.username).send_keys(username)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.signInBtn).click()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def home(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='/angularpractice/shop']")))
        self.driver.find_element(By.CSS_SELECTOR, "a[href='/angularpractice/shop']").click()
        print(self.driver.current_url)
        assert self.driver.current_url == "https://rahulshettyacademy.com/angularpractice/shop"
