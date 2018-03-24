# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class CourseManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) <= 5:
            errors["name"] = "name has to be more than 5 characters long"
        if len(postData['description']) <= 15:
            errors["description"] = "description has to be more than 15 characters long"
        return errors
class Course(models.Model):
    name = models.CharField(max_length = 255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    objects = CourseManager()
