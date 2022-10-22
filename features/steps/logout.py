import behave
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from features import test_config


@behave.when('I try to log out')
def step_impl(context):
    logout_ref = context.browser.find_element(By.XPATH, "//a[text()='Выйти']")
    logout_ref.click()


@behave.then('I verify I am not authenticated')
def step_impl(context):
    assert context.browser.current_url == test_config.SERVER_ADDRESS
    try: assert not context.browser.find_element(By.XPATH, "//a[text()='Выйти']").is_displayed()
    except NoSuchElementException: pass
    assert context.browser.find_element(By.XPATH, "//a[text()='Войти']").is_displayed()
