from rest_framework import serializers
from todo.models import Task
from django.contrib.auth.models import User
from todo.models.category import Category

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'status', 'priority', 'deadline', 'user', 'category', 'created_at', 'updated_at']

class TaskCreateSerializer(TaskSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset = User.objects.all(), required =True)
    category = serializers.PrimaryKeyRelatedField( queryset = Category.objects.all(), required =False, allow_null = True)