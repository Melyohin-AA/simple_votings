import behave
import parse


# INIT

@parse.with_pattern(r".*")
def parse_text(text) -> str: return text


@parse.with_pattern(r"[01]")
def parse_flag(text) -> bool: return text != '0'


behave.register_type(Text=parse_text, Flag=parse_flag)
behave.use_step_matcher("cfparse")


# HOOK

def after_scenario(context, scenario):
    if hasattr(context, "browser"):
        context.browser.close()
