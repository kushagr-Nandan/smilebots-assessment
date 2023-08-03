from django.db import models
from users.models import CustomUser
class Exam(models.Model):
    user =models.ForeignKey(CustomUser,on_delete=models.CASCADE, related_name="exams")
    name = models.CharField(max_length=200, blank=True, null=True)

class Section(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    exam = models.ForeignKey(Exam,on_delete=models.CASCADE, related_name="sections")

class Topic(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    section = models.ForeignKey(Section,on_delete=models.CASCADE, related_name="topics")

class Quiz(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE, related_name="quizes")


class Question(models.Model):
    quiz = models.ForeignKey(Quiz,on_delete=models.CASCADE, related_name="questions")
    question = models.TextField(null=True, blank = True)
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
    question = models.ForeignKey(Question,on_delete=models.CASCADE, related_name="all_answers", blank=True, null=True),
    given_ans = models.CharField(max_length=200)
