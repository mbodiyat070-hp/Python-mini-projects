"""
Python trivia game — my own project, tidied into working code.

Picks 5 random questions, asks them, checks the answers and keeps score.
Run:  python trivia_game.py
"""

import random

questions = {
    "What is the keyword to define a function in Python?": "def",
    "Which data type stores True or False values?": "boolean",
    "What is the correct file extension for Python files?": ".py",
    "Which symbol is used to comment in Python?": "#",
    "What function gets input from the user?": "input",
    "How do you start a for loop in Python?": "for",
    "What is the output of 2 ** 3 in Python?": "8",
    "What keyword imports a module in Python?": "import",
    "What does the len() function return?": "length",
    "What is the result of 10 // 3 in Python?": "3",
}


def python_trivia_game() -> None:
    total_questions = 5
    score = 0

    selected = random.sample(list(questions.keys()), total_questions)

    for question in selected:
        print("\n" + question)
        user_answer = input("Your answer: ").lower().strip()
        correct_answer = questions[question]

        if user_answer == correct_answer.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong. The correct answer is: {correct_answer}.")

    print(f"\nGame over! Your final score is: {score}/{total_questions}")


if __name__ == "__main__":
    python_trivia_game()
