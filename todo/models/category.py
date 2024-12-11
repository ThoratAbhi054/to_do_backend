from django.db import models
from django.utils.timezone import now

from utils.mixins.pk_mixin import PKModelMixin
from utils.mixins.timestampmixin import TimeStampMixin
from django.contrib.auth.models import User



class Category(PKModelMixin, TimeStampMixin, models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
