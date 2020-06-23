from django.db import models

# Create your models here.

class picture(models.Model):
    objects = models.Manager()
    explain = models.TextField(default='사진에 대한 설명을 적어주세요')
    photo = models.ImageField(upload_to = "image", blank= True)