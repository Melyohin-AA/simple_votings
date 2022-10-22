import behave
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from features.steps.common import submit_user_credentials
from features import test_config


@behave.when('I try log in as "{username:Text}":"{password:Text}"')
def step_impl(context, username, password):
    submit_user_credentials(context, username, password)


@behave.then('I verify index page is loaded')
def step_impl(context):
    assert context.browser.current_url == test_config.SERVER_ADDRESS
    try: assert not context.browser.find_element(By.XPATH, "//a[text()='Войти']").is_displayed()
    except NoSuchElementException: pass
    assert context.browser.find_element(By.XPATH, "//a[text()='Выйти']").is_displayed()


@behave.then('I verify credentials are rejected')
def step_impl(context):
    assert context.browser.current_url == test_config.SERVER_ADDRESS + "login/"


@behave.when('I navigate to profile page')
def step_impl(context):
    profile_ref = context.browser.find_element(By.XPATH, "//a[text()='Мой профиль']")
    profile_ref.click()


@behave.then('I verify username is proper')
def step_impl(context):
    username_field = context.browser.find_element(By.XPATH, "//label[text()='Логин']/../input")
    assert username_field.get_attribute("value") == context.username
