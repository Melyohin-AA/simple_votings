import datetime
import main.forms

from main.db_tools.db_user_tools import DB_UserTools
from main.db_tools.db_voting_tools import DB_VotingTools
from django.shortcuts import render
from django.contrib.auth.decorators import login_required



def get_menu_context():
    return [
        {'url': '/', 'name': 'Главная'},
        {'url': '/time/', 'name': 'Текущее время'},
    ]


def index_page(request):
    context = {
        'pagename': 'Главная',
        'author': 'Andrew',
        'pages': 4,
        'menu': get_menu_context()
    }
    return render(request, 'pages/index.html', context)


def time_page(request):
    context = {
        'pagename': 'Текущее время',
        'time': datetime.datetime.now().time(),
        'menu': get_menu_context()
    }
    return render(request, 'pages/time.html', context)


def registration_page(request): #временно
    context = {}
    success = ok = False
    error = None
    if request.method == "POST":
        form = main.forms.RegistrationForm(request.POST)
        context["form"] = form
        if form.is_valid():
            password1 = form.data["password1"]
            if password1 == form.data["password2"]:
                ok, error = DB_UserTools.try_register_user(form.data["login"], password1, form.data["name"], form.data["email"])
                if ok:
                    success = True
            else:
                error = "Указанные пароли не совпадают!"
        else:
            error = "Здесь нет уязвимости!"
    else:
        context["form"] = main.forms.RegistrationForm()
        ok = True
    context["ok"] = ok
    context["error"] = error
    context["success"] = success
    return render(request, 'registration/registration.html', context)


def clear_all_data_page(request): #Developer's tool
    DB_UserTools.clear_user_list()
    DB_VotingTools.clear_voting_list()
    return render(request, 'pages/cad.html')


@login_required
def new_voting_page(request): #временно
    context = {}
    success = ok = False
    error = None
    if (request.method == "POST") and request.POST:
        form = main.forms.NewVotingForm(request.POST)
        context["form"] = form
        if form.is_valid():
            author = request.user
            title = form.data["title"]
            description = form.data["description"]
            type_ = int(form.data["type"])
            show_votes_before_end = form.data.get("show_votes_before_end", 'off') == 'on'
            anonymous = form.data.get("anonymous", 'off') == 'on'
            ok, error = DB_VotingTools.try_create_voting(author, title, description, type_, show_votes_before_end, anonymous)
            if ok:
                success = True
        else:
            error = "Здесь нет уязвимости!"
    else:
        context["form"] = main.forms.NewVotingForm()
        ok = True
    context["ok"] = ok
    context["error"] = error
    context["success"] = success
    return render(request, "pages/voting_management/new_voting.html", context)


@login_required
def add_vote_variant(request): #временно
    context = {}
    success = ok = False
    error = None
    if (request.method == "POST") and request.POST:
        form = main.forms.AddVoteVariantForm(request.POST)
        context["form"] = form
        if form.is_valid():
            author = request.user
            voting_title = form.data["voting_title"]
            description = form.data["description"]
            ok, error = DB_VotingTools.try_add_vote_variant(author, voting_title, description)
            if ok:
                success = True
        else:
            error = "Здесь нет уязвимости!"
    else:
        context["form"] = main.forms.AddVoteVariantForm()
        ok = True
    context["ok"] = ok
    context["error"] = error
    context["success"] = success
    return render(request, "pages/voting_management/add_vote_variant.html", context)