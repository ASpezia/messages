# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.timezone import get_current_timezone
from time import strptime, localtime, strftime
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from models import *
import bcrypt
# Create your views here.

def register(request):
    errors = User.objects.basic_validator(request.POST)
    print "line 11"
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
            print errors
        print errors
        return redirect("/")
        print "whats going on"
    else:
        pw = request.POST["password"]
        hash1 = bcrypt.hashpw(pw.encode(), bcrypt.gensalt())
        b = User.objects.create(name=request.POST["name"], email=request.POST["email"], password=hash1)
        #above created a user, and stored it in a variable called b
        request.session["user_id"] = b.id #stored the user id in session
        request.session["name"] = b.name #stored the ailias in session
        print "*****", b.name
    return redirect("/messages")

def login(request):
    errors = User.objects.login_validator(request.POST)
    print errors
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
            print errors
        return redirect("/")
    else:
        user = User.objects.get(email = request.POST["email"]) #get the user based on their email. This could be any column in the User table
        request.session["user_id"] = user.id #store user id in session
        request.session['name'] = user.name
        print "after login"
        return redirect("/messages")

def index(request):
    return render(request,'index.html')



def add(request):
#    errors = Message.objects.add_validator(request.POST)
#    if len(errors):
#        for tag, error in errors.iteritems():
#            messages.error(request, error, extra_tags=tag)
#        return redirect("/messages")
#    else:
        a = User.objects.get(name=request.session['name'])
        Message.objects.create(messages=request.POST["messages"], user = a)
        return redirect("/messages")

def messages(request):
    m = User.objects.get(id=request.session["user_id"])

    context = {
        "my_messages" : Message.objects.filter(user = m),
        "other_messages" : Message.objects.all().exclude(messages =request.session["user_id"])
    }
    return render(request, 'messages.html', context)

def delete_msg(request, id):
    d = Message.objects.get(id=id)
    d.delete()
    return redirect('/messsages')

def edit_msg(request, id):
    context = {
        others : User.objects.all().exclude(id = request.session["user_id"]),
        "message_id" : Message.objects.get(id=id),
        }
    print context
    return render(request, 'profile.html', context)

def save_msg(request, id):
    errors = Message.objects.add_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect("/profile/" + id)
    else:
        s = Message.objects.get(id=id)
        s.message = request.POST["message"]
        s.save()
        return redirect("/messages")
def logout(request): #dome
    return render(request,'index.html')

def logoutfunc(request): #dome we need a seperate function and url for the logout method
    request.session.flush()
    return redirect('/logout')
