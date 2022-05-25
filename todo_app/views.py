from django.views.generic import ListView, CreateView, UpdateView

from .forms import *
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


class ToDoListCreate(CreateView):
    form_class = AddToDoListForm
    template_name = 'todo_app/todo_list_form.html'
    extra_context = {'title': 'Add a new list'}


class ToDoItemCreate(CreateView):
    form_class = AddToDoItemForm
    template_name = 'todo_app/todo_item_form.html'

    def get_initial(self):
        initial_data = super(ToDoItemCreate, self).get_initial()
        todo_list = ToDoList.objects.get(id=self.kwargs['list_id'])
        initial_data['todo-list'] = todo_list
        return initial_data

    def get_context_data(self, **kwargs):
        context = super(ToDoItemCreate, self).get_context_data()
        todo_list = ToDoList.objects.get(id=self.kwargs['list_id'])
        context['todo_list'] = todo_list
        context['title'] = 'Create a new item'
        return context


class ToDoItemUpdate(UpdateView):
    model = ToDoItem
    form_class = AddToDoItemForm
    template_name = 'todo_app/todo_item_form.html'

    def get_context_data(self, **kwargs):
        context = super(ToDoItemUpdate, self).get_context_data()
        context['todo_list'] = self.object.todo_list
        context['title'] = 'Edit item'
        return context
