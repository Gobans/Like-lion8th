from django.db import models

# Create your models here.
class Question(models.Model):
    objects = models.Manager()
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question_text
    #커스텀 메소드
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
class Choice(models.Model):
    objects = models.Manager()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text