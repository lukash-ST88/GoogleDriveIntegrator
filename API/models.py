from django.db import models


# Create your models here.
class File(models.Model):
    name = models.CharField(max_length=255)
    data = models.TextField(blank=True, null=True)



