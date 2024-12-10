from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from todo.filters.category import CategoryFilter
from todo.models import Category

from django_filters.rest_framework import DjangoFilterBackend

from todo.serializers.category import CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CategoryFilter
    permission_classes = [IsAuthenticated]
    serializer_class = CategorySerializer
   