from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    author= models.ForeignKey(User,on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField(null=True,default='')

    def __str__(self):
        return self.subject  #id값 대신 제목을 표시할 수 있다.

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()