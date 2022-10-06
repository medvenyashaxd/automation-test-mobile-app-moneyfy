from appium.webdriver.common.appiumby import AppiumBy


class SettingLocators:

    THEME_MODE = (AppiumBy.ID, 'com.monefy.app.pro:id/is_night_mode_enabled_checkbox')
    LANGUAGE_NAME = (AppiumBy.ID, 'com.monefy.app.pro:id/language_name')
    RUSSIAN = (AppiumBy.XPATH, '//android.widget.CheckedTextView[@text="Русский"]')

    BUTTON_OK = (AppiumBy.ID, 'android:id/button1')
    CURRENCY_BUTTON = (AppiumBy.ID, 'com.monefy.app.pro:id/currency_name')
    BUDGET_BUTTON = (AppiumBy.ID, 'com.monefy.app.pro:id/is_budget_mode_checkbox')

    INPUT_SEARCH_CURRENCY = (AppiumBy.ID, 'com.monefy.app.pro:id/search_src_text')
    BYN_CURRENCY = (AppiumBy.ID, 'com.monefy.app.pro:id/textViewName')

    FIRST_DAY_OF_WEEK_VALUE = (AppiumBy.ID, 'com.monefy.app.pro:id/first_day_of_week_value')
    FIRST_DAY_OF_MONTH_VALUE = (AppiumBy.ID, 'com.monefy.app.pro:id/first_day_of_month_value')

    BUDGET_AMOUNT = (AppiumBy.ID, 'com.monefy.app.pro:id/budget_amount')
    MONTHLY_BUDGET_AMOUNT_INPUT = (AppiumBy.XPATH, '//android.widget.EditText[@text="0"]')

