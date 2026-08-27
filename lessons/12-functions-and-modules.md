# Class 12: Functions and Modules — Naming Your Own Instructions

> **Time budget**: 45 minutes (≈ 32 min teach + 13 min practice)
> **Prerequisites**: Class 11 (Dictionaries)

You have used `print()`, `len()`, `input()` and `sorted()` — functions somebody else wrote. Today you write your own. A function lets you name a piece of work once and then use it as often as you like, which is how programs stay manageable as they grow.

## What You Will Learn

- Defining a function with **`def`** and calling it
- **Parameters** and **arguments** — passing information in
- **`return`** — getting a result back out
- **Default** and **keyword** arguments
- Local vs global **scope**
- Importing from the **`math`** and **`random`** modules

---

## 12.1 Why Functions?

Look at this repetition:

```python
print("=" * 30)
print("PHYSICS")
print("=" * 30)

print("=" * 30)
print("CHEMISTRY")
print("=" * 30)

print("=" * 30)
print("BIOLOGY")
print("=" * 30)
```

Nine lines to print three headings, and changing the style means editing nine places. With a function:

```python
def print_heading(title):
    print("=" * 30)
    print(title)
    print("=" * 30)


print_heading("PHYSICS")
print_heading("CHEMISTRY")
print_heading("BIOLOGY")
```

**Expected output:**

```
==============================
PHYSICS
==============================
==============================
CHEMISTRY
==============================
==============================
BIOLOGY
==============================
```

The style now lives in exactly one place. Change `=` to `-` once and all three headings change.

> **Analogy**: A function is a recipe. You write "how to make dal bhat" once, then say "make dal bhat" whenever you want it, rather than reciting every step each time.

Functions give you four things:

1. **No repetition** — write it once, use it many times
2. **One place to fix** — a bug lives in one function, not scattered through your program
3. **Readable names** — `calculate_grade(85)` explains itself; twelve lines of `elif` do not
4. **Divide and conquer** — a big problem becomes several small, testable pieces

---

## 12.2 Defining and Calling

```python
def greet():
    print("Namaste!")
    print("Welcome to Python.")


greet()
greet()
```

**Expected output:**

```
Namaste!
Welcome to Python.
Namaste!
Welcome to Python.
```

| Piece | Meaning |
|-------|---------|
| `def` | The keyword that defines a function |
| `greet` | The function's name — same rules as a variable name |
| `()` | Where parameters go, empty here |
| `:` | Required, as always |
| indented block | The **body** — what the function does |
| `greet()` | **Calling** it. The brackets are what actually run it |

Two rules that catch beginners out:

**Defining is not running.** The body does not execute when you write `def`. Nothing happens until you call it.

**Define before you call.** Python reads top to bottom:

```python
greet()

def greet():
    print("Namaste!")
```

**Expected output:**

```
NameError: name 'greet' is not defined
```

Put all your `def`s at the top of the file and the calls below. Both the Quiz Game and every program from here on follow that layout.

> **Careful**: `greet` and `greet()` are different things. Without the brackets you are referring to the function itself; with them, you are running it. `print(greet)` shows something like `<function greet at 0x104a2f1a0>` rather than calling it.

---

## 12.3 Parameters — Passing Information In

A **parameter** is a variable listed in the definition. An **argument** is the actual value you pass when calling.

```python
def greet(name):
    print(f"Namaste, {name}!")


greet("Sita")
greet("Bibek")
```

**Expected output:**

```
Namaste, Sita!
Namaste, Bibek!
```

`name` is the parameter; `"Sita"` is the argument.

### Several parameters

```python
def show_marks(name, subject, marks):
    print(f"{name} scored {marks} in {subject}.")


show_marks("Aarya", "Physics", 91)
show_marks("Nisha", "Biology", 63)
```

**Expected output:**

```
Aarya scored 91 in Physics.
Nisha scored 63 in Biology.
```

Arguments are matched to parameters **by position**, so order matters:

```python
def show_marks(name, subject, marks):
    print(f"{name} scored {marks} in {subject}.")


show_marks("Physics", "Aarya", 91)
```

**Expected output:**

```
Physics scored 91 in Aarya.
```

No error — just nonsense. Python cannot know you meant them the other way round.

The count must match, though:

```python
def show_marks(name, subject, marks):
    print(f"{name} scored {marks} in {subject}.")


show_marks("Aarya", "Physics")
```

**Expected output:**

```
TypeError: show_marks() missing 1 required positional argument: 'marks'
```

### Keyword arguments

Naming the arguments removes any doubt about order:

```python
def show_marks(name, subject, marks):
    print(f"{name} scored {marks} in {subject}.")


show_marks(subject="Physics", marks=91, name="Aarya")
```

**Expected output:**

```
Aarya scored 91 in Physics.
```

You have already used this — `marks.sort(reverse=True)` in Class 9 passes `reverse` as a keyword argument.

### Default values

Give a parameter a default and it becomes optional:

```python
def print_heading(title, symbol="=", width=30):
    print(symbol * width)
    print(title)
    print(symbol * width)


print_heading("PHYSICS")
print_heading("CHEMISTRY", "-")
print_heading("SHORT", "*", 12)
```

**Expected output:**

```
==============================
PHYSICS
==============================
------------------------------
CHEMISTRY
------------------------------
************
SHORT
************
```

> **Careful**: Parameters with defaults must come **after** those without. `def f(a=1, b)` raises `SyntaxError: parameter without a default follows parameter with a default`.

---

## 12.4 `return` — Getting a Result Back

So far our functions have printed things. Far more often, you want a function to **work something out and hand it back**.

```python
def add(a, b):
    return a + b


result = add(5, 3)
print(result)
print(add(10, 20))
print(add(5, 3) * 2)
```

**Expected output:**

```
8
30
16
```

`return` does two things: it sends a value back, and it **ends the function immediately**.

### Printing is not returning

This is the distinction that matters most today.

```python
def add_and_print(a, b):
    print(a + b)


def add_and_return(a, b):
    return a + b


x = add_and_print(5, 3)
y = add_and_return(5, 3)

print(f"x is {x}")
print(f"y is {y}")
```

**Expected output:**

```
8
x is None
y is 8
```

`add_and_print` displayed the answer but gave nothing back, so `x` is `None` and the value is lost. `add_and_return` handed the value over, so `y` can be used in further calculations.

**Rule of thumb**: functions that *calculate* should `return`. Functions that *display* should `print`. Mixing the two makes a function hard to reuse — you cannot use a printed value in a later sum.

### `return` ends the function

```python
def grade_for(percentage):
    if percentage >= 90:
        return "A+"
    if percentage >= 80:
        return "A"
    if percentage >= 70:
        return "B"
    if percentage >= 60:
        return "C"
    if percentage >= 50:
        return "D"
    return "Not passed"


print(grade_for(95))
print(grade_for(84))
print(grade_for(45))
```

**Expected output:**

```
A+
A
Not passed
```

Because `return` exits immediately, plain `if`s work just as well as `elif` here — once one returns, nothing below it can run. This is exactly the `grade_for` function in the Quiz Game.

### Returning several values

Return a tuple and unpack it, as in Class 10:

```python
def analyse(marks):
    total = sum(marks)
    average = total / len(marks)
    return total, average, max(marks), min(marks)


total, average, highest, lowest = analyse([82, 76, 91, 88])

print(f"Total:   {total}")
print(f"Average: {average:.2f}")
print(f"Highest: {highest}")
print(f"Lowest:  {lowest}")
```

**Expected output:**

```
Total:   337
Average: 84.25
Highest: 91
Lowest:  76
```

### Docstrings

A string on the first line of a function describes what it does. This is a **docstring**, and every function in the Quiz Game has one.

```python
def area_of_circle(radius):
    """Return the area of a circle with the given radius."""
    return 3.14159 * radius ** 2


print(area_of_circle(7))
print(area_of_circle.__doc__)
```

**Expected output:**

```
153.93791
Return the area of a circle with the given radius.
```

Write docstrings as a command — "Return the area", not "This returns the area".

---

## 12.5 Scope

Variables created inside a function exist **only** inside it.

```python
def calculate():
    hidden = 42
    print(f"Inside: {hidden}")


calculate()
print(hidden)
```

**Expected output:**

```
Inside: 42
NameError: name 'hidden' is not defined
```

`hidden` is a **local** variable. It is created when the function runs and destroyed when it finishes.

This is a feature, not a limitation. It means you can use `total` inside twenty different functions without them interfering with one another.

A variable created outside any function is **global** and can be read anywhere:

```python
PASS_MARK = 40


def has_passed(marks):
    return marks >= PASS_MARK


print(has_passed(45))
print(has_passed(35))
```

**Expected output:**

```
True
False
```

But assigning to it inside a function creates a *new local* variable instead of changing the global one:

```python
count = 0


def increase():
    count = 99
    print(f"Inside: {count}")


increase()
print(f"Outside: {count}")
```

**Expected output:**

```
Inside: 99
Outside: 0
```

The global `count` is untouched. Python does have a `global` keyword to override this, but it makes programs hard to follow. **Pass values in as parameters and hand results back with `return`** — that is the habit worth building.

```python
count = 0


def increased(current):
    return current + 1


count = increased(count)
print(count)
```

**Expected output:**

```
1
```

> **Tip**: Use capitals for global constants that never change — `PASS_MARK`, `SCORES_FILE`, `QUESTIONS_PER_ROUND`. Reading them inside functions is fine and normal. It is *assigning* to globals that causes trouble.

---

## 12.6 Modules

A **module** is a file of ready-made functions. Python ships with hundreds. We need two.

### `math`

```python
import math

print(math.sqrt(64))
print(math.pi)
print(math.floor(9.7))
print(math.ceil(9.2))
print(math.pow(2, 10))
```

**Expected output:**

```
8.0
3.141592653589793
9
10
1024.0
```

`import math` must appear **before** you use it, conventionally at the very top of the file. Then `math.sqrt` means "the `sqrt` function from `math`".

| Function | Does |
|----------|------|
| `math.sqrt(x)` | Square root |
| `math.pi` | π to full precision (a value, not a function — no brackets) |
| `math.floor(x)` | Round **down** to a whole number |
| `math.ceil(x)` | Round **up** to a whole number |
| `math.pow(x, y)` | x to the power y, always a float |

`math.pi` is far better than typing `3.14159`:

```python
import math

radius = 7
print(f"Area: {math.pi * radius ** 2:.4f}")
```

**Expected output:**

```
Area: 153.9380
```

### `random`

This is what makes the Quiz Game unpredictable.

```python
import random

print(random.randint(1, 6))
print(random.choice(["Physics", "Chemistry", "Biology"]))

marks = [82, 76, 91, 88]
random.shuffle(marks)
print(marks)
```

**Sample output** (yours will differ — that is the point):

```
4
Chemistry
[91, 82, 88, 76]
```

| Function | Does |
|----------|------|
| `random.randint(a, b)` | A whole number from a to b, **both included** |
| `random.choice(items)` | One random item from a list |
| `random.shuffle(items)` | Rearranges a list **in place** |
| `random.random()` | A float between 0.0 and 1.0 |

> **Careful**: `random.randint(1, 6)` **can** return 6 — unlike `range(1, 6)`, which stops at 5. The two are deliberately different, and mixing them up is a common bug.

> **Careful**: `random.shuffle()` changes the list in place and returns `None`, exactly like `.sort()`. Never write `marks = random.shuffle(marks)`.

Now the guessing game from Class 7 becomes a real game:

```python
import random

secret = random.randint(1, 100)
print("I am thinking of a number between 1 and 100.")
```

---

## 12.7 Putting It All Together

Create `science_toolkit.py`:

```python
# science_toolkit.py
# A menu-driven toolkit built entirely from functions.

import math
import random


def print_heading(title, symbol="=", width=44):
    """Print a title inside a box of the given symbol."""
    print(symbol * width)
    print(f"{title:^{width}}")
    print(symbol * width)


def ask_number(prompt):
    """Keep asking until the user types a valid number. Return it as a float."""
    while True:
        typed = input(prompt).strip()
        if typed.replace(".", "", 1).replace("-", "", 1).isdigit():
            return float(typed)
        print("Please type a number, for example 12.5")


def circle_area(radius):
    """Return the area of a circle."""
    return math.pi * radius ** 2


def quadratic_roots(a, b, c):
    """Return a tuple of (description, root1, root2) for ax^2 + bx + c."""
    discriminant = b ** 2 - 4 * a * c

    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return "Two real roots", root1, root2

    if discriminant == 0:
        root = -b / (2 * a)
        return "One repeated root", root, root

    return "No real roots", None, None


def average(values):
    """Return the mean of a list of numbers."""
    return sum(values) / len(values)


def grade_for(percentage):
    """Return the grade letter for a percentage."""
    if percentage >= 90:
        return "A+"
    if percentage >= 80:
        return "A"
    if percentage >= 70:
        return "B"
    if percentage >= 60:
        return "C"
    if percentage >= 50:
        return "D"
    return "Not passed"


def roll_dice(sides=6):
    """Return a random roll of a dice with the given number of sides."""
    return random.randint(1, sides)


# --- The program itself ---

print_heading("SCIENCE TOOLKIT")

radius = 7
print(f"\nArea of a circle with radius {radius}: {circle_area(radius):.4f}")

description, r1, r2 = quadratic_roots(1, -5, 6)
print(f"\nx^2 - 5x + 6  ->  {description}")
if r1 is not None:
    print(f"   Roots: {r1:.2f} and {r2:.2f}")

description, r1, r2 = quadratic_roots(1, 2, 5)
print(f"x^2 + 2x + 5  ->  {description}")

marks = [82, 76, 91, 88, 67]
mean = average(marks)
print(f"\nMarks:   {marks}")
print(f"Average: {mean:.2f}")
print(f"Grade:   {grade_for(mean)}")

print_heading("DICE ROLLS", "-")
for roll_number in range(1, 6):
    print(f"Roll {roll_number}: {roll_dice()}")

print(f"\nA 20-sided dice gives: {roll_dice(20)}")
```

**Sample run** (the dice rolls will differ every time):

```
============================================
              SCIENCE TOOLKIT               
============================================

Area of a circle with radius 7: 153.9380

x^2 - 5x + 6  ->  Two real roots
   Roots: 3.00 and 2.00
x^2 + 2x + 5  ->  No real roots

Marks:   [82, 76, 91, 88, 67]
Average: 80.80
Grade:   A
--------------------------------------------
                 DICE ROLLS                 
--------------------------------------------
Roll 1: 3
Roll 2: 6
Roll 3: 1
Roll 4: 5
Roll 5: 2

A 20-sided dice gives: 14
```

Points worth studying:

- Every function has a **docstring** and does exactly one job. `circle_area` calculates; `print_heading` displays. None of them mixes the two.
- `quadratic_roots` **returns a tuple** of three values, unpacked at the call site. When there are no real roots it returns `None` for both, and the caller checks with `if r1 is not None:`. Use `is not None`, not `!= None` — it is the standard way to test for `None`.
- `roll_dice(sides=6)` has a **default**, so `roll_dice()` gives a normal dice and `roll_dice(20)` gives a twenty-sided one.
- `f"{title:^{width}}"` puts a **variable** inside the format spec, so the width follows the parameter. Nesting brackets like this is occasionally very handy.
- `ask_number` is a rough validator using `.isdigit()`. It works for `12.5` and `-3` but would be fooled by `1.2.3`. Class 13 replaces it with `try` / `except`, which handles every case properly.

---

## Practice Exercises

1. **Unit converter functions** — Write four functions, each with a docstring: `celsius_to_fahrenheit(c)`, `fahrenheit_to_celsius(f)`, `km_to_miles(km)` and `kg_to_pounds(kg)`. Each must `return` its result, not print it. Then write a loop that prints a conversion table for 0, 10, 20, 30 and 40 °C.

2. **Refactor the grade calculator** — Take `grade_calculator.py` from Class 5 and rewrite it using functions: `get_marks()` to gather input, `calculate_percentage(marks)`, `grade_for(percentage)` and `print_report(...)` to display. The main part of the program should be about five lines. Is it easier or harder to read now, and why?

3. **Return versus print** — Write `double_print(n)` which prints `n * 2`, and `double_return(n)` which returns it. Now try to work out `double_print(5) + double_return(5)`. What error do you get, and what does it tell you about what `double_print` gave back?

4. **A better guessing game** — Rebuild the Class 7 guessing game using `random.randint(1, 100)` and at least three functions: one to get a valid guess, one to give the "too high / too low" hint, and one to play a full round. Then let the player play again without restarting the program.

---

## Key Takeaways

- **`def name(parameters):`** defines a function; **`name(arguments)`** runs it. Defining is not running.
- **Define functions before you call them** — put all `def`s at the top of the file.
- **Parameters** are the names in the definition; **arguments** are the values you pass. They match **by position** unless you use keyword arguments.
- **Default values** (`def f(x, symbol="=")`) make parameters optional. Defaults must come last.
- **`return`** sends a value back **and ends the function immediately**.
- **Calculating functions should `return`; displaying functions should `print`.** A function with no `return` gives back `None`.
- Return a **tuple** to hand back several values, then unpack at the call site.
- A **docstring** on the first line documents the function. Write it as a command.
- Variables inside a function are **local**. Reading a global constant is fine; assigning to a global is not — pass values in and return them out.
- **`import math`** gives `sqrt`, `pi`, `floor`, `ceil`. **`import random`** gives `randint`, `choice`, `shuffle`.
- **`random.randint(1, 6)` includes 6**, unlike `range(1, 6)`. **`random.shuffle()` returns `None`** — it changes the list in place.

Next class we will handle things going wrong — catching errors with `try` and `except` — and learn to save data to files so it survives after the program closes.
