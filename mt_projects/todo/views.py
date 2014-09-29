# coding=utf8
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from mt_projects.todo.models import Todo
from mt_projects.todo.forms import TodoFormWithProject
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.
@login_required
def todo(request):
    todos = Todo.objects.all()
    users = User.objects.all()
    is_employee = False
    for group in request.user.groups.all():
        if group.name == 'Employee':
            is_employee = True
    if request.user.is_superuser or is_employee:
        for user in users:
            user.todos = todos.filter(user=user)
        return render(request, 'todo/todos.html', {'users': users, 'is_freelancer': False})
    else:
        user = request.user
        user.todos = todos.filter(user=user)
        return render(request, 'todo/todos.html', {'users': [user],  'is_freelancer': True})


@login_required
def finish(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    is_employee = False
    for group in request.user.groups.all():
        if group.name == 'Employee':
            is_employee = True
    if not (request.user.is_staff or is_employee or request.user == todo.user):
        messages.add_message(
            request,
            messages.DANGER,
            u'Du har ikke tilgang til å endre oppgaven "' + todo.title + '"!'
        )
    else:
        todo.is_finished = True
        todo.save()
        messages.add_message(
            request,
            messages.SUCCESS,
            u'Oppgaven "' + todo.title + u'" er ferdig. Gratulerer!'
        )
    return HttpResponseRedirect('/todo/')


@login_required
def reopen(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    is_employee = False
    for group in request.user.groups.all():
        if group.name == 'Employee':
            is_employee = True
    if not (request.user.is_staff or is_employee or request.user == todo.user):
        messages.add_message(
            request,
            messages.WARNING,
            u'Du har ikke tilgang til å endre oppgaven "' + todo.title + '"!'
        )
    else:
        todo.is_finished = False
        todo.save()
        messages.add_message(
            request,
            messages.WARNING,
            u'Oppgaven "' + todo.title + u'" er gjenåpnet. Gjorde du den ikke ordentlig?'
        )
    return HttpResponseRedirect('/todo/')


@login_required
def delete(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    is_employee = False
    for group in request.user.groups.all():
        if group.name == 'Employee':
            is_employee = True
    if request.user.is_staff or is_employee or request.user == todo.user:
        todo.delete()
        messages.add_message(
            request,
            messages.WARNING,
            u'Oppgaven "' + todo.title + ' er slettet"!'
        )
    return HttpResponseRedirect('/todo/')


@login_required
def add(request):
    is_employee = False
    for group in request.user.groups.all():
        if group.name == 'Employee':
            is_employee = True
    if request.user.is_superuser or is_employee:
        if request.method == 'GET':
            form = TodoFormWithProject()
            return render(request, 'project/add_todo.html', {
                'form': form
            })
        elif request.method == 'POST':
            form = TodoFormWithProject(request.POST)
            if form.is_valid():
                todo = form.save()
                todo.save()
                messages.add_message(
                    request,
                    messages.SUCCESS,
                    'La til oppgaven  "' + todo.title + '"!'
                )
                return HttpResponseRedirect('/todo/')
            return render(request, 'project/add_todo.html', {
                'form': form
            })
    raise Http404


@login_required
def edit(request, todo_id):
    is_employee = False
    todo = get_object_or_404(Todo, id=todo_id)
    for group in request.user.groups.all():
        if group.name == 'Employee':
            is_employee = True
    if request.user.is_superuser or is_employee:
        if request.method == 'GET':
            form = TodoFormWithProject(instance=todo)
            return render(request, 'project/edit_todo.html', {
                'form': form
            })
        elif request.method == 'POST':
            form = TodoFormWithProject(request.POST, instance=todo)
            if form.is_valid():
                todo = form.save()
                todo.save()
                messages.add_message(
                    request,
                    messages.SUCCESS,
                    'Endret oppgaven "' + todo.title + '"!'
                )
                return HttpResponseRedirect('/todo/')
            return render(request, 'project/edit_todo.html', {
                'form': form
            })
    raise Http404
