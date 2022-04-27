from django.contrib import admin

from .models import *


@admin.register(ToDoList)
class ToDoListAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('title',)
    search_fields = ('title',)


@admin.register(ToDoItem)
class ToDoItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'due_date', 'title', 'todo_list')
    list_filter = ('todo_list', 'due_date')
    search_fields = ('title',)
