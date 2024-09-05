# This program is a quiz game.

import random

# ----------------
# Subprograms
# ----------------

global questions
with open('level-9/questions.txt', 'r') as questions_file:
    questions = questions_file.readlines()

global completedQuestions
completedQuestions = []

def getRandomQuestion(used = False):
    qTempArr = []
    for question in questions:
        qTempArr.append(question)
    if (used == False):
        for q in qTempArr:
            if q in completedQuestions:
                qTempArr.pop(qTempArr.index(q))
    random_question = random.choice(qTempArr)
    completedQuestions.append(random_question)
    return random_question.rsplit(',', 1)

def parseAnswer(bad):
    bad = bad.replace('\n', '')
    if bad == 'true' or bad == 'false':
        return bad
    else:
        return '_'
# ----------------
# Main program
# ----------------

i = 0

while len(completedQuestions) < len(questions):
    try:
        question = getRandomQuestion()
        # Error likely to happen during parsing.
        # If error does occur, we'll just skip the question and the user won't know.
        answer = parseAnswer(question[1]) 
        if answer != 'true' and answer != 'false':
            print('Skipping question', i)
            raise Exception('An error occured whilst parsing the answer.')
        i+=1
        print()
        print(f"Question {i}:")
        print(question[0])
        userAnswer = (input("True or False? ")).lower()
        if (userAnswer == answer):
            print()
            print('Correct!')
            print()
        else:
            print()
            print('Nope, the answer was', answer)
            print()
    except :
        i+=1
        print('Skipping question', i)

