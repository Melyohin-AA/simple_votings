from selenium import webdriver
import behave
import parse
from features import test_config, funcs


# HOOKS

def before_scenario(context, scenario):
    if test_config.BROWSER is webdriver.Chrome:
        context.browser = funcs.launch_chrome_browser()
    else:
        raise ValueError(f"Launcher for {test_config.BROWSER.name}' browser is not implemented!")


def after_scenario(context, scenario):
    if hasattr(context, "browser"):
        if hasattr(context, "cmd_list"):
            for cmd, args in context.cmd_list:
                status = funcs.run_cmd(cmd, args, context.browser)
                print(f"Command {cmd}({args}) returned {status} code")
        context.browser.quit()#.close()


# PARSERS

@parse.with_pattern(r".*")
def parse_text(text) -> str: return text


@parse.with_pattern(r"(\w*\/)+")
def parse_page(text) -> str: return text


@parse.with_pattern(r"[01]")
def parse_flag(text) -> bool: return text != '0'


behave.register_type(Text=parse_text, Page=parse_page, Flag=parse_flag)
behave.use_step_matcher("cfparse")
