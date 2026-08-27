# Class 5: Making Decisions — `if`, `elif` and `else`

> **Time budget**: 45 minutes (≈ 32 min teach + 13 min practice)
> **Prerequisites**: Class 4 (Operators and Expressions)

Everything you have written so far runs straight through, top to bottom, every single time. Today your programs learn to **choose**. This is the moment code stops being a calculator and starts being a program.

## What You Will Learn

- How **`if`** runs a block of code only when a condition is true
- Adding **`else`** for the other case, and **`elif`** for several cases
- Why **indentation** is not decoration in Python — it is the syntax
- **Nested** conditions, and when to avoid them
- **Truthiness** — the values Python treats as false

---

## 5.1 The `if` Statement

```python
marks = 87

if marks >= 40:
    print("You passed!")

print("Program finished.")
```

**Expected output:**

```
You passed!
Program finished.
```

Now change the first line to `marks = 32` and run it again:

**Expected output:**

```
Program finished.
```

The `print("You passed!")` line was **skipped entirely**. Python checked `32 >= 40`, got `False`, and jumped over the indented block.

### The anatomy of an `if`

```python
if marks >= 40:
    print("You passed!")
```

| Piece | What it does |
|-------|--------------|
| `if` | The keyword that starts the decision |
| `marks >= 40` | The **condition** — must produce `True` or `False` |
| `:` | A colon. **Required.** It means "the block starts here" |
| 4 spaces | **Indentation.** Marks which lines belong to the `if` |
| `print(...)` | The **body** — runs only when the condition is true |

> **Common error**: Forgetting the colon gives `SyntaxError: expected ':'`. Forgetting the indentation gives `IndentationError: expected an indented block after 'if' statement on line 3`. Both messages name exactly what is missing — read them and fix them.

### A block can be several lines

Every line at the same indentation belongs to the same block:

```python
marks = 87

if marks >= 40:
    print("You passed!")
    print("Well done.")
    print("Certificate will be issued.")

print("Program finished.")
```

**Expected output:**

```
You passed!
Well done.
Certificate will be issued.
Program finished.
```

Set `marks = 32` and the first three lines all disappear together, while `Program finished.` still runs — it is not indented, so it is not part of the block.

---

## 5.2 Indentation Is the Syntax

Most programming languages use `{ }` to mark a block and treat indentation as a matter of taste. **Python uses the indentation itself.** Get it wrong and the program either crashes or, worse, quietly does the wrong thing.

```python
marks = 32

if marks >= 40:
    print("You passed!")
print("Certificate issued.")
```

**Expected output:**

```
Certificate issued.
```

The certificate line is not indented, so it is not inside the `if` — it runs whatever the marks. A failing student just got a certificate. Python did not complain, because the code is perfectly legal. It is just wrong.

**The rules:**

1. Use **4 spaces** per level. This is the universal Python convention.
2. Be **consistent**. Never mix tabs and spaces in the same file.
3. Every line in a block must have the **same** indentation.

> **Tip**: In VS Code, press the Tab key and it inserts 4 spaces automatically for `.py` files. You do not need to press the space bar four times. If a file ever misbehaves mysteriously, use **View → Render Whitespace** to see exactly what is there.

Inconsistent indentation inside one block is an error:

```python
if marks >= 40:
    print("Passed")
      print("Well done")
```

**Expected output:**

```
IndentationError: unexpected indent
```

---

## 5.3 `else` — the Other Path

`if` handles one case. `else` handles everything else.

```python
marks = 32

if marks >= 40:
    print("Result: PASS")
else:
    print("Result: FAIL")
```

**Expected output:**

```
Result: FAIL
```

`else` takes no condition — it is "in every other case". Exactly one of the two blocks always runs; never both, never neither.

```python
number = int(input("Enter a number: "))

if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")
```

**Sample run:**

```
Enter a number: 24
24 is even.
```

There is the `% 2 == 0` test from Class 4, doing real work.

---

## 5.4 `elif` — Several Cases

Grades are not pass-or-fail. There are bands. This is what `elif` — short for "else if" — is for.

```python
marks = 87

if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 50:
    grade = "D"
else:
    grade = "Not passed"

print(f"Marks: {marks}  Grade: {grade}")
```

**Expected output:**

```
Marks: 87  Grade: A
```

### How Python works down the chain

This is the part to understand properly.

Python tests each condition **in order** and **stops at the first one that is true**. Everything below it is skipped.

For `marks = 87`:

1. `87 >= 90`? `False` — move on
2. `87 >= 80`? `True` — set grade to `"A"`, **skip the whole rest**
3. Never even looks at `>= 70`, `>= 60`, `>= 50` or `else`

That "stops at the first true one" behaviour is why the conditions can be so simple. The second test does not need to say `87 >= 80 and 87 < 90` — if we reached it at all, we already know the first test failed.

### Order matters enormously

Write the same chain in the wrong order:

```python
marks = 87

if marks >= 50:
    grade = "D"
elif marks >= 60:
    grade = "C"
elif marks >= 80:
    grade = "A"

print(f"Grade: {grade}")
```

**Expected output:**

```
Grade: D
```

A student who scored 87 gets a D. `87 >= 50` is true, so Python stops there and never looks further. No error, no warning — just a wrong result.

> **Careful**: With `elif` chains that test ranges, always go from the **most extreme end inwards** — highest to lowest, or lowest to highest. A chain in a jumbled order will run without complaint and produce nonsense.

### `if` versus a chain of `if`s

These two look similar and behave completely differently:

```python
marks = 95

if marks >= 90:
    print("A+")
if marks >= 80:
    print("A")
if marks >= 70:
    print("B")
```

**Expected output:**

```
A+
A
B
```

Three separate `if` statements, so all three are tested and all three run. With `elif`, only the first would.

Use `elif` when the cases are **alternatives** — one and only one should apply. Use separate `if`s when the checks are genuinely independent.

---

## 5.5 Nested Conditions

An `if` can live inside another `if`. Indent it one more level.

```python
marks = 85
attendance = 60

if marks >= 40:
    print("Marks are sufficient.")
    if attendance >= 75:
        print("Attendance is sufficient.")
        print("Result: PASS")
    else:
        print("Attendance is too low.")
        print("Result: DETAINED")
else:
    print("Result: FAIL")
```

**Expected output:**

```
Marks are sufficient.
Attendance is too low.
Result: DETAINED
```

The inner `if` is only ever reached when the outer condition was true. Follow the indentation to see which `else` pairs with which `if` — the one at the same level.

### Prefer `and` where you can

Nesting gets unreadable fast. Where the nested version has no separate message, `and` says it better:

```python
marks = 85
attendance = 80

# Harder to read
if marks >= 40:
    if attendance >= 75:
        print("PASS")

# Better
if marks >= 40 and attendance >= 75:
    print("PASS")
```

**Expected output:**

```
PASS
PASS
```

> **Tip**: If you find yourself three levels deep in nested `if`s, stop and ask whether `and` or an `elif` chain would flatten it. Deeply nested code is where bugs go to hide.

---

## 5.6 Truthiness

Python lets you put almost anything where a condition is expected. Values that are "empty" or "zero" count as `False`; everything else counts as `True`.

| Counts as `False` | Counts as `True` |
|-------------------|------------------|
| `False` | `True` |
| `0` and `0.0` | Any other number, including negatives |
| `""` (empty string) | Any string with characters in it |
| `[]` (empty list) | Any list with items in it |
| `None` | Practically everything else |

```python
name = input("Your name: ")

if name:
    print(f"Namaste, {name}!")
else:
    print("You did not type a name.")
```

**Sample run** (user just presses Enter):

```
Your name: 
You did not type a name.
```

`if name:` reads as "if there is a name". It is shorter than `if name != "":` and every Python programmer writes it this way. The Quiz Game uses exactly this check on the player's name.

Careful with numbers, though:

```python
marks = 0

if marks:
    print("This does not run — 0 is falsy.")
else:
    print("Zero counts as False!")
```

**Expected output:**

```
Zero counts as False!
```

A student who genuinely scored 0 would be treated as though they had no marks at all. When zero is a **valid value**, always compare explicitly — write `if marks >= 0:`, not `if marks:`.

---

## 5.7 Putting It All Together

Create `grade_calculator.py`:

```python
# grade_calculator.py
# Works out a student's result from four subject marks.

print("=" * 46)
print("TRITON COLLEGE — RESULT CALCULATOR")
print("=" * 46)

name = input("\nStudent name: ")

if not name:
    name = "Unnamed student"

physics = float(input("Physics marks (out of 100): "))
chemistry = float(input("Chemistry marks (out of 100): "))
biology = float(input("Biology marks (out of 100): "))
maths = float(input("Maths marks (out of 100): "))
attendance = float(input("Attendance percentage: "))

total = physics + chemistry + biology + maths
percentage = total / 4

# --- Has any single subject been failed? ---
failed_a_subject = physics < 40 or chemistry < 40 or biology < 40 or maths < 40

# --- Work out the grade ---
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "E"

print()
print("-" * 46)
print(f"Student:    {name}")
print(f"Total:      {total:.1f} out of 400")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade:      {grade}")
print(f"Attendance: {attendance:.1f}%")
print("-" * 46)

# --- The final decision ---
if failed_a_subject:
    print("RESULT: FAIL — at least one subject is below 40.")
elif attendance < 75:
    print("RESULT: DETAINED — attendance is below 75%.")
elif percentage >= 40:
    print("RESULT: PASS")
    if percentage >= 80:
        print("Awarded distinction. Excellent work!")
    elif percentage >= 60:
        print("Awarded first division.")
else:
    print("RESULT: FAIL — overall percentage is below 40.")

print("-" * 46)
```

**Sample run:**

```
==============================================
TRITON COLLEGE — RESULT CALCULATOR
==============================================

Student name: Aarya Gurung
Physics marks (out of 100): 82
Chemistry marks (out of 100): 76
Biology marks (out of 100): 91
Maths marks (out of 100): 88
Attendance percentage: 85

----------------------------------------------
Student:    Aarya Gurung
Total:      337.0 out of 400
Percentage: 84.25%
Grade:      A
Attendance: 85.0%
----------------------------------------------
RESULT: PASS
Awarded distinction. Excellent work!
----------------------------------------------
```

Notice the order of the final chain. Failing a subject is checked **first**, because it overrides everything else — a student with 95% overall who scored 30 in Chemistry has still failed. Getting that order right is the whole skill of writing an `elif` chain.

> **Try it**: Run it again with Chemistry set to 30 and everything else unchanged. The percentage stays high but the result flips to FAIL. Then set attendance to 60 and watch DETAINED take over.

---

## Practice Exercises

1. **Leap year checker** — Ask for a year and print whether it is a leap year. The rule: divisible by 4, **except** century years, which must be divisible by 400. So 2024 and 2000 are leap years; 1900 and 2023 are not. Use `%` and logical operators. Test all four of those years.

2. **Largest of three** — Ask for three different numbers and print the largest, using only `if` / `elif` / `else` and comparisons. Do **not** use Python's `max()`. Then test it with the largest value in each of the three positions — does it work every time?

3. **Fix the broken chain** — This program gives every student a D. Explain exactly why, then fix it by changing only the order of the lines:

   ```python
   marks = 92
   if marks >= 50:
       print("D")
   elif marks >= 70:
       print("B")
   elif marks >= 90:
       print("A+")
   ```

4. **Quadratic roots** — Ask for the coefficients `a`, `b` and `c`. Work out the discriminant `b**2 - 4*a*c`. If it is positive, print "Two real roots"; if zero, "One repeated root"; if negative, "No real roots". As a bonus, print the actual roots in the first case using `** 0.5` for the square root.

---

## Key Takeaways

- **`if condition:`** runs its indented block only when the condition is `True`.
- The **colon** and the **4-space indentation** are both required. Indentation is Python's syntax, not styling.
- **`else`** catches every other case and takes no condition.
- **`elif`** adds more cases. Python tests them **in order and stops at the first true one**, so the order of a range chain is critical.
- Separate `if`s are all tested; an `elif` chain runs at most one branch. Choose deliberately.
- Conditions can be **nested**, but `and` is usually clearer than a nested `if`.
- **Truthiness**: `0`, `""`, `[]`, `None` and `False` are falsy; everything else is truthy. `if name:` is idiomatic — but never use it where `0` is a valid value.
- Check the condition that **overrides everything else first**.

Next class we will stop repeating ourselves and learn **loops** — running the same block of code many times with `for` and `range()`.
