from django import forms
from .models import *


class AddToDoListForm(forms.ModelForm):
    class Meta:
        model = ToDoList
        fields = ['title']


class AddToDoItemForm(forms.ModelForm):
    class Meta:
        model = ToDoItem
        fields = [
            'todo_list',
            'title',
            'description',
            'due_date',
        ]
