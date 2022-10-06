from screens.main_screen import MainScreen
from screens.setting_screen import SettingScreen


class Application:

    def __init__(self, driver):
        self.main_screen = MainScreen(driver)
        self.setting_screen = SettingScreen(driver)
