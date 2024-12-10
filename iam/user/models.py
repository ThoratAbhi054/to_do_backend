from django.contrib.auth.models import User
from django.db import models

from utils.mixins.cms_mixin import CMSMixin
from utils.mixins.timestampmixin import TimeStampMixin


class UserProfile(CMSMixin, TimeStampMixin, models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    contact_no = models.CharField(max_length=16, null=False)
    city = models.CharField(max_length=32, null=False)
    avatar = models.ImageField(upload_to="iam/users/avatar", null=True, blank=True)
    def __str__(self):
        return self.user.username

    def get_full_name(self):
        return f"{self.user.first_name} {self.user.last_name}"

