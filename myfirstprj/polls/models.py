from django.db import models

class Question(models.Model):   #Question : 테이블 이름
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):      #admin 페이지에서 노출되는 정보가 무엇이냐
        return str(self.pk) + ". " + self.question_text + " | " + str(self.pub_date)[:10]      
        #pub_date는 문자열이 아니기 때문에 형변환해야함
        #1. 당신이 좋아하는 음식은? | 2019-08-21 02:44:54    -> 1. 당신이 좋아하는 음식은? | 2019-08-21

class Choice(models.Model):     #Choice : 테이블 이름
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return str(self.question) + " | " + str(self.choice_text)