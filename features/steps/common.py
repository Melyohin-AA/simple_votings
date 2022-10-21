import os
import behave
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


# FUNCS

def submit_user_credentials(context, username, password):
    context.username = eval(username, {}, {})
    context.password = eval(password, {}, {})
    context.browser.find_element(By.ID, "id_username").send_keys(context.username)
    context.browser.find_element(By.ID, "id_password").send_keys(context.password)
    context.browser.find_element(By.XPATH, "//button[@type='submit']").click()


# STEPS

@behave.given('Chrome browser is launched (headless="{headless}")')
def step_impl(context, headless):
    driver_path = os.path.join(__file__[:__file__.find("features")], "drivers", "chromedriver.exe")
    options = Options()
    if headless != "0":
        options.add_argument("--headless")
    context.browser = webdriver.Chrome(driver_path, options=options)


@behave.given('server address is "{index}"')
def step_impl(context, index):
    context.index = index


@behave.then('I close browser')
def step_impl(context):
    context.browser.close()


@behave.given('logged in as "{username}":"{password}"')
def step_impl(context, username, password):
    context.browser.get(context.index + "login/")
    submit_user_credentials(context, username, password)


@behave.given('"{page}" page is opened')
def step_impl(context, page):
    context.browser.get(context.index + page)
