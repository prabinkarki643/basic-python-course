# Class 14: Mini Project Part 1 — Building the Quiz Game

> **Time budget**: 45 minutes (≈ 32 min teach + 13 min practice)
> **Prerequisites**: Classes 1–13 (everything so far)

Today we start building a real program — a Quiz Game you can play, and that your friends can play. By the end of this class you will have a working game. In Class 15 we will make it shuffle, filter by category and remember high scores.

## What You Will Learn

- How to **plan** a program before writing any code
- Storing a **question bank** as a list of dictionaries
- Splitting a program across **two files** with `from ... import`
- Displaying options and **validating** the player's answer
- Writing the **scoring loop**

---

## 14.1 Planning First

Nobody good writes a program by starting at line 1 and typing until it works. You decide what it must do, then break that into small jobs.

**What the Quiz Game must do:**

1. Greet the player and ask their name
2. Show a question with four lettered options
3. Accept an answer, and refuse anything invalid without crashing
4. Say whether it was right, and show the correct answer if not
5. Repeat for five questions
6. Show the score, a percentage and a grade

**Breaking it into functions:**

| Function | Job | Returns |
|----------|-----|---------|
| `ask_for_letter(option_count)` | Get a valid A/B/C/D from the player | The position chosen (0–3) |
| `ask_question(item, number, total)` | Show one question and mark it | `True` if correct |
| `grade_for(percentage)` | Turn a percentage into a grade | A grade string |
| `play_round(questions, name)` | Run all the questions and score them | `(score, total)` |
| `main()` | Tie it all together | Nothing |

Each function does **one job** and is small enough to test on its own. This is the habit that separates code you can fix from code you have to rewrite.

> **Tip**: Write the list of functions on paper before you touch the keyboard. Ten minutes of planning saves an hour of confusion.

---

## 14.2 The Question Bank

Create a **new folder** called `python-quiz-game`, and inside it a file called `questions.py`.

Each question is a dictionary with four keys — exactly the shape from Class 11:

```python
# questions.py
"""The question bank for the Quiz Game."""

QUESTIONS = [
    {
        "category": "Physics",
        "question": "What is the SI unit of force?",
        "options": ["Joule", "Newton", "Watt", "Pascal"],
        "answer": 1,
    },
    {
        "category": "Physics",
        "question": "What is the approximate acceleration due to gravity on Earth?",
        "options": ["3.7 m/s^2", "6.0 m/s^2", "9.8 m/s^2", "12.5 m/s^2"],
        "answer": 2,
    },
    {
        "category": "Chemistry",
        "question": "What is the chemical symbol for sodium?",
        "options": ["So", "Sd", "Na", "S"],
        "answer": 2,
    },
    {
        "category": "Chemistry",
        "question": "What is the atomic number of carbon?",
        "options": ["4", "6", "8", "12"],
        "answer": 1,
    },
    {
        "category": "Biology",
        "question": "Which organelle is known as the powerhouse of the cell?",
        "options": ["Ribosome", "Nucleus", "Mitochondrion", "Golgi body"],
        "answer": 2,
    },
    {
        "category": "Maths",
        "question": "What is the value of pi, correct to two decimal places?",
        "options": ["3.12", "3.14", "3.16", "3.18"],
        "answer": 1,
    },
    {
        "category": "Python",
        "question": "Which symbol starts a comment in Python?",
        "options": ["//", "#", "/*", "--"],
        "answer": 1,
    },
]
```

### Why `"answer"` holds a number

`"answer": 1` means "the correct option is at **position 1**" — which is `"Newton"`, because counting starts at 0.

This is much better than storing the answer text. To show the correct answer you write `item["options"][item["answer"]]`, and to mark the player you compare two numbers. No spelling, no capitals, no stray spaces to worry about.

> **Careful**: The commonest mistake when adding questions is an off-by-one `"answer"`. Options are numbered **0, 1, 2, 3**, not 1, 2, 3, 4. Count on your fingers starting at zero.

### Checking the bank loads

```python
from questions import QUESTIONS

print(f"Loaded {len(QUESTIONS)} questions.")
print(QUESTIONS[0]["question"])
print(QUESTIONS[0]["options"][QUESTIONS[0]["answer"]])
```

**Expected output:**

```
Loaded 7 questions.
What is the SI unit of force?
Newton
```

---

## 14.3 Splitting a Program Across Files

`from questions import QUESTIONS` is new. You met `import math` in Class 12; this is the other form.

| Form | Effect | Use it as |
|------|--------|-----------|
| `import math` | Brings in the whole module | `math.sqrt(9)` |
| `from questions import QUESTIONS` | Brings in **one name** from it | `QUESTIONS` |

Both files must sit in the **same folder**. The file is `questions.py`; the import drops the `.py`.

Splitting the program in two is not showing off — it is what makes the game easy to extend. Adding a question means editing a plain data file with no logic in it. The Quiz Game's rules and the Quiz Game's content stay apart.

---

## 14.4 Getting a Valid Answer

Now create `quiz_game.py` in the same folder.

```python
# quiz_game.py
"""A terminal quiz game."""

from questions import QUESTIONS

LETTERS = "ABCD"


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
```

This one function uses six things you have learned:

| Line | Concept | Class |
|------|---------|-------|
| `LETTERS[:option_count]` | String slicing | 8 |
| `"/".join(valid)` | Joining | 8 |
| `while True:` | Loop until valid | 7 |
| `.strip().upper()` | Chained string methods | 8 |
| `valid.find(typed)` | `-1` means not found | 8 |
| `return position` | Returning a value | 12 |

`.upper()` means the player can type `a` or `A`. `.strip()` forgives a stray space. `find()` returning `-1` is how we detect a letter that is not an option.

Test it on its own before going further:

```python
print(ask_for_letter(4))
```

**Sample run:**

```
Your answer (A/B/C/D): z
'Z' is not one of the options. Try again.
Your answer (A/B/C/D): bb
Please type a single letter.
Your answer (A/B/C/D): b
1
```

> **Tip**: Test each function as soon as you write it. Finding a bug in ten lines is easy; finding it in a hundred is not.

---

## 14.5 Asking One Question

```python
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
```

Three things to note:

- The three values are pulled out into `category`, `options` and `correct` at the top. Doing this once is clearer than writing `item["options"]` five times.
- `for index in range(len(options))` is used because we need the **position** — `LETTERS[index]` gives us `A`, `B`, `C`, `D`. This is the Class 9 pattern for when the index matters.
- It returns `True` or `False` rather than printing a score. The caller decides what to do with that, which keeps the function reusable.

Test it:

```python
print(ask_question(QUESTIONS[0], 1, 1))
```

**Sample run:**

```

Question 1 of 1   [Physics]
What is the SI unit of force?
   A. Joule
   B. Newton
   C. Watt
   D. Pascal
Your answer (A/B/C/D): b
Correct!
True
```

---

## 14.6 Grading and the Round

```python
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


def play_round(questions, player_name):
    """Play one full round of the quiz. Return a tuple of (score, total)."""
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
```

`play_round` is the **accumulator pattern** from Class 6, wrapped in a function: `score = 0` before the loop, `score += 1` inside it when `ask_question` returns `True`.

The `if len(questions) < total` guard matters. Asking for five questions from a bank of three would raise an `IndexError`, so we quietly ask three instead. Guarding against the data being smaller than you assumed is a habit worth having.

Add the two constants at the top of the file, under `LETTERS`:

```python
QUESTIONS_PER_ROUND = 5
LINE = "-" * 46
```

Both are in capitals because they never change — the Class 2 convention, and the reason you can change the round length by editing one line.

---

## 14.7 Putting It All Together

Add `main()` at the bottom of `quiz_game.py`, then call it. Your complete file should now read:

```python
# quiz_game.py
"""A terminal quiz game. Class 14 version."""

from questions import QUESTIONS

LETTERS = "ABCD"
QUESTIONS_PER_ROUND = 5
LINE = "-" * 46


def ask_for_letter(option_count):
    """Keep asking until the player types a valid option letter."""
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


def play_round(questions, player_name):
    """Play one full round of the quiz. Return a tuple of (score, total)."""
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


def main():
    """Run the whole game."""
    print("=" * 46)
    print("     TRITON COLLEGE — PYTHON QUIZ GAME")
    print("=" * 46)

    player_name = input("\nWhat is your name? ").strip()
    if player_name == "":
        player_name = "Player"

    print(f"\nWelcome, {player_name}. Answer by typing a letter, then press Enter.")
    print(f"There are {len(QUESTIONS)} questions in the bank.")

    score, total = play_round(QUESTIONS, player_name)

    print(f"\nThanks for playing, {player_name}. Goodbye!")


main()
```

Run it with `python quiz_game.py`.

**Sample run:**

```
==============================================
     TRITON COLLEGE — PYTHON QUIZ GAME
==============================================

What is your name? Sita

Welcome, Sita. Answer by typing a letter, then press Enter.
There are 7 questions in the bank.

Question 1 of 5   [Physics]
What is the SI unit of force?
   A. Joule
   B. Newton
   C. Watt
   D. Pascal
Your answer (A/B/C/D): b
Correct!

Question 2 of 5   [Physics]
What is the approximate acceleration due to gravity on Earth?
   A. 3.7 m/s^2
   B. 6.0 m/s^2
   C. 9.8 m/s^2
   D. 12.5 m/s^2
Your answer (A/B/C/D): c
Correct!

Question 3 of 5   [Chemistry]
What is the chemical symbol for sodium?
   A. So
   B. Sd
   C. Na
   D. S
Your answer (A/B/C/D): a
Wrong. The answer was C. Na

Question 4 of 5   [Chemistry]
What is the atomic number of carbon?
   A. 4
   B. 6
   C. 8
   D. 12
Your answer (A/B/C/D): b
Correct!

Question 5 of 5   [Biology]
Which organelle is known as the powerhouse of the cell?
   A. Ribosome
   B. Nucleus
   C. Mitochondrion
   D. Golgi body
Your answer (A/B/C/D): c
Correct!

----------------------------------------------
Round finished, Sita.
Score: 4 out of 5   (80.0%)   Grade: A
----------------------------------------------

Thanks for playing, Sita. Goodbye!
```

**You have written a working game.** Somebody who has never seen your code can sit down and play it.

Notice the one thing that is unsatisfying: it asks the **same five questions in the same order** every single time, and always the first five in the bank. The last two questions never get asked at all. That is what Class 15 fixes.

> **Try it**: Play it and deliberately type nonsense — press Enter with nothing, type `zzz`, type `5`, type a space. It should refuse all of them politely and never crash. Then change `QUESTIONS_PER_ROUND` to `3` and confirm the round gets shorter with no other edit.

---

## Practice Exercises

1. **Grow the bank** — Add at least five more questions to `questions.py` from your own subjects, including a new category that does not exist yet. Run the game and confirm `len(QUESTIONS)` reports the new total. Double-check every `"answer"` index by counting from zero.

2. **Two-option questions** — Add a true/false question with only two options: `"options": ["True", "False"]`. Run the game until it appears. The prompt should read `Your answer (A/B):` and typing `C` should be rejected. Which line of `ask_for_letter` makes that work automatically?

3. **Show the running score** — Change `play_round` so that after each question it prints `Score so far: 3/4`. You will need to move the print inside the loop. Why must it come *after* the `if ask_question(...)` line rather than before it?

4. **Encouragement** — Add a function `message_for(percentage)` that returns an encouraging sentence: "Outstanding!" above 90, "Well done." above 70, "A good effort." above 50, and "Keep practising." below that. Call it in `play_round` and print it under the grade.

---

## Key Takeaways

- **Plan before you type.** List what the program must do, then break it into functions that each do one job.
- A **question bank** is a **list of dictionaries** — the standard shape for records.
- Storing `"answer"` as an **index** into `"options"` avoids all string-matching problems. Options are numbered from **0**.
- **`from questions import QUESTIONS`** brings one name in from another file in the same folder. Keeping data and logic in separate files makes both easier to change.
- `ask_for_letter` combines slicing, `.join()`, `.strip().upper()`, `.find()` and `while True` to make invalid input impossible.
- **`.find()` returning `-1`** is how you detect an answer that is not an option.
- `ask_question` **returns `True`/`False`** rather than printing a score, so the caller decides what to do with it.
- `play_round` is the **accumulator pattern** in a function.
- **Guard against the data being smaller than you assume** — `if len(questions) < total`.
- **Test each function as you write it.** Bugs are cheap to find in ten lines.

Next class we will finish the game — shuffling questions, choosing a category, saving high scores to a file, and playing again without restarting.
