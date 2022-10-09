from behave import given, when, then


@given('Setting a budget {budget}')
def set_budget(context, budget):
    context.app.main_screen.go_to_settings()
    context.app.setting_screen.set_budget(budget)
    context.app.setting_screen.check_budget('$1,000.00')


@when('Budget expense')
def budget_waste(context):
    context.app.main_screen.expense_budget('Entertainment', 'Chips, pizza, beer')
    context.app.main_screen.check_budget_main_page('Balance $850.00')

    context.app.main_screen.expense_budget('Car', 'Filled up the car')
    context.app.main_screen.check_budget_main_page('Balance $350.00')


@when('Budget income')
def budget_income(context):
    context.app.main_screen.income_budget('Sold bitcoin')


@then('Result: The budget has changed')
def verify_change_budget(context):
    context.app.main_screen.check_note()
