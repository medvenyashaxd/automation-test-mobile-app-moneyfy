import time

import allure
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as ec
from appium.webdriver.common.touch_action import TouchAction


class BaseScreen:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Find element")
    def find_element(self, locator, timeout=10):
        return Wait(self.driver, timeout).until(ec.visibility_of_element_located(locator))

    @allure.step("Find elements")
    def find_elements(self, locator, timeout=10):
        return Wait(self.driver, timeout).until(ec.visibility_of_all_elements_located(locator))

    @allure.step("Tap on element")
    def click(self, locator):
        element = self.find_element(locator)
        element.click()

    @allure.step("Sending text to a field")
    def input(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    @allure.step("Tap by x, y")
    def tap_by_x_y(self, x, y):
        action = TouchAction(self.driver)
        action.tap(x=x, y=y).perform()

    @allure.step("Swipe by x, y")
    def swipe_by_x_y(self, x, y, move_to_x, move_to_y):
        action = TouchAction(self.driver)
        time.sleep(2)
        action.press(x=x, y=y).move_to(x=move_to_x, y=move_to_y).release().perform()

    @allure.step("Swipe to settings")
    def setting_swipe(self):
        action = TouchAction(self.driver)
        time.sleep(2)
        action.long_press(x=1065, y=1300, duration=1800).move_to(x=200, y=1300).release().perform()

    @allure.step("Check property changes")
    def check_property_changes(self, mutable_property: str, locator):
        text = self.find_element(locator).text
        assert mutable_property in text, f'{text} does not math {mutable_property}'

    @allure.step("Swipe to change settings")
    def swipe_to_change_settings(self, x, y, move_to_x, move_to_y, locator, button_ok):
        self.click(locator)
        self.swipe_by_x_y(x, y, move_to_x, move_to_y)
        self.click(button_ok)

    @allure.step("Hide keyboad")
    def hide_keyboard(self):
        self.driver.hide_keyboard()
        time.sleep(2)

    @allure.step("Set screen landscape")
    def set_screen_orientation(self):
        self.driver.orientation = "LANDSCAPE"

