import behave
from features import test_config


@behave.given('index page is opened')
def step_impl(context):
    context.browser.get(test_config.SERVER_ADDRESS)


@behave.given('login page is opened')
def step_impl(context):
    context.browser.get(test_config.SERVER_ADDRESS + "/login/")


@behave.given('registration page is opened')
def step_impl(context):
    context.browser.get(test_config.SERVER_ADDRESS + "/registration/?test")
