# Class 15: Mini Project Part 2 — Finishing the Quiz Game

> **Time budget**: 45 minutes (≈ 32 min teach + 13 min practice)
> **Prerequisites**: Class 14 (Mini Project Part 1)

Your game works, but it asks the same five questions in the same order every time. Today we make it shuffle, let the player pick a category, remember high scores between runs, and offer another round. Then we look at where to go next.

## What You Will Learn

- **Shuffling** the questions so every round differs
- Building a **category menu** from the data itself
- **Saving** and **reading** high scores with files
- The **replay loop**
- What you have learned, and what to learn next

---

## 15.1 Shuffling

Add `import random` at the top of `quiz_game.py`, below the docstring:

```python
import random

from questions import QUESTIONS
```

Now change the first lines of `play_round`:

```python
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
    ...
```

Two lines, and every round is now different.

`questions = list(question_bank)` makes a **copy** first. This matters more than it looks. `random.shuffle()` changes a list **in place** — it does not return a new one, exactly like `.sort()` from Class 9. Without the copy, the shuffle would permanently rearrange `QUESTIONS` itself, and the original order in your data file would be lost for the rest of the run.

> **Careful**: Never write `questions = random.shuffle(questions)`. `shuffle()` returns `None`, so that line would replace your list with nothing and the next line would fail with `TypeError: object of type 'NoneType' has no len()`.

Because we take the first five of a shuffled list, all seven questions now get a turn across several rounds instead of the last two never appearing.

---

## 15.2 The Category Menu

The interesting part here is that the menu is built **from the data**, not typed out by hand. Add a new question category to `questions.py` and it appears in the menu with no other change.

```python
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
```

`get_categories` is the Class 10 pattern exactly: a **set** removes duplicates automatically — five Physics questions give one `"Physics"` entry — and `sorted()` turns it into a predictable order, because a set has none.

Now the menu itself:

```python
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
```

This is the Class 13 validated-input pattern doing real work — `while True`, `try`/`except ValueError`, `continue`, and `return` to escape. Nothing the player types can break it.

The `number - 1` matters: the menu shows 1, 2, 3 to the player, but the list is indexed 0, 1, 2. Converting between "what humans count" and "what lists count" is a permanent part of programming.

---

## 15.3 Saving High Scores

Add two more constants at the top:

```python
SCORES_FILE = "scores.txt"
```

Then the saving function:

```python
def save_score(player_name, score, total):
    """Add one result to the end of the scores file."""
    try:
        with open(SCORES_FILE, "a") as scores_file:
            scores_file.write(f"{player_name}|{score}|{total}\n")
    except OSError:
        print("Your score could not be saved this time.")
```

Mode `"a"` for append — mode `"w"` would wipe every previous score each time somebody played. The `\n` is essential, or every result would run together on one line.

Reading them back is the defensive-parsing function from Class 13:

```python
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
```

Every guard earns its place:

| Guard | Protects against |
|-------|------------------|
| `except FileNotFoundError` | The very first run, when no file exists yet |
| `if line == ""` | The blank line at the end of most text files |
| `if len(parts) != 3` | A line that has been edited into the wrong shape |
| inner `try` / `except ValueError` | A score that is not a number |
| `if total <= 0` | A `ZeroDivisionError` on the very next line |

That last one is the subtle one. Without it, a line reading `Sita|0|0` would crash the program on `score / total`. Guarding a division against zero **before** doing it is a habit worth keeping.

Now display them:

```python
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
```

`results.sort(reverse=True)` sorts a list of **tuples**. Python compares tuples item by item, starting with the first — and we deliberately put `percentage` first when building each one. That is why the best score comes out on top. Had we stored `(name, percentage, ...)` it would have sorted alphabetically instead.

The `shown` counter with `if shown == 5: break` limits the table to the top five, using `break` from Class 7.

---

## 15.4 The Replay Loop

Finally, wrap the whole game in a loop so one round can follow another:

```python
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
```

`score, total = play_round(...)` is **tuple unpacking** from Class 10, catching the two values the function returns.

`again != "y"` after `.strip().lower()` means anything except `y` or `Y` ends the game — including an accidental Enter. Being generous about what counts as "yes" and strict about everything else is usually the right choice.

---

## 15.5 The Finished Game

Run it with `python quiz_game.py`.

**Sample run:**

```
==============================================
     TRITON COLLEGE — PYTHON QUIZ GAME
==============================================

What is your name? Aarya

Welcome, Aarya. Answer by typing a letter, then press Enter.

Choose a category:
   0. All categories
   1. Biology
   2. Chemistry
   3. Maths
   4. Physics
   5. Python
Category number: 4

Category: Physics — 2 questions available.

Question 1 of 2   [Physics]
What is the approximate acceleration due to gravity on Earth?
   A. 3.7 m/s^2
   B. 6.0 m/s^2
   C. 9.8 m/s^2
   D. 12.5 m/s^2
Your answer (A/B/C/D): c
Correct!

Question 2 of 2   [Physics]
What is the SI unit of force?
   A. Joule
   B. Newton
   C. Watt
   D. Pascal
Your answer (A/B/C/D): b
Correct!

----------------------------------------------
Round finished, Aarya.
Score: 2 out of 2   (100.0%)   Grade: A+
----------------------------------------------

High scores
----------------------------------------------
1. Aarya          2/2   (100.0%)
----------------------------------------------

Play again? (y/n): n

Thanks for playing, Aarya. Goodbye!
```

Run it a second time and the high-score table still shows Aarya. **The data outlived the program.**

> **Note**: That run used the seven-question bank you built in Class 14, which is why Physics offers only two questions. The reference copy in `python-quiz-game/` ships with fifteen questions — three in each of the five categories — so its rounds are longer. Both run on exactly the same `quiz_game.py`. That is the whole point of keeping the data in its own file.

> **Try it**: Play three rounds under different names, then quit and restart. All the scores are still there. Now open `scores.txt` in VS Code — it is a plain text file you can read. Delete a line, add a rubbish line, and run the game again. It should ignore the damage and carry on.

### Every class, in one program

| Class | Where it shows up |
|-------|-------------------|
| 1 | `print()`, `"=" * 46`, comments |
| 2 | Variables, `CONSTANTS` in capitals |
| 3 | `input()`, f-strings, `int()` |
| 4 | `%`, comparisons, `and`/`or` |
| 5 | `if` / `elif` / `else` in `grade_for` |
| 6 | `for` loops, the accumulator `score += 1` |
| 7 | `while True`, `break`, `continue` |
| 8 | `.strip()`, `.upper()`, `.find()`, `.join()`, slicing, `{name:<14}` |
| 9 | Lists, `.append()`, `.sort(reverse=True)`, `len()` |
| 10 | Sets in `get_categories`, tuples returned and unpacked |
| 11 | Dictionaries — the whole question bank |
| 12 | Every function, `random.shuffle` |
| 13 | `try`/`except`, `with open(...)`, `FileNotFoundError` |

Nothing was taught that you did not use. That was the plan from Class 1.

---

## 15.6 Where To Go Next

You can now write real programs. Here is an honest map of what you have not seen.

### Things this course deliberately skipped

| Topic | What it gives you |
|-------|-------------------|
| **Classes and objects** | Bundling data and functions together — the next big idea in Python |
| **List comprehensions** | `[n * 2 for n in numbers]` — a one-line loop that builds a list |
| **`if __name__ == "__main__":`** | The standard guard that lets a file be both a program and a module |
| **Modules and packages** | Organising a program across many files properly |
| **`pip` and virtual environments** | Installing the hundreds of thousands of libraries other people have written |

### Where Python goes from here

| Field | Libraries to look up |
|-------|---------------------|
| Data analysis | `pandas`, `numpy` |
| Graphs and charts | `matplotlib` |
| Websites | `Django`, `Flask` |
| Automation | `requests`, `openpyxl` |
| Machine learning | `scikit-learn`, `PyTorch` |
| Games | `pygame` |

For Class 12 Science students, `matplotlib` is the natural next step — plotting your Physics practical data is far more satisfying than plotting it on graph paper.

### How to keep improving

1. **Keep writing programs.** Reading about code teaches you very little. Pick something small and irritating in your own life and automate it.
2. **Extend this game.** The exercises below are a genuine to-do list.
3. **Read the official tutorial** at [docs.python.org/3/tutorial](https://docs.python.org/3/tutorial/) — it is well written and free.
4. **Do not fear errors.** You have read enough tracebacks now to know they are instructions, not insults.
5. **Type the code out.** Copying and pasting teaches your clipboard, not you.

> The gap between a beginner and a competent programmer is not talent. It is the number of programs written. You have written about thirty. Write thirty more.

---

## Practice Exercises

These are ordered by difficulty. Do as many as you can — this is your project now.

1. **Add your own questions** — Grow `questions.py` to at least 25 questions across five categories, drawn from your own NEB syllabus. Confirm the category menu updates itself with no change to `quiz_game.py`. This is the payoff for building the menu from the data.

2. **Negative marking** — Change the scoring so a correct answer gives 4 marks and a wrong one deducts 1, as in a real entrance exam. You will need to change what `ask_question` returns, or how `play_round` uses it, and the percentage calculation must change too. What is the lowest possible score, and does your grade function cope with it?

3. **Show the player their personal best** — Before the round starts, use `read_scores()` to find the highest percentage this player has ever scored, and print "Your best so far: 80.0%". Handle the case where they have never played before.

4. **Difficulty levels** — Add `"difficulty": "easy"` or `"hard"` to every question. Let the player choose a difficulty as well as a category, and filter on both. Hint: write a second filter function rather than complicating the first one.

5. **A timed round** — Look up the `time` module, specifically `time.time()`. Record the time before and after a round, and report how many seconds the player took and their average seconds per question. This uses something the course never taught you — finding out how a new module works from its documentation is the real skill.

---

## Key Takeaways

- **`random.shuffle()`** changes a list **in place** and returns `None`. Copy the list first with `list(...)` if you need the original order preserved.
- Build menus **from the data**, not by hand — then adding data updates the interface for free.
- A **set** plus **`sorted()`** turns duplicated values into a clean, ordered menu.
- Convert between the numbers you **show** a person (1, 2, 3) and the indexes a **list** uses (0, 1, 2).
- Save with mode **`"a"`** so previous data survives. Always write the **`\n`**.
- **Guard every assumption** when reading a file: missing file, blank line, wrong shape, non-numeric value, and division by zero.
- Sorting a list of **tuples** compares the first item first — so put the value you want to sort by at the front.
- **`score, total = play_round(...)`** unpacks a returned tuple.
- You have used every concept from Classes 1 to 13 in one working program.
- The way to get better is to **write more programs**. Nothing else works as well.

---

## Well done

Fifteen classes ago you had never written a line of code. You can now take input, make decisions, repeat work, store data in four different collection types, write your own functions, handle things going wrong, and save your work to disk — and you have built a complete game that other people can play.

That is a genuine skill, and it belongs to you now. Keep using it.
