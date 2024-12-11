from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from todo.filters.task import TaskFilter
from todo.models import Task
from django_filters.rest_framework import DjangoFilterBackend

from todo.serializers.task import TaskCreateSerializer, TaskSerializer
from rest_framework import permissions

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_class = TaskFilter
    permission_classes = [permissions.AllowAny]


    def get_queryset(self):
        queryset = super().get_queryset()
        if not self.request.user.is_staff and not self.request.user.is_superuser:
            queryset = queryset.filter(user=self.request.user)
        return queryset

    def get_serializer_class(self):
        if self.action in ["create", "partial_update"]:
            return TaskCreateSerializer
        return TaskSerializer
