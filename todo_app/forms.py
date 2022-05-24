from django import forms
from .models import *


class AddToDoListForm(forms.ModelForm):
    class Meta:
        model = ToDoList
        fields = ['title']
