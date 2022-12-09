from django.db import models
from django.contrib.auth.models import User

value = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)]


# Create your models here.
class Value_choosed(models.Model):
    user_name = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    value = models.IntegerField()
    count = models.IntegerField(default=0)
    datetime = models.CharField(null=True,max_length=50)
    spin = models.BooleanField(default=False)
    bet_amount = models.IntegerField(default=0)




class Value_set(models.Model):
    value = models.IntegerField(choices=value)


class spin_time(models.Model):
    hours = models.IntegerField()
    minutes = models.IntegerField()
    hint = models.BooleanField(default=False)


class wallet(models.Model):
    total_balance = models.IntegerField()
