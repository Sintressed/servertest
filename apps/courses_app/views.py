# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect,reverse
from .models import *
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,"courses_app/index.html", {'courseid' : Course.objects.order_by("id")})
def prompt(request,courseid):
    return render(request,"courses_app/prompt.html",{'courseid' : Course.objects.get(id = courseid)})
#---Post Routes---#
def add(request):
    if request.method == "POST":
        errors = Course.objects.basic_validator(request.POST)
        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags=tag)
            return redirect(reverse('index'))
        else:
            Course.objects.create(name = request.POST['name'],description = request.POST['description'])
            return redirect(reverse("index"))
    else:
        return redirect(reverse("index"))
def destroy(request):
    if request.method == "POST":
        Course.objects.get(id = request.POST['id']).delete()
        return redirect(reverse("index"))
    else:
        return redirect(reverse("index"))