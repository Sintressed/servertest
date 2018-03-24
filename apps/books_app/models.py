# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..belt_review.models import User
class AuthorManager(models.Manager):
    def add_validator(self,postData):
        errors = {}
        name = postData['add_author']
        if self.filter(name = name):
            errors['authors'] = "Author already exists please select from dropdown"
            return errors
        else:
            if len(postData['author']) == 0:
                if len(postData['add_author']) == 0:
                    errors['author'] = "Please either select an author or write in a new one"
                else:
                    if postData['author'].isdigit():
                        errors['author'] = "Author field cannot have digits"
        return errors
class BookManager(models.Manager):
    def add_validator(self,postData):
        errors = {}
        if len(postData['title']) == 0:
            errors['title'] = "Title field required"
        if self.filter(title = postData['title']):
            errors['exist'] = "Book Title already exists"
        return errors
class ReviewManager(models.Manager):
    def add_validator(self,postData):
        errors = {}
        if len(postData['review']) == 0:
            errors['review'] = "Review field required"
        return errors
    def review_validator(self,postData):
        errors = {}
        print "review",postData['add_review']
        if len(postData['add_review']) == 0:
            print "error"
            errors['review'] = "Review field cannot be blank"
        return errors
# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = AuthorManager()
class Book(models.Model):
    authors = models.ForeignKey(Author)
    title = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = BookManager()
class Review(models.Model):
    reviewer = models.ForeignKey(User)
    books = models.ForeignKey(Book)
    review = models.CharField(max_length = 255)
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = ReviewManager()