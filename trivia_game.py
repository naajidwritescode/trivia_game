# ----- TRIVIA GAME -----

# Steps:
# List of questions
# Randomly pick from the list
# Ask the user and store the answers
# Check if they are correct
# Keep track of the score
# Display the score to the player

import random

trivia_questions = {
    "What is the capital of France?": "Paris",
    "Which planet is known as the Red Planet?": "Mars",
    "What does CPU stand for?": "Central Processing Unit",
    "Who is known as the father of computers?": "Charles Babbage",
    "What is the largest ocean on Earth?": "Pacific Ocean",
    "How many continents are there on Earth?": "7",
    "What gas do plants absorb from the atmosphere?": "Carbon Dioxide",
    "What is the square root of 144?": "12",
    "Which programming language is known for its snake logo?": "Python",
    "What is the boiling point of water in Celsius?": "100",
    "Which country invented paper?": "China",
    "What is the fastest land animal?": "Cheetah",
    "Who discovered gravity?": "Isaac Newton",
    "What does RAM stand for?": "Random Access Memory",
    "Which element has the chemical symbol O?": "Oxygen"
}


def python_trivia_game():

    print("\n--------WELCOME TO THE TRIVIA GAME---------\n")

    questions = list(trivia_questions.keys())
    total_number_of_questions = 5

    selected_questions = random.sample(questions, total_number_of_questions)

    score = 0

    incorrect_questions = []

    for idx, question in enumerate(selected_questions):
        print(f"\n{idx + 1}. {question}")
        user_answer = input("Your answer:")

        if user_answer.title().strip() == trivia_questions[question]:
            print("\nCorrect!")
            score += 1

        else:
            print("\nIncorrect!")
            incorrect_questions.append(question)

    print(f"\nHere is your final score: {score}/{total_number_of_questions}\n")

    see_questions = input(
        "Press X to see which questions you got wrong ").lower()

    print()

    if see_questions == 'x':
        print("You got the following question(s) wrong:")
        for incorrect_question in incorrect_questions:
            print(
                f"{incorrect_question} | Ans:{trivia_questions[incorrect_question]}")
        print("\nThanks for playing!\n")
    else:
        print("Thanks for playing!")


while True:
    python_trivia_game()
    print()
    print()
    play_again = input("Do you want to play again? (y/n) ").lower()

    if play_again != 'y':
        print("\nThanks for playing!")
        break
