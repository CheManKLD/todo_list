from django.views.generic import ListView

from .models import *


class ToDoListView(ListView):
    model = ToDoList
    template_name = 'todo_app/index.html'
