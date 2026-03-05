import random

filepath = question_generator.py

question_path = filepath

Number_Questions_Per_Quiz = 5

def run_quiz():
    questions = prepare_questions(question_path)

    number_correct = 0
# gets index and item (question), and prints it out with the total number correct
    for number, question in enumerate(questions, start=1):
        print(f"\nQuestion {num}:")
        number_correct += ask_question(question)
    print(f"\nYou got {number_correct} correct out of {number} questions!")



def prepare_questions(filepath, number_questions):
    with open(filepath, "r") as file:
# reads all questions from file
      questions = file.readlines()  
# prevents asking more questions than we have
    number_questions = min(number_questions, len(questions))
    return random.sample(questions, k=number_questions)


def ask_question(question):
    correct_answer = question["correct"]
    wrong = question["correct"] + question["wrong"]
    ordered_wrong = random.sample(wrong, k=len(wrong))

    correct = get_answers(
        question=question["question"]
        wrong=ordered_wrong,
        number_choices=len(correct_answer)
    
    )

    if correct := (set(correct)) == set(correct_answer):
        print("🏆  CORRECT ANSWER!")