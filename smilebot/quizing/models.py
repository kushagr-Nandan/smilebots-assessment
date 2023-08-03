from django.db import models
from users.models import CustomUser

# Create your models here.
class Quiz(models.Model):
    user =models.ForeignKey(CustomUser,on_delete=models.CASCADE, related_name="quizes")
    topic = models.CharField(max_length=200)

class Question(models.Model):
    quiz = models.ForeignKey(Quiz,on_delete=models.CASCADE, related_name="questions")
    question = models.TextField()
    image = models.ImageField(upload_to='quiz_images/', blank=True, null=True)
    option_1 = models.CharField(max_length=200)
    option_2 = models.CharField(max_length=200)
    option_3 = models.CharField(max_length=200)
    option_4 = models.CharField(max_length=200)
    correct_ans = models.CharField(max_length=200)

class Result(models.Model):
    student = models.ForeignKey(CustomUser,on_delete=models.CASCADE, related_name="all_results")
    quiz =  models.ForeignKey(Quiz,on_delete=models.CASCADE, related_name="quiz_results")
    correct_answers_count = models.IntegerField(default=0,null=True,blank=True)
    wrong_answers_count = models.IntegerField(default=0,null=True,blank=True)
    not_answered_count = models.IntegerField(default=0,null=True,blank=True)

class Answer(models.Model):
    result = models.ForeignKey(Result,on_delete=models.CASCADE, related_name="answers")
    question = models.ForeignKey(Question,on_delete=models.CASCADE, related_name="all_answers")
    given_ans = models.CharField(max_length=200)
