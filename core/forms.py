from django import forms

from .models import Project, Task, Comment
from django.contrib.auth.models import User


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            'name',
            'description',
        ]

        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Enter project name'
            }),

            'description': forms.Textarea(attrs={
                'placeholder': 'Describe your project',
                'rows': 5
            }),
        }


class AddMemberForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter username'
        })
    )

    def clean_username(self):
        username = self.cleaned_data['username']

        if not User.objects.filter(username=username).exists():
            raise forms.ValidationError('User not found.')

        return username

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            'title',
            'description',
            'assigned_to',
            'status',
            'priority',
            'due_date',
        ]
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Enter task title'
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Describe the task',
                'rows': 5
            }),
            'due_date': forms.DateInput(attrs={
                'type': 'date'
            }),
        }

    def __init__(self, *args, project=None, **kwargs):
        super().__init__(*args, **kwargs)

        if project:
            self.fields['assigned_to'].queryset = project.members.all()


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'placeholder': 'Write a comment...',
                'rows': 4
            }),
        }