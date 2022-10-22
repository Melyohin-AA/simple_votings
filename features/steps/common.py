from selenium.webdriver.common.by import By
import behave
from features import test_config


# FUNCS

def submit_user_credentials(context, username, password):
    context.username = username
    context.password = password
    context.browser.find_element(By.ID, "id_username").send_keys(context.username)
    context.browser.find_element(By.ID, "id_password").send_keys(context.password)
    context.browser.find_element(By.XPATH, "//button[@type='submit']").click()


# STEPS

@behave.given('logged in as "{username:Text}":"{password:Text}"')
def step_impl(context, username: str, password: str):
    context.browser.get(test_config.SERVER_ADDRESS + "login/")
    submit_user_credentials(context, username, password)


@behave.given('"{page}" page is opened')
def step_impl(context, page: str):
    context.browser.get(test_config.SERVER_ADDRESS + page)
