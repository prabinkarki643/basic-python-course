# Class 1: Introduction to Python — Setup and Your First Program

> **Time budget**: 45 minutes (≈ 32 min teach + 13 min practice)
> **Prerequisites**: None. This is the very first class.

Welcome. Over the next fifteen classes you will go from never having written a line of code to building a working quiz game that other people can play. You already know how to follow a formula in Physics and balance an equation in Chemistry. Programming is the same kind of thinking — you are just writing the steps down in a language a computer understands.

## What You Will Learn

- What a **program** is, and what a **programming language** does
- Why **Python** is the right first language
- How to **install Python** and check that it worked
- How to **install and set up VS Code** as your editor
- How to write and run your **first Python program**
- How to write **comments** and read your first **error message**

---

## 1.1 What Is a Program?

A computer is fast but completely unimaginative. It will do exactly what you tell it, in exactly the order you tell it, and not one step more.

A **program** is a list of instructions written for a computer. That is the whole idea.

> **Analogy**: A program is a recipe. A recipe says "heat the oil, add the onions, wait five minutes". It does not say "make it taste nice" — it lists exact steps in exact order. If you swap two steps, you get a different dinner.

Here is a program written in English:

```
1. Ask the student for their marks in Physics.
2. Ask for their marks in Chemistry.
3. Add the two numbers together.
4. Divide by 2.
5. Show the result on screen.
```

Every human can follow that. A computer cannot, because English is too vague. So we write the same steps in a **programming language** — a language strict enough that there is only one possible meaning.

---

## 1.2 Why Python?

There are hundreds of programming languages. We are starting with Python for four reasons:

| Reason | What it means for you |
|--------|----------------------|
| **It reads like English** | `if marks > 40: print("Pass")` means almost exactly what it looks like |
| **It is short** | A task that takes 10 lines in Java takes 3 in Python |
| **It is everywhere** | Data science, artificial intelligence, websites, automation, scientific research |
| **It is free** | No licence, no cost, works on Windows, macOS and Linux |

Python was created by Guido van Rossum and released in 1991. It is named after the comedy show *Monty Python's Flying Circus*, not the snake — a small piece of trivia that surprises most people.

> **Tip**: Almost every big name you have heard of runs Python somewhere — NASA, Google, Netflix, Instagram and Spotify all use it in production. You are not learning a toy language.

---

## 1.3 Installing Python

Python does not come pre-installed on Windows, and the version that ships with macOS is often out of date. We install it properly.

### Step 1 — Download

Go to [python.org/downloads](https://www.python.org/downloads/) and click the big yellow **Download Python 3.x** button. The site detects your operating system automatically.

We need **Python 3.12 or newer**. Anything starting with `3.` will work for this course; anything starting with `2.` is obsolete and will not.

### Step 2 — Install (Windows)

Run the downloaded file. On the very first screen there is a small tick box at the bottom:

> ☐ **Add python.exe to PATH**

**Tick it.** This is the single most common setup mistake in this course. If you miss it, your computer will not know where Python lives and every command will fail with "python is not recognised".

Then click **Install Now** and wait.

### Step 3 — Install (macOS)

Open the downloaded `.pkg` file and click through the installer. There is nothing to tick — it configures itself.

### Step 4 — Check it worked

Open a terminal:

- **Windows**: press the Start key, type `cmd`, press Enter
- **macOS**: press `Cmd + Space`, type `Terminal`, press Enter

Then type this and press Enter:

```
python --version
```

**Expected output:**

```
Python 3.12.5
```

On macOS and Linux, use `python3` instead:

```
python3 --version
```

If you see a version number starting with `3.`, you are ready.

> **Common error**: `'python' is not recognised as an internal or external command`. This almost always means the **Add python.exe to PATH** box was not ticked. Re-run the installer, choose **Modify**, and make sure PATH is included. On macOS, try `python3` before assuming anything is broken.

**From here on**, this course writes `python`. If you are on macOS or Linux, type `python3` every time you see it.

---

## 1.4 Installing VS Code

You could write Python in Notepad, but you would hate it. **Visual Studio Code** is a free editor that colours your code, spots mistakes as you type, and runs programs with one click.

1. Go to [code.visualstudio.com](https://code.visualstudio.com) and download it for your system.
2. Install it and open it.
3. Click the **Extensions** icon in the left sidebar — it looks like four squares with one flying away. Or press `Ctrl + Shift + X` (`Cmd + Shift + X` on macOS).
4. Search for **Python** and install the one published by **Microsoft**. It will say `ms-python.python`.

That is all we need. No other extensions, no downloads, no accounts.

### Make a folder for your work

Create a folder called `python-class` somewhere you will find it again — your Desktop is fine. Then in VS Code choose **File → Open Folder** and select it.

Every program you write on this course goes in this folder. By Class 15 you will have around thirty files in it, and scrolling back to today's will be genuinely satisfying.

---

## 1.5 Your First Program

In VS Code, click **File → New File**, then save it immediately as `hello.py` inside your `python-class` folder.

> **Careful**: the `.py` ending matters. It tells both VS Code and Python that this is a Python file. A file called `hello.txt` will not run.

Type this — do not copy and paste. Typing is how the syntax gets into your fingers.

```python
print("Hello, world!")
print("My name is Sita.")
print("I am learning Python at Triton College.")
```

Save the file with `Ctrl + S` (`Cmd + S` on macOS).

### Running it

There are two ways. Learn both.

**Way 1 — the play button.** Click the ▷ triangle in the top-right corner of VS Code. A terminal panel opens at the bottom and shows the result.

**Way 2 — the terminal.** Open the terminal (**Terminal → New Terminal**) and type:

```
python hello.py
```

**Expected output:**

```
Hello, world!
My name is Sita.
I am learning Python at Triton College.
```

Three lines in, three lines out. Congratulations — you are a programmer.

---

## 1.6 Understanding `print()`

Let us take that first line apart, because every piece of it matters.

```python
print("Hello, world!")
```

| Piece | Name | What it does |
|-------|------|--------------|
| `print` | a **function** | The instruction: "show this on screen" |
| `(` `)` | **brackets** | Hold the thing you want to show |
| `"Hello, world!"` | a **string** | Text. Quotes mark where the text starts and ends. |

A **function** is a named instruction the computer already knows how to carry out. `print` is one of many built into Python. We will write our own in Class 12.

A **string** is the programming word for text. It must be wrapped in quotes. Python accepts either double quotes or single quotes, as long as you use the same one at both ends:

```python
print("Double quotes work.")
print('Single quotes work too.')
```

**Expected output:**

```
Double quotes work.
Single quotes work too.
```

### Printing more than one thing

Separate items with a comma. Python puts a space between them automatically.

```python
print("Physics", "Chemistry", "Biology")
print("Total marks:", 240)
```

**Expected output:**

```
Physics Chemistry Biology
Total marks: 240
```

Notice that `240` has **no quotes**. It is a number, not text. Python can do arithmetic with numbers, but not with text — a difference that matters enormously from Class 2 onwards.

### An empty line

`print()` with nothing inside prints a blank line. It is the easiest way to space out your output.

```python
print("Section A")
print()
print("Section B")
```

**Expected output:**

```
Section A

Section B
```

> **Try it**: Change the text between the quotes to your own name and school, then run it again. Nothing breaks — the computer prints whatever you put there.

---

## 1.7 Comments

Sometimes you want to write a note to yourself inside your code. A **comment** starts with a `#`. Python ignores everything after it on that line.

```python
# This program greets the student.
# Written by Sita, Class 12 Science.

print("Namaste!")        # this bit is ignored too
print("Welcome to Python.")
```

**Expected output:**

```
Namaste!
Welcome to Python.
```

The two note lines and the note at the end of line 4 produce nothing. They exist purely for humans.

Comments are useful for three things:

1. **Explaining why** you did something, when the reason is not obvious
2. **Labelling sections** of a longer program
3. **Temporarily switching a line off** without deleting it — put a `#` in front and it stops running

```python
print("This line runs.")
# print("This line does not.")
print("This line runs too.")
```

**Expected output:**

```
This line runs.
This line runs too.
```

> **Tip**: Do not comment the obvious. `# print a message` above a `print` is noise. `# 9.8 is gravity in metres per second squared` is useful.

---

## 1.8 Your First Error

You will see errors constantly. Every programmer does, all day, forever. An error is not a failure — it is Python telling you precisely what confused it.

Make one on purpose. Create `broken.py`:

```python
print("Hello)
```

The closing quote is missing. Run it.

**Expected output:**

```
  File "broken.py", line 1
    print("Hello)
          ^
SyntaxError: unterminated string literal (detected at line 1)
```

Read it from the bottom up — that is where the useful part lives:

- **`SyntaxError`** — the type of problem. Python could not even understand the sentence.
- **`unterminated string literal`** — a string was opened and never closed.
- **`line 1`** — where to look.
- The **`^`** points at roughly where Python got lost.

Fix it by adding the closing quote, and it runs.

Two more you will meet in your first week:

```python
Print("Hello")
```

**Expected output:**

```
NameError: name 'Print' is not defined. Did you mean: 'print'?
```

Python is **case-sensitive**. `print` and `Print` are two different words, and only one of them exists.

```python
print("Hello"
```

**Expected output:**

```
SyntaxError: '(' was never closed
```

Every `(` needs a `)`. Every `"` needs a `"`.

> **Tip**: When you hit an error, read the **last line first**. It names the problem. Then look at the line number. Ninety per cent of beginner errors are a missing quote, a missing bracket, or a capital letter that should be lower case.

---

## 1.9 Putting It All Together

Create a file called `about_me.py` and type this out in full:

```python
# about_me.py
# My first Python program.
# Class 12 Science — Triton College

print("=" * 30)
print("ABOUT ME")
print("=" * 30)

print()
print("Name:", "Sita Sharma")
print("Class:", 12)
print("Stream:", "Science")
print("College:", "Triton College")

print()
print("My subjects are:")
print("  - Physics")
print("  - Chemistry")
print("  - Biology")
print("  - Maths")

print()
print("Favourite subject:", "Physics")
print("Reason: it explains why things fall.")
print("=" * 30)
```

**Expected output:**

```
==============================
ABOUT ME
==============================

Name: Sita Sharma
Class: 12
Stream: Science
College: Triton College

My subjects are:
  - Physics
  - Chemistry
  - Biology
  - Maths

Favourite subject: Physics
Reason: it explains why things fall.
==============================
```

Two things worth noticing:

- `"=" * 30` prints the `=` character thirty times. Multiplying text by a number repeats it. That is a genuinely useful trick for tidy output, and we will use it again in the final project.
- The spaces before `- Physics` are inside the quotes, so they appear in the output. Anything inside quotes is printed exactly as typed.

---

## Practice Exercises

1. **Your own profile** — Rewrite `about_me.py` with your real details: your name, your subjects, your favourite one and why. Add a line for your hobby. Run it and check every line appears as you expect.

2. **Break it deliberately** — Make three separate copies of a working program and introduce one error in each: remove a closing bracket, capitalise `print`, and delete a closing quote. Run all three and write down the exact error message each one gives. Why is it useful to have seen these before you make them by accident?

3. **A decorated banner** — Using only `print()` and the `"=" * 30` trick, produce this exact output. Work out how many characters wide each line needs to be:

   ```
   ******************************
   *      TRITON  COLLEGE       *
   *   Basic Python — Class 1   *
   ******************************
   ```

4. **Comment practice** — Take your `about_me.py` and add a comment at the top saying who wrote it and when. Then comment out the line that prints your hobby, run the program, and confirm that line disappears. Why is commenting a line out more useful than deleting it while you are still experimenting?

---

## Key Takeaways

- A **program** is a list of exact instructions; a **programming language** removes the vagueness of English.
- Python is free, readable and used professionally everywhere — it is a real language, not a training one.
- **Tick "Add python.exe to PATH"** on Windows. Check the install with `python --version` (`python3` on macOS).
- Python files end in **`.py`**. Run them with `python filename.py` or the ▷ button in VS Code.
- **`print()`** shows things on screen. Text needs quotes; numbers do not. Commas separate several items.
- **`#`** starts a comment — a note for humans that Python ignores completely.
- Errors are normal. Read the **last line** of the message first; it names the problem.
- Python is **case-sensitive**: `print` works, `Print` does not.

Next class we will store information in **variables**, so our programs can work with data instead of just printing fixed text.
