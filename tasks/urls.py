from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),  # Cette ligne associe la page d'accueil à la vue task_list
    path('toggle/<int:task_id>/', views.toggle_task, name='toggle_task'),
]