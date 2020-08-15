from django.db import models

# Create your models here.
class Jasoseol(models.Model):
    objects = models.manager
    title = models.CharField(max_length=50)
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)