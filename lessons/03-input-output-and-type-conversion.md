# Class 3: Input, Output and Type Conversion — Talking to the User

> **Time budget**: 45 minutes (≈ 32 min teach + 13 min practice)
> **Prerequisites**: Class 2 (Variables and Data Types)

So far your programs only know what you typed into them. Today they start asking questions. By the end of this class your programs will take information from whoever is using them, do something useful with it, and present the result neatly.

## What You Will Learn

- How to ask a question with **`input()`**
- Why `input()` **always** gives you a string, and why that causes the classic beginner bug
- Converting between types with **`int()`**, **`float()`** and **`str()`**
- Formatting output beautifully with **f-strings**
- Rounding numbers with **`round()`**

---

## 3.1 Asking a Question with `input()`

```python
name = input("What is your name? ")
print("Namaste,", name)
```

**Sample run:**

```
What is your name? Sita
Namaste, Sita
```

Here is what happens, step by step:

1. Python prints the text inside the brackets — `What is your name? `
2. The program **stops** and waits
3. The user types something and presses Enter
4. Whatever they typed is handed back and stored in `name`

The text inside the brackets is called the **prompt**. It is optional, but a program that stops with a blank screen and no explanation is a bad program. Always write a prompt.

> **Tip**: End your prompt with a space, as in `"What is your name? "`. Without it, the user's typing runs straight into your question text and looks cramped.

Asking for several things is just several calls:

```python
name = input("Name: ")
college = input("College: ")
subject = input("Favourite subject: ")

print()
print(name, "studies at", college, "and likes", subject)
```

**Sample run:**

```
Name: Bibek
College: Triton
Favourite subject: Chemistry

Bibek studies at Triton and likes Chemistry
```

---

## 3.2 The Big Catch — `input()` Always Gives a String

This is the most important idea in today's class, and the source of nearly every beginner's first serious bug.

**`input()` always returns a `str`. Always. No exceptions.**

Even when the user types digits.

```python
age = input("How old are you? ")
print(age)
print(type(age))
```

**Sample run:**

```
How old are you? 17
17
<class 'str'>
```

It *looks* like the number 17. It is the **text** `"17"`.

Watch what that does:

```python
marks = input("Enter your marks: ")
print("Doubled:", marks * 2)
```

**Sample run:**

```
Enter your marks: 45
Doubled: 4545
```

Not 90. `4545`. Because `marks` holds the text `"45"`, and multiplying text by 2 repeats it — exactly the `"=" * 30` trick from Class 1.

And arithmetic fails outright:

```python
physics = input("Physics marks: ")
chemistry = input("Chemistry marks: ")
print("Total:", physics + chemistry)
```

**Sample run:**

```
Physics marks: 82
Chemistry marks: 76
Total: 8276
```

`"82" + "76"` joins the two pieces of text into `"8276"`. Python did nothing wrong. It did precisely what you asked. You asked the wrong thing.

> **Common error**: If your marks total comes out as an impossible number like `8276`, or you get `TypeError: can only concatenate str`, you have forgotten to convert your input. This will happen to you at least once. Now you will recognise it.

---

## 3.3 Converting Types

Python gives you three conversion functions, named after the types they produce.

| Function | Turns a value into | Example | Result |
|----------|-------------------|---------|--------|
| `int()` | a whole number | `int("45")` | `45` |
| `float()` | a decimal number | `float("9.8")` | `9.8` |
| `str()` | text | `str(45)` | `"45"` |

Converting is sometimes called **casting**.

### Fixing the marks program

```python
physics = int(input("Physics marks: "))
chemistry = int(input("Chemistry marks: "))

print("Total:", physics + chemistry)
```

**Sample run:**

```
Physics marks: 82
Chemistry marks: 76
Total: 158
```

Read `int(input("Physics marks: "))` from the inside out — that is the order Python does it in:

1. `input("Physics marks: ")` runs first and gives back the text `"82"`
2. `int("82")` converts that text to the number `82`
3. `82` is stored in `physics`

Wrapping `int()` around `input()` like this is a pattern you will type hundreds of times.

### When to use `int()` and when to use `float()`

Use **`int()`** for things that are always whole: a count of students, a roll number used as a number, someone's age, a quantity.

Use **`float()`** for things that can have a fraction: marks that might be 82.5, a temperature, a measurement, a percentage.

```python
students = int(input("Number of students: "))
temperature = float(input("Room temperature in °C: "))

print(students, "students in a room at", temperature, "degrees")
```

**Sample run:**

```
Number of students: 42
Room temperature in °C: 23.5
42 students in a room at 23.5 degrees
```

> **Careful**: `int("23.5")` **crashes**. `int()` only accepts text that is a whole number. If the value might have a decimal point, use `float()`. If you genuinely need a whole number from a decimal, convert twice: `int(float("23.5"))` gives `23`.

### Converting a number to text with `str()`

You need `str()` when you want to **join** a number onto a string with `+`:

```python
marks = 87
message = "You scored " + str(marks) + " marks."
print(message)
```

**Expected output:**

```
You scored 87 marks.
```

Without `str()` that line raises a `TypeError`. In practice you will rarely write this, because f-strings — coming next — do the job far more comfortably.

### What happens when conversion fails

```python
marks = int(input("Enter your marks: "))
```

**Sample run:**

```
Enter your marks: hello
ValueError: invalid literal for int() with base 10: 'hello'
```

A **`ValueError`** means the value had the right *type* — it was text — but the wrong *content*. `"hello"` is not a number in any base.

For now, assume the user types sensible things. In Class 13 you will learn `try` / `except`, which lets your program catch this and ask again instead of crashing. That is exactly how the Quiz Game handles it.

---

## 3.4 f-strings — Formatting Output Properly

You have been separating things with commas. It works, but it is clumsy and you cannot control the spacing.

An **f-string** is a string with an `f` in front of the opening quote. Inside it, anything you put in `{curly brackets}` gets replaced by its value.

```python
name = "Sita"
marks = 87

print(f"{name} scored {marks} marks.")
```

**Expected output:**

```
Sita scored 87 marks.
```

Compare the two styles:

```python
name = "Sita"
marks = 87

print("Congratulations", name + ",", "you scored", marks, "out of 100!")
print(f"Congratulations {name}, you scored {marks} out of 100!")
```

**Expected output:**

```
Congratulations Sita, you scored 87 out of 100!
Congratulations Sita, you scored 87 out of 100!
```

Same result. The f-string reads like the sentence you actually want, with the values slotted in. From here on, this course uses f-strings for everything.

> **Careful**: the `f` must come **before** the opening quote — `f"..."`, not `"f..."`. Forget it and you get the literal text `{name}` in your output, curly brackets and all. That is a good clue when your output looks wrong.

### Calculations inside an f-string

You can put a whole expression in the brackets, not just a variable name:

```python
physics = 82
chemistry = 76

print(f"Total: {physics + chemistry}")
print(f"Average: {(physics + chemistry) / 2}")
```

**Expected output:**

```
Total: 158
Average: 79.0
```

### Controlling decimal places

Long decimals are ugly. Add `:.2f` inside the brackets to show exactly two decimal places:

```python
average = 79.66666666666667

print(f"Average: {average}")
print(f"Average: {average:.2f}")
print(f"Average: {average:.1f}")
print(f"Average: {average:.0f}")
```

**Expected output:**

```
Average: 79.66666666666667
Average: 79.67
Average: 79.7
Average: 80
```

Read `.2f` as "2 decimal places, in **f**ixed-point style". The number is rounded for display, but the variable itself is untouched — `average` still holds all those sixes.

> **Tip**: Marks and money almost always want `:.2f`. Percentages usually read better with `:.1f`. Pick one and use it consistently across a program, so your output lines up.

---

## 3.5 Rounding with `round()`

`:.2f` changes how a number is **displayed**. `round()` changes the **value** itself.

```python
average = 79.66666666666667

rounded = round(average, 2)
print(rounded)
print(type(rounded))
```

**Expected output:**

```
79.67
<class 'float'>
```

The second argument is how many decimal places to keep. Leave it out and you get a whole number:

```python
print(round(79.6))
print(round(79.4))
print(round(79.66666, 3))
```

**Expected output:**

```
80
79
79.667
```

| You want | Use | Result type |
|----------|-----|-------------|
| To display a value neatly, once | `f"{value:.2f}"` | `str` |
| To store a rounded value and keep using it | `round(value, 2)` | `float` (or `int` with no second argument) |

### One genuine surprise

Try this and watch carefully:

```python
print(round(2.5))
print(round(3.5))
print(round(0.5))
```

**Expected output:**

```
2
4
0
```

`round(2.5)` gives `2`, not `3`. Python does not use the "always round a half upwards" rule you were taught at school. When a value sits exactly halfway, it rounds to the **nearest even number** — 2.5 goes down to 2, 3.5 goes up to 4.

This is called banker's rounding, and it exists because always rounding halves upwards slowly inflates a long column of figures. It almost never matters in this course, but if a marks total ever comes out one lower than you expected, this is why.

> **Try it**: Run `round(1.5)`, `round(4.5)` and `round(5.5)` and see whether you can predict each one before you press Enter.

---

## 3.6 Putting It All Together

Create `temperature_converter.py`. This is a real, useful program: it converts a temperature the way your Physics textbook does.

```python
# temperature_converter.py
# Converts a temperature from Celsius to Fahrenheit and Kelvin.

print("=" * 40)
print("TEMPERATURE CONVERTER")
print("=" * 40)

# --- Input ---
name = input("\nYour name: ")
celsius = float(input("Temperature in Celsius: "))

# --- Calculations ---
fahrenheit = (celsius * 9 / 5) + 32
kelvin = celsius + 273.15

# --- Output ---
print()
print("-" * 40)
print(f"Results for {name}")
print("-" * 40)
print(f"Celsius:    {celsius:.2f} °C")
print(f"Fahrenheit: {fahrenheit:.2f} °F")
print(f"Kelvin:     {kelvin:.2f} K")
print("-" * 40)

print(f"\n{celsius} °C is the same temperature as {fahrenheit:.1f} °F.")
```

**Sample run:**

```
========================================
TEMPERATURE CONVERTER
========================================

Your name: Aarya
Temperature in Celsius: 37

----------------------------------------
Results for Aarya
----------------------------------------
Celsius:    37.00 °C
Fahrenheit: 98.60 °F
Kelvin:     310.15 K
----------------------------------------

37.0 °C is the same temperature as 98.6 °F.
```

Three details to notice:

- **`\n`** inside a string means "start a new line here". `input("\nYour name: ")` prints a blank line before the prompt. It is tidier than an extra `print()`.
- `float()` not `int()`, because a temperature of `36.5` is perfectly reasonable.
- The last line prints `37.0`, not `37`, because `float("37")` is `37.0`. The `.0` is real and honest — the value genuinely is a float.

---

## Practice Exercises

1. **Marks calculator** — Ask the user for their name and their marks in Physics, Chemistry, Biology and Maths. Print their name, the total out of 400, and the percentage to two decimal places using an f-string. Test it with 82, 76, 91 and 88 — you should get 337 and 84.25%.

2. **Find the bug** — This program is wrong. Run it, note what it prints, then fix it with a single change:

   ```python
   length = input("Length of the room in metres: ")
   width = input("Width of the room in metres: ")
   print(f"Area: {length * width} square metres")
   ```

   What does it do before the fix, and why does that particular strange thing happen?

3. **Speed, distance, time** — Ask for a distance in kilometres and a time in hours, both as decimals. Work out and print the speed in km/h to one decimal place, and also in metres per second (divide km/h by 3.6) to two decimal places. Test with 120 km in 1.5 hours.

4. **Round versus format** — Take `value = 3.14159`. Print it four ways: with `round(value, 2)`, with `f"{value:.2f}"`, with `round(value)` and with `f"{value:.0f}"`. Note the type each one produces using `type()`. When would you want `round()` rather than the f-string version?

---

## Key Takeaways

- **`input("prompt")`** displays a prompt, waits, and returns whatever the user typed.
- **`input()` always returns a `str`** — even for digits. This is the number one beginner bug.
- Convert with **`int()`**, **`float()`** and **`str()`**. The usual pattern is `int(input("..."))`, read from the inside out.
- Use `int()` for whole things, `float()` for anything that can have a decimal. `int("23.5")` crashes.
- A **`ValueError`** means the content could not be converted — `"hello"` is not a number.
- **f-strings** (`f"Hi {name}"`) are the modern way to build output. Put any expression inside `{ }`.
- **`{value:.2f}`** displays two decimal places; **`round(value, 2)`** changes the stored value.
- **`\n`** inside a string starts a new line.

Next class we will look at all of Python's **operators** in detail — including the two division operators, the remainder operator, and how Python decides what to work out first.
