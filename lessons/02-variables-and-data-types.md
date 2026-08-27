# Class 2: Variables and Data Types — Storing Information

> **Time budget**: 45 minutes (≈ 32 min teach + 13 min practice)
> **Prerequisites**: Class 1 (Introduction and Setup)

Last class every program printed fixed text. Change the output and you had to change the code. Today we learn to store information in **variables**, so a program can work on data that changes — which is what makes programs useful.

## What You Will Learn

- What a **variable** is and how to create one
- The four core **data types**: `int`, `float`, `str` and `bool`
- How to check a value's type with **`type()`**
- The rules for **naming** variables, and the conventions professionals follow
- How to **reassign** a variable and assign several at once

---

## 2.1 What Is a Variable?

A **variable** is a name that holds a value.

```python
marks = 87
print(marks)
```

**Expected output:**

```
87
```

The line `marks = 87` does three things at once: it creates a box in the computer's memory, puts the number 87 into it, and sticks the label `marks` on the front. From then on, writing `marks` anywhere in your program means "whatever is in that box".

> **Analogy**: A variable is a labelled box on a shelf. The label is the name, the contents are the value. You can look inside whenever you like, and you can swap the contents for something else without changing the label.

### The `=` sign does not mean "equals"

This is the first thing that trips up students who are good at Maths.

In Maths, `x = 5` is a **statement of fact**: x and 5 are the same thing.

In Python, `=` is the **assignment operator**. It means "put the value on the right into the box named on the left". It is an instruction, not a fact. Which is why this is perfectly legal:

```python
count = 10
count = count + 1
print(count)
```

**Expected output:**

```
11
```

In Maths, `count = count + 1` is nonsense — no number equals itself plus one. In Python it reads as "take what is in `count`, add 1, and put the result back into `count`". Python always works out the **right-hand side first**, then stores it.

### Using variables

Once a value has a name, you can use it anywhere:

```python
name = "Aarya"
physics = 82
chemistry = 76

print("Student:", name)
print("Physics:", physics)
print("Chemistry:", chemistry)
print("Total:", physics + chemistry)
```

**Expected output:**

```
Student: Aarya
Physics: 82
Chemistry: 76
Total: 158
```

Notice the last line. Python worked out `82 + 76` before printing. Variables are not just storage — they are the things your calculations operate on.

---

## 2.2 The Four Core Data Types

Every value in Python has a **type**. The type decides what you are allowed to do with the value. You cannot divide a name by two, and Python will stop you from trying.

There are four types you need today.

| Type | Full name | What it holds | Examples |
|------|-----------|---------------|----------|
| `int` | integer | Whole numbers, positive or negative | `12`, `0`, `-45`, `1000000` |
| `float` | floating-point | Numbers with a decimal point | `9.8`, `3.14`, `-0.5`, `98.0` |
| `str` | string | Text | `"Sita"`, `"Physics"`, `"12"`, `""` |
| `bool` | boolean | One of exactly two values | `True`, `False` |

### `int` — whole numbers

```python
students = 42
year = 2026
temperature = -5

print(students, year, temperature)
```

**Expected output:**

```
42 2026 -5
```

No quotes, no decimal point. Python integers have no upper limit — they grow as large as your computer's memory allows, which is unusual and rather nice.

### `float` — decimal numbers

```python
gravity = 9.8
pi = 3.14159
percentage = 76.5

print(gravity, pi, percentage)
```

**Expected output:**

```
9.8 3.14159 76.5
```

The name "floating-point" refers to how the computer stores the decimal point internally. You do not need the detail; you need to know that a number with a `.` in it is a `float`.

> **Careful**: `98` and `98.0` are **not the same type**. The first is an `int`, the second a `float`. They compare as equal, but `type()` tells them apart, and occasionally that matters.

### `str` — text

```python
name = "Bibek Thapa"
subject = 'Chemistry'
empty = ""

print(name)
print(subject)
print("Empty string between arrows:", empty, "<- nothing there")
```

**Expected output:**

```
Bibek Thapa
Chemistry
Empty string between arrows:  <- nothing there
```

Anything inside quotes is a string, **including digits**:

```python
roll_number = "042"
print(roll_number)
```

**Expected output:**

```
042
```

`"042"` is text, so the leading zero is preserved. Written as the number `42` the zero would vanish, because numerically it means nothing. This is exactly why roll numbers, phone numbers and postcodes are stored as strings, not numbers.

### `bool` — true or false

```python
passed = True
absent = False

print(passed)
print(absent)
```

**Expected output:**

```
True
False
```

`True` and `False` must have a **capital first letter**. `true` is not a Python word and gives you a `NameError`.

Booleans usually come out of comparisons rather than being typed by hand:

```python
marks = 87
print(marks > 40)
print(marks > 90)
```

**Expected output:**

```
True
False
```

Booleans are the foundation of decision-making, which we reach in Class 5.

---

## 2.3 Checking the Type with `type()`

When you are unsure what you are holding, ask Python:

```python
print(type(42))
print(type(9.8))
print(type("Sita"))
print(type(True))
```

**Expected output:**

```
<class 'int'>
<class 'float'>
<class 'str'>
<class 'bool'>
```

Ignore the word `class` for now — it is Python's internal vocabulary. The part that matters is `int`, `float`, `str`, `bool`.

It works on variables too:

```python
marks = 87
average = 76.5
name = "Aarya"

print(type(marks))
print(type(average))
print(type(name))
```

**Expected output:**

```
<class 'int'>
<class 'float'>
<class 'str'>
```

### Why the type matters

Watch what `+` does to two different types:

```python
print(10 + 5)
print("10" + "5")
```

**Expected output:**

```
15
105
```

With numbers, `+` **adds**. With strings, `+` **joins** — a process called concatenation. Same symbol, completely different job, decided entirely by the type.

And mixing them fails:

```python
print("10" + 5)
```

**Expected output:**

```
TypeError: can only concatenate str (not "int") to str
```

Python refuses to guess whether you meant `15` or `"105"`. This is a **feature**: a language that guessed would silently produce wrong marks sheets. Class 3 shows you how to convert between types deliberately.

> **Tip**: `TypeError` almost always means you mixed text and numbers. When you see one, use `type()` on the values involved to find out which is which.

---

## 2.4 Naming Variables

### The rules — Python enforces these

1. Names may contain **letters, digits and underscores** only
2. A name may **not start with a digit**
3. Names are **case-sensitive**: `marks`, `Marks` and `MARKS` are three different variables
4. Names may not be one of Python's **reserved words**

```python
student_name = "Sita"      # ✅ fine
marks2 = 90                # ✅ digits allowed, just not first
_total = 100               # ✅ underscore first is allowed
```

```python
2marks = 90                # ❌ SyntaxError — starts with a digit
student-name = "Sita"      # ❌ SyntaxError — the hyphen means "minus"
class = 12                 # ❌ SyntaxError — "class" is reserved
```

The reserved words are the ones Python has already given a meaning: `if`, `else`, `for`, `while`, `True`, `False`, `None`, `class`, `def`, `import`, `return`, `and`, `or`, `not`, and about twenty more. You will meet them all in due course. If VS Code colours a word differently as you type it, it is reserved — pick another name.

> **Common error**: `class = 12` is the single most likely naming mistake on this course, because you are all in Class 12. Use `class_name`, `grade` or `student_class` instead.

### The conventions — good programmers follow these

Rules stop your program crashing. Conventions stop your program being unreadable.

| Convention | Example | Why |
|------------|---------|-----|
| Use **snake_case** — lower case, underscores between words | `student_name`, `total_marks` | Standard across the whole Python world |
| Choose **descriptive** names | `average_marks`, not `am` or `x` | You will read this code again in six months |
| Do not shorten aggressively | `temperature`, not `tmp` | Saving four keystrokes costs an hour later |
| Use **CAPITALS** for values that never change | `PI = 3.14159` | Signals "do not modify this" |

Compare these two programs. They do exactly the same thing:

```python
a = 82
b = 76
c = (a + b) / 2
print(c)
```

```python
physics_marks = 82
chemistry_marks = 76
average_marks = (physics_marks + chemistry_marks) / 2
print(average_marks)
```

**Expected output** (both):

```
79.0
```

The second one needs no explanation. That is the entire point.

---

## 2.5 Reassigning and Multiple Assignment

### Reassigning

A variable holds one value at a time. Assign a new one and the old value is gone.

```python
marks = 45
print("Before:", marks)

marks = 92
print("After:", marks)
```

**Expected output:**

```
Before: 45
After: 92
```

A variable can even change **type**, which most languages forbid:

```python
value = 42
print(value, type(value))

value = "forty-two"
print(value, type(value))
```

**Expected output:**

```
42 <class 'int'>
forty-two <class 'str'>
```

This flexibility is called **dynamic typing**. It is convenient, but it means Python cannot warn you when you accidentally overwrite a number with text — so keep your names meaningful.

### Assigning several at once

```python
physics, chemistry, biology = 82, 76, 91
print(physics, chemistry, biology)
```

**Expected output:**

```
82 76 91
```

The values are matched to the names left to right. The counts must match exactly — three names need three values.

Giving several variables the same value:

```python
maths = physics = chemistry = 0
print(maths, physics, chemistry)
```

**Expected output:**

```
0 0 0
```

This is a tidy way to set several counters to zero at the start of a program.

### Swapping two values

Most languages need a third variable to swap two values. Python does not:

```python
first = "Physics"
second = "Chemistry"

first, second = second, first

print(first, second)
```

**Expected output:**

```
Chemistry Physics
```

Python evaluates the whole right-hand side before assigning anything, so both original values are safely captured before either box is overwritten.

---

## 2.6 Putting It All Together

Create `student_record.py`:

```python
# student_record.py
# Stores and displays one student's record.

# --- Student details ---
student_name = "Aarya Gurung"
roll_number = "042"
student_class = 12
stream = "Science"

# --- Marks out of 100 ---
physics = 82
chemistry = 76
biology = 91
maths = 88

# --- Calculations ---
total_marks = physics + chemistry + biology + maths
average_marks = total_marks / 4
has_passed = average_marks >= 40

# --- Output ---
print("=" * 34)
print("STUDENT RECORD")
print("=" * 34)

print("Name:      ", student_name)
print("Roll no:   ", roll_number)
print("Class:     ", student_class, stream)

print()
print("Physics:   ", physics)
print("Chemistry: ", chemistry)
print("Biology:   ", biology)
print("Maths:     ", maths)

print()
print("Total:     ", total_marks, "out of 400")
print("Average:   ", average_marks)
print("Passed:    ", has_passed)
print("=" * 34)

print()
print("Type of total_marks:  ", type(total_marks))
print("Type of average_marks:", type(average_marks))
print("Type of has_passed:   ", type(has_passed))
```

**Expected output:**

```
==================================
STUDENT RECORD
==================================
Name:       Aarya Gurung
Roll no:    042
Class:      12 Science

Physics:    82
Chemistry:  76
Biology:    91
Maths:      88

Total:      337 out of 400
Average:    84.25
Passed:     True
==================================

Type of total_marks:   <class 'int'>
Type of average_marks: <class 'float'>
Type of has_passed:    <class 'bool'>
```

Three things worth noticing:

- `total_marks` is an `int` because adding whole numbers gives a whole number.
- `average_marks` is a `float` even though we divided by 4. In Python, `/` **always** produces a `float`, even when the division comes out exact. `8 / 4` gives `2.0`, not `2`.
- `has_passed` is a `bool` because `>=` is a comparison, and comparisons produce `True` or `False`.

---

## Practice Exercises

1. **Your own record** — Rewrite `student_record.py` with your details and your real marks in four subjects. Add a fifth subject and update the total, the average and the "out of" figure. Check the average changes as you expect.

2. **Type detective** — Predict the type of each of these *before* running anything, then check with `type()`:

   ```python
   a = 100
   b = 100.0
   c = "100"
   d = 100 > 50
   e = 100 + 0.0
   ```

   Which two surprised you, and why? Pay particular attention to `e`.

3. **The concatenation trap** — Write a program with `subject = "Physics"` and `marks = 82`, then try `print(subject + marks)`. Record the exact error. Now make it work using a comma instead of `+`. Why does the comma succeed where `+` fails?

4. **Circle calculations** — Create variables `PI = 3.14159` and `radius = 7`. Work out and print the circumference (`2 × π × r`) and the area (`π × r²`, which you can write as `PI * radius * radius`). Why is `PI` written in capitals when the other variables are not?

---

## Key Takeaways

- A **variable** is a named box holding a value. `=` means "put this in that", not "these are equal".
- Python's four core types: **`int`** (whole numbers), **`float`** (decimals), **`str`** (text in quotes), **`bool`** (`True`/`False`).
- **`type(value)`** tells you what you are holding — use it whenever you are unsure.
- The type decides what operations mean: `+` **adds** numbers but **joins** strings, and mixing the two raises a `TypeError`.
- Names use **snake_case**, must not start with a digit, and must avoid reserved words. `class` is reserved — do not use it.
- Descriptive names are not decoration; they are how code stays readable.
- A variable can be **reassigned** at any time, even to a different type. Python evaluates the right-hand side first, which is why swapping works in one line.
- **`/` always gives a `float`**, even when the division is exact.

Next class we will make programs interactive — asking the user for input, converting it to the right type, and printing formatted results with f-strings.
