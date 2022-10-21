import os
import behave
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@behave.given('Chrome browser is launched (headless="{headless}")')
def step_impl(context, headless):
    driver_path = os.path.join(__file__[:__file__.find("features")], "drivers", "chromedriver.exe")
    options = Options()
    if headless != "0":
        options.add_argument("--headless")
    context.browser = webdriver.Chrome(driver_path, options=options)


@behave.then('I close browser')
def step_impl(context):
    context.browser.close()


@behave.given('logged in as "{username}":"{password}"')
def step_impl(context, username, password):
    context.username = username = eval(username, {}, {})
    context.password = password = eval(password, {}, {})
    context.browser.get("http://www.old.practicalsqa.net/wp-login.php")
    context.browser.find_element_by_id("user_login").send_keys(username)
    context.browser.find_element_by_id("user_pass").send_keys(password)
    context.browser.find_element_by_id("wp-submit").click()


@behave.given('"{url}" page is opened')
def step_impl(context, url):
    context.browser.get(url)
