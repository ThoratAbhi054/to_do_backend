import django_filters
from todo.models import Task
from django.contrib.auth.models import User
from todo.models.category import Category


class TaskFilter(django_filters.FilterSet):
    status = django_filters.CharFilter(lookup_expr='iexact')
    priority = django_filters.CharFilter(lookup_expr='iexact')
    user = django_filters.ModelChoiceFilter(queryset=User.objects.all())
    category = django_filters.ModelChoiceFilter(queryset=Category.objects.all())
    created_at = django_filters.DateFromToRangeFilter()
    updated_at = django_filters.DateFromToRangeFilter()

    class Meta:
        model = Task
        fields = ['status', 'priority', 'user', 'category', 'created_at', 'updated_at']
