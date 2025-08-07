from django.urls import path, include
from . import views
# urls.py
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'tasks', views.TaskViewSet)

urlpatterns = [
    path('', views.home, name='home'),
    path('completed/<int:id>/', views.completed_tasks, name='completed'),
    path('delete/<int:id>/', views.delete_task, name='delete_task'),
    path('add/', views.add_task, name='add_task'),
    path('edit/<int:id>/',views.edit_task, name='edit_task'),
    path('api/', include(router.urls)),
]




