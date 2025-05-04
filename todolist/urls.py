from django.contrib import admin
from django.urls import path, include
from tasks import views  # Ajout de l'import de la vue delete_task

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tasks.urls')),  # Inclut les URLs de l'application tasks
    # Route pour la suppression de tâche
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),  # Nouvelle route pour supprimer une tâche
]