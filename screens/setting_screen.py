import allure

from locators.setting_locators import SettingLocators
from screens.base_screen import BaseScreen


class SettingScreen(BaseScreen):

    locators = SettingLocators()

    @allure.step("Change theme")
    def click_on_theme(self, locator=locators):
        self.click(locator.THEME_MODE)

    @allure.step("Change language")
    def set_language(self, locator=locators):
        self.click(locator.LANGUAGE_NAME)
        self.click(locator.RUSSIAN)
        self.click(locator.BUTTON_OK)

    @allure.step("Change currency")
    def set_currency(self, search_currency: str, locator=locators):
        self.click(locator.CURRENCY_BUTTON)
        self.input(locator.INPUT_SEARCH_CURRENCY, search_currency)
        if search_currency == 'BYN':
            self.click(locator.BYN_CURRENCY)

    @allure.step("Set budget")
    def set_budget(self, budget, locator=locators):
        self.click(locator.BUDGET_BUTTON)
        self.input(locator.MONTHLY_BUDGET_AMOUNT_INPUT, budget)
        self.click(locator.BUTTON_OK)

    @allure.step("Set week value")
    def set_week_value(self, x, y, move_to_x, move_to_y, locator=locators):
        self.swipe_to_change_settings(x, y, move_to_x, move_to_y, locator.FIRST_DAY_OF_WEEK_VALUE, locator.BUTTON_OK)

    @allure.step("Set month value")
    def set_month_value(self, x, y, move_to_x, move_to_y, locator=locators):
        self.swipe_to_change_settings(x, y, move_to_x, move_to_y, locator.FIRST_DAY_OF_MONTH_VALUE, locator.BUTTON_OK)

    @allure.step("Checking the changed theme")
    def check_theme(self, name_theme: str, locator=locators):
        self.check_property_changes(name_theme, locator.THEME_MODE)

    @allure.step("Checking the changed language")
    def check_language(self, language_name: str, locator=locators):
        self.check_property_changes(language_name, locator.LANGUAGE_NAME)

    @allure.step("Checking the changed currency")
    def check_currency(self, currency: str, locator=locators):
        self.check_property_changes(currency, locator.CURRENCY_BUTTON)

    @allure.step("Check the changed week value")
    def check_week_value(self, week: str, locator=locators):
        self.check_property_changes(week, locator.FIRST_DAY_OF_WEEK_VALUE)

    @allure.step("Check the changed month value")
    def check_month_value(self, month: str, locator=locators):
        self.check_property_changes(month, locator.FIRST_DAY_OF_MONTH_VALUE)

    @allure.step("Check the changed budget")
    def check_budget(self, budget:str, locator=locators):
        self.check_property_changes(budget, locator.BUDGET_AMOUNT)

