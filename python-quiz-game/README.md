# Python Quiz Game — Reference Project

This is the finished mini project for the **Basic Python Course**. Students build it themselves across **Class 14** and **Class 15**; this folder is the reference to check against if a student gets stuck.

## Running it

Open a terminal **in this folder** and run:

```
python quiz_game.py      # Windows
python3 quiz_game.py     # macOS and Linux
```

Nothing needs to be installed. The game uses only Python's standard library.

## What it does

- Asks the player for their name
- Lets them choose a category, or play across all categories
- Shuffles the questions so no two rounds are the same
- Asks five multiple-choice questions, one at a time
- Refuses invalid answers politely and asks again, rather than crashing
- Scores the round, works out a percentage and awards a grade
- Saves the result to `scores.txt` and shows the five best scores so far
- Offers another round

## Files

| File | What it holds |
|------|---------------|
| `questions.py` | The question bank — 15 questions across Physics, Chemistry, Biology, Maths and Python |
| `quiz_game.py` | The game itself — all the functions and the `main()` loop |
| `scores.txt` | Saved results, one per line, in the format `name\|score\|total` |

`scores.txt` is created automatically the first time somebody plays. The copy in this folder holds sample data so the high-score table has something to show.

## Which class teaches which part

| Function | Concept | Taught in |
|----------|---------|-----------|
| `get_categories` | Sets, `sorted()` | Class 10 |
| `filter_by_category` | Lists, `for`, `if` | Classes 5, 6, 9 |
| `choose_category` | `while True`, `try`/`except`, `int()` | Classes 3, 7, 13 |
| `ask_for_letter` | String slicing, `.join()`, `.find()` | Class 8 |
| `ask_question` | Dictionaries, `range(len(...))` | Classes 6, 11 |
| `grade_for` | `if`/`elif`/`else`, `return` | Classes 5, 12 |
| `play_round` | `random.shuffle`, accumulator, tuples | Classes 6, 10, 12 |
| `save_score` | `with open(..., "a")` | Class 13 |
| `read_scores` | Reading a file, `.split()`, `try`/`except` | Classes 8, 13 |
| `show_high_scores` | `.sort(reverse=True)`, f-string alignment | Classes 8, 9 |

## Extending it

Class 15 ends with these challenges, in rough order of difficulty:

1. **Add your own questions.** Copy a dictionary in `questions.py`, change the four values, and check `"answer"` points at the right option. The game picks them up with no other change.
2. **Add a new category.** Add three questions with a `"category"` that does not exist yet — it appears in the menu automatically.
3. **Change the round length.** Edit `QUESTIONS_PER_ROUND` at the top of `quiz_game.py`.
4. **Add a points system.** Award 4 marks for a correct answer and deduct 1 for a wrong one, the way a real entrance exam does.
5. **Add a difficulty key.** Give every question `"difficulty": "easy"` or `"hard"` and let the player choose.
6. **Show the player their best-ever score** before the round starts, using `read_scores()`.

## Note for instructors

The file ends with a plain call to `main()` rather than the `if __name__ == "__main__":` guard. That guard is deliberately not taught on this course — it needs concepts well beyond a beginner's first fifteen classes, and explaining it properly would cost more time than it is worth here. It is mentioned in Class 15 as one of the things to look up next.
