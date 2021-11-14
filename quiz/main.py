from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for element in question_data:
    question_bank.append(Question(element['text'], element['answer']))

qb = QuizBrain(question_bank)
for i in range(0, len(question_bank)):
    qb.question_number = i
    answer = input(qb.ask_question())
    qb.evaluate(answer)

print(f"Your total score is {qb.score} !!")