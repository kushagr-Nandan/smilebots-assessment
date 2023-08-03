from django.urls import path
from .views import CreateQuiz, AddQuestion, SubmitAnswer

urlpatterns = [
    path('create/', CreateQuiz.as_view(), name='create-quiz'),
    path('add-question/',AddQuestion.as_view(), name='add-question'),
    path('submit-answer/',SubmitAnswer.as_view(), name='submit-answer'),
]