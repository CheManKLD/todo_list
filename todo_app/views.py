from django.views.generic import ListView

from .models import *


class ToDoListView(ListView):
    model = ToDoList
    template_name = 'todo_app/index.html'
    extra_context = {'list_selected': 0}


class ToDoItemView(ListView):
    model = ToDoItem
    template_name = 'todo_app/todo_list.html'

    def get_queryset(self):
        return ToDoItem.objects.filter(todo_list_id=self.kwargs['list_id'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['todo_list'] = ToDoList.objects.get(id=self.kwargs['list_id'])
        return context
