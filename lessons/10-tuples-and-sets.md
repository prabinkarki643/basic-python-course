# Class 10: Tuples and Sets — Two More Collections

> **Time budget**: 45 minutes (≈ 32 min teach + 13 min practice)
> **Prerequisites**: Class 9 (Lists)

Lists are flexible, and sometimes that is exactly what you do not want. Today we meet two collections with deliberate restrictions: **tuples**, which cannot be changed, and **sets**, which refuse to hold duplicates. Each restriction buys you something useful.

## What You Will Learn

- Creating **tuples** and why immutability is a feature
- **Unpacking** a tuple, and returning several values at once
- Creating **sets** and using them to remove duplicates
- Set operations: **union**, **intersection** and **difference**
- Converting between list, tuple and set — and choosing the right one

---

## 10.1 Tuples

A tuple is written with round brackets instead of square ones.

```python
point = (3, 7)
subjects = ("Physics", "Chemistry", "Biology")

print(point)
print(subjects)
print(len(subjects))
```

**Expected output:**

```
(3, 7)
('Physics', 'Chemistry', 'Biology')
3
```

Indexing and slicing work exactly as with lists:

```python
subjects = ("Physics", "Chemistry", "Biology", "Maths")

print(subjects[0])
print(subjects[-1])
print(subjects[1:3])
print("Physics" in subjects)
```

**Expected output:**

```
Physics
Maths
('Chemistry', 'Biology')
True
```

Looping is identical too:

```python
subjects = ("Physics", "Chemistry", "Biology")

for subject in subjects:
    print(subject)
```

**Expected output:**

```
Physics
Chemistry
Biology
```

### The one big difference — tuples are immutable

```python
subjects = ("Physics", "Chemistry")
subjects[0] = "Maths"
```

**Expected output:**

```
TypeError: 'tuple' object does not support item assignment
```

There is no `.append()`, no `.remove()`, no `.sort()`. Once a tuple is made, it is fixed — like a string, and unlike a list.

### Why would you *want* that?

Because some things genuinely should not change, and a tuple says so in the code itself.

| Use a tuple for | Because |
|-----------------|---------|
| Coordinates `(x, y)` | A point has exactly two parts, always |
| RGB colours `(255, 0, 0)` | Always three components |
| A database record `("Sita", 12, 84.25)` | The shape is fixed |
| Values returned together from a function | You do not want the caller editing them |
| Days of the week | The list will never grow |

Choosing a tuple documents your intention and protects you from an accidental `.append()` somewhere far away in the program.

> **Careful**: A one-item tuple needs a trailing comma. `(5)` is just the number 5 in brackets; `(5,)` is a tuple containing 5. Check with `type()` if you are unsure — this catches people out regularly.

```python
not_a_tuple = (5)
actually_a_tuple = (5,)

print(type(not_a_tuple))
print(type(actually_a_tuple))
```

**Expected output:**

```
<class 'int'>
<class 'tuple'>
```

The brackets are optional, incidentally. This is a tuple too:

```python
point = 3, 7
print(point)
print(type(point))
```

**Expected output:**

```
(3, 7)
<class 'tuple'>
```

It is the **commas** that make a tuple, not the brackets. Write the brackets anyway — they make your intention obvious.

---

## 10.2 Unpacking

Unpacking pulls a tuple's items into separate variables in one line.

```python
point = (3, 7)
x, y = point

print(f"x is {x}, y is {y}")
```

**Expected output:**

```
x is 3, y is 7
```

The number of names must match the number of items exactly, or you get `ValueError: too many values to unpack`.

You have already used this without knowing:

```python
physics, chemistry, biology = 82, 76, 91
print(physics, chemistry, biology)
```

**Expected output:**

```
82 76 91
```

The right-hand side is a tuple, and the left-hand side unpacks it. The one-line swap from Class 2 is the same trick:

```python
a = "Physics"
b = "Chemistry"
a, b = b, a
print(a, b)
```

**Expected output:**

```
Chemistry Physics
```

Python builds the tuple `("Chemistry", "Physics")` first, then unpacks it — which is why nothing is lost.

### Returning several values

This matters enormously from Class 12 onwards. A function can only return one thing — but that one thing can be a tuple:

```python
total_seconds = 3725

hours = total_seconds // 3600
remaining = total_seconds % 3600
result = (hours, remaining // 60, remaining % 60)

h, m, s = result
print(f"{h} h {m} min {s} s")
```

**Expected output:**

```
1 h 2 min 5 s
```

The Quiz Game's `play_round` returns `(score, total)` and the caller unpacks it with `score, total = play_round(...)`.

### Unpacking while looping

A list of tuples is an extremely common shape, and the loop can unpack each one:

```python
results = [("Sita", 82), ("Bibek", 35), ("Aarya", 91)]

for name, marks in results:
    print(f"{name:<10}{marks:>4}")
```

**Expected output:**

```
Sita        82
Bibek       35
Aarya       91
```

This solves the "two parallel lists" awkwardness from Class 9 — the name and the mark are now bound together and cannot drift apart.

---

## 10.3 Sets

A set is written with curly brackets. It has two defining properties: **no duplicates** and **no order**.

```python
subjects = {"Physics", "Chemistry", "Biology"}
print(subjects)
print(len(subjects))
```

**Expected output:**

```
{'Physics', 'Chemistry', 'Biology'}
3
```

The order you see may well differ from the order you typed, and can even differ between runs of the same program. That is not a fault — **a set has no order at all**, so Python is free to show the items however it likes. It follows that a set has no positions either, so `subjects[0]` is an error:

```python
subjects = {"Physics", "Chemistry"}
print(subjects[0])
```

**Expected output:**

```
TypeError: 'set' object is not subscriptable
```

### Duplicates simply vanish

```python
marks = {82, 76, 91, 82, 76, 82}
print(marks)
print(len(marks))
```

**Expected output:**

```
{82, 91, 76}
3
```

Three copies of 82 went in; one came out. No error, no warning — a set just cannot contain the same value twice.

### Removing duplicates from a list

This is the everyday use of sets, and it is worth memorising:

```python
marks = [82, 76, 91, 82, 88, 76, 82]

unique = list(set(marks))
unique.sort()

print(f"Original: {marks}  ({len(marks)} values)")
print(f"Unique:   {unique}  ({len(unique)} values)")
```

**Expected output:**

```
Original: [82, 76, 91, 82, 88, 76, 82]  (7 values)
Unique:   [76, 82, 88, 91]  (4 values)
```

`set(marks)` drops the duplicates, `list(...)` turns it back into a list, and `.sort()` puts it in order — because the set threw the order away.

> **Careful**: An empty set is written `set()`, **not** `{}`. Curly brackets with nothing in them make an empty **dictionary**, which is next class's subject. This is a genuine trap.

```python
empty_set = set()
empty_dict = {}

print(type(empty_set))
print(type(empty_dict))
```

**Expected output:**

```
<class 'set'>
<class 'dict'>
```

### Adding and removing

```python
subjects = {"Physics", "Chemistry"}

subjects.add("Biology")
subjects.add("Physics")

print(len(subjects))

subjects.discard("Chemistry")
subjects.discard("History")

print(sorted(subjects))
```

**Expected output:**

```
3
['Biology', 'Physics']
```

Adding `"Physics"` a second time did nothing. `.discard()` removes an item and is safe when the item is absent; `.remove()` does the same but raises a `KeyError` if it is missing.

Note `sorted(subjects)` — since sets have no order, sorting is how you print them predictably. The Quiz Game uses exactly this to build its category menu.

### Membership is the other reason to use a set

Checking `in` on a set is dramatically faster than on a list, because a set does not have to look through its items one by one. With a handful of values you will not notice; with fifty thousand, you very much will.

```python
valid_grades = {"A+", "A", "B", "C", "D"}

print("A" in valid_grades)
print("F" in valid_grades)
```

**Expected output:**

```
True
False
```

---

## 10.4 Set Operations

These are the Venn diagrams from your Maths syllabus, as working code.

```python
science = {"Sita", "Bibek", "Aarya", "Nisha"}
maths = {"Aarya", "Nisha", "Rohan"}

print(sorted(science | maths))
print(sorted(science & maths))
print(sorted(science - maths))
print(sorted(science ^ maths))
```

**Expected output:**

```
['Aarya', 'Bibek', 'Nisha', 'Rohan', 'Sita']
['Aarya', 'Nisha']
['Bibek', 'Sita']
['Bibek', 'Rohan', 'Sita']
```

| Operator | Method | Name | Gives you |
|----------|--------|------|-----------|
| `\|` | `.union()` | Union | Everyone in either set |
| `&` | `.intersection()` | Intersection | Only those in **both** |
| `-` | `.difference()` | Difference | In the first but **not** the second |
| `^` | `.symmetric_difference()` | Symmetric difference | In one or the other, but **not both** |

Read them as questions:

- Union — "who takes at least one of these subjects?"
- Intersection — "who takes **both**?"
- Difference — "who takes Science but **not** Maths?"
- Symmetric difference — "who takes exactly one of the two?"

The method forms read more clearly when you are new to this:

```python
science = {"Sita", "Bibek", "Aarya"}
maths = {"Aarya", "Rohan"}

print(sorted(science.intersection(maths)))
print(sorted(science.difference(maths)))
```

**Expected output:**

```
['Aarya']
['Bibek', 'Sita']
```

---

## 10.5 Choosing the Right Collection

| | List | Tuple | Set |
|---|------|-------|-----|
| Written with | `[ ]` | `( )` | `{ }` |
| Can be changed? | Yes | **No** | Yes |
| Keeps its order? | Yes | Yes | **No** |
| Allows duplicates? | Yes | Yes | **No** |
| Indexing `x[0]`? | Yes | Yes | **No** |
| Typical use | A collection that grows | A fixed record | Unique values, fast lookup |

Ask yourself in this order:

1. **Do I need to stop it changing?** → tuple
2. **Do I need duplicates gone, or fast `in` checks?** → set
3. **Otherwise** → list

Converting between them is easy:

```python
marks_list = [82, 76, 91, 82]

print(tuple(marks_list))
print(set(marks_list))
print(list(set(marks_list)))
print(list("Python"))
```

**Expected output:**

```
(82, 76, 91, 82)
{82, 91, 76}
[76, 82, 91]
['P', 'y', 't', 'h', 'o', 'n']
```

---

## 10.6 Putting It All Together

Create `subject_analyser.py`:

```python
# subject_analyser.py
# Compares the subject choices of two groups of students.

print("=" * 52)
print(f"{'SUBJECT CHOICE ANALYSER':^52}")
print("=" * 52)

# --- Fixed data that must never change: use tuples ---
STREAMS = ("Science", "Management", "Humanities")
GRADE_BANDS = (("A+", 90), ("A", 80), ("B", 70), ("C", 60), ("D", 50))

# --- Student records as a list of tuples ---
records = [
    ("Sita", "Physics", 82),
    ("Bibek", "Chemistry", 35),
    ("Aarya", "Physics", 91),
    ("Nisha", "Biology", 67),
    ("Rohan", "Physics", 74),
    ("Sita", "Chemistry", 88),
    ("Aarya", "Maths", 79),
]

print(f"\nStreams offered: {', '.join(STREAMS)}")
print(f"Records held:    {len(records)}")

# --- Unpack each record while looping ---
print()
print("-" * 52)
print(f"{'Student':<12}{'Subject':<14}{'Marks':>6}  Grade")
print("-" * 52)

for name, subject, marks in records:
    grade = "E"
    for band_name, minimum in GRADE_BANDS:
        if marks >= minimum:
            grade = band_name
            break

    print(f"{name:<12}{subject:<14}{marks:>6}  {grade}")

print("-" * 52)

# --- Use sets to answer questions about uniqueness ---
students = set()
subjects_taught = set()
passing_students = set()

for name, subject, marks in records:
    students.add(name)
    subjects_taught.add(subject)
    if marks >= 40:
        passing_students.add(name)

failing_students = students - passing_students
physics_students = set()
chemistry_students = set()

for name, subject, marks in records:
    if subject == "Physics":
        physics_students.add(name)
    elif subject == "Chemistry":
        chemistry_students.add(name)

print()
print(f"Unique students:        {len(students)}")
print(f"Unique subjects:        {len(subjects_taught)}")
print(f"Names:                  {', '.join(sorted(students))}")
print(f"Subjects:               {', '.join(sorted(subjects_taught))}")

print()
print(f"Takes Physics:          {', '.join(sorted(physics_students))}")
print(f"Takes Chemistry:        {', '.join(sorted(chemistry_students))}")
print(f"Takes both:             {', '.join(sorted(physics_students & chemistry_students))}")
print(f"Physics but not Chem:   {', '.join(sorted(physics_students - chemistry_students))}")
print(f"Exactly one of the two: {', '.join(sorted(physics_students ^ chemistry_students))}")

print()
if failing_students:
    print(f"Failed at least one:    {', '.join(sorted(failing_students))}")
else:
    print("Every student passed everything.")
```

**Expected output:**

```
====================================================
              SUBJECT CHOICE ANALYSER               
====================================================

Streams offered: Science, Management, Humanities
Records held:    7

----------------------------------------------------
Student     Subject        Marks  Grade
----------------------------------------------------
Sita        Physics           82  A
Bibek       Chemistry         35  E
Aarya       Physics           91  A+
Nisha       Biology           67  C
Rohan       Physics           74  B
Sita        Chemistry         88  A
Aarya       Maths             79  B
----------------------------------------------------

Unique students:        5
Unique subjects:        4
Names:                  Aarya, Bibek, Nisha, Rohan, Sita
Subjects:               Biology, Chemistry, Maths, Physics

Takes Physics:          Aarya, Rohan, Sita
Takes Chemistry:        Bibek, Sita
Takes both:             Sita
Physics but not Chem:   Aarya, Rohan
Exactly one of the two: Aarya, Bibek, Rohan

Failed at least one:    Bibek
```

Three ideas working together:

- **Tuples for fixed data.** `STREAMS` and `GRADE_BANDS` cannot be modified by accident. `GRADE_BANDS` is a tuple of tuples, unpacked in the inner loop as `band_name, minimum` — a neat way to replace a long `elif` chain with data you can loop over.
- **A list of tuples for records.** `for name, subject, marks in records:` unpacks each record automatically. Compare this with the two-parallel-lists approach in Class 9 — nothing can fall out of step.
- **Sets for uniqueness.** Sita appears twice in the records but once in `students`, because a set cannot hold her twice. `failing_students = students - passing_students` answers "who never passed anything?" in a single line that reads like the question.

> **Try it**: Add `("Rohan", "Chemistry", 45)` to `records` and run it again. Watch `Takes both` grow to include Rohan and `Exactly one of the two` shrink. Nothing else needs changing — that is the value of computing these from sets rather than writing them out.

---

## Practice Exercises

1. **Common and unique letters** — Ask for two words. Convert each to a set of characters and report: letters in both, letters only in the first, and all the distinct letters across the two. Test with `PHYSICS` and `CHEMISTRY`. Why does turning a string into a set lose the repeated letters?

2. **Deduplicate a roll call** — Given `attendance = ["Sita", "Bibek", "Sita", "Aarya", "Bibek", "Sita"]`, print how many attendance marks were recorded, how many distinct students there are, a sorted list of names, and which name appears most often. You will need `set()`, `len()` and `.count()`.

3. **Tuple or list?** — For each of these, decide whether a tuple or a list is the better choice and write one sentence saying why: (a) the twelve months of the year, (b) a shopping basket, (c) a screen resolution such as `1920 × 1080`, (d) the marks of everyone in your class, (e) the three primary colours.

4. **Fix the marks ranking** — Return to `marks_analyser_v2.py` from Class 9, where duplicate marks named the same student repeatedly. Rebuild it with a **list of tuples** — `[("Sita", 82), ("Bibek", 35), ...]` — and sort it. Hint: `records.sort(reverse=True)` on a list of `(marks, name)` tuples sorts by marks first. Why does putting the marks **first** in each tuple matter?

---

## Key Takeaways

- A **tuple** `(1, 2, 3)` is an ordered collection that **cannot be changed**. Use it for fixed data and to signal "this must not be modified".
- It is the **commas** that make a tuple. A single-item tuple needs the trailing comma: `(5,)`.
- **Unpacking** — `x, y = point` — splits a tuple into variables. It powers the one-line swap, multiple return values, and `for name, marks in records:`.
- A **list of tuples** keeps related values bound together, which is safer than two parallel lists.
- A **set** `{1, 2, 3}` holds **no duplicates** and has **no order**, so there is no indexing.
- `list(set(items))` removes duplicates; sort afterwards to restore a predictable order.
- An empty set is **`set()`** — `{}` gives you an empty dictionary.
- Set operations: `|` union, `&` intersection, `-` difference, `^` symmetric difference. They are the Venn diagrams from Maths.
- Choose: **tuple** if it must not change, **set** if duplicates must go or lookups must be fast, **list** otherwise.

Next class we will meet **dictionaries** — collections that store values against names rather than numbers, and the structure the Quiz Game is built on.
