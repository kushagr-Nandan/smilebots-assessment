from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from quizing import models as QuizingModels
from rest_framework.response import Response
# Create your views here.
class CreateQuiz(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    def post(self, request):
        user = request.user
        topic = request.data.get('topic')
        # questions = request.data.get('questions')
        QuizingModels.Quiz.objects.create(
            user = user,
            topic = topic
        )
        return Response({"quiz Created"})

class AddQuestion(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    def post(self, request):
        id = request.data.get('quiz_id')
        try:
            quiz_obj = QuizingModels.Quiz.objects.get(id = id)
        except:
            print(id)
            return Response({"message":"wrong Quiz Id entered"})
        question = request.data.get('question')
        image = request.data.get('image')
        option_1 = request.data.get('option_1')
        option_2 = request.data.get('option_2')
        option_3 = request.data.get('option_3')
        option_4 = request.data.get('option_4')
        correct_ans = request.data.get('correct_ans')
        if not correct_ans:
            correct_option = request.data.get('correct_option')
            if correct_option:
                if correct_option == '1':
                    correct_ans = option_1
                elif correct_option == '2':
                    correct_ans = option_2
                elif correct_option == '3':
                    correct_ans = option_3
                elif correct_option == '4':
                    correct_ans = option_4
                else:
                    print(correct_option, type(correct_option))
                    return Response({"message":"wrong option entered"})
        QuizingModels.Question.objects.create(
            quiz = quiz_obj,
            question = question,
            image = image,
            option_1 = option_1,
            option_2 = option_2,
            option_3 = option_3,
            option_4 = option_4,
            correct_ans = correct_ans,
        )
        return Response({"message":"question added to the quiz"})
        
class SubmitAnswer(APIView):
    permission_classes = [IsAuthenticated,]
    def post(self, request):
        student = request.user
        quiz_id = request.data.get('quiz_id')
        answer = request.data.get('answer')
        question_id = request.data.get('question_id')
        try:
            quiz_obj = QuizingModels.Quiz.objects.get(id = quiz_id)
        except:
            print(quiz_id)
            return Response({"message":"wrong Quiz Id entered"})
        
        try:
            question_obj = QuizingModels.Question.objects.get(id = question_id)
        except:
            print(question_id)
            return Response({"message":"wrong Question Id entered"})
        
        if QuizingModels.Result.objects.filter(student = student,quiz = quiz_obj).exists():
           result_obj =  QuizingModels.Result.objects.get(student = student,quiz = quiz_obj)
        else:
            result_obj =  QuizingModels.Result.objects.create(
                student=student,
                quiz = quiz_obj
            )

        if QuizingModels.Answer.objects.filter(result = result_obj, question = question_obj).exists():
            answer_obj = QuizingModels.Answer.objects.get(result = result_obj, question = question_obj)
            answer_obj.given_ans = answer
            answer_obj.save()
        else:
            answer_obj = QuizingModels.Answer.objects.create(
                result = result_obj,
                question  = question_obj,
                given_ans = answer
            )
        return Response({"message":"answeris Submitted"})

class EvaluateResult(APIView):
    permission_classes = [IsAuthenticated,]
    def post(self, request):
        student = request.user
        quiz_id = request.data.get('quiz_id')
        try:
            quiz_obj = QuizingModels.Quiz.objects.get(id = quiz_id)
        except:
            print(quiz_id)
            return Response({"message":"wrong Quiz Id entered"})
        if QuizingModels.Result.objects.filter(student = student,quiz = quiz_obj).exists():
           result_obj =  QuizingModels.Result.objects.get(student = student,quiz = quiz_obj)
        else:
            result_obj =  QuizingModels.Result.objects.create(
                student=student,
                quiz = quiz_obj
            )
        answers = result_obj.answers.all()
        response_answer_object =[]
        for ans in answers:
            if ans.given_ans == ans.question.correct_ans:
                result_obj.correct_answers_count+=1
            else:
                result_obj.wrong_answers_count+=1
            response_answer_object.append(
                {
                    "question":ans.question.question,
                    "Given Answer":ans.given_ans,
                    "Correct Answer":ans.question.correct_ans
                }
            )
        
        quiz_obj = result_obj.quiz
        all_questions_count = quiz_obj.questions.all().count()
        result_obj.not_answered_count = all_questions_count - answers.count()
        result_obj.save()
        

        return Response({
            "message":"Score Calculated",
            "Total Questions":all_questions_count,
            "Answered Questions":answers.count(),
            "Correct Answers":result_obj.correct_answers_count,
            "Wrong AnswerS":result_obj.wrong_answers_count,
            "Un-Answered Count":result_obj.not_answered_count,
            "Answers":response_answer_object
        })
        
            
class GetQuestions(APIView):
    permission_classes = [IsAuthenticated,]

    def post(self, request):
        quiz_id = request.data.get('quiz_id')
        try:
            quiz_obj = QuizingModels.Quiz.objects.get(id = quiz_id)
        except:
            print(quiz_id)
            return Response({"message":"wrong Quiz Id entered"})
        
        questions = quiz_obj.questions.all()
        response_question_object = []
        for que in questions:
            response_question_object.append(
                {
                    "id":que.id,
                    "question":que.question,
                    "Option 1":que.option_1,
                    "Option 2":que.option_2,
                    "Option 3":que.option_3,
                    "Option 4":que.option_4,
                }
            )
        return Response(
            {
                "message":"Questions Successfully Fetched",
                "Questions":response_question_object
            }
        )

class GetQuizes(APIView):
    permission_classes = [IsAuthenticated,]
    def post(self, request):
        response_quiz_object = []
        quizes = QuizingModels.Quiz.objects.all()
        for q in quizes:
            response_quiz_object.append(
                {
                    "Id":q.id,
                    "Topic":q.topic
                }
            )
        return Response(
            {
                "Message":"Quizes Fetched Successfully",
                "Quizes":response_quiz_object
            }
        )



    

        
            
