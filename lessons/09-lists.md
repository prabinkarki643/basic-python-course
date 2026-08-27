# Class 9: Lists — Storing Many Values at Once

> **Time budget**: 45 minutes (≈ 32 min teach + 13 min practice)
> **Prerequisites**: Class 8 (Strings in Depth)

In Class 6 we wrote a marks analyser that could not draw a bar chart, because each new mark overwrote the last. Today we fix that. A **list** holds many values under one name, and it is the single most used data structure in Python.

## What You Will Learn

- Creating **lists** and reaching items by index
- **Slicing** a list — the same rules as strings
- **Changing** lists: `append`, `insert`, `remove`, `pop`, `sort`, `reverse`
- The built-ins that make lists powerful: `len`, `sum`, `max`, `min`, `sorted`
- **Looping** through a list, and the difference between `sort()` and `sorted()`

---

## 9.1 Creating a List

A list is written with square brackets, items separated by commas.

```python
marks = [82, 76, 91, 88, 67]
subjects = ["Physics", "Chemistry", "Biology", "Maths"]
empty = []

print(marks)
print(subjects)
print(empty)
print(len(marks))
```

**Expected output:**

```
[82, 76, 91, 88, 67]
['Physics', 'Chemistry', 'Biology', 'Maths']
[]
5
```

> **Analogy**: A list is a row of numbered lockers. The name `marks` is the row; each locker has a number starting at 0; each holds one value. You can open any locker directly, swap what is inside, or add another locker on the end.

A list can hold mixed types, though in practice you usually keep them uniform:

```python
student = ["Aarya", 12, 84.25, True]
print(student)
```

**Expected output:**

```
['Aarya', 12, 84.25, True]
```

---

## 9.2 Reaching Items

Indexing works exactly as it did for strings. Counting starts at 0, and negatives count from the end.

```python
subjects = ["Physics", "Chemistry", "Biology", "Maths"]

print(subjects[0])
print(subjects[2])
print(subjects[-1])
print(subjects[-2])
```

**Expected output:**

```
Physics
Biology
Maths
Biology
```

Out of range is an error, same as before:

```python
subjects = ["Physics", "Chemistry", "Biology", "Maths"]
print(subjects[4])
```

**Expected output:**

```
IndexError: list index out of range
```

### Slicing

```python
marks = [82, 76, 91, 88, 67, 45]

print(marks[0:3])
print(marks[:3])
print(marks[3:])
print(marks[-2:])
print(marks[::-1])
```

**Expected output:**

```
[82, 76, 91]
[82, 76, 91]
[88, 67, 45]
[67, 45]
[45, 67, 88, 91, 76, 82]
```

Start included, stop excluded — the same rule as `range()` and strings. Slicing a list gives you a **new list**, not a single item: `marks[0:1]` is `[82]`, while `marks[0]` is `82`.

---

## 9.3 Lists Are Mutable

Here is the crucial difference from strings. You **can** change a list in place.

```python
marks = [82, 76, 91]
marks[1] = 100
print(marks)
```

**Expected output:**

```
[82, 100, 91]
```

With a string, `word[0] = "J"` raised a `TypeError`. With a list, it just works. Lists are **mutable**; strings are **immutable**.

This difference runs through everything else today: list methods usually change the list itself and return nothing, whereas string methods returned a new string and left the original alone.

---

## 9.4 Adding and Removing

### `.append()` — add one item to the end

```python
marks = [82, 76]

marks.append(91)
marks.append(88)

print(marks)
```

**Expected output:**

```
[82, 76, 91, 88]
```

`.append()` is how you build a list inside a loop — the list version of the accumulator pattern:

```python
squares = []

for number in range(1, 6):
    squares.append(number ** 2)

print(squares)
```

**Expected output:**

```
[1, 4, 9, 16, 25]
```

Start with an empty list before the loop, append inside it. You will write this constantly.

### `.insert()` — add at a position

```python
subjects = ["Physics", "Biology"]
subjects.insert(1, "Chemistry")
print(subjects)
```

**Expected output:**

```
['Physics', 'Chemistry', 'Biology']
```

The first argument is where to put it; everything from there onwards shifts along.

### `.remove()` — delete by value

```python
subjects = ["Physics", "Chemistry", "Biology", "Chemistry"]
subjects.remove("Chemistry")
print(subjects)
```

**Expected output:**

```
['Physics', 'Biology', 'Chemistry']
```

`.remove()` deletes only the **first** match. Asking for something that is not there raises `ValueError: list.remove(x): x not in list`, so check with `in` first if you are unsure.

### `.pop()` — delete by position, and hand it back

```python
marks = [82, 76, 91, 88]

last = marks.pop()
print(last)
print(marks)

first = marks.pop(0)
print(first)
print(marks)
```

**Expected output:**

```
88
[82, 76, 91]
82
[76, 91]
```

`.pop()` with no argument takes the last item. Unlike `.remove()`, it **returns** what it removed, so you can use the value.

### `.clear()` — empty it

```python
marks = [82, 76, 91]
marks.clear()
print(marks)
print(len(marks))
```

**Expected output:**

```
[]
0
```

---

## 9.5 Searching and Counting

```python
subjects = ["Physics", "Chemistry", "Biology", "Maths"]

print("Physics" in subjects)
print("History" in subjects)
print(subjects.index("Biology"))
print(subjects.count("Physics"))
```

**Expected output:**

```
True
False
2
1
```

`in` is the friendly way to check membership. `.index()` gives the position but **crashes** if the item is absent — so guard it:

```python
subjects = ["Physics", "Chemistry", "Biology"]
wanted = "Maths"

if wanted in subjects:
    print(f"{wanted} is at position {subjects.index(wanted)}")
else:
    print(f"{wanted} is not in the list.")
```

**Expected output:**

```
Maths is not in the list.
```

---

## 9.6 Built-in Functions for Lists

These four save you writing loops.

```python
marks = [82, 76, 91, 88, 67]

print(len(marks))
print(sum(marks))
print(max(marks))
print(min(marks))
print(sum(marks) / len(marks))
```

**Expected output:**

```
5
404
91
67
80.8
```

Compare that to Class 6, where finding the total and the maximum took a loop and two accumulators. `sum()` and `max()` do it in a word each.

`max()` and `min()` work on strings too, using dictionary order:

```python
subjects = ["Physics", "Chemistry", "Biology", "Maths"]
print(max(subjects))
print(min(subjects))
```

**Expected output:**

```
Physics
Biology
```

> **Careful**: `sum()` only works on numbers. `sum(["a", "b"])` raises a `TypeError`. To join strings, use `.join()` from Class 8.

---

## 9.7 Sorting

### `.sort()` — changes the list itself

```python
marks = [82, 76, 91, 88, 67]

marks.sort()
print(marks)

marks.sort(reverse=True)
print(marks)
```

**Expected output:**

```
[67, 76, 82, 88, 91]
[91, 88, 82, 76, 67]
```

`reverse=True` sorts from largest to smallest. The Quiz Game uses exactly this to put the best score at the top.

### `sorted()` — returns a new list, original untouched

```python
marks = [82, 76, 91]

ordered = sorted(marks)

print(ordered)
print(marks)
```

**Expected output:**

```
[76, 82, 91]
[82, 76, 91]
```

| | `.sort()` | `sorted()` |
|---|-----------|------------|
| Changes the original? | Yes | No |
| Returns | `None` | A new list |
| Works on | Lists only | Lists, sets, strings, anything you can loop over |

> **Common error**: Writing `marks = marks.sort()` sets `marks` to `None`, because `.sort()` returns nothing. Then everything afterwards fails with `TypeError: object of type 'NoneType' has no len()`. Either call `marks.sort()` on its own line, or use `marks = sorted(marks)`. Never both.

### `.reverse()`

```python
subjects = ["Physics", "Chemistry", "Biology"]
subjects.reverse()
print(subjects)
```

**Expected output:**

```
['Biology', 'Chemistry', 'Physics']
```

`.reverse()` flips the current order; it does **not** sort. `[3, 1, 2]` reversed is `[2, 1, 3]`.

---

## 9.8 Looping Through Lists

The straightforward way, when you only need the values:

```python
subjects = ["Physics", "Chemistry", "Biology"]

for subject in subjects:
    print(f"Studying {subject}")
```

**Expected output:**

```
Studying Physics
Studying Chemistry
Studying Biology
```

When you need the **position** as well, loop over `range(len(...))`:

```python
subjects = ["Physics", "Chemistry", "Biology"]

for i in range(len(subjects)):
    print(f"{i + 1}. {subjects[i]}")
```

**Expected output:**

```
1. Physics
2. Chemistry
3. Biology
```

This is why `range()` excludes its stop value: `range(len(subjects))` gives exactly 0, 1, 2 — every valid index and nothing more. The two conventions were designed to fit together.

### Two lists side by side

When two lists line up item for item, one index reaches both:

```python
subjects = ["Physics", "Chemistry", "Biology", "Maths"]
marks = [82, 76, 91, 88]

for i in range(len(subjects)):
    print(f"{subjects[i]:<12}{marks[i]:>4}")
```

**Expected output:**

```
Physics       82
Chemistry     76
Biology       91
Maths         88
```

> **Careful**: Never change a list's length while looping over it. Appending inside a `for` over the same list can loop forever; removing items makes the loop skip entries. Build a **new** list instead.

---

## 9.9 Putting It All Together

Here is the marks analyser from Class 6, finished properly — bar chart and all.

Create `marks_analyser_v2.py`:

```python
# marks_analyser_v2.py
# The Class 6 analyser, rebuilt with lists.

print("=" * 50)
print(f"{'CLASS MARKS ANALYSER':^50}")
print("=" * 50)

names = []
marks = []

student_count = int(input("\nHow many students? "))

for i in range(student_count):
    name = input(f"\nName of student {i + 1}: ").strip()
    score = float(input(f"Marks for {name}: "))

    names.append(name)
    marks.append(score)

# --- Statistics, using built-ins instead of loops ---
total = sum(marks)
average = total / len(marks)
highest = max(marks)
lowest = min(marks)

top_student = names[marks.index(highest)]
bottom_student = names[marks.index(lowest)]

# --- Build lists of passes and fails ---
passed = []
failed = []

for i in range(len(marks)):
    if marks[i] >= 40:
        passed.append(names[i])
    else:
        failed.append(names[i])

print()
print("-" * 50)
print(f"{'Students':<20}{len(marks)}")
print(f"{'Total':<20}{total:.1f}")
print(f"{'Average':<20}{average:.2f}")
print(f"{'Highest':<20}{highest:.1f}  ({top_student})")
print(f"{'Lowest':<20}{lowest:.1f}  ({bottom_student})")
print(f"{'Passed':<20}{len(passed)}")
print(f"{'Failed':<20}{len(failed)}")
print("-" * 50)

# --- The bar chart we could not draw in Class 6 ---
print("\nBar chart (one # per 5 marks):")
for i in range(len(names)):
    bar = "#" * int(marks[i] // 5)
    print(f"{names[i]:<12}{marks[i]:>6.1f}  {bar}")

# --- Ranking ---
print("\nRanking, highest first:")
ranked = sorted(marks, reverse=True)

for position in range(len(ranked)):
    score = ranked[position]
    student = names[marks.index(score)]
    print(f"{position + 1}. {student:<12}{score:>6.1f}")

print(f"\nPassed: {', '.join(passed)}")

if failed:
    print(f"Failed: {', '.join(failed)}")
else:
    print("Nobody failed. Excellent.")
```

**Sample run:**

```
==================================================
               CLASS MARKS ANALYSER               
==================================================

How many students? 4

Name of student 1: Sita
Marks for Sita: 82

Name of student 2: Bibek
Marks for Bibek: 35

Name of student 3: Aarya
Marks for Aarya: 91

Name of student 4: Nisha
Marks for Nisha: 67

--------------------------------------------------
Students            4
Total               275.0
Average             68.75
Highest             91.0  (Aarya)
Lowest              35.0  (Bibek)
Passed              3
Failed              1
--------------------------------------------------

Bar chart (one # per 5 marks):
Sita          82.0  ################
Bibek         35.0  #######
Aarya         91.0  ##################
Nisha         67.0  #############

Ranking, highest first:
1. Aarya         91.0
2. Sita          82.0
3. Nisha         67.0
4. Bibek         35.0

Passed: Sita, Aarya, Nisha
Failed: Bibek
```

Three techniques from today are doing the heavy lifting:

- **Two parallel lists.** `names[i]` and `marks[i]` always refer to the same student, because both lists were appended to together inside the same loop. Keeping them in step is your responsibility — nothing enforces it.
- **`marks.index(highest)`** finds *where* the top mark is, and that same position in `names` gives you *who* scored it. Looking up a position in one list to reach into another is a pattern you will use often.
- **`"#" * int(marks[i] // 5)`** builds each bar. Floor division says how many whole fives the mark contains, and multiplying a string repeats it — the `"=" * 30` trick from Class 1, finally earning its keep.

### One weakness worth knowing about

The ranking has a real flaw. Run it with three students who all scored 80:

```
Ranking, highest first:
1. A             80.0
2. A             80.0
3. A             80.0
```

Student A is named three times, and B and C never appear. The cause is `marks.index(score)`: it always returns the position of the **first** matching mark, so an identical score always points back to the same name. Exercise 4 asks you to fix this — and Class 11's dictionaries offer a much better way to tie a name to a mark than two lists that must be kept in step by hand.

---

## Practice Exercises

1. **Shopping list manager** — Start with an empty list. Using a `while True` menu, let the user add an item, remove an item, view the list numbered from 1, or quit. Guard the remove option with `in` so a missing item does not crash the program.

2. **Second largest** — Given `marks = [82, 76, 91, 88, 67]`, find the second largest value **without** using `sorted()` or `.sort()`. Then do it again *with* sorting and compare how much shorter it is. What happens to each version if the list contains `[91, 91, 76]`?

3. **Split the evens and odds** — Ask the user for ten numbers, storing them in a list as you go. Then build two new lists — one of evens, one of odds — and print each with `.join()`. You will need `str()` to convert the numbers before joining. Why can `.join()` not handle numbers directly?

4. **Finish the analyser** — Take `marks_analyser_v2.py` and fix the ranking so it still works when two students score exactly the same mark. Hint: `marks.index()` always finds the first match, so a duplicate score names the same student twice. Try it with three students all on 80.

---

## Key Takeaways

- A **list** holds many values in order: `[82, 76, 91]`. Indexing and slicing follow the same rules as strings.
- **Lists are mutable** — `marks[1] = 100` works, unlike with strings.
- **`.append()`** adds to the end and is how you build a list inside a loop. **`.insert(i, x)`** adds at a position.
- **`.remove(x)`** deletes by value (first match only); **`.pop(i)`** deletes by position **and returns** the item.
- **`in`** tests membership safely; **`.index()`** gives a position but crashes when absent.
- **`len()`, `sum()`, `max()`, `min()`** replace whole loops.
- **`.sort()`** changes the list and returns `None`; **`sorted()`** returns a new list. Never write `x = x.sort()`.
- Loop with `for item in list` for values, or `for i in range(len(list))` when you need positions — including to walk two parallel lists at once.
- **Never change a list's length while looping over it.**

Next class we will meet two more collections — **tuples**, which cannot be changed, and **sets**, which refuse to hold duplicates.
