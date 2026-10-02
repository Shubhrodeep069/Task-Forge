from django.contrib import admin
from django.urls import include, path

from core.views import (
    create_project,
    create_task,
    dashboard,
    delete_project,
    delete_task,
    edit_project,
    edit_task,
    home,
    project_detail,
     remove_member,
    task_detail,

)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('dashboard/', dashboard, name='dashboard'),
    path('accounts/', include('accounts.urls')),

    path(
    'projects/create/',
    create_project,
    name='create_project'
),

path(
    'projects/<int:project_id>/',
    project_detail,
    name='project_detail'
),

path(
    'projects/<int:project_id>/tasks/create/',
    create_task,
    name='create_task'
),

path(
    'projects/<int:project_id>/tasks/<int:task_id>/',
    task_detail,
    name='task_detail'
),

path(
    'projects/<int:project_id>/tasks/<int:task_id>/edit/',
    edit_task,
    name='edit_task'
),
path(
    'projects/<int:project_id>/tasks/<int:task_id>/delete/',
    delete_task,
    name='delete_task'
),

path(
    'projects/<int:project_id>/delete/',
    delete_project,
    name='delete_project'
),

path(
    'projects/<int:project_id>/edit/',
    edit_project,
    name='edit_project'
),

path(
    'projects/<int:project_id>/members/<int:user_id>/remove/',
    remove_member,
    name='remove_member'
),
]