from django.contrib.auth.decorators import login_required
from django.http import request
from django.shortcuts import redirect, render
from django.contrib.auth.models import User

from .forms import ProjectForm, TaskForm, CommentForm, AddMemberForm
from .models import Project, Task


def home(request):
    return render(request, 'home.html')


@login_required
def dashboard(request):
    projects = Project.objects.filter(
        members=request.user
    ).order_by('-updated_at')

    tasks = Task.objects.filter(
        project__in=projects
    )

    context = {
        'project_count': projects.count(),
        'task_count': tasks.count(),
        'completed_count': tasks.filter(status='done').count(),
        'projects': projects,
    }

    return render(request, 'dashboard.html', context)


@login_required
def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)

        if form.is_valid():
            project = form.save(commit=False)
            project.owner = request.user
            project.save()

            project.members.add(request.user)

            return redirect('dashboard')

    else:
        form = ProjectForm()

    return render(
        request,
        'projects/create_project.html',
        {'form': form}
    )

@login_required
def edit_project(request, project_id):
    project = Project.objects.filter(
        id=project_id,
        owner=request.user
    ).first()

    if not project:
        return redirect('dashboard')

    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)

        if form.is_valid():
            form.save()

            return redirect(
                'project_detail',
                project_id=project.id
            )
    else:
        form = ProjectForm(instance=project)

    return render(
        request,
        'projects/edit_project.html',
        {
            'form': form,
            'project': project,
        }
    )


@login_required
def project_detail(request, project_id):
    project = Project.objects.filter(
        id=project_id,
        members=request.user
    ).first()

    if not project:
        return redirect('dashboard')

    tasks = project.tasks.all().order_by('-created_at')

    if request.method == 'POST':
        member_form = AddMemberForm(request.POST)

        if member_form.is_valid():
            username = member_form.cleaned_data['username']

            user_to_add = User.objects.filter(
                username=username
            ).first()

            if user_to_add:
                project.members.add(user_to_add)

            return redirect(
                'project_detail',
                project_id=project.id
            )
    else:
        member_form = AddMemberForm()

    return render(
        request,
        'projects/project_detail.html',
        {
            'project': project,
            'tasks': tasks,
            'member_form': member_form,
        }
    )

@login_required
def remove_member(request, project_id, user_id):
    project = Project.objects.filter(
        id=project_id,
        owner=request.user
    ).first()

    if not project:
        return redirect('dashboard')

    member = User.objects.filter(id=user_id).first()

    if member and member != project.owner:
        project.members.remove(member)

    return redirect(
        'project_detail',
        project_id=project.id
    )

@login_required
def create_task(request, project_id):
    project = Project.objects.filter(
        id=project_id,
        members=request.user
    ).first()

    if not project:
        return redirect('dashboard')

    if request.method == 'POST':
        form = TaskForm(request.POST, project=project)
        if form.is_valid():
            task = form.save(commit=False)
            task.project = project
            task.save()

            return redirect(
                'project_detail',
                project_id=project.id
            )

    else:
        form = TaskForm(project=project)

    return render(
        request,
        'tasks/create_task.html',
        {
            'form': form,
            'project': project,
        }
    )


@login_required
def edit_task(request, project_id, task_id):
    project = Project.objects.filter(
        id=project_id,
        members=request.user
    ).first()

    if not project:
        return redirect('dashboard')

    task = Task.objects.filter(
        id=task_id,
        project=project
    ).first()

    if not task:
        return redirect(
            'project_detail',
            project_id=project.id
        )

    if request.method == 'POST':
        form = TaskForm(
    request.POST,
    instance=task,
    project=project
)

        if form.is_valid():
            form.save()

            return redirect(
                'task_detail',
                project_id=project.id,
                task_id=task.id
            )
    else:
        form = TaskForm(
    instance=task,
    project=project
)

    return render(
        request,
        'tasks/edit_task.html',
        {
            'form': form,
            'project': project,
            'task': task,
        }
    )


@login_required
def delete_task(request, project_id, task_id):
    project = Project.objects.filter(
        id=project_id,
        members=request.user
    ).first()

    if not project:
        return redirect('dashboard')

    task = Task.objects.filter(
        id=task_id,
        project=project
    ).first()

    if not task:
        return redirect(
            'project_detail',
            project_id=project.id
        )

    if request.method == 'POST':
        task.delete()

        return redirect(
            'project_detail',
            project_id=project.id
        )

    return redirect(
        'task_detail',
        project_id=project.id,
        task_id=task.id
    )

@login_required
def delete_project(request, project_id):
    project = Project.objects.filter(
        id=project_id,
        owner=request.user
    ).first()

    if not project:
        return redirect('dashboard')

    if request.method == 'POST':
        project.delete()
        return redirect('dashboard')

    return redirect(
        'project_detail',
        project_id=project.id
    )



@login_required
def task_detail(request, project_id, task_id):
    project = Project.objects.filter(
        id=project_id,
        members=request.user
    ).first()

    if not project:
        return redirect('dashboard')

    task = Task.objects.filter(
        id=task_id,
        project=project
    ).first()

    if not task:
        return redirect(
            'project_detail',
            project_id=project.id
        )

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.task = task
            comment.author = request.user
            comment.save()

            return redirect(
                'task_detail',
                project_id=project.id,
                task_id=task.id
            )
    else:
        comment_form = CommentForm()

    comments = task.comments.all().order_by('-created_at')

    return render(
        request,
        'tasks/task_detail.html',
        {
            'project': project,
            'task': task,
            'comment_form': comment_form,
            'comments': comments,
        }
    )