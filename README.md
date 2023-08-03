# smilebots-assessment

<h1>Curls for APIs </h1>
<br>
<h2>========================Admin Perspective============================</h2>
<br>
<h2>Login</h2>
<br>
curl --location 'http://127.0.0.1:8001/authapi/login/' \
--header 'Content-Type: application/json' \
--data '{
    "username":"admin",
    "password":"admin"
}'
<br>
<h2>Create Exam</h2>
<br>
curl --location 'http://127.0.0.1:8001/quiz/create-exam/' \
--header 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjkxMDk1MDAyLCJpYXQiOjE2OTEwOTQ3MDIsImp0aSI6ImRhYjlhZjg4YmE0MTQ0MTk4OTlhM2FhZmNhYTlkYjM2IiwidXNlcl9pZCI6MX0.ejXps__4ZUMu8UdjbCbghMy9c0YBwdOc9rBDut-zMFs' \
--header 'Content-Type: application/json' \
--data '{
    "name":"Interview"
}'
<br>
<h2>Create Section</h2>
<br>
curl --location 'http://127.0.0.1:8001/quiz/create-section/' \
--header 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjkxMDk1MDAyLCJpYXQiOjE2OTEwOTQ3MDIsImp0aSI6ImRhYjlhZjg4YmE0MTQ0MTk4OTlhM2FhZmNhYTlkYjM2IiwidXNlcl9pZCI6MX0.ejXps__4ZUMu8UdjbCbghMy9c0YBwdOc9rBDut-zMFs' \
--header 'Content-Type: application/json' \
--data '{
    "name":"Coding",
    "exam_id":1
}'
<br>
<h2>Create Topic</h2>
<br>
curl --location 'http://127.0.0.1:8001/quiz/create-topic/' \
--header 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjkxMDk1MDAyLCJpYXQiOjE2OTEwOTQ3MDIsImp0aSI6ImRhYjlhZjg4YmE0MTQ0MTk4OTlhM2FhZmNhYTlkYjM2IiwidXNlcl9pZCI6MX0.ejXps__4ZUMu8UdjbCbghMy9c0YBwdOc9rBDut-zMFs' \
--header 'Content-Type: application/json' \
--data '{
    "name":"DSA",
    "section_id":1
}'
<br>
<h2>Create Quiz</h2>
<br>
curl --location 'http://127.0.0.1:8001/quiz/create-quiz/' \
--header 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjkxMDk1MzIxLCJpYXQiOjE2OTEwOTUwMjEsImp0aSI6ImMyMjJhMzZhYjE4NDQ5YTM5OThhYjc3NmY4OTUyYjI4IiwidXNlcl9pZCI6MX0.NJ4pmOnSJq01VL4hqzj_bg1zek4hkO6Tenn4q9rwG9w' \
--header 'Content-Type: application/json' \
--data '{
    "name":"DSA Rapid Fire",
    "topic_id":1
}'
<br>
<h2>Adding Question to Quiz</h2>
<br>
curl --location 'http://127.0.0.1:8001/quiz/add-question/' \
--header 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjkxMDk1NjU2LCJpYXQiOjE2OTEwOTUzNTYsImp0aSI6Ijg3MThjYmE4ZjQyYjQ3OWNiZGYyNWEwNzE1OWI2ZjE2IiwidXNlcl9pZCI6MX0.saUJJGrytioXdJsy-JZ6nCfQ6bmp4fF2f6HW15VkSr0' \
--form 'question="What is the full form of DSA"' \
--form 'option_1="Data Structure Algorithm"' \
--form 'option_2="Dance of Spiraling Algorithms"' \
--form 'option_3="Digital Symphony of Abstractions"' \
--form 'option_4="None of these"' \
--form 'image=@"/home/kushagr/Desktop/Riyalto/image generation/output/images/Earrings/emerald_cut_bezel_set_stud_earring_83449.jpg"' \
--form 'correct_option="1"' \
--form 'quiz_id="1"'

<br>
<h2>========================User Perspective============================</h2>
<br>
<br>
<h2>List All Exams</h2>
<br>
curl --location --request POST 'http://127.0.0.1:8001/quiz/get-exams/' \
--header 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjkxMDk1ODQzLCJpYXQiOjE2OTEwOTU1NDMsImp0aSI6IjNjYmRkYjQ3NDhhZjQ2MWQ5ODQ3NDdjMDQ4ZjYwZjY2IiwidXNlcl9pZCI6MX0.6UxFpmHeTKe1QSqLlWv2Oc3bz3eR4dMO8uRW8sdJr8w' \
--data ''
<br>
<h2>List All Section of Exam with requested exam id</h2>
<br>
curl --location 'http://127.0.0.1:8001/quiz/get-sections/' \
--header 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjkxMDk1ODQzLCJpYXQiOjE2OTEwOTU1NDMsImp0aSI6IjNjYmRkYjQ3NDhhZjQ2MWQ5ODQ3NDdjMDQ4ZjYwZjY2IiwidXNlcl9pZCI6MX0.6UxFpmHeTKe1QSqLlWv2Oc3bz3eR4dMO8uRW8sdJr8w' \
--header 'Content-Type: application/json' \
--data '{
    "exam_id":1
}'
<br>
<h2>List All Topics of Section with requested section id</h2>
<br>
curl --location 'http://127.0.0.1:8001/quiz/get-topics/' \
--header 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjkxMDk1ODQzLCJpYXQiOjE2OTEwOTU1NDMsImp0aSI6IjNjYmRkYjQ3NDhhZjQ2MWQ5ODQ3NDdjMDQ4ZjYwZjY2IiwidXNlcl9pZCI6MX0.6UxFpmHeTKe1QSqLlWv2Oc3bz3eR4dMO8uRW8sdJr8w' \
--header 'Content-Type: application/json' \
--data '{
    "section_id":1
}'
<br>
<h2>List All Quizes of Topic with requested topic id</h2>
<br>
curl --location 'http://127.0.0.1:8001/quiz/get-quizes/' \
--header 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjkxMDk1ODQzLCJpYXQiOjE2OTEwOTU1NDMsImp0aSI6IjNjYmRkYjQ3NDhhZjQ2MWQ5ODQ3NDdjMDQ4ZjYwZjY2IiwidXNlcl9pZCI6MX0.6UxFpmHeTKe1QSqLlWv2Oc3bz3eR4dMO8uRW8sdJr8w' \
--header 'Content-Type: application/json' \
--data '{
    "topic_id":1
}'
<br>
<h2>List All questions of quiz with requested quiz id</h2>
<br>
curl --location 'http://127.0.0.1:8001/quiz/get-questions/' \
--header 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjkxMDk1ODQzLCJpYXQiOjE2OTEwOTU1NDMsImp0aSI6IjNjYmRkYjQ3NDhhZjQ2MWQ5ODQ3NDdjMDQ4ZjYwZjY2IiwidXNlcl9pZCI6MX0.6UxFpmHeTKe1QSqLlWv2Oc3bz3eR4dMO8uRW8sdJr8w' \
--header 'Content-Type: application/json' \
--data '{
    "quiz_id":1
}'
<br>
<h2>Submit answer of a question</h2>
<br>
curl --location 'http://127.0.0.1:8001/quiz/submit-answer/' \
--header 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjkxMDk2NTYzLCJpYXQiOjE2OTEwOTYyNjMsImp0aSI6IjVlYWNjZTljNzFiNjRhMmI4NjFjZTA3ZWMwMDhlMmIzIiwidXNlcl9pZCI6MX0.6FWVKWhBXhYj5OZbzCeerYrXI-YzN2LcpJG4B-Y994w' \
--header 'Content-Type: application/json' \
--data '{
    "quiz_id":1,
    "question_id":1,
    "answer":"Data Structure Algorithm"
}'
<br>
<h2>Evaluate Result of Quiz</h2>
<br>
curl --location 'http://127.0.0.1:8001/quiz/evaluate-result/' \
--header 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjkxMDk2NTYzLCJpYXQiOjE2OTEwOTYyNjMsImp0aSI6IjVlYWNjZTljNzFiNjRhMmI4NjFjZTA3ZWMwMDhlMmIzIiwidXNlcl9pZCI6MX0.6FWVKWhBXhYj5OZbzCeerYrXI-YzN2LcpJG4B-Y994w' \
--header 'Content-Type: application/json' \
--data '{
    "quiz_id":1
}'
