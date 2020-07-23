from django.db import models

# Create your models here.

class FirstModel(models.Model):
    x=(
        ('Good','좋아요'),
        ('Bad','싫어요'),    
    )
    title = models.CharField(max_length=50)
    text = models.TextField()
    recommend = models.CharField(max_length=5,choices=x)
