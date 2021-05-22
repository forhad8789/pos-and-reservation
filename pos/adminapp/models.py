from django.db import models

# Create your models here.


class Roles(models.Model):
    name = models.TextField(null=False)
    status = models.BooleanField(default=False)

    class Meta:
        db_table = 'roles'

