from django.contrib.auth.models import User
from django.db import models


def get_sentinel_user():
    return User.objects.get_or_create(username='deleted')[0]


#class User:
    # first_name - имя
    # email - email
    # username - логин
    # password - хэш пароля
    # date_joined - дата регистрации


class UserData(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    activated = models.BooleanField
    extra_info = models.TextField


class Voting(models.Model):
    aut_hor = models.ForeignKey(to=User, on_delete=models.SET(get_sentinel_user))
    title = models.TextField
    description = models.TextField
    type = models.IntegerField
    show_votes_before_end = models.BooleanField
    anonymous = models.BooleanField
    completed = models.BooleanField


class VoteVariant(models.Model):
    voting = models.ForeignKey(to=Voting, on_delete=models.CASCADE)
    description = models.TextField


class VoteFact(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.SET(get_sentinel_user))
    voting = models.ForeignKey(to=Voting, on_delete=models.CASCADE)
    answer = models.BigIntegerField #0 if user is anonym


class VotingAbuse(models.Model):
    abuser = models.ForeignKey(to=User, on_delete=models.SET(get_sentinel_user))
    voting = models.ForeignKey(to=Voting, on_delete=models.CASCADE)
    description = models.TextField