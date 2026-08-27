# Basic Python Course — Claude Project Instructions

## Project Identity
This is a **teaching/educational project** designed to take complete beginners — **Class 12 Science students** — from zero programming knowledge to writing working Python programs and building a small terminal game. The instructor is **Er. Prabin Karki**, a senior full-stack developer teaching at Triton College (Nepal).

This course is **fundamentals-only**. It teaches core Python using nothing but the standard library, so a college computer lab needs Python installed and nothing else — no internet, no `pip install`, no virtual environments.

## Project Purpose
Teach Class 12 Science students to read, write and debug basic Python programs across **15 classes of 45 minutes**, delivered inside a **10-day training window**. The course ends with a mini project — a **terminal Quiz Game** — built across the final two classes, which pulls together every concept taught: variables, conditionals, loops, strings, lists, dictionaries, functions, error handling and file input/output.

The number of classes per day is **flexible** (sometimes one, sometimes two) at the college's discretion. Each lesson file is sized for exactly **one** 45-minute class, so the schedule can flex without changing the material.

## Language and Tools
- **Language**: Python 3.12 or newer
- **Editor**: Visual Studio Code with the official **Python** extension (`ms-python.python`)
- **Fallback editor**: IDLE, which ships with Python, for lab machines that cannot install VS Code
- **Modules used**: `math` and `random` only — both part of the standard library
- **Terminal**: `python` on Windows, `python3` on macOS and Linux
- **No third-party packages.** No `pip install`, no virtual environments, no NumPy, no pandas.
- **Formatting**: f-strings only. Never teach `%` formatting or `.format()`.

## Project Structure
```
basic-python-course/
├── CLAUDE.md                 # This file — project instructions
├── README.md                 # Public-facing course overview
├── SUMMARY.md                # Curriculum, schedule, per-class checklist and budget
├── .gitignore
├── assets/                   # Course images and diagrams
├── lessons/                  # 15 individual class files
│   ├── 01-introduction-and-setup.md
│   ├── 02-variables-and-data-types.md
│   ├── 03-input-output-and-type-conversion.md
│   ├── 04-operators-and-expressions.md
│   ├── 05-decisions-if-elif-else.md
│   ├── 06-for-loops-and-range.md
│   ├── 07-while-loops-break-continue.md
│   ├── 08-strings.md
│   ├── 09-lists.md
│   ├── 10-tuples-and-sets.md
│   ├── 11-dictionaries.md
│   ├── 12-functions-and-modules.md
│   ├── 13-errors-files-and-exceptions.md
│   ├── 14-project-quiz-game-part-1.md
│   └── 15-project-quiz-game-part-2.md
└── python-quiz-game/         # Reference project — the finished mini project
    ├── README.md
    ├── questions.py
    ├── quiz_game.py
    └── scores.txt
```

## Schedule
- **Total classes**: 15
- **Class length**: 45 minutes (each lesson file is sized for exactly one class)
- **Frequency**: 1 or 2 classes per day, flexible
- **Total duration**: 10 days maximum (≈ 11.25 teaching hours)

## Teaching Guidelines
- **Audience**: Class 12 Science students. Assume basic computer literacy and school-level Maths and Physics, but **no prior coding experience whatsoever**.
- **Language**: UK English. Short, plain sentences. Never use jargon without explaining it immediately with an analogy.
- **Approach**: Theory first (with an analogy) → complete runnable code example → line-by-line walkthrough → expected output → practice exercises.
- **Pace**: Each class builds on the previous — never use a concept before the class that introduces it.
- **Code examples**: Every concept must include a complete, runnable snippet with its expected output shown.
- **Exercises**: Each class ends with **Practice Exercises** a student can finish in 15–25 minutes.
- **Subject-linked examples**: Wherever possible, use Physics, Chemistry, Maths and Biology examples — the students already understand the domain, so only the code is new.

## Rules for Content Creation
1. Keep explanations simple and beginner-friendly — students are seeing this for the first time.
2. Use real-world analogies (variable = a labelled box; list = a row of lockers; dictionary = a roll-number register; function = a recipe; loop = doing laps of a field).
3. Every code block must be complete and runnable exactly as printed.
4. Always show an **Expected output:** block after a code example.
5. Each class must fit in 45 minutes of teaching (≈ 32 min teach + 13 min supervised practice).
6. Begin every class with **What You Will Learn** (4–6 bullets).
7. End every class with **Practice Exercises** (3–4 tasks) and a **Key Takeaways** section.
8. Use **UK English** spelling (colour, organise, behaviour, practise as a verb, licence, centre).
9. Make **no assumptions** about prior knowledge — explain every term the first time it appears.
10. Build incrementally — never use a feature before it has been taught. In particular: no functions before Class 12, no dictionaries before Class 11, no `try`/`except` before Class 13.
11. Use **f-strings** for all output formatting. Never `%` formatting, never `.format()`.
12. Use only the **standard library**, and only `math` and `random` from it.
13. No object-oriented programming, no classes, no decorators, no generators, no lambda. List comprehensions are mentioned once, in Class 15, as a "what next" teaser only.
14. Write file paths and commands for **both Windows and macOS** where they differ (`python` vs `python3`).
15. Number every teaching section as `## <class number>.<section index>` — for example `## 7.1`, `## 7.2`.

## Voice and Style
- Friendly, encouraging, never condescending.
- Short paragraphs. Bullet points where helpful.
- Tables for comparison or quick reference.
- Code first, words second when a concept is best shown.
- Blockquote callouts for emphasis: `> **Tip**:`, `> **Try it**:`, `> **Careful**:`, `> **Analogy**:`, `> **Common error**:`.
- `---` horizontal rules between numbered sections.
- **No emoji in headings.** `✅` and `❌` may appear only as inline markers inside code comments.
- Always invite curiosity ("Change the number and run it again — what happens?").

## What This Course Does NOT Cover
- Object-oriented programming — classes, objects, inheritance.
- Third-party libraries — NumPy, pandas, Matplotlib, Requests.
- Web frameworks (Django, Flask) and databases.
- GUI applications (Tkinter, PyQt).
- Virtual environments, `pip`, packaging and deployment.
- Advanced features — decorators, generators, comprehensions, lambda, recursion.

These are named honestly in Class 15 as "where to go next", so students leave knowing what they have and have not learned.

## Reference Course
A sibling course exists at `../react-beginner-course/`. Consult it for tone, formatting conventions and lesson structure. Do **not** copy its content — that course is web development for BCA students, this one is Python fundamentals for Class 12 Science.
