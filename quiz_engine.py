import random

filepath = question_generator.py

question_path = filepath

Number_Questions_Per_Quiz = 5

def run_quiz():
    questions = prepare_questions(question_path)

    number_correct = 0
    for number, question in enumerate(questions, start=1):
        print(f"\nQuestion {num}:")
        number_correct += ask_question(question)
    print(f"\nYou got {number_correct} correct out of {number} questions!")



def prepare_questions(filepath, number_questions):
    with open(filepath, "r") as file:
        questions = file.readlines()

    number_questions = min(number_questions, len(questions))
    return random.sample(questions, k=number_questions)