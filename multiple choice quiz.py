from Question import Question


question_prompts = [
    "What color are Watermelons?\n(a) Red/Green\n(b)Purple\n(c) Orange\n\n",
    "What color are Blueberries?\n(a) Teal\n(b) Pink\n(c) Dark purple\n\n",
    "What color are Kiwis?\n(a) Green\n(b)Dark red\n(c) brown\n\n"



]


questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "a"),


]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1 

    print("You got " + str(score)+ "/" + str(len(questions)) + " correct")

run_test(questions)
