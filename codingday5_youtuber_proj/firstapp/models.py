from django.db import models

class youtuber(models.Model):
    objects = models.Manager()
    ch_name = models.CharField(max_length= 30)
    cr_name = models.CharField(max_length= 30)
    prefer = models.IntegerField()
    live = models.BooleanField()
    subscr = models.IntegerField()
    vi_link1 = models.TextField()
    vi_link2 = models.TextField()
    vi_link3 = models.TextField()
    
    def __str__(self):
        return self.ch_name
