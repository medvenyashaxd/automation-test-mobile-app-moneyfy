from appium import webdriver
from app.application import Application


def before_scenario(context, scenario):
    desired_capabilities = {
        "deviceName": "Pixel 4 API 30",
        "platformName": "Android",
        "automationName": "UiAutomator2",
        "platformVersion": "11",
        "skipUnlock": "false",
        "app": r"C:\Users\xmedv\PycharmProjects\qa-mobile-application\app_binaries\money-pro.apk"
    }

    context.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_capabilities)
    context.driver.implicitly_wait(5)
    context.app = Application(context.driver)


def after_scenario(context, scenario):
    context.driver.quit()
