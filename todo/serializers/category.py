from rest_framework import serializers
from todo.models import Category
from django.contrib.auth.models import User

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'user', 'created_at', 'updated_at']


class CategoryCreateSerializer(CategorySerializer):
    user = serializers.PrimaryKeyRelatedField(queryset = User.objects.all(), required =True)