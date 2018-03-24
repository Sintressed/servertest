# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect,HttpResponse, reverse
import bcrypt
from django.contrib import messages
from .models import *
from ..books_app.models import Review,Book
# Create your views here.
def index(request):
    return render(request, "belt_review/index.html")
def user(request,user_id):
    content = {
        'user': User.objects.get(id = user_id),
        'review':Review.objects.filter(reviewer_id = user_id).count(),
        'books': Review.objects.filter(reviewer_id = user_id)
    }
    return render(request,"belt_review/user.html",content)
#POST routes
def process_login(request):
    if request.method == "POST":
        errors = User.objects.login_validator(request.POST)
        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags=tag)
            return redirect('/')
        else:
            request.session['name'] = User.objects.get(email= request.POST['login_email']).name
            return redirect("/books/")
    else:
        return redirect(reverse("index"))
def process_register(request):
    if request.method == "POST":
        errors = User.objects.register_validator(request.POST)
        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags=tag)
                return redirect(reverse('index'))
        else:
            name = request.POST['name']
            alias = request.POST['alias']
            email = request.POST['email']
            password = request.POST['password']
            hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
            User.objects.create(name = name, alias = alias, email = email, password = hashed)
            request.session['name'] = User.objects.get(email = request.POST['email']).name
            print "register successful"
            return redirect(reverse("index"))
    else:
        return redirect(reverse("index"))
