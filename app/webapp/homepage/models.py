from django.db import models

# Create your models here.
from django.db import models

class Baby(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    id = models.IntegerField(primary_key=True)

class Daddy(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    id = models.IntegerField(primary_key=True)