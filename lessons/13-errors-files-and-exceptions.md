# Class 13: Errors, Exceptions and Files — Programs That Survive

> **Time budget**: 45 minutes (≈ 32 min teach + 13 min practice)
> **Prerequisites**: Class 12 (Functions and Modules)

Every program you have written so far crashes if the user types something unexpected, and forgets everything the moment it closes. Today we fix both. This is the last class before the project, and it supplies the final two pieces the Quiz Game needs.

## What You Will Learn

- The difference between a **syntax error** and an **exception**
- How to read a **traceback**
- Catching problems with **`try`** / **`except`** / **`else`** / **`finally`**
- The exceptions you will actually meet: `ValueError`, `ZeroDivisionError`, `FileNotFoundError`
- **Reading and writing files** with `with open(...)`

---

## 13.1 Two Kinds of Error

**Syntax errors** happen before the program runs. Python cannot even understand the code, so nothing executes at all.

```python
print("Hello"
```

**Expected output:**

```
SyntaxError: '(' was never closed
```

**Exceptions** happen *while* the program is running. The code was valid — something went wrong when it met real data.

```python
print("Starting...")
result = 10 / 0
print("This never runs.")
```

**Expected output:**

```
Starting...
ZeroDivisionError: division by zero
```

The first line ran. Then Python hit something impossible and stopped dead. **Only exceptions can be caught** — a syntax error must be fixed by you.

### Reading a traceback

```python
def divide(a, b):
    return a / b


def calculate():
    return divide(10, 0)


calculate()
```

**Expected output:**

```
Traceback (most recent call last):
  File "example.py", line 9, in <module>
    calculate()
  File "example.py", line 6, in calculate
    return divide(10, 0)
           ^^^^^^^^^^^^^
  File "example.py", line 2, in divide
    return a / b
           ~~^~~
ZeroDivisionError: division by zero
```

"Most recent call last" is the key phrase. Read it **bottom-up**:

- The **last line** names the problem: `ZeroDivisionError: division by zero`
- The **line above it** shows where it actually happened: line 2, in `divide`
- The lines above that show how you got there: `calculate()` called `divide()`

Beginners panic at the wall of text. Read the bottom two lines first; they answer almost every question.

### The exceptions you will meet

| Exception | Cause | Example |
|-----------|-------|---------|
| `ValueError` | Right type, wrong content | `int("hello")` |
| `TypeError` | Wrong type altogether | `"10" + 5` |
| `ZeroDivisionError` | Dividing by zero | `10 / 0` |
| `IndexError` | Position does not exist | `[1, 2][5]` |
| `KeyError` | Dictionary key does not exist | `{"a": 1}["b"]` |
| `NameError` | Using an undefined name | `print(undefined_thing)` |
| `FileNotFoundError` | Opening a file that is not there | `open("missing.txt")` |
| `AttributeError` | Method does not exist for that type | `"abc".append("d")` |

You have met most of these already. Now you can handle them.

---

## 13.2 `try` and `except`

```python
try:
    marks = int(input("Enter your marks: "))
    print(f"You entered {marks}.")
except ValueError:
    print("That was not a whole number.")
```

**Sample run:**

```
Enter your marks: hello
That was not a whole number.
```

The program **did not crash**. Python tried the block, hit a `ValueError`, and ran the `except` block instead.

How it works:

1. Run everything in `try`
2. If nothing goes wrong, skip `except` entirely
3. If a **matching** exception occurs, jump immediately to `except`
4. Carry on with the rest of the program either way

> **Careful**: The moment an exception fires, the rest of the `try` block is abandoned. Keep `try` blocks **short** — just the line or two that might fail — so you know exactly what was skipped.

### Catching the right exception

```python
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Cannot divide by zero.")
        return None


print(safe_divide(10, 2))
print(safe_divide(10, 0))
```

**Expected output:**

```
5.0
Cannot divide by zero.
None
```

### Catching several

```python
def safe_divide(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        return "Those were not numbers."
    except ZeroDivisionError:
        return "Cannot divide by zero."


print(safe_divide("10", "2"))
print(safe_divide("ten", "2"))
print(safe_divide("10", "0"))
```

**Expected output:**

```
5.0
Those were not numbers.
Cannot divide by zero.
```

Python runs the **first** `except` that matches. You can also group them:

```python
try:
    value = int("hello")
except (ValueError, TypeError):
    print("Something was wrong with that value.")
```

**Expected output:**

```
Something was wrong with that value.
```

### Seeing the message

```python
try:
    marks = int("hello")
except ValueError as error:
    print(f"Python said: {error}")
```

**Expected output:**

```
Python said: invalid literal for int() with base 10: 'hello'
```

`as error` captures the exception so you can inspect it. Useful while debugging; usually too technical to show a real user.

### Do not catch everything

```python
try:
    marks = int(input("Marks: "))
except:
    print("Something went wrong.")
```

This works, but it is a bad habit. A bare `except:` swallows **every** problem — including typing mistakes in your own code — and hides them behind a useless message. It will even catch `Ctrl + C`.

**Always name the exception you expect.** If you genuinely do not know which one, run the code, read the traceback, and then catch that.

---

## 13.3 `else` and `finally`

```python
try:
    marks = int(input("Enter your marks: "))
except ValueError:
    print("That was not a number.")
else:
    print(f"Thank you. You entered {marks}.")
finally:
    print("Input attempt finished.")
```

**Sample run** (valid input):

```
Enter your marks: 87
Thank you. You entered 87.
Input attempt finished.
```

**Sample run** (invalid input):

```
Enter your marks: hello
That was not a number.
Input attempt finished.
```

| Block | Runs when |
|-------|-----------|
| `try` | Always — this is the risky code |
| `except` | Only if a matching exception occurred |
| `else` | Only if **no** exception occurred |
| `finally` | **Always**, whatever happened |

`else` keeps the risky line separate from the code that depends on it succeeding. `finally` is for cleanup that must happen either way.

### The validated-input pattern

Combine `try` / `except` with the `while True` loop from Class 7 and you have a genuinely robust input function. This is the exact pattern the Quiz Game uses:

```python
def ask_for_number(prompt, lowest, highest):
    """Keep asking until the user types a whole number in range."""
    while True:
        typed = input(prompt).strip()

        try:
            value = int(typed)
        except ValueError:
            print("Please type a whole number.")
            continue

        if lowest <= value <= highest:
            return value

        print(f"Please type a number between {lowest} and {highest}.")


marks = ask_for_number("Enter marks (0-100): ", 0, 100)
print(f"Accepted: {marks}")
```

**Sample run:**

```
Enter marks (0-100): abc
Please type a whole number.
Enter marks (0-100): 150
Please type a number between 0 and 100.
Enter marks (0-100): 87
Accepted: 87
```

Nothing the user types can crash this. Read it once more and make sure you see how `continue`, `return` and `except` work together — this function is worth memorising.

---

## 13.4 Writing to a File

Everything so far vanishes when the program ends. Files fix that.

```python
with open("results.txt", "w") as file:
    file.write("Sita|82\n")
    file.write("Bibek|35\n")
    file.write("Aarya|91\n")

print("File written.")
```

**Expected output:**

```
File written.
```

Look in your project folder and `results.txt` is there, containing three lines.

### The `with` statement

`with open(...) as file:` opens the file, gives it the name `file`, and **closes it automatically** when the indented block ends — even if an error occurs partway through. Always use `with`. Opening a file without it means remembering to close it, and forgetting can lose data.

### `\n` matters

`.write()` does **not** add a line break. Without `\n` everything ends up on one line:

```python
with open("oneline.txt", "w") as file:
    file.write("Sita|82")
    file.write("Bibek|35")
```

That file contains `Sita|82Bibek|35`. Remember the `\n`.

### The modes

| Mode | Name | Does |
|------|------|------|
| `"r"` | read | Read only. **Error** if the file does not exist. The default. |
| `"w"` | write | **Erases everything** and starts fresh. Creates the file if needed. |
| `"a"` | append | Adds to the **end**. Creates the file if needed. |

> **Careful**: `"w"` destroys the existing contents the instant the file is opened — before you write a single thing. If you meant to add to a file and typed `"w"`, the old data is gone. When in doubt, use `"a"`.

```python
with open("results.txt", "a") as file:
    file.write("Nisha|67\n")

print("One line appended.")
```

**Expected output:**

```
One line appended.
```

The file now has four lines. Run it again and it has five.

---

## 13.5 Reading from a File

### Line by line — the usual way

```python
with open("results.txt", "r") as file:
    for line in file:
        print(line.strip())
```

**Expected output:**

```
Sita|82
Bibek|35
Aarya|91
Nisha|67
```

Looping over the file object gives one line at a time. Each line **includes its `\n`**, which is why `.strip()` is there — without it you get a blank line between every entry.

### The whole file at once

```python
with open("results.txt", "r") as file:
    contents = file.read()

print(contents)
print(f"Characters: {len(contents)}")
```

**Expected output:**

```
Sita|82
Bibek|35
Aarya|91
Nisha|67

Characters: 35
```

There is a blank line before `Characters:` because the last line of the file ends with `\n`, and `print` adds another. The count of 35 includes all four `\n` characters — they are real characters in the file, just invisible ones.

`.read()` gives one big string. `.readlines()` gives a list of lines. Both load the entire file into memory, so for anything large, prefer the line-by-line loop.

### Handling a missing file

```python
try:
    with open("missing.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("That file does not exist yet.")
```

**Expected output:**

```
That file does not exist yet.
```

This is essential. The first time anybody runs the Quiz Game there is no `scores.txt`, and the program must cope rather than crash.

### Parsing the data back

Data comes out of a file as **strings**. To use it, split it and convert it — bringing together `.split()` from Class 8, `int()` from Class 3 and `try` / `except` from today.

```python
results = []

try:
    with open("results.txt", "r") as file:
        for line in file:
            line = line.strip()
            if line == "":
                continue

            parts = line.split("|")
            if len(parts) != 2:
                continue

            try:
                results.append((parts[0], int(parts[1])))
            except ValueError:
                continue
except FileNotFoundError:
    print("No results file found.")

print(results)

if results:
    marks_only = []
    for name, marks in results:
        marks_only.append(marks)

    print(f"Average: {sum(marks_only) / len(marks_only):.2f}")
    print(f"Highest: {max(marks_only)}")
```

**Expected output:**

```
[('Sita', 82), ('Bibek', 35), ('Aarya', 91), ('Nisha', 67)]
Average: 68.75
Highest: 91
```

Three separate guards, each skipping a bad line rather than crashing:

- `if line == "": continue` — skips blank lines, including the one at the end of most files
- `if len(parts) != 2: continue` — skips lines in the wrong format
- the inner `try` — skips lines where the marks are not a number

This is called **defensive programming**: assume the file might have been edited by hand, and refuse to fall over. `read_scores()` in the Quiz Game is this exact function.

---

## 13.6 Putting It All Together

Create `marks_store.py`:

```python
# marks_store.py
# Saves and loads student marks, and never crashes.

DATA_FILE = "marks_data.txt"


def ask_for_number(prompt, lowest, highest):
    """Keep asking until the user types a whole number in range."""
    while True:
        typed = input(prompt).strip()

        try:
            value = int(typed)
        except ValueError:
            print("   Please type a whole number.")
            continue

        if lowest <= value <= highest:
            return value

        print(f"   Please type a number between {lowest} and {highest}.")


def save_record(name, marks):
    """Append one record to the data file. Return True if it worked."""
    try:
        with open(DATA_FILE, "a") as file:
            file.write(f"{name}|{marks}\n")
        return True
    except OSError:
        print("   Could not write to the file.")
        return False


def load_records():
    """Read every valid record. Return a list of (name, marks) tuples."""
    records = []

    try:
        with open(DATA_FILE, "r") as file:
            for line in file:
                line = line.strip()
                if line == "":
                    continue

                parts = line.split("|")
                if len(parts) != 2:
                    continue

                try:
                    records.append((parts[0], int(parts[1])))
                except ValueError:
                    continue
    except FileNotFoundError:
        return records

    return records


def show_records(records):
    """Print all records with statistics."""
    if not records:
        print("\nNo records saved yet.")
        return

    print(f"\n{'Name':<16}{'Marks':>6}")
    print("-" * 22)

    marks_only = []
    for name, marks in records:
        print(f"{name:<16}{marks:>6}")
        marks_only.append(marks)

    print("-" * 22)
    print(f"{'Count':<16}{len(marks_only):>6}")
    print(f"{'Average':<16}{sum(marks_only) / len(marks_only):>6.2f}")
    print(f"{'Highest':<16}{max(marks_only):>6}")
    print(f"{'Lowest':<16}{min(marks_only):>6}")


def main():
    """Run the menu."""
    print("=" * 40)
    print(f"{'MARKS STORE':^40}")
    print("=" * 40)

    while True:
        print("\n1. Add a record")
        print("2. Show all records")
        print("3. Quit")

        choice = input("Choose: ").strip()

        if choice == "1":
            name = input("   Student name: ").strip()
            if not name:
                print("   A name is required.")
                continue

            marks = ask_for_number("   Marks (0-100): ", 0, 100)

            if save_record(name, marks):
                print(f"   Saved {name} with {marks} marks.")

        elif choice == "2":
            show_records(load_records())

        elif choice == "3":
            print("\nGoodbye.")
            break

        else:
            print("   Please choose 1, 2 or 3.")


main()
```

**Sample run:**

```
========================================
              MARKS STORE               
========================================

1. Add a record
2. Show all records
3. Quit
Choose: 1
   Student name: Sita
   Marks (0-100): abc
   Please type a whole number.
   Marks (0-100): 150
   Please type a number between 0 and 100.
   Marks (0-100): 82
   Saved Sita with 82 marks.

1. Add a record
2. Show all records
3. Quit
Choose: 2

Name             Marks
----------------------
Sita                82
----------------------
Count                1
Average          82.00
Highest             82
Lowest              82

1. Add a record
2. Show all records
3. Quit
Choose: 3

Goodbye.
```

Run it a second time and choose option 2 straight away — **your record is still there**. The data outlived the program. That is what files are for.

Everything from Classes 1 to 13 is in this one file: variables, f-strings, comparisons, `while True`, `if`/`elif`/`else`, lists, tuples, functions, `try`/`except` and file handling. You now have every tool the Quiz Game needs.

> **Try it**: Open `marks_data.txt` in VS Code and deliberately corrupt it — add a blank line, a line reading `rubbish`, and a line reading `Bibek|not-a-number`. Run option 2 again. The program should ignore all three and still show correct statistics. Which guard catches which bad line?

---

## Practice Exercises

1. **Safe calculator** — Write a function `safe_divide(a, b)` that takes two strings, converts them, divides them, and returns the answer. Catch `ValueError` and `ZeroDivisionError` separately with a clear message for each. Test it with `("10", "2")`, `("ten", "2")` and `("10", "0")`.

2. **Diary** — Write a program that asks the user for a note and appends it to `diary.txt`, then prints the whole diary numbered from 1. Handle the first run, when the file does not exist, using `try` / `except FileNotFoundError`. Why must you use mode `"a"` here rather than `"w"`?

3. **Word counter from a file** — Write a program that reads a text file and reports the number of lines, words and characters. Use `.split()` and the counting pattern. If the file is missing, print a helpful message rather than crashing. Test it on a file you wrote earlier in this class.

4. **Break it on purpose** — Take `marks_store.py` and remove the `try` / `except ValueError` from `ask_for_number`. Run it and type `abc`. Record the exact traceback. Then remove the `except FileNotFoundError` from `load_records`, delete `marks_data.txt`, and choose option 2. Record that traceback too. Put both back. Why is a program that crashes on bad input unacceptable in something real, like a bank's software?

---

## Key Takeaways

- **Syntax errors** stop the program before it runs and must be fixed. **Exceptions** happen during the run and **can be caught**.
- Read a traceback **bottom-up** — the last line names the problem, the line above shows where.
- **`try:` / `except ExceptionName:`** runs risky code and handles failure gracefully.
- Keep `try` blocks **short**, and **always name the exception**. A bare `except:` hides your own bugs.
- **`else`** runs when nothing went wrong; **`finally`** runs whatever happens.
- **`while True` + `try`/`except` + `return`** is the standard pattern for input that cannot be broken.
- **`with open(filename, mode) as file:`** opens a file and closes it automatically. Always use `with`.
- Modes: **`"r"`** read, **`"w"`** overwrite (destroys existing content), **`"a"`** append.
- **`.write()` does not add `\n`** — you must include it yourself.
- Looping over a file gives one line at a time, each ending in `\n`, so **`.strip()`** it.
- Catch **`FileNotFoundError`** for a file that may not exist yet — as on a program's very first run.
- Everything read from a file is a **string**. Split it, convert it, and guard every step.

Next class we begin the **mini project** — building the Quiz Game, using everything from the last thirteen classes.
