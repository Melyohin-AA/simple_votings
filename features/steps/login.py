import behave
from features.steps.common import submit_user_credentials, By


@behave.when('I try log in as "{username:Text}":"{password:Text}"')
def step_impl(context, username, password):
    submit_user_credentials(context, username, password)


@behave.then('I verify index page is loaded')
def step_impl(context):
    assert context.browser.current_url == context.index


@behave.then('I verify credentials are rejected')
def step_impl(context):
    assert context.browser.current_url == context.index + "login/"


@behave.when('I navigate to profile page')
def step_impl(context):
    context.browser.get(context.index + "my_profile/")


@behave.then('I verify username is proper')
def step_impl(context):
    username_field = context.browser.find_element(By.XPATH, "//label[text()='Логин']/../input")
    assert username_field.get_attribute("value") == context.username
