import behave
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from features import test_config, funcs


@behave.when('I try log in as "{login:Text}":"{password:Text}"')
def step_impl(context, login, password):
    funcs.submit_user_credentials(context, login, password)


@behave.when('I navigate to login page')
def step_impl(context):
    context.browser.find_element(By.XPATH, "//a[text()='Войти']").click()


@behave.when('I navigate to profile page')
def step_impl(context):
    context.browser.find_element(By.XPATH, "//a[text()='Мой профиль']").click()


@behave.then('I verify login page is loaded')
def step_impl(context):
    assert context.browser.current_url == test_config.SERVER_ADDRESS + "/login/"


@behave.then('I verify index page is loaded')
def step_impl(context):
    assert context.browser.current_url == test_config.SERVER_ADDRESS + "/"
    try: assert not context.browser.find_element(By.XPATH, "//a[text()='Войти']").is_displayed()
    except NoSuchElementException: pass
    assert context.browser.find_element(By.XPATH, "//a[text()='Выйти']").is_displayed()


@behave.then('I verify credentials are rejected')
def step_impl(context):
    assert context.browser.current_url == test_config.SERVER_ADDRESS + "/login/"


@behave.then('I verify login is proper')
def step_impl(context):
    login_field = context.browser.find_element(By.XPATH, "//label[text()='Логин']/../input")
    assert login_field.get_attribute("value") == context.login
