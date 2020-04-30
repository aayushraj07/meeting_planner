from django.db import models

# Create your models here.
class Meetings(models.Model):
    title = models.CharField(max_length=2000)
    date = models.DateField()