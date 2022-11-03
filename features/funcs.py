import os
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from features import test_config


def launch_chrome_browser():
    driver_path = os.path.join(__file__[:__file__.find("features")], "drivers", "chromedriver.exe")
    options = Options()
    if test_config.HEADLESS_MODE:
        options.add_argument("--headless")
    return webdriver.Chrome(driver_path, options=options)


def run_cmd(cmd, args, browser):
    browser.get(f"{test_config.SERVER_ADDRESS}/qa_api/?cmd={cmd}")
    status = browser.find_element(By.XPATH, "html/body").text
    if status == "400":
        raise RuntimeError(f"Command {cmd}({args}) load has failed!")
    for key, value in args.items():
        browser.find_element(By.XPATH, f"html/body/form/input[@name='{key}']").send_keys(value)
    browser.find_element(By.XPATH, f"html/body/form/button").click()
    status = int(browser.find_element(By.XPATH, "html/body").text)
    if status == 400:
        raise RuntimeError(f"Command {cmd}({args}) execution has failed!")
    return status


def generate_unique_login(min_length, max_length, a, b) -> str:
    browser = launch_chrome_browser()
    while True:
        length = random.randint(min_length, max_length)
        login = [chr(random.randint(a, b)) for _ in range(length)]
        login = "".join(login)
        if run_cmd("has_user", {"login": login}, browser) != 200:
            break
    browser.quit()#.close()
    return login


def submit_user_credentials(context, login, password):
    context.login = login
    context.password = password
    context.browser.find_element(By.ID, "id_username").send_keys(context.login)
    context.browser.find_element(By.ID, "id_password").send_keys(context.password)
    context.browser.find_element(By.XPATH, "//button[@type='submit']").click()


def submit_user_creation(context, login, pw1, pw2, name):
    context.login = login
    context.password = pw1
    context.browser.find_element(By.ID, "id_login").send_keys(login)
    context.browser.find_element(By.ID, "id_password1").send_keys(pw1)
    context.browser.find_element(By.ID, "id_password2").send_keys(pw2)
    context.browser.find_element(By.ID, "id_name").send_keys(name)
    context.browser.find_element(By.ID, "reg_button").click()
