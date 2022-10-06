import random

from locators.main_screen_locators import MainScreenLocators
from screens.base_screen import BaseScreen


class MainScreen(BaseScreen):
    locators = MainScreenLocators()

    def go_to_settings(self, locator=locators):
        num = random.randint(1, 2)
        if num == 1:
            self.click(locator.THREE_DOTS)
            self.click(locator.BUTTON_SETTING)
        else:
            self.setting_swipe()
            self.click(locator.BUTTON_SETTING)