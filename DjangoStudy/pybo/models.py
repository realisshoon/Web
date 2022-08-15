from django.db import models

# Create your models here.
class Question(models.Model):
    subject = models.CharField(max_length=200) #제목(최대 200자)
    content = models.TextField() #내용 (글자수를 제한 할 수 없는 텍스트)
    create_date = models.DateTimeField() #작성일시

    def __str__(self):
        return self.subject

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) #외래키를 사용해서 Q모델을 A의 속성으로 연결(Q가 사라지면 Q와 연결된 A도 사라짐)
    content = models.TextField()
    create_date = models.DateTimeField()