"""
Python trivia game — my own project, tidied into working code.

Picks 5 random questions, asks them, checks the answers and keeps score.
Each question accepts a few reasonable phrasings (e.g. "bool" or
"boolean"), so a right answer isn't marked wrong over exact wording.
Run:  python trivia_game.py
"""

import random

# question -> (display answer, all accepted answers)
questions = {
    "What is the keyword to define a function in Python?":
        ("def", {"def"}),
    "Which data type stores True or False values?":
        ("bool", {"bool", "boolean"}),
    "What is the correct file extension for Python files?":
        (".py", {".py", "py"}),
    "Which symbol is used to comment in Python?":
        ("#", {"#", "hash", "hashtag"}),
    "What function gets input from the user?":
        ("input()", {"input", "input()"}),
    "How do you start a for loop in Python?":
        ("for", {"for"}),
    "What is the output of 2 ** 3 in Python?":
        ("8", {"8"}),
    "What keyword imports a module in Python?":
        ("import", {"import"}),
    "What does the len() function return?":
        ("the length of an object", {"length", "the length",
                                     "the length of an object", "size"}),
    "What is the result of 10 // 3 in Python?":
        ("3", {"3"}),
}


def normalise(answer: str) -> str:
    """Lower-case and trim an answer so comparison ignores formatting."""
    return answer.lower().strip()


def is_correct(user_answer: str, accepted: set[str]) -> bool:
    return normalise(user_answer) in {normalise(a) for a in accepted}


def python_trivia_game() -> None:
    total_questions = 5
    score = 0

    selected = random.sample(list(questions.keys()), total_questions)

    for question in selected:
        print("\n" + question)
        user_answer = input("Your answer: ")
        display_answer, accepted = questions[question]

        if is_correct(user_answer, accepted):
            print("Correct!")
            score += 1
        else:
            print(f"Wrong. The correct answer is: {display_answer}.")

    print(f"\nGame over! Your final score is: {score}/{total_questions}")


if __name__ == "__main__":
    python_trivia_game()
