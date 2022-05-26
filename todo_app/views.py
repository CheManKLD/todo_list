from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .forms import AddToDoListForm, AddToDoItemForm
from .models import ToDoList, ToDoItem


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
    extra_context = {'template_title': 'Add a new list'}


class ToDoListDelete(DeleteView):
    model = ToDoList
    template_name = 'todo_app/todo_list_confirm_delete.html'
    extra_context = {'template_title': 'Delete list'}
    success_url = reverse_lazy('index')


class ToDoItemCreate(CreateView):
    form_class = AddToDoItemForm
    template_name = 'todo_app/todo_item_form.html'

    def get_initial(self):
        initial_data = super().get_initial()
        todo_list = ToDoList.objects.get(id=self.kwargs['list_id'])
        initial_data['todo-list'] = todo_list
        return initial_data

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        todo_list = ToDoList.objects.get(id=self.kwargs['list_id'])
        context['todo_list'] = todo_list
        context['title'] = 'Create a new item'
        return context


class ToDoItemUpdate(UpdateView):
    model = ToDoItem
    form_class = AddToDoItemForm
    template_name = 'todo_app/todo_item_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['todo_list'] = self.object.todo_list
        context['title'] = 'Edit item'
        return context


class ToDoItemDelete(DeleteView):
    model = ToDoItem
    template_name = 'todo_app/todo_item_confirm_delete.html'
    extra_context = {'template_title': 'Delete item'}

    def get_success_url(self):
        return reverse_lazy('list', args=[self.kwargs['list_id']])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['todo_list'] = self.object.todo_list
        return context
