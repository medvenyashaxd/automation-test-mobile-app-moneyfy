from behave import given, when, then


@given('Tap on three dots at the top right of the screen and tap setting or swipe to bring up the menu')
def go_to_settings(context):
    context.app.main_screen.go_to_settings()


@when('The light theme should change to dark')
def set_theme(context):
    context.app.setting_screen.click_on_theme()


@when('The language should change to russian')
def set_language(context):
    context.app.main_screen.go_to_settings()
    context.app.setting_screen.set_language()


@when('Set currency {name}')
def set_currency(context, name):
    context.app.main_screen.go_to_settings()
    context.app.setting_screen.set_currency(name)


@when('Set first day of week value')
def set_first_day(context):
    context.app.setting_screen.set_week_value(850, 1300, 850, 1150)


@when('Set start month')
def set_set_start_month(context):
    context.app.setting_screen.set_month_value(850, 1300, 850, 1150)


@then('Result: changed settings language, night mode, currency, week and month')
def verify_change_setting(context):
    context.app.setting_screen.check_theme('Темная тема')
    context.app.setting_screen.check_language('Русский')
    context.app.setting_screen.check_currency('BYN')
    context.app.setting_screen.check_week_value('Ср')
    context.app.setting_screen.check_month_value('3')

