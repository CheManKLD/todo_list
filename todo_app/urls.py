from django.urls import path

from . import views

urlpatterns = [
    path('', views.ToDoListView.as_view(), name='index'),
    path('list/<int:list_id>/', views.ToDoItemView.as_view(), name='list'),
    path('list/add/', views.ToDoListCreate.as_view(), name='list-add'),
]
