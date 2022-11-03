import behave
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from features import test_config, funcs


@behave.when('I navigate to registration page')
def step_impl(context):
    context.browser.find_element(By.XPATH, "//a[text()='Регистрация']").click()


@behave.when('I try register as unique PW1="{pw1:Text}", PW2="{pw2:Text}", name="{name:Text}"')
def step_impl(context, pw1, pw2, name):
    login = funcs.generate_unique_login(1, 64, 32, 126)
    funcs.submit_user_creation(context, login, pw1, pw2, name)


@behave.when('I try register as login="{login:Text}", PW1="{pw1:Text}", PW2="{pw2:Text}", name="{name:Text}"')
def step_impl(context, login, pw1, pw2, name):
    funcs.submit_user_creation(context, login, pw1, pw2, name)


@behave.then('I verify registration page is loaded')
def step_impl(context):
    assert context.browser.current_url == test_config.SERVER_ADDRESS + "/registration/"


@behave.then('I verify registration has succeeded')
def step_impl(context):
    context.cmd_list = [("del_user", {"login": context.login, "password": context.password})]
    try: assert not context.browser.find_element(By.XPATH, "//div[contains(@class,'alert-danger')]").is_displayed()
    except NoSuchElementException: pass
    assert context.browser.find_element(By.XPATH, "//div[contains(@class,'alert-success')]").is_displayed()


@behave.then('I verify registration is rejected')
def step_impl(context):
    try:
        try:
            assert not context.browser.find_element(By.XPATH, "//div[contains(@class,'alert-success')]").is_displayed()
        except NoSuchElementException:
            pass
        #try:
        #    assert context.browser.find_element(By.XPATH, "//div[contains(@class,'alert-danger')]").is_displayed()
        #except NoSuchElementException:
        #    assert False
    except AssertionError as error:
        context.cmd_list = [("del_user", {"login": context.login, "password": context.password})]
        raise error
