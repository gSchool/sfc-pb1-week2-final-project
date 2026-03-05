import question_generator as qg

Number_Questions_Per_Quiz = 5

def run_quiz(lore):
    # call the generator from question_generator.py
    questions = qg.generate_questions(lore, num_questions=NUMBER_QUESTIONS_PER_QUIZ)

    number_correct = 0

    for number, question in enumerate(questions, start=1):
        print(f"\nQuestion {number}:")
        if ask_question(question):
            number_correct += 1

    print(f"\nYou got {number_correct} correct out of {len(questions)} questions!")


# def run_quiz():
#     questions = genderate_questions(lore, num_question=NUMBER_QUESTIONS_PER_QUIZ)

#     number_correct = 0

# # gets index and item (question), and prints it out with the total number correct
#     for number, question in enumerate(questions, start=1):
#         print(f"\nQuestion {number}:")
#     if ask_question(question):
#         number_correct +=1
#     print(f"\nYou got {number_correct} correct out of {number} questions!")

def ask_question(question):
    prompt = question["prompt"]
    choices = question["choices"]
    answer_index = question["answer_index"]
    explanation = question.get("explanation", "")

    print(prompt)

    labels = ["A", "B", "C", "D", "E", "F"]

    for i, choice in enumerate(choices):
        print(f"  {labels[i]}) {choice}")

    while True:
        raw = input(f"\nYour choice ({'/'.join(labels[:len(choices)])}): ").strip().upper()

        if raw not in labels[:len(choices)]:
            print(f"Please choose one of: {', '.join(labels[:len(choices)])}")
            continue

        picked_index = labels.index(raw)

        if picked_index == answer_index:
            print("🏆  CORRECT ANSWER! 🏆")
            if explanation:
                print(f"ℹ️ {explanation}")
            return True
        else:
            correct_label = labels[answer_index]
            correct_text = choices[answer_index]
            print(f"❌ Not quite. The answer is {correct_label}) {correct_text}")
            if explanation:
                print(f"ℹ️ {explanation}")
            return False

# def prepare_questions(filepath, number_questions):
#     with open(filepath, "r") as file:
# # reads all questions from file
#       questions = file.readlines()  
# # prevents asking more questions than we have
#     number_questions = min(number_questions, len(questions))
#     return random.sample(questions, k=number_questions)



# Here I am trying to make the correct answer list and the wrong answer list, and take a random set of wrong answers
# as well as get the list of right answers for each question, and create an error message when they are answered incorrectly


# def ask_question(question):
#   prompt = question["prompt"]
#   choices = question["choices"]
#   answer_index = question["answer_index"]
#   explaination = question.get("explaination", "")

#   print(prompt)
#   labels = ["A", "B", "C", "D", "E", "F"]
    
#   for item, choice in enumerate(choices):
#       print(f"  {labels[i]}) {choice}")


#   while True:
#       raw = input("\nYour choice (A/B/C/D):  ").strip().upper()
#       if raw not in labels[:len(choices):]
#          print(f"Please choose one of: {','.join(labels[:leb(choices)])}")
#          continue   
      
#       picked_index == labels.index(raw)

#       if picked_index == answer_index:
#           print("🏆  CORRECT ANSWER! 🏆")
#           return True
#   else:
#        correct_label = labels[answer_index]
#        correct_text = choices[answer_index]
#        print(f"❌ Not quite. The answer is {correct_label}) {correct_text}")
#        if explanation:
#             print(f"ℹ️ {explanation}")
#        return False
      
      