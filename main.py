from data import question_data
from quiz_brain import QuizBrain
from question_model import Question

question_bank = []

for index in range(0, len(question_data)):
    question_bank.append(Question(question_data[index]['question'], question_data[index]['correct_answer']))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"You've completed the quiz! Your final score is {quiz.score}/{quiz.question_number}")
