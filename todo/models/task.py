from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

from todo.models.category import Category
from utils.mixins.pk_mixin import PKModelMixin
from utils.mixins.timestampmixin import TimeStampMixin
from django.utils.translation import gettext_lazy as _


class StatusChoices(models.TextChoices):
    IN_PROGRESS = "IN_PROGRESS", _("In Pogress")
    COMPLETED = "COMPLETED", _("Completed")

class PriorityChoices(models.TextChoices):
    HIGH = "HIGH", _("High")
    MEDIUM = "MEDIUM", _("Medium")
    LOW = "LOW", _("Low")


class Task(PKModelMixin, TimeStampMixin, models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=StatusChoices.choices, default=PriorityChoices.LOW)
    priority = models.CharField(max_length=10, choices=PriorityChoices.choices, default=StatusChoices.IN_PROGRESS)
    deadline = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    @property
    def is_overdue(self):
        return self.deadline and self.deadline < now() and self.status != 'Completed'

    def __str__(self):
        return self.title