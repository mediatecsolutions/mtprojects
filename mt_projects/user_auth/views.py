# coding=utf8
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def login_view(request):
    if request.method == 'GET':
        return render(request, 'user_auth/login.html')
    elif request.method == 'POST':
        try:
            user_object = User.objects.get(email=request.POST['email'])
        except:
            messages.add_message(
                request,
                messages.WARNING,
                'Noe gikk galt under innlogging. Skrev du alt riktig?!'
            )
            return render(request, 'user_auth/login.html')
        user = authenticate(username=user_object.username, password=request.POST['password'])
        if user is not None:
            if user.is_active:
                login(request, user)
                messages.add_message(
                    request,
                    messages.SUCCESS,
                    'Velkommen, '+ user.first_name + ' ' + user.last_name + '!'
                )
                return HttpResponseRedirect('/')
    messages.add_message(
        request,
        messages.WARNING,
        u'Noe gikk galt under innlogging. Skrev du alt riktig?!'
    )
    return render(request, 'user_auth/login.html')

def logout_view(request):
    messages.add_message(
        request,
        messages.SUCCESS,
        u'Du er nå logget ut. på gjensyn, ' + request.user.first_name + '!'
    )
    logout(request)
    return HttpResponseRedirect('/login/')
