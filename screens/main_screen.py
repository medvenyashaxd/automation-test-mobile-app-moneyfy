import random
import allure

from locators.main_screen_locators import MainScreenLocators
from screens.base_screen import BaseScreen


class MainScreen(BaseScreen):
    locators = MainScreenLocators()

    @allure.step("Go to settings")
    def go_to_settings(self, locator=locators):
        num = random.randint(1, 2)
        with allure.step("Go to settings with a button"):
            if num == 1:
                self.click(locator.THREE_DOTS)
                self.click(locator.BUTTON_SETTING)

            else:
                with allure.step("Go to settings with a swipe"):
                    self.setting_swipe()
                    self.click(locator.BUTTON_SETTING)

    @allure.step("Income budget")
    def income_budget(self, note, locator=locators):
        with allure.step("Go to income page"):
            self.tap_by_x_y(100, 400)
            self.click(locator.INCOME_BUTTON)

        self.input(locator.EXPENSE_NOTE, note)
        self.hide_keyboard()

        self.click(locator.KB6)
        self.click(locator.KB5)
        self.click(locator.KB0)

        self.click(locator.CHOOSE_CATEGORY)
        self.click(locator.SALARY)

    @allure.step("Expense_budget")
    def expense_budget(self, category: str, note: str, locator=locators):
        with allure.step("Go to expense page"):
            self.tap_by_x_y(100, 400)
            self.click(locator.EXPENSE_BUTTON)

        self.input(locator.EXPENSE_NOTE, note)
        self.hide_keyboard()

        if category == 'Entertainment':
            self.click(locator.KB1)
            self.click(locator.KB5)
            self.click(locator.KB0)
            self.click(locator.CHOOSE_CATEGORY)
            self.click(locator.ENTERTAINMENT)

        elif category == 'Car':
            self.click(locator.KB5)
            self.click(locator.KB0)
            self.click(locator.KB0)
            self.click(locator.CHOOSE_CATEGORY)
            self.click(locator.CAR)

    @allure.step("Check budget in main page")
    def check_budget_main_page(self, budget, locator=locators):
        self.check_property_changes(budget, locator.BALANCE)

    @allure.step("Check note")
    def check_note(self, locator=locators):
        with allure.step("Go to records"):
            self.tap_by_x_y(100, 400)
            self.click(locator.BALANCE)

        with allure.step("Tap on records "):
            self.click(locator.ENTERTAINMENT)
            self.click(locator.CAR)
            self.click(locator.SALARY)

        with allure.step("Get text in records"):
            salary_amount = self.find_elements(locator.SALARY)
            transaction_note = self.find_elements(locator.TRANSACTION_NOTE)
            transaction_amount = self.find_elements(locator.TRANSACTION_AMOUNT)

            expenses_note = []
            for note in transaction_note:
                expenses_note.append(note.text)

            for amount in transaction_amount:
                expenses_note.append(amount.text)

            for salary in salary_amount:
                expenses_note.append(salary.text)

        with allure.step("Assert note"):
            assert ['Sold bitcoin', 'Filled up the car', 'Chips, pizza, beer', '$650.00', '$500.00', '$150.00', 'Salary'] \
               == expenses_note

