from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from mt_projects.project.models import Project
from mt_projects.project.forms import ProjectForm
from mt_projects.todo.models import Todo
from mt_projects.todo.forms import TodoForm


# Create your views here.
@login_required
def projects(request):
    projects = Project.objects.all()
    todos = Todo.objects.all()
    is_employee = False
    for group in request.user.groups.all():
        if group.name == 'Employee':
            is_employee = True
    if request.user.is_superuser or is_employee:
        for project in projects:
            project_todos = todos.filter(project=project)
            if project_todos:
                project.todos_count = len(project_todos)
                project.finished_todos = len(project_todos.filter(is_finished=True))
                project.completion_percentage = int(100 * (float(project.finished_todos) / project.todos_count))

        return render(request, 'project/projects.html', {
            'projects': projects,
            'is_freelancer': False
        })
    else:
        user_projects = []
        for project in projects:
            project_todos = todos.filter(project=project)
            for project_todo in project_todos:
                if request.user == project_todo.user:
                    user_projects.append(project)
                    break
            if request.user in project.responsible.all() and project not in user_projects:
                user_projects.append(project)
        for project in user_projects:
            project_todos = todos.filter(project=project)
            if project_todos:
                project.todos_count = len(project_todos)
                project.finished_todos = len(project_todos.filter(is_finished=True))
                project.completion_percentage = int(100 * (float(project.finished_todos) / project.todos_count))
        return render(request, 'project/projects.html', {
            'projects': user_projects,
            'is_freelancer': True
        })


@login_required
def new_project(request):
    is_employee = False
    for group in request.user.groups.all():
        if group.name == 'Employee':
            is_employee = True
    if request.user.is_superuser or is_employee:
        if request.method == 'GET':
            form = ProjectForm()
            return render(request, 'project/new.html', {
                'form': form
            })
        elif request.method == 'POST':
            form = ProjectForm(request.POST)
            print form
            if form.is_valid():
                form.save()
                messages.add_message(
                    request,
                    messages.SUCCESS,
                    'Opprettet prosjektet ' + form.cleaned_data['name'] + '!'
                )
                return HttpResponseRedirect('/project/')
            return render(request, 'project/new.html', {
                'form': form
            })
    raise Http404


@login_required
def edit_project(request, project_id):
    is_employee = False
    for group in request.user.groups.all():
        if group.name == 'Employee':
            is_employee = True
    if request.user.is_superuser or is_employee:
        if request.method == 'GET':
            project = get_object_or_404(Project, id=project_id)
            form = ProjectForm(instance=project)
            return render(request, 'project/edit.html', {
                'form': form
            })
        elif request.method == 'POST':
            project = get_object_or_404(Project, id=project_id)
            form = ProjectForm(request.POST, instance=project)
            if form.is_valid():
                form.save()
                messages.add_message(
                    request,
                    messages.SUCCESS,
                    'Lagret endringer i prosjektet "' + form.cleaned_data['name'] + '"!'
                )
                return HttpResponseRedirect('/project/'+project_id+'/')
            return render(request, 'project/edit.html', {
                'form': form
            })
    raise Http404


@login_required
def add_todo(request, project_id):
    is_employee = False
    for group in request.user.groups.all():
        if group.name == 'Employee':
            is_employee = True
    if request.user.is_superuser or is_employee:
        if request.method == 'GET':
            form = TodoForm()
            return render(request, 'project/add_todo.html', {
                'form': form
            })
        elif request.method == 'POST':
            form = TodoForm(request.POST)
            if form.is_valid():
                todo = form.save()
                todo.project = Project.objects.get(id=project_id)
                todo.save()
                messages.add_message(
                    request,
                    messages.SUCCESS,
                    'La til oppgaven "' + todo.title + '" i prosjektet ' + todo.project.name + '!'
                )
                return HttpResponseRedirect('/project/' + project_id + '/')
            return render(request, 'project/add_todo.html', {
                'form': form
            })
    raise Http404


@login_required
def delete_todo(request, project_id, todo_id):
    project = Project.objects.get(id=project_id)
    todo = Todo.objects.get(id=todo_id)
    if not project == todo.project:
        raise Http404
    is_employee = False
    for group in request.user.groups.all():
        if group.name == 'Employee':
            is_employee = True
    if request.user.is_staff or is_employee or request.user == todo.user:
        todo.delete()
        messages.add_message(
            request,
            messages.WARNING,
            u'Oppgaven "' + todo.title + '" er slettet fra ' + '"' + project.name + '"!'
        )
    return HttpResponseRedirect('/project/' + project_id + '/')


@login_required
def edit_todo(request, project_id, todo_id):
    is_employee = False
    todo = get_object_or_404(Todo, id=todo_id)
    project = get_object_or_404(Project, id=project_id)
    for group in request.user.groups.all():
        if group.name == 'Employee':
            is_employee = True
    if request.user.is_superuser or is_employee:
        if request.method == 'GET':
            form = TodoForm(instance=todo)
            return render(request, 'project/edit_todo.html', {
                'form': form
            })
        elif request.method == 'POST':
            form = TodoForm(request.POST, instance=todo)
            if form.is_valid():
                todo = form.save()
                todo.save()
                messages.add_message(
                    request,
                    messages.SUCCESS,
                    u'Oppgaven "' + todo.title + '" er endret i ' + '"' + project.name + '"!'
                )
                return HttpResponseRedirect('/project/' + project_id + '/')
            return render(request, 'project/edit_todo.html', {
                'form': form
            })
    raise Http404


@login_required
def project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    if not project:
        raise Http404
    todos = Todo.objects.all().filter(project=project)
    if todos:
        finished_todos = todos.filter(is_finished=True)
        remaining_todos = todos.filter(is_finished=False)
        project.remaining_todos = remaining_todos
        project.finished_todos = finished_todos
    is_employee = False
    for group in request.user.groups.all():
        if group.name == 'Employee':
            is_employee = True
    if request.user.is_superuser or is_employee:
        return render(request, 'project/project.html', {
            'project': project,
            'is_freelancer': False
        })
    else:
        project_todos = Todo.objects.all().filter(project=project)
        for project_todo in project_todos:
            if request.user == project_todo.user:
                return render(request, 'project/project.html', {
                    'project': project,
                    'is_freelancer': True
                })
        if request.user in project.responsible.all():
            return render(request, 'project/project.html', {
                'project': project,
                'is_freelancer': True
            })
    raise Http404


@login_required
def schedule(request):
    projects = Project.objects.all()
    todos = Todo.objects.all()
    is_employee = False
    for group in request.user.groups.all():
        if group.name == 'Employee':
            is_employee = True
    if request.user.is_superuser or is_employee:
        for project in projects:
            project_todos = todos.filter(project=project)
            if project_todos:
                project.todos_count = len(project_todos)
                project.finished_todos = len(project_todos.filter(is_finished=True))
                project.completion_percentage = int(100 * (float(project.finished_todos) / project.todos_count))
        return render(request, 'project/schedule.html', {
            'projects': projects,
            'length': len(projects)
        })
    else:
        user_projects = []
        for project in projects:
            project_todos = todos.filter(project=project)
            for project_todo in project_todos:
                if request.user == project_todo.user:
                    user_projects.append(project)
                    break
            if request.user in project.responsible.all() and project not in user_projects:
                user_projects.append(project)
        return render(request, 'project/schedule.html', {
            'projects': user_projects,
            'length': len(user_projects)
        })
    raise Http404
