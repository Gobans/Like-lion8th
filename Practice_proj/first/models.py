from django.db import models

# Create your models here.
class test(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length= 30)
    summary = models.TextField(max_length=200)
    photo = models.ImageField(upload_to="image",blank=True)
    def __str__(self):
        return self.name