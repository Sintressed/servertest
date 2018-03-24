# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re
import bcrypt

# Create your models here.
class LRManager(models.Manager):
    def register_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')     
        if self.filter(email_address = postData['email_address']):
            errors['exist'] = "User email Already exists, please log in"
            return errors
        else:
            if len(postData['first_name']) < 2:
                if len(postData['first_name']) <= 0:
                    errors['first_name'] = "First name field required"
                else:
                    errors["first_name"] = "First name has to be more than 2 characters long"
            for letter in postData['first_name']:
                if letter.isdigit():
                    errors['first_name'] = "First name can only have letters"
            if len(postData['last_name']) < 2:
                if len(postData['last_name']) <= 0:
                    errors['last_name'] = "Last name field required"
                else:
                    errors["last_name"] = "Last name has to be more than 2 characters long"
            for letter in postData['last_name']:
                if letter.isdigit():
                    errors['last_name'] = "Last name can only have letters"
            if not EMAIL_REGEX.match(postData['email_address']):
                errors["email"] = "Email address invalid"
            if len(postData['email_address']) == 0:
                errors['email'] = "Email address field required"
            if len(postData['password']) < 8:
                if len(postData['password']) <= 0:
                    errors['password'] = "Password field required"
                else:
                    errors["password"] = "Password has to be more than 8 characters long"
            if postData['confirm_password'] != postData['password']:
                errors['confirm'] = "Passwords don't match"
            return errors
    def login_validator(self, postData):
        errors = {} 
        if self.filter(email_address = postData['login_email_address']):
            x = LoginRegistration.objects.get(email_address = postData['login_email_address'])
            if bcrypt.checkpw(postData['login_password'].encode(), x.password.encode()) != True:
                errors['invalid_password'] = "Invalid Password!"
        else:
            errors['unregistered'] = "Email invalid or not in database!"
        return errors
class LoginRegistration(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email_address = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    objects = LRManager()
    
    