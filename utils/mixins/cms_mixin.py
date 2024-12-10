from django.db import models
from django.utils.translation import gettext_lazy as _

from utils.mixins.pk_mixin import PKModelMixin



class StatusChoices(models.TextChoices):
    PUBLISHED = "PUB", _("Published")
    DRAFT = "DRF", _("Draft")
    ARCHIVED = "ARC", _("Archived")


class CMSMixin(PKModelMixin, models.Model):
    status = models.CharField(
        choices=StatusChoices.choices, default=StatusChoices.DRAFT, max_length=3
    )
    sort = models.IntegerField(null=True, blank=True)

    class Meta:
        abstract = True
