# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, reverse, HttpResponse
from .models import *
from django.contrib import messages
from ..belt_review.models import User
# Create your views here.
def index(request):
    return render(request, "books_app/index.html",{'reviews': Review.objects.order_by("-created_at")[0:3],'books':Book.objects.all()})
def add(request):
    return render(request, "books_app/add.html",{'authors' : Author.objects.order_by("id")})
def view(request,book_id):
    content = {
        'book': Book.objects.get(id = book_id),
        'reviews': Review.objects.filter(books_id = book_id),
        'id': book_id
    }
    return render(request, "books_app/view.html",content)
#process route#
def add_process(request):
    if request.method == "POST":
        if request.POST['rev_submit']:
            errors = Review.objects.review_validator(request.POST)
            if len(errors):
                for tag, error in errors.iteritems():
                    messages.error(request, error, extra_tags=tag)
                return redirect(reverse('view',kwargs={'book_id': request.POST['id']}))
            else:
                Review.objects.create(reviewer = User.objects.get(name = request.session['name']),books_id = Book.objects.get(id = request.POST['id']).id,review = request.POST['add_review'], rating = request.POST['rate'])
                return redirect(reverse("view",kwargs={'book_id': request.POST['id']}))
        else:
            print "no"
        errors = Book.objects.add_validator(request.POST)
        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags=tag)
            return redirect(reverse('add'))
        errors = Author.objects.add_validator(request.POST)
        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags=tag)
            return redirect(reverse('add'))
        errors = Review.objects.add_validator(request.POST)
        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags=tag)
            return redirect(reverse('add'))
        else:
            ptitle = request.POST['title']
            preview = request.POST['review']
            prating = request.POST['rating']
            if request.POST['add_author'] == "":
                Book.objects.create(authors = Author.objects.get(name = request.POST['author']),title = ptitle)
                Review.objects.create(reviewer = User.objects.get(id = 1),books = Book.objects.get(title = ptitle),review = preview,rating = prating)
                return redirect(reverse("view",kwargs={'book_id': Book.objects.get(title = ptitle).id}))
            else: 
                pauthor = request.POST['add_author']
                Author.objects.create(name = pauthor)
                Book.objects.create(authors = Author.objects.get(name = pauthor),title = ptitle)
                Review.objects.create(reviewer = User.objects.get(id = 1),books = Book.objects.get(title = ptitle),review = preview,rating = prating)
                return redirect(reverse("view",kwargs={'book_id':Book.objects.get(title = ptitle).id}))
    else:
        return redirect(reverse("view",kwargs={'book_id': 1}))
def delete_process(request):
    if request.method == "POST":
        if request.POST['return_index']:
            Review.objects.get(id = request.POST['rev_id']).delete()
            return redirect(reverse("index"))
        else:
            Review.objects.get(id = request.POST['rev_id']).delete()
            return redirect(reverse("view",kwargs={'book_id': Book.objects.get(id = request.POST['book_id']).id}))
    else:
        return redirect(reverse("view",kwargs={'book_id': Book.objects.get(id = request.POST['book_id']).id}))