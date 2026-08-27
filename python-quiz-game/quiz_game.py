"""Quiz Game — the finished mini project for the Basic Python Course.

Built in Class 14 and Class 15 using only the ideas taught in Classes 1 to 13:
variables, f-strings, operators, if/elif/else, loops, strings, lists, tuples,
sets, dictionaries, functions, the random module, try/except and file handling.

Run it from this folder with:

    python quiz_game.py      (Windows)
    python3 quiz_game.py     (macOS and Linux)
"""

import random

from questions import QUESTIONS

LETTERS = "ABCD"
SCORES_FILE = "scores.txt"
QUESTIONS_PER_ROUND = 5
LINE = "-" * 46


def get_categories(question_bank):
    """Return a sorted list of every unique category in the question bank."""
    found = set()
    for item in question_bank:
        found.add(item["category"])
    return sorted(found)


def filter_by_category(question_bank, category):
    """Return only the questions belonging to one category."""
    chosen = []
    for item in question_bank:
        if item["category"] == category:
            chosen.append(item)
    return chosen


def choose_category(question_bank):
    """Ask the player to pick a category.

    Returns a tuple of (category name, list of questions).
    """
    categories = get_categories(question_bank)

    print("\nChoose a category:")
    print("   0. All categories")
    for index in range(len(categories)):
        print(f"   {index + 1}. {categories[index]}")

    while True:
        typed = input("Category number: ").strip()

        try:
            number = int(typed)
        except ValueError:
            print("Please type a number, for example 1.")
            continue

        if number == 0:
            return "All categories", list(question_bank)

        if 1 <= number <= len(categories):
            name = categories[number - 1]
            return name, filter_by_category(question_bank, name)

        print("That is not one of the numbers listed. Try again.")


def ask_for_letter(option_count):
    """Keep asking until the player types a valid option letter.

    Returns the position of the chosen option (0 for A, 1 for B, and so on).
    """
    valid = LETTERS[:option_count]
    prompt = "Your answer (" + "/".join(valid) + "): "

    while True:
        typed = input(prompt).strip().upper()

        if len(typed) != 1:
            print("Please type a single letter.")
            continue

        position = valid.find(typed)
        if position == -1:
            print(f"'{typed}' is not one of the options. Try again.")
            continue

        return position


def ask_question(item, number, total):
    """Ask one question. Return True if the player answers it correctly."""
    category = item["category"]
    options = item["options"]
    correct = item["answer"]

    print(f"\nQuestion {number} of {total}   [{category}]")
    print(item["question"])

    for index in range(len(options)):
        print(f"   {LETTERS[index]}. {options[index]}")

    chosen = ask_for_letter(len(options))

    if chosen == correct:
        print("Correct!")
        return True

    print(f"Wrong. The answer was {LETTERS[correct]}. {options[correct]}")
    return False


def grade_for(percentage):
    """Turn a percentage into a grade the students recognise."""
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "Not passed"


def play_round(question_bank, player_name):
    """Play one full round of the quiz. Return a tuple of (score, total)."""
    questions = list(question_bank)
    random.shuffle(questions)

    total = QUESTIONS_PER_ROUND
    if len(questions) < total:
        total = len(questions)

    score = 0
    for number in range(total):
        if ask_question(questions[number], number + 1, total):
            score += 1

    percentage = round(score / total * 100, 1)
    grade = grade_for(percentage)

    print(f"\n{LINE}")
    print(f"Round finished, {player_name}.")
    print(f"Score: {score} out of {total}   ({percentage}%)   Grade: {grade}")
    print(LINE)

    return score, total


def save_score(player_name, score, total):
    """Add one result to the end of the scores file."""
    try:
        with open(SCORES_FILE, "a") as scores_file:
            scores_file.write(f"{player_name}|{score}|{total}\n")
    except OSError:
        print("Your score could not be saved this time.")


def read_scores():
    """Read every saved result. Return a list of (percentage, name, score, total)."""
    results = []

    try:
        with open(SCORES_FILE, "r") as scores_file:
            for line in scores_file:
                line = line.strip()
                if line == "":
                    continue

                parts = line.split("|")
                if len(parts) != 3:
                    continue

                try:
                    name = parts[0]
                    score = int(parts[1])
                    total = int(parts[2])
                except ValueError:
                    continue

                if total <= 0:
                    continue

                percentage = round(score / total * 100, 1)
                results.append((percentage, name, score, total))
    except FileNotFoundError:
        return results

    return results


def show_high_scores():
    """Print the five best results saved so far."""
    results = read_scores()

    if len(results) == 0:
        print("\nNo scores saved yet — you are the first to play!")
        return

    results.sort(reverse=True)

    print("\nHigh scores")
    print(LINE)

    shown = 0
    for result in results:
        percentage = result[0]
        name = result[1]
        score = result[2]
        total = result[3]

        shown += 1
        print(f"{shown}. {name:<14} {score}/{total}   ({percentage}%)")

        if shown == 5:
            break

    print(LINE)


def main():
    """Run the whole game."""
    print("=" * 46)
    print("     TRITON COLLEGE — PYTHON QUIZ GAME")
    print("=" * 46)

    player_name = input("\nWhat is your name? ").strip()
    if player_name == "":
        player_name = "Player"

    print(f"\nWelcome, {player_name}. Answer by typing a letter, then press Enter.")

    while True:
        category_name, questions = choose_category(QUESTIONS)
        print(f"\nCategory: {category_name} — {len(questions)} questions available.")

        score, total = play_round(questions, player_name)
        save_score(player_name, score, total)
        show_high_scores()

        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            break

    print(f"\nThanks for playing, {player_name}. Goodbye!")


main()
