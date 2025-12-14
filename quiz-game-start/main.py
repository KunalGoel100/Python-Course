from data import question_data
from question_model import question
from quiz_brain import quizBrain

q1 = []
for i in range(0,len(question_data),1):
    q = question(question_data[i]['text'],question_data[i]['answer'])
    q1.append(q)

quiz = quizBrain(q1)

while quiz.stillQuestion() == 1:
    userAnswer = quiz.nextQuestion()


