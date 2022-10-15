from datetime import datetime

import allure
from appium import webdriver
from app.application import Application


def before_scenario(context, scenario):
    desired_capabilities = {
        "deviceName": "Pixel 4 API 30",
        "platformName": "Android",
        "automationName": "UiAutomator2",
        "platformVersion": "11",
        "skipUnlock": "false",
        "app": r"C:\Users\xmedv\PycharmProjects\automation-qa-test-mobile-app-moneyfy\app_bin\money-pro.apk"
    }

    context.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_capabilities)
    context.driver.implicitly_wait(5)
    context.app = Application(context.driver)

    attach = context.driver.get_screenshot_as_png()
    allure.attach(attach, name=f'Screenshot{datetime.today()}', attachment_type=allure.attachment_type.PNG)


def after_scenario(context, scenario):
    context.driver.quit()

