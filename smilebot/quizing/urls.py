from django.urls import path
from .views import CreateExam,CreateSection,CreateTopic, CreateQuiz, AddQuestion, SubmitAnswer, EvaluateResult, GetQuestions, GetExams, GetSections, GetTopics, GetQuizes

urlpatterns = [
    path('create-exam/', CreateExam.as_view(), name='create-exam'),
    path('create-section/', CreateSection.as_view(), name='create-section'),
    path('create-topic/', CreateTopic.as_view(), name='create-topic'),
    path('create-quiz/', CreateQuiz.as_view(), name='create-quiz'),

    path('add-question/',AddQuestion.as_view(), name='add-question'),
    path('submit-answer/',SubmitAnswer.as_view(), name='submit-answer'),
    path('evaluate-result/',EvaluateResult.as_view(), name='evaluate-result'),
    
    path('get-exams/',GetExams.as_view(), name='get-exams'),
    path('get-sections/',GetSections.as_view(), name='get-sections'),
    path('get-topics/',GetTopics.as_view(), name='get-topics'),
    path('get-quizes/',GetQuizes.as_view(), name='get-quizes'),
    path('get-questions/',GetQuestions.as_view(), name='get-questions'),


]