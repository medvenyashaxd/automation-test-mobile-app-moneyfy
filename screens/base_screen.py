from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as ec


class BaseScreen:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, timeout=10):
        return Wait(self.driver, timeout).until(ec.visibility_of_element_located(locator))

    def find_elements(self, locator, timeout=10):
        return Wait(self.driver, timeout).until(ec.visibility_of_all_elements_located(locator))

    def click(self, locator):
        element = self.find_element(locator)
        element.click()

    def input(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)