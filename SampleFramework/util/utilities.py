class Util:
    def __init__(self, driver):
        self.driver = driver

    def get_title(self):
        print(self.driver.title)
        assert self.driver.title == "ProtoCommerce"