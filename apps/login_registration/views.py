# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect,HttpResponse, reverse, render
from .models import *
from django.contrib import messages
import bcrypt


# Create your views here.
def index(request):
    return render(request, "login_registration/index.html")
def success(request):
    return render(request, "login_registration/success.html")

#---Post Routes---#

def login_process(request):
    if request.method == "POST":
        errors = LoginRegistration.objects.login_validator(request.POST)
        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags=tag)
            return redirect(reverse('index'))
        else:
            request.session['name'] = LoginRegistration.objects.get(email_address = request.POST['login_email_address']).first_name
            return redirect(reverse("success"))
    else:
        return redirect(reverse("index"))
def register_process(request):
    if request.method == "POST":
        errors = LoginRegistration.objects.register_validator(request.POST)
        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags=tag)
            return redirect(reverse('index'))
        else:
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email_address = request.POST['email_address']
            password = request.POST['password']
            hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
            LoginRegistration.objects.create(first_name = first_name, last_name = last_name, email_address = email_address, password = hashed)
            request.session['name'] = LoginRegistration.objects.get(email_address = request.POST['email_address']).first_name
            return redirect(reverse("success"))
        
    else:
        return redirect(reverse("index"))
