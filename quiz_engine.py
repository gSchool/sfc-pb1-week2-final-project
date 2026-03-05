import random

filepath = question_generator.py

question_path = filepath

Number_Questions_Per_Quiz = 5

correct = answer

wrong = alternative 

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



# Here I am trying to make the correct answer list and the wrong answer list, and take a random set of wrong answers
# as well as get the list of right answers for each question, and create an error message when they are answered incorrectly


def ask_question(question):
    correct_answer = question["answer"]
    alternative = question["answer"] + question["alternative"]
    ordered_wrong = random.sample(wrong, k=len(wrong))

    correct = get_answers(
        question=question["question"]
        alternative=ordered_alternative,
        number_choices=len(correct_answer)
    
    )

    if correct := (set(answers)) == set(correct_answer):
        print("🏆  CORRECT ANSWER! 🏆 ")
    else:
        if len(correct_answer) == 1:
            print("No, the answer is:")
        else:
            print("No, the answeres are:")

        for answer in correct_answer:
            print("-", correct)



def get_answer(question, alternatives, number_choices=1):
    print(f"{question}?")
    labeled_alternatives = dict(alternatives, strict=False)

    for alternatives in labeled_alternatives.items():
        print(f" {lable} {alternatives}")

    while True:
        plural_s = "" if number_choices == 1 else f"s" (choose {number_choices})
        answer = input(f"\nChoice{plural_s}?")
        answer = set(answer.replace(",", "").split())


        if len(answer) != number_choices:
         plural_s = "" if number_choices == 1 else "s, separated by comma"
         print(f"Please answer {number_choices} alternative{plural_s}")
         continue


        if any(
            (invalid := answer) not in labeled_alternatives
            for answer in answers):
             
             print (
                 f"{invalid!r} is not the right choice."
                 f"Please use {','.join(labeled_alternatives)}"
             )
             continue
        return [labeled_alternatives[answer] for answer in answers]
    
