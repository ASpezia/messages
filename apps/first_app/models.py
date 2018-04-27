# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re
import bcrypt
password_regex = re.compile('^(?=\S{6,20}$)(?=.*?\d)(?=.*?[a-z])(?=.*?[A-Z])(?=.*?[^A-Za-z\s0-9])')
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.

class RegManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if User.objects.filter(email = postData["email"]).exists():
            errors["email"] = "Email already exists"
        #if count > 0:
        #    errors["email"] = "Email already registered"
        if len(postData["name"]) < 3:
            errors["name"] = " name should be more than 3 characters"
        if len(postData["email"]) < 3:
            errors["email"] = "Email should be more than 3 characters"
        if len(postData["password"]) < 8:
            errors["password"] = "Password should be more thatn 8 characters"
        # elif not password_regex.match(postData["password"]):
        #     errors["password"] = "Invalid password"
        if postData["password"] != postData["confirm_password"]:
            errors["confirm_password"] = "Password confirmation does not match"
            print errors
        return errors
    def login_validator(self, postData):
        errors = {}
        if len(postData["email"]) < 3:
            errors["email"] = "Email should be more than 3 characters"
        if len(postData["password"]) < 8:
            errors["password"] = "Password must be longer than 8 characters"
        check = User.objects.filter(email=postData["email"])
        if len(check) == 0:
            errors["email"] = "Must enter an email address"
            return errors
        if not bcrypt.checkpw(postData["password"].encode(), check[0].password.encode()):
            errors["password"] = "Password doesn't match"
        return errors
    def pw_validator(self, postData):
        errors = {}
        if len(postData["password"]) < 8:
            errors["password"] = "Password must be longer than 8 characters"
        if postData["password"] != postData["confirm_password"]:
            errors["confirm_password"] = "Password confirmation does not match"
        return errors
    def add_validator(self, postData):
        errors = {}
        if len(postData["messages"]) < 1:
             errors["messages"] = "Messages cannot be empty"
        return errors




# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = RegManager()

class Message(models.Model):
    messages = models.CharField(max_length=255)
    others_messages = models.CharField(max_length=255)
    user = models.ForeignKey(User, related_name = "messages")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = RegManager()
