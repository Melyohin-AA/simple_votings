import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import behave
import parse
from features import test_config


# FUNCS

def launch_chrome_browser():
    driver_path = os.path.join(__file__[:__file__.find("features")], "drivers", "chromedriver.exe")
    options = Options()
    if test_config.HEADLESS_MODE: options.add_argument("--headless")
    return webdriver.Chrome(driver_path, options=options)


# HOOK

def before_scenario(context, scenario):
    if test_config.BROWSER is webdriver.Chrome:
        context.browser = launch_chrome_browser()
    else:
        raise ValueError(f"Launcher for {test_config.BROWSER.name}' browser is not implemented!")


def after_scenario(context, scenario):
    if hasattr(context, "browser"):
        context.browser.close()


# PARSERS

@parse.with_pattern(r".*")
def parse_text(text) -> str: return text


@parse.with_pattern(r"[01]")
def parse_flag(text) -> bool: return text != '0'


behave.register_type(Text=parse_text, Flag=parse_flag)
behave.use_step_matcher("cfparse")
