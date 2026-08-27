# Class 11: Dictionaries — Storing Values Against Names

> **Time budget**: 45 minutes (≈ 32 min teach + 13 min practice)
> **Prerequisites**: Class 10 (Tuples and Sets)

Lists store values against **numbers** — position 0, position 1, position 2. But you rarely think "give me student number 3"; you think "give me Aarya's marks". A **dictionary** stores values against names, and it is the structure the Quiz Game is built from.

## What You Will Learn

- Creating **dictionaries** as key–value pairs
- Reading values safely with `[ ]` and **`.get()`**
- Adding, updating and deleting entries
- Looping with **`.keys()`**, **`.values()`** and **`.items()`**
- **Nested** dictionaries, and a list of dictionaries — the Quiz Game's shape

---

## 11.1 What Is a Dictionary?

A dictionary stores **key–value pairs**. You look something up by its key and get its value.

```python
student = {
    "name": "Aarya Gurung",
    "class": 12,
    "stream": "Science",
    "percentage": 84.25
}

print(student)
print(student["name"])
print(student["percentage"])
```

**Expected output:**

```
{'name': 'Aarya Gurung', 'class': 12, 'stream': 'Science', 'percentage': 84.25}
Aarya Gurung
84.25
```

> **Analogy**: A real dictionary. You do not look up the 4,271st word — you look up "photosynthesis" and get its meaning. The word is the **key**, the meaning is the **value**.

Compare the two ways of storing the same student:

```python
# As a list — what does position 2 mean?
student_list = ["Aarya Gurung", 12, "Science", 84.25]
print(student_list[2])

# As a dictionary — no guessing needed
student_dict = {"name": "Aarya Gurung", "class": 12, "stream": "Science", "percentage": 84.25}
print(student_dict["stream"])
```

**Expected output:**

```
Science
Science
```

Both work. Only one still makes sense in six months. Notice too that `"class"` is a perfectly good **key**, even though it is a reserved word and could not be a variable name.

### The rules

- Keys must be **unique**. Assign the same key twice and the second value wins.
- Keys must be **immutable** — strings, numbers and tuples are fine; a list is not.
- Values can be **anything** — including lists and other dictionaries.
- Dictionaries **keep their insertion order** in modern Python. Unlike sets, what you put in first comes out first.

```python
marks = {"Physics": 82, "Chemistry": 76, "Physics": 91}
print(marks)
```

**Expected output:**

```
{'Physics': 91, 'Chemistry': 76}
```

The second `"Physics"` overwrote the first. There is only ever one entry per key.

---

## 11.2 Reading Values

### Square brackets — strict

```python
marks = {"Physics": 82, "Chemistry": 76}
print(marks["Physics"])
print(marks["Biology"])
```

**Expected output:**

```
82
KeyError: 'Biology'
```

A missing key raises a **`KeyError`**. This is the dictionary equivalent of `IndexError`.

### `.get()` — forgiving

```python
marks = {"Physics": 82, "Chemistry": 76}

print(marks.get("Physics"))
print(marks.get("Biology"))
print(marks.get("Biology", 0))
print(marks.get("Biology", "Not taken"))
```

**Expected output:**

```
82
None
0
Not taken
```

`.get()` returns `None` when the key is missing instead of crashing, and a second argument lets you choose a different fallback. `None` is Python's way of saying "no value at all" — you met it in Class 9 when `.sort()` returned it.

| You want | Use |
|----------|-----|
| To be certain the key exists, and crash loudly if not | `marks["Physics"]` |
| A sensible default when the key may be missing | `marks.get("Physics", 0)` |

### Checking first

```python
marks = {"Physics": 82, "Chemistry": 76}

print("Physics" in marks)
print("Biology" in marks)

if "Biology" in marks:
    print(marks["Biology"])
else:
    print("Biology was not taken.")
```

**Expected output:**

```
True
False
Biology was not taken.
```

`in` checks the **keys**, not the values. To search values, use `in marks.values()`.

---

## 11.3 Adding, Updating and Deleting

```python
marks = {"Physics": 82}

marks["Chemistry"] = 76          # new key — added
marks["Physics"] = 91            # existing key — updated
marks["Biology"] = 67

print(marks)
print(len(marks))
```

**Expected output:**

```
{'Physics': 91, 'Chemistry': 76, 'Biology': 67}
3
```

Adding and updating use identical syntax. If the key exists, the value is replaced; if not, the pair is added. This is why dictionaries are so convenient for counting things.

### Deleting

```python
marks = {"Physics": 82, "Chemistry": 76, "Biology": 67}

del marks["Chemistry"]
print(marks)

removed = marks.pop("Biology")
print(removed)
print(marks)

safe = marks.pop("History", "was not there")
print(safe)
```

**Expected output:**

```
{'Physics': 82, 'Biology': 67}
67
{'Physics': 82}
was not there
```

`del` deletes and gives nothing back. `.pop(key)` deletes and **returns** the value, and takes an optional default so it does not crash on a missing key.

### `.update()`

```python
marks = {"Physics": 82}
marks.update({"Chemistry": 76, "Biology": 67})
print(marks)
```

**Expected output:**

```
{'Physics': 82, 'Chemistry': 76, 'Biology': 67}
```

---

## 11.4 Looping Through a Dictionary

There are three ways, and choosing the right one makes your code read well.

```python
marks = {"Physics": 82, "Chemistry": 76, "Biology": 67}

print("Keys:")
for subject in marks.keys():
    print(f"  {subject}")

print("Values:")
for score in marks.values():
    print(f"  {score}")

print("Both:")
for subject, score in marks.items():
    print(f"  {subject}: {score}")
```

**Expected output:**

```
Keys:
  Physics
  Chemistry
  Biology
Values:
  82
  76
  67
Both:
  Physics: 82
  Chemistry: 76
  Biology: 67
```

`.items()` gives you each pair as a **tuple**, which the loop unpacks into two variables — exactly the unpacking you learned in Class 10.

Looping over a dictionary directly gives the **keys**, so `.keys()` is usually redundant:

```python
marks = {"Physics": 82, "Chemistry": 76}

for subject in marks:
    print(f"{subject}: {marks[subject]}")
```

**Expected output:**

```
Physics: 82
Chemistry: 76
```

> **Tip**: Use `.items()` whenever you need both the key and the value. It is clearer and faster than looping over keys and looking each value up again.

### Statistics on the values

The built-ins from Class 9 work on `.values()`:

```python
marks = {"Physics": 82, "Chemistry": 76, "Biology": 67, "Maths": 88}

total = sum(marks.values())
average = total / len(marks)
best = max(marks.values())

print(f"Total:   {total}")
print(f"Average: {average:.2f}")
print(f"Best:    {best}")
```

**Expected output:**

```
Total:   313
Average: 78.25
Best:    88
```

To find **which subject** scored best, loop with `.items()`:

```python
marks = {"Physics": 82, "Chemistry": 76, "Biology": 67, "Maths": 88}

best_subject = ""
best_score = 0

for subject, score in marks.items():
    if score > best_score:
        best_score = score
        best_subject = subject

print(f"Best subject: {best_subject} ({best_score})")
```

**Expected output:**

```
Best subject: Maths (88)
```

### Counting with a dictionary

This is one of the most useful patterns in all of Python:

```python
attendance = ["Sita", "Bibek", "Sita", "Aarya", "Bibek", "Sita"]

counts = {}

for name in attendance:
    counts[name] = counts.get(name, 0) + 1

print(counts)

for name, times in counts.items():
    print(f"{name:<8}{times}")
```

**Expected output:**

```
{'Sita': 3, 'Bibek': 2, 'Aarya': 1}
Sita    3
Bibek   2
Aarya   1
```

The line `counts[name] = counts.get(name, 0) + 1` does all the work. `.get(name, 0)` returns the count so far, or 0 if this is the first time the name has appeared, and adding 1 then storing it back handles both cases without an `if`.

---

## 11.5 Nesting

Values can be any type at all — including lists and other dictionaries. This is what lets you build realistic data.

### A dictionary of dictionaries

```python
students = {
    "Sita": {"physics": 82, "chemistry": 88},
    "Aarya": {"physics": 91, "chemistry": 79},
}

print(students["Sita"])
print(students["Sita"]["physics"])
print(students["Aarya"]["chemistry"])
```

**Expected output:**

```
{'physics': 82, 'chemistry': 88}
82
79
```

Read `students["Sita"]["physics"]` left to right: get Sita's record, then get physics from it.

Looping over nested data needs a nested loop:

```python
students = {
    "Sita": {"physics": 82, "chemistry": 88},
    "Aarya": {"physics": 91, "chemistry": 79},
}

for name, subjects in students.items():
    total = sum(subjects.values())
    print(f"{name}: total {total}")
    for subject, score in subjects.items():
        print(f"   {subject:<12}{score}")
```

**Expected output:**

```
Sita: total 170
   physics     82
   chemistry   88
Aarya: total 170
   physics     91
   chemistry   79
```

### A list of dictionaries — the Quiz Game's shape

This is the single most common data shape in real programming, and it is exactly how the Quiz Game stores its questions.

```python
questions = [
    {
        "category": "Physics",
        "question": "What is the SI unit of force?",
        "options": ["Joule", "Newton", "Watt", "Pascal"],
        "answer": 1,
    },
    {
        "category": "Chemistry",
        "question": "What is the chemical symbol for sodium?",
        "options": ["So", "Sd", "Na", "S"],
        "answer": 2,
    },
]

print(f"There are {len(questions)} questions.")

for item in questions:
    print()
    print(f"[{item['category']}] {item['question']}")

    for i in range(len(item["options"])):
        print(f"   {i}. {item['options'][i]}")

    correct = item["answer"]
    print(f"   Correct answer: {item['options'][correct]}")
```

**Expected output:**

```
There are 2 questions.

[Physics] What is the SI unit of force?
   0. Joule
   1. Newton
   2. Watt
   3. Pascal
   Correct answer: Newton

[Chemistry] What is the chemical symbol for sodium?
   0. So
   1. Sd
   2. Na
   3. S
   Correct answer: Na
```

Study that structure — you will build on it directly in Class 14:

- `questions` is a **list**, so you can loop through it, count it, and shuffle it
- each item is a **dictionary**, so every field has a name rather than a position
- `"options"` is a **list inside a dictionary inside a list**
- `"answer"` holds the **index** into `options`, so `item["options"][item["answer"]]` is the correct text

> **Careful**: Inside an f-string, use **single** quotes for the key when the f-string itself uses double quotes — `f"{item['category']}"`. Using double quotes on both would end the string early.

---

## 11.6 Putting It All Together

Create `student_database.py`:

```python
# student_database.py
# A small student database built from dictionaries.

print("=" * 54)
print(f"{'STUDENT DATABASE':^54}")
print("=" * 54)

database = {
    "Sita": {"Physics": 82, "Chemistry": 88, "Biology": 74, "Maths": 91},
    "Bibek": {"Physics": 35, "Chemistry": 42, "Biology": 51, "Maths": 38},
    "Aarya": {"Physics": 91, "Chemistry": 79, "Biology": 85, "Maths": 88},
    "Nisha": {"Physics": 67, "Chemistry": 71, "Biology": 63, "Maths": 58},
}

PASS_MARK = 40

# --- Per-student report ---
summary = {}

for name, subjects in database.items():
    total = sum(subjects.values())
    average = total / len(subjects)

    failed = []
    for subject, score in subjects.items():
        if score < PASS_MARK:
            failed.append(subject)

    if average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "E"

    summary[name] = {
        "total": total,
        "average": average,
        "grade": grade,
        "failed": failed,
    }

# --- Print the table ---
print()
print("-" * 54)
print(f"{'Student':<10}{'Total':>7}{'Average':>10}{'Grade':>7}   Failed")
print("-" * 54)

for name, record in summary.items():
    failed_text = ", ".join(record["failed"])
    if not failed_text:
        failed_text = "-"

    print(f"{name:<10}{record['total']:>7}{record['average']:>10.2f}"
          f"{record['grade']:>7}   {failed_text}")

print("-" * 54)

# --- Class-wide statistics per subject ---
subject_totals = {}

for name, subjects in database.items():
    for subject, score in subjects.items():
        subject_totals[subject] = subject_totals.get(subject, 0) + score

print("\nClass average by subject:")
for subject, total in subject_totals.items():
    print(f"   {subject:<12}{total / len(database):>6.2f}")

# --- Best and worst ---
best_name = ""
best_average = 0

for name, record in summary.items():
    if record["average"] > best_average:
        best_average = record["average"]
        best_name = name

print(f"\nTop of the class: {best_name} ({best_average:.2f}%)")

# --- Look up one student ---
wanted = "Aarya"
if wanted in database:
    print(f"\nRecord for {wanted}:")
    for subject, score in database[wanted].items():
        status = "pass" if score >= PASS_MARK else "FAIL"
        print(f"   {subject:<12}{score:>4}  {status}")
else:
    print(f"\n{wanted} is not in the database.")
```

**Expected output:**

```
======================================================
                   STUDENT DATABASE                   
======================================================

------------------------------------------------------
Student     Total   Average  Grade   Failed
------------------------------------------------------
Sita          335     83.75      A   -
Bibek         166     41.50      E   Physics, Maths
Aarya         343     85.75      A   -
Nisha         259     64.75      C   -
------------------------------------------------------

Class average by subject:
   Physics      68.75
   Chemistry    70.00
   Biology      68.25
   Maths        68.75

Top of the class: Aarya (85.75%)

Record for Aarya:
   Physics       91  pass
   Chemistry     79  pass
   Biology       85  pass
   Maths         88  pass
```

Three things to take from this:

- **`summary` is built as a dictionary of dictionaries**, computed from `database`. Deriving a new structure from an old one, rather than modifying in place, keeps the original data trustworthy.
- **`subject_totals[subject] = subject_totals.get(subject, 0) + score`** is the counting pattern again, this time summing rather than counting. It builds the totals without knowing the subject names in advance.
- The long `print` is split across two lines. Two string pieces sitting next to each other inside brackets are joined automatically, which is how you keep a wide line readable.

You have also just met `status = "pass" if score >= PASS_MARK else "FAIL"` — a **conditional expression**. It is a compact `if`/`else` that produces a value. Use it only for short, obvious choices like this one.

> **Try it**: Add a fifth student to `database` with a different set of subjects — say only Physics and Maths. What breaks, and what still works? Where does the code assume every student takes the same four subjects?

---

## Practice Exercises

1. **Phone book** — Build a `while True` menu that lets the user add a name and number, look up a name, delete a name, list everything sorted by name, or quit. Store it all in one dictionary. Use `.get()` so a missing name gives a polite message instead of a `KeyError`.

2. **Word frequency counter** — Ask for a sentence, split it into words, lower-case them, and count each one using the `counts.get(word, 0) + 1` pattern. Print the results sorted so the most frequent word comes first. Hint: build a list of `(count, word)` tuples and sort it with `reverse=True`.

3. **Marks by subject** — Turn `records = [("Sita", "Physics", 82), ("Bibek", "Physics", 35), ("Sita", "Chemistry", 88)]` into a dictionary shaped `{"Sita": {"Physics": 82, "Chemistry": 88}, "Bibek": {"Physics": 35}}`. You will need to check whether the student's key exists before adding a subject to it.

4. **Your first question bank** — Write a list of five dictionaries in the Quiz Game's shape — `category`, `question`, `options`, `answer` — using questions from your own subjects. Then write a loop that prints each question with its options lettered A, B, C, D and shows the correct answer underneath. You will reuse this file in Class 14, so save it as `questions.py`.

---

## Key Takeaways

- A **dictionary** stores **key–value pairs**: `{"name": "Aarya", "class": 12}`. You look values up by key, not by position.
- Keys must be **unique** and immutable; values can be anything. Dictionaries keep insertion order.
- **`d[key]`** raises a `KeyError` if the key is missing; **`d.get(key, default)`** returns a fallback instead.
- **`in`** checks the **keys**. Use `in d.values()` to search values.
- Assigning to a key **adds or updates** — the syntax is the same either way.
- **`del d[key]`** deletes; **`d.pop(key)`** deletes and returns the value.
- Loop with **`.items()`** when you need key and value together — it unpacks into two variables.
- **`counts[x] = counts.get(x, 0) + 1`** is the counting pattern. Learn it; you will use it constantly.
- A **list of dictionaries** is the standard shape for records — and exactly how the Quiz Game stores its questions.
- Inside an f-string, quote dictionary keys with **single** quotes: `f"{item['category']}"`.

Next class we will write our own **functions**, so we can name a piece of work once and reuse it — and import ready-made tools from the `math` and `random` modules.
