from django.db import models

# Create your models here.
class Note(models.Model):
    tittle = models.CharField(max_length=255)
    content = models.TextField()
    