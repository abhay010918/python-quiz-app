from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

# Create a list of Question objects from the provided question_data
question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# Initialize a QuizBrain instance with the question bank
quiz = QuizBrain(question_bank)

# Initialize a QuizInterface instance with the QuizBrain
Quiz_if = QuizInterface(quiz)

# Uncomment the following lines if you want to run the quiz without the GUI
# while quiz.still_has_questions():
#     quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
