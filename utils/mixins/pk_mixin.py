from django.db import models


class PKModelMixin(models.Model):
    id = models.AutoField(primary_key=True, unique=True, editable=False)

    class Meta:
        abstract = True
