from django.db import models
from django import forms

class Registration(models.Model):
        First_Name = models.CharField(max_length=20)
        Last_Name = models.CharField(max_length=20)
        Email = models.EmailField()
        Password = models.CharField(max_length=20)


class Login(models.Model):
        UserId = models.EmailField()
        password = models.CharField(max_length=20)



