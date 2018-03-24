# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re
import bcrypt

# Create your models here.
class UserManager(models.Manager):
    def register_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')     
        if self.filter(name = postData['name']):
            errors['exist'] = "User email Already exists, please log in"
            return errors
        else:
            if len(postData['name']) < 2:
                if len(postData['name']) <= 0:
                    errors['name'] = "name field required"
                else:
                    errors["name"] = "name has to be more than 2 characters long"
            for letter in postData['name']:
                if letter.isdigit():
                    errors['name'] = "First name can only have letters"
            if len(postData['alias']) < 2:
                if len(postData['alias']) <= 0:
                    errors['alias'] = "Alias field required"
                else:
                    errors["alias"] = "alias has to be more than 2 characters long"
            if not EMAIL_REGEX.match(postData['email']):
                errors["email"] = "Email address invalid"
            if len(postData['email']) == 0:
                errors['email'] = "Email address field required"
            if len(postData['password']) < 8:
                if len(postData['password']) <= 0:
                    errors['password'] = "Password field required"
                else:
                    errors["password"] = "Password has to be more than 8 characters long"
            if postData['confirm'] != postData['password']:
                errors['confirm'] = "Passwords don't match"
            return errors
    def login_validator(self, postData):
        errors = {} 
        if self.filter(email = postData['login_email']):
            x = User.objects.get(email= postData['login_email'])
            if bcrypt.checkpw(postData['login_password'].encode(), x.password.encode()) != True:
                errors['invalid_password'] = "Invalid Password!"
        else:
            errors['unregistered'] = "Email invalid or not in database!"
        return errors
class User(models.Model):
    name = models.CharField(max_length = 255)
    alias = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    objects = UserManager()
