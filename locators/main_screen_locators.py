from appium.webdriver.common.appiumby import AppiumBy


class MainScreenLocators:

    THREE_DOTS = (AppiumBy.ID, 'com.monefy.app.pro:id/overflow')
    BUTTON_SETTING = (AppiumBy.ID, 'com.monefy.app.pro:id/settings_imagebutton')

    EXPENSE_BUTTON = (AppiumBy.ID, 'com.monefy.app.pro:id/expense_button')
    INCOME_BUTTON = (AppiumBy.ID, 'com.monefy.app.pro:id/income_button')

    TRANSACTION_AMOUNT = (AppiumBy.ID, 'com.monefy.app.pro:id/textViewTransactionAmount')
    EXPENSE_AMOUNT = (AppiumBy.ID, 'com.monefy.app.pro:id/amount_text')

    EXPENSE_NOTE = (AppiumBy.ID, 'com.monefy.app.pro:id/textViewNote')
    TRANSACTION_NOTE = (AppiumBy.ID, 'com.monefy.app.pro:id/textViewTransactionNote')

    CHOOSE_CATEGORY = (AppiumBy.ID, 'com.monefy.app.pro:id/keyboard_action_button')

    ENTERTAINMENT = (AppiumBy.XPATH, '//android.widget.TextView[@text="Entertainment"]')
    CAR = (AppiumBy.XPATH, '//android.widget.TextView[@text="Car"]')
    SALARY = (AppiumBy.XPATH, '//android.widget.TextView[@text="Salary"]')

    BALANCE = (AppiumBy.ID, 'com.monefy.app.pro:id/balance_amount')

    KB0 = (AppiumBy.ID, 'com.monefy.app.pro:id/buttonKeyboard0')
    KB1 = (AppiumBy.ID, 'com.monefy.app.pro:id/buttonKeyboard1')
    KB2 = (AppiumBy.ID, 'com.monefy.app.pro:id/buttonKeyboard2')
    KB3 = (AppiumBy.ID, 'com.monefy.app.pro:id/buttonKeyboard3')
    KB4 = (AppiumBy.ID, 'com.monefy.app.pro:id/buttonKeyboard4')
    KB5 = (AppiumBy.ID, 'com.monefy.app.pro:id/buttonKeyboard5')
    KB6 = (AppiumBy.ID, 'com.monefy.app.pro:id/buttonKeyboard6')
    KB7 = (AppiumBy.ID, 'com.monefy.app.pro:id/buttonKeyboard7')
    KB8 = (AppiumBy.ID, 'com.monefy.app.pro:id/buttonKeyboard8')
    KB9 = (AppiumBy.ID, 'com.monefy.app.pro:id/buttonKeyboard9')
