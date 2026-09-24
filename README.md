# Basic Python Course — Programming Fundamentals for Class 12 Science

A complete **15-class** beginner course taking Class 12 Science students from zero programming knowledge to writing working Python programs and building their own terminal game — delivered inside a **10-day training window**.

## Instructor

**Er. Prabin Karki**
Bachelor in Computer Science and Engineering
[prabin-karki.com.np](https://prabin-karki.com.np) · prabinkarki643@gmail.com

**Course URL:**
https://github.com/prabinkarki643/basic-python-course


## Who This Course Is For

- **Class 12 Science students** (NEB or equivalent)
- Complete beginners to programming
- Students who can use a computer and browse the web, but have **never written code before**

No Maths beyond school level is needed. If you can work out a percentage and rearrange a formula, you have everything required.

## What You Will Learn

By the end of this course, every student will be able to:

1. Install Python and run a program from the terminal and from an editor
2. Store and use data with **variables** and the four core types — `int`, `float`, `str`, `bool`
3. Take input from a user, convert it to the right type, and print formatted output with **f-strings**
4. Use all of Python's **operators**, including `//`, `%` and `**`, with correct precedence
5. Make decisions with `if` / `elif` / `else` and combine conditions with `and`, `or`, `not`
6. Repeat work with `for` and `while` **loops**, and control them with `break` and `continue`
7. Slice, search and transform **strings** with Python's built-in string methods
8. Store collections of data in **lists**, **tuples**, **sets** and **dictionaries**, and choose the right one
9. Write reusable **functions** and import from the `math` and `random` modules
10. Read a traceback, handle errors with `try` / `except`, and read and write **text files**
11. Combine everything to build a complete, working **Quiz Game**

## The Project — a Terminal Quiz Game

From Class 14 the whole class builds **one project**: a Quiz Game that runs in the terminal. It stores its questions as a list of dictionaries, shuffles them with `random`, asks multiple-choice questions, validates every answer the player types, scores the round, awards a grade, and saves high scores to a text file that survives after the program closes.

The finished reference code lives in [`python-quiz-game/`](python-quiz-game/) — students build it themselves across the last two classes, then extend it.

## Course Structure

| Phase | Classes | Topic | Time |
|-------|---------|-------|------|
| 1 — Getting Started | 1–3 | Setup, variables, input and output | 2¼ hrs |
| 2 — Logic & Control Flow | 4–7 | Operators, decisions, loops | 3 hrs |
| 3 — Working With Data | 8–11 | Strings, lists, tuples, sets, dictionaries | 3 hrs |
| 4 — Functions, Files & Safety | 12–13 | Functions, modules, errors, file handling | 1½ hrs |
| 5 — Mini Project | 14–15 | Building and finishing the Quiz Game | 1½ hrs |
| **Total** | **15 classes** | | **11¼ hrs** |

**Schedule**: 45 minutes per class, 1 or 2 classes per day, spread across a maximum of 10 days. Each lesson file is sized for exactly **one** class. See [SUMMARY.md](SUMMARY.md) for the suggested day-by-day map.

## Tools

| Item | What we use |
|------|-------------|
| **Language** | Python 3.12 or newer |
| **Editor** | Visual Studio Code + the Python extension |
| **Fallback editor** | IDLE (ships with Python) |
| **Modules** | `math`, `random` — both built in |
| **Third-party packages** | None. Nothing to install, nothing to download. |

## Prerequisites — Before Class 1

The lab or the student's own laptop needs:

### Software installed
- [ ] **Python 3.12 or newer** — [python.org/downloads](https://www.python.org/downloads/)
      (On Windows, tick **"Add python.exe to PATH"** on the first installer screen — this is the single most common setup mistake.)
- [ ] **Visual Studio Code** — [code.visualstudio.com](https://code.visualstudio.com)
- [ ] **Python extension for VS Code** (`ms-python.python`)

### Nothing else
No accounts, no internet connection during class, no package downloads. Everything in this course runs on a plain Python installation.

Full step-by-step setup instructions, including how to check the install worked, are in [Class 1](lessons/01-introduction-and-setup.md).

## Repository Structure

```
basic-python-course/
├── README.md                  # This file — public-facing overview
├── SUMMARY.md                 # Curriculum, schedule, checklists and budget
├── CLAUDE.md                  # Project instructions for Claude Code
├── .gitignore
├── assets/                    # Images and diagrams
├── lessons/                   # 15 class files (Markdown)
│   ├── 01-introduction-and-setup.md
│   ├── 02-variables-and-data-types.md
│   ├── ... (11 more) ...
│   └── 15-project-quiz-game-part-2.md
└── python-quiz-game/          # Reference project — the finished Quiz Game
    ├── questions.py
    ├── quiz_game.py
    └── scores.txt
```

## How To Use This Course

### Students
1. Complete the **Prerequisites** above before Class 1.
2. Read one lesson per class. **Type out every code example yourself** — do not copy and paste. Typing is how the syntax sticks.
3. Run every example and check the output matches. When it does not, read the error message before asking — it usually tells you the answer.
4. Complete the **Practice Exercises** at the end of each class.
5. Keep every program you write in one folder. By Class 15 you will have around thirty of them, and looking back at Class 1 is genuinely satisfying.

### Instructors
1. Read [SUMMARY.md](SUMMARY.md) for the full curriculum, per-class checklists, day map and budget.
2. Read [CLAUDE.md](CLAUDE.md) for the course's tone, style and content rules.
3. Each lesson file in `lessons/` is the **single source of truth** for that class — teach directly from it.
4. Every code block is tested and runs as printed. Type them live on the projector; do not paste.
5. Use the **Practice Exercises** as in-class supervised work (13 minutes are reserved at the end of every class) or as homework.

## What This Course Does Not Cover

Stated honestly so nobody is surprised: no object-oriented programming, no third-party libraries such as NumPy or pandas, no web frameworks, no databases and no GUI applications. This is a fundamentals course. Class 15 ends with a clear map of where to go next.

## Related Courses

- **Web development**: `../react-beginner-course/` — HTML, CSS, JavaScript and React, for students who want to build websites.

## Licence

Course content © Er. Prabin Karki. Free to use for educational purposes with attribution.
