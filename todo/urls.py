from django.urls import path, include
from rest_framework.routers import DefaultRouter

from todo.views.category import CategoryViewSet
from todo.views.task import TaskViewSet

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
