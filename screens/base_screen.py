import time

from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as ec
from appium.webdriver.common.touch_action import TouchAction


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

    def tap_by_x_y(self, x, y):
        action = TouchAction(self.driver)
        action.tap(x=x, y=y).perform()

    def swipe_by_x_y(self, x, y, move_to_x, move_to_y):
        action = TouchAction(self.driver)
        time.sleep(2)
        action.press(x=x, y=y).move_to(x=move_to_x, y=move_to_y).release().perform()

    def setting_swipe(self):
        action = TouchAction(self.driver)
        time.sleep(2)
        action.long_press(x=1065, y=1300, duration=1800).move_to(x=200, y=1300).release().perform()

    def check_property_changes(self, mutable_property: str, locator):
        text = self.find_element(locator).text
        assert mutable_property in text, f'{text} does not math {mutable_property}'

    def set_value(self, x, y, move_to_x, move_to_y, locator, button_ok):
        self.click(locator)
        self.swipe_by_x_y(x, y, move_to_x, move_to_y)
        self.click(button_ok)

    def hide_keyboard(self):
        self.driver.hide_keyboard()
        time.sleep(2)

    def set_screen_orientation(self):
        self.driver.orientation = "LANDSCAPE"
