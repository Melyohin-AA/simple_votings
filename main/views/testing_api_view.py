from main.db_tools.db_user_tools import DB_UserTools
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views import View


""" RESPONSE CODES
+-----+-------------------+-------------------------+
|     | GET               | POST                    |
+-----+-------------------+-------------------------+
| 200 | command loaded    | command succeeded       |
| 242 | -                 | positive answer         |
| 243 | -                 | negative answer         |
| 400 | command not found | command name/args error |
| 406 | -                 | command not applicable  |
| 501 | -                 | undefined command body  |
+-----+-------------------+-------------------------+
"""


class TestingApiView(View):
    def get(self, request: HttpRequest):
        try:
            cmd = request.GET["cmd"]
            context = {"cmd": cmd, "args": self.__cmds[cmd].ARG_LIST}
        except KeyError:
            return HttpResponse(400)
        return render(request, "pages/testing_api.html", context)

    def post(self, request: HttpRequest):
        try:
            cmd = request.GET["cmd"]
            status = self.__cmds[cmd](request.POST).execute()
        except KeyError:
            status = 400
        return HttpResponse(status)

    class __Command:
        NAME = None
        ARG_LIST = None

        def __init__(self, params: dict[str, str]):
            for arg in self.ARG_LIST:
                setattr(self, arg, params[arg])

        def execute(self) -> int:
            return 501

    class __DelUser(__Command):
        NAME = "del_user"
        ARG_LIST = ["login", "password"]

        def execute(self) -> int:
            user, _ = DB_UserTools.try_find_user(self.login)
            if (user is not None) and user.check_password(self.password):
                user_data, _ = DB_UserTools.try_get_user_data(user)
                if (user_data is not None) and user_data.test:
                    user_data.delete()
                    user.delete()
                    return 200
            return 406

    class __HasUser(__Command):
        NAME = "has_user"
        ARG_LIST = ["login"]

        def execute(self) -> int:
            user, _ = DB_UserTools.try_find_user(self.login)
            return 242 if user is not None else 243

    class __TestingUser(__Command):
        NAME = "testing_user"
        ARG_LIST = ["login"]

        def execute(self) -> int:
            user, _ = DB_UserTools.try_find_user(self.login)
            if user is not None:
                user_data, _ = DB_UserTools.try_get_user_data(user)
                if user_data is not None:
                    return 242 if user_data.test else 243
            return 406

    __cmds = {
        __DelUser.NAME: __DelUser,
        __HasUser.NAME: __HasUser,
        __TestingUser.NAME: __TestingUser,
    }
