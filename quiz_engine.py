import random

filepath = question_generator.py

Question_Path = filepath

Number_Questions_Per_Quiz = 5

def Run_Quiz():
    questions = Prepare_Questions(Question_Path)

    number_correct = 0
    for number, question in enumerate(questions, start=1):
        print(f"\nQuestion {num}:")
        number_correct += Ask_Question(question)
    print(f"\nYou got {number_correct} correct out of {number} questions!")



def Prepare_Questions(filepath, number_questions):
    with open(filepath, "r") as file:
        for questions in file:
            number_questions = min(number_questions, len(questions))
            return random.sample(questions, k=number_questions)