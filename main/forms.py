from django import forms
from main.db_tools.db_voting_tools import DB_VotingTools


class CommonFields:
    @staticmethod
    def get_voting_title_field(required, label="Название голосования", attrs=None):
        if attrs is None:
            return forms.CharField(label=label, min_length=1, max_length=256, required=required)
        return forms.CharField(label=label, min_length=1, max_length=256, required=required,
                               widget=forms.TextInput(attrs=attrs))

    @staticmethod
    def get_description_field(required, label="Описание", attrs=None):
        if attrs is None:
            return forms.CharField(widget=forms.Textarea, label=label, min_length=1, max_length=4096, required=required)
        return forms.CharField(widget=forms.Textarea(attrs=attrs), label=label, min_length=1, max_length=4096,
                               required=required)

    @staticmethod
    def get_login_field(required, label="Логин", attrs={}):
        return forms.CharField(label=label, min_length=1, max_length=64, required=required,
                               widget=forms.TextInput(attrs=attrs))

    @staticmethod
    def get_name_field(required, label="Имя", attrs={}):
        return forms.CharField(label=label, min_length=1, max_length=64, required=required,
                               widget=forms.TextInput(attrs=attrs))

    @staticmethod
    def get_password_field(required, label="Пароль", attrs={}):
        return forms.CharField(widget=forms.PasswordInput(attrs=attrs), label=label, min_length=1, max_length=64,
                               required=required)

    @staticmethod
    def get_filter_option_field(label, attrs=None):
        if attrs is None:
            return forms.ChoiceField(widget=forms.Select, label=label, required=False,
                    choices=[(0, "--- (0)"), (1, "исключение (1)"), (-1, "исключение иных (-1)")])
        return forms.ChoiceField(widget=forms.Select(attrs=attrs), label=label, required=False,
                                 choices=[(0, "--- (0)"), (1, "исключение (1)"), (-1, "исключение иных (-1)")])

    @staticmethod
    def get_invisible_field(type_, id, value=''):
        return type_(label="", widget=forms.HiddenInput(attrs={"id": id, "value": value}))


class RegistrationForm(forms.Form):
    login = CommonFields.get_login_field(True, attrs={"class": "form-control"})
    password1 = CommonFields.get_password_field(True, attrs={"class": "form-control"})
    password2 = CommonFields.get_password_field(True, "Повторите пароль", attrs={"class": "form-control"})
    name = CommonFields.get_name_field(True, attrs={"class": "form-control"})


class NewVotingForm(forms.Form):
    __tnames = DB_VotingTools.voting_type_names
    title = CommonFields.get_voting_title_field(True, label="Название", attrs={"class": "form-control col-sm-9"})
    description = CommonFields.get_description_field(False, attrs={"class": "w-100"})
    type = forms.ChoiceField(label="Тип голосования", choices=((0, __tnames[0]), (1, __tnames[1]), (2, __tnames[2])),
                             required=True)
    show_votes_before_end = forms.BooleanField(label="Показывать статистику голосов до окончания", required=False)
    anonymous = forms.BooleanField(label="Скрывать соответствие голосов и участников (анонимность)", required=False)


class AddVoteVariantForm(forms.Form):
    voting_title = CommonFields.get_voting_title_field(True)
    description = CommonFields.get_description_field(True, label="Описание варианта")


class VoteForm(forms.Form):
    answer = forms.CharField(label="", min_length=1, required=True,
                             widget=forms.HiddenInput(attrs={"id": "answer_tag"}))


class SearchVotingForm(forms.Form):
    author_login = CommonFields.get_login_field(False, "Логин автора",
                                                attrs={"class": "form-control col-sm-9 ml-4", "style": "height: 45px"})
    voting_title = CommonFields.get_voting_title_field(False, attrs={"class": "form-control col-sm-9 ml-4"})
    started_option = CommonFields.get_filter_option_field("Фильтрация начатых",
                                                          attrs={"class": "custom-select col-sm-9 ml-4"})
    completed_option = CommonFields.get_filter_option_field("Фильтрация законченных",
                                                            attrs={"class": "custom-select col-sm-9 ml-4"})
    show_votes_before_end_option = CommonFields.get_filter_option_field(
        "Фильтрация показывающих статистику до завершения", attrs={"class": "custom-select col-sm-9 ml-4"})
    anonymous_option = CommonFields.get_filter_option_field("Фильтрация анонимных",
                                                            attrs={"class": "custom-select col-sm-9 ml-4"})
    offset = CommonFields.get_invisible_field(forms.IntegerField, "offset_tag", 0)


class ManageVotingForm(forms.Form):
    description = CommonFields.get_description_field(False, label="Описание варианта",
                                                     attrs={"class": "w-100", "rows": "20"})
    action = CommonFields.get_invisible_field(forms.CharField, "action_tag", '')


class ProfileForm(forms.Form):
    name = CommonFields.get_name_field(False)
    about = CommonFields.get_description_field(False, label="О себе")
    password = CommonFields.get_password_field(False)
    new_password = CommonFields.get_password_field(False)
    action = CommonFields.get_invisible_field(forms.CharField, "action_tag", '')
