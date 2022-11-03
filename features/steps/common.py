import behave
from features import test_config, funcs


@behave.given('logged in as "{login:Text}":"{password:Text}"')
def step_impl(context, login: str, password: str):
    context.browser.get(test_config.SERVER_ADDRESS + "/login/")
    funcs.submit_user_credentials(context, login, password)


@behave.given('"{page:Page}" page is opened')
def step_impl(context, page: str):
    context.browser.get(test_config.SERVER_ADDRESS + page)
