# Class 8: Strings in Depth — Working With Text

> **Time budget**: 45 minutes (≈ 32 min teach + 13 min practice)
> **Prerequisites**: Class 7 (Loops Part 2 — `while`, `break` and `continue`)

You have used strings since Class 1. Today you learn what you can actually *do* with them: reach into them, cut pieces out, search them, clean them up and reshape them. Almost every program that talks to a human is mostly string handling.

## What You Will Learn

- **Indexing** — reaching a single character, forwards and backwards
- **Slicing** — cutting out a section
- The most useful **string methods**: `.upper()`, `.strip()`, `.split()`, `.replace()`, `.find()` and more
- Why strings are **immutable**, and what that means in practice
- **`.join()`** and f-string **alignment** for tidy output

---

## 8.1 Indexing — Reaching One Character

Every character in a string has a numbered position, called its **index**. Counting starts at **0**.

```
 P  y  t  h  o  n
 0  1  2  3  4  5
-6 -5 -4 -3 -2 -1
```

Use square brackets to reach one:

```python
word = "Python"

print(word[0])
print(word[1])
print(word[5])
```

**Expected output:**

```
P
y
n
```

`word[0]` is the **first** character, not the second. The index is the *offset* from the start — the first character is zero steps in. This is why `range(5)` starts at 0 too; the two conventions line up deliberately.

### Negative indexing

Negative numbers count from the **end**, starting at `-1`:

```python
word = "Python"

print(word[-1])
print(word[-2])
print(word[-6])
```

**Expected output:**

```
n
o
P
```

`word[-1]` is the last character, always, whatever the length. That is much better than working out `word[len(word) - 1]`.

### `len()` and going out of range

```python
word = "Python"
print(len(word))
print(word[len(word) - 1])
```

**Expected output:**

```
6
n
```

Ask for an index that does not exist and Python stops you:

```python
word = "Python"
print(word[6])
```

**Expected output:**

```
IndexError: string index out of range
```

A six-character string has indexes 0 to 5. There is no 6.

> **Careful**: The last valid index is always `len(word) - 1`, never `len(word)`. This off-by-one is the most common indexing mistake there is, and it will bite you again in Class 9 with lists.

### Looping through characters

You met this in Class 6. Both of these work, and the first is better:

```python
word = "Python"

for letter in word:
    print(letter, end=" ")

print()

for i in range(len(word)):
    print(f"{i}:{word[i]}", end=" ")

print()
```

**Expected output:**

```
P y t h o n 
0:P 1:y 2:t 3:h 4:o 5:n 
```

Use the first form when you only need the characters. Use the second when you need the **position** as well.

---

## 8.2 Slicing — Cutting Out a Section

Slicing takes a **piece** of a string. The syntax is `text[start:stop]`.

```python
word = "Programming"

print(word[0:7])
print(word[7:11])
print(word[3:6])
```

**Expected output:**

```
Program
ming
gra
```

The rule is the same as `range()`: **start is included, stop is excluded**. `word[0:7]` gives characters 0, 1, 2, 3, 4, 5, 6 — seven characters, stopping just before index 7.

### Leaving parts out

```python
word = "Programming"

print(word[:7])
print(word[7:])
print(word[:])
```

**Expected output:**

```
Program
ming
Programming
```

- Leave out the **start** and it begins at 0
- Leave out the **stop** and it runs to the end
- Leave out both and you get the whole string

`text[:n]` reads as "the first n characters" and `text[n:]` as "everything from n onwards". Both are extremely common.

### Negative slicing

```python
word = "Programming"

print(word[-4:])
print(word[:-4])
print(word[-7:-4])
```

**Expected output:**

```
ming
Program
ram
```

`word[-4:]` is "the last four characters" — a genuinely useful idiom.

### The step, and reversing a string

Slicing takes a third value, exactly like `range()`:

```python
word = "Programming"

print(word[::2])
print(word[::-1])
```

**Expected output:**

```
Pormig
gnimmargorP
```

`[::-1]` steps backwards through the whole string, which **reverses** it. It looks cryptic the first time and then you use it forever. It is how you test for a palindrome.

> **Tip**: Slicing never raises an `IndexError`. `"Python"[0:100]` quietly gives you `"Python"` rather than crashing. Indexing is strict; slicing is forgiving.

---

## 8.3 String Methods

A **method** is a function that belongs to a value. You call it by writing a dot after the value: `text.upper()`.

### Changing case

```python
name = "sita SHARMA"

print(name.upper())
print(name.lower())
print(name.title())
print(name.capitalize())
```

**Expected output:**

```
SITA SHARMA
sita sharma
Sita Sharma
Sita sharma
```

`.lower()` is the standard trick for comparing input case-insensitively:

```python
answer = "YES"

if answer.lower() == "yes":
    print("The user agreed.")
```

**Expected output:**

```
The user agreed.
```

Without `.lower()`, a user typing `Yes` or `YES` would be rejected. The Quiz Game uses `.upper()` on the player's answer for exactly this reason.

### Cleaning up whitespace

```python
messy = "   Triton College   "

print(f"[{messy}]")
print(f"[{messy.strip()}]")
print(f"[{messy.lstrip()}]")
print(f"[{messy.rstrip()}]")
```

**Expected output:**

```
[   Triton College   ]
[Triton College]
[Triton College   ]
[   Triton College]
```

`.strip()` removes spaces, tabs and newlines from **both ends** — never from the middle. Users type stray spaces constantly, so `input().strip()` is worth making a habit.

### Searching

```python
sentence = "Physics is the best subject"

print(sentence.find("best"))
print(sentence.find("Chemistry"))
print(sentence.count("s"))
print(sentence.startswith("Physics"))
print(sentence.endswith("subject"))
```

**Expected output:**

```
15
-1
5
True
True
```

`.find()` returns the index where the text starts, or **`-1`** if it is not there at all. That `-1` is how you test for absence — and it is exactly how the Quiz Game checks whether the player typed a valid option letter.

The `in` keyword is simpler when you only need yes or no:

```python
sentence = "Physics is the best subject"

print("best" in sentence)
print("Chemistry" in sentence)
print("chemistry" in sentence.lower())
```

**Expected output:**

```
True
False
False
```

### Replacing

```python
sentence = "Physics is hard. Physics is interesting."

print(sentence.replace("Physics", "Chemistry"))
print(sentence.replace("Physics", "Chemistry", 1))
```

**Expected output:**

```
Chemistry is hard. Chemistry is interesting.
Chemistry is hard. Physics is interesting.
```

`.replace()` changes **every** occurrence unless you give it a limit.

### Splitting and joining

`.split()` breaks a string into a **list** of pieces. Lists are Class 9's subject, but you need this now.

```python
subjects = "Physics,Chemistry,Biology,Maths"
parts = subjects.split(",")
print(parts)
print(len(parts))
print(parts[0])
```

**Expected output:**

```
['Physics', 'Chemistry', 'Biology', 'Maths']
4
Physics
```

With no argument, `.split()` breaks on whitespace — the easiest way to count words:

```python
sentence = "Python is a very readable language"
words = sentence.split()
print(words)
print(f"Word count: {len(words)}")
```

**Expected output:**

```
['Python', 'is', 'a', 'very', 'readable', 'language']
Word count: 6
```

`.join()` is the exact opposite — it glues a list back into one string, using whatever you put in front of it as the separator:

```python
subjects = ["Physics", "Chemistry", "Biology"]

print(", ".join(subjects))
print(" | ".join(subjects))
print("-".join("ABC"))
```

**Expected output:**

```
Physics, Chemistry, Biology
Physics | Chemistry | Biology
A-B-C
```

The separator goes **before** the dot, which looks backwards until you read it as "join these with this".

### Checking content

```python
print("12345".isdigit())
print("12a45".isdigit())
print("Sita".isalpha())
print("".isdigit())
```

**Expected output:**

```
True
False
True
False
```

`.isdigit()` is a gentle way to check a number before converting it, without needing `try` / `except` yet:

```python
typed = "87"

if typed.isdigit():
    marks = int(typed)
    print(f"Marks: {marks}")
else:
    print("That was not a whole number.")
```

**Expected output:**

```
Marks: 87
```

### The methods worth remembering

| Method | Does | Example → result |
|--------|------|------------------|
| `.upper()` / `.lower()` | Change case | `"abc".upper()` → `"ABC"` |
| `.title()` | Capitalise each word | `"sita sharma".title()` → `"Sita Sharma"` |
| `.strip()` | Remove whitespace at both ends | `" hi ".strip()` → `"hi"` |
| `.find(x)` | Index of `x`, or `-1` | `"abc".find("c")` → `2` |
| `.count(x)` | How many times `x` appears | `"banana".count("a")` → `3` |
| `.replace(a, b)` | Swap `a` for `b` | `"a-b".replace("-", "+")` → `"a+b"` |
| `.split(sep)` | Break into a list | `"a,b".split(",")` → `["a", "b"]` |
| `.join(list)` | Glue a list together | `"-".join(["a","b"])` → `"a-b"` |
| `.startswith(x)` | Does it begin with `x`? | `"Physics".startswith("P")` → `True` |
| `.isdigit()` | Is it all digits? | `"42".isdigit()` → `True` |

---

## 8.4 Strings Are Immutable

You cannot change a character inside a string.

```python
word = "Python"
word[0] = "J"
```

**Expected output:**

```
TypeError: 'str' object does not support item assignment
```

Strings are **immutable** — fixed once created. Every method you just met returns a **new** string and leaves the original alone:

```python
name = "sita"
name.upper()
print(name)
```

**Expected output:**

```
sita
```

Nothing changed. `.upper()` produced `"SITA"` and then threw it away, because nothing caught it. You must assign the result:

```python
name = "sita"
name = name.upper()
print(name)
```

**Expected output:**

```
SITA
```

> **Common error**: Calling a string method and wondering why nothing happened is one of the most frequent beginner bugs. **String methods return a new value; they never modify the original.** If you want to keep the result, store it.

To change one character, build a new string with slicing:

```python
word = "Python"
word = "J" + word[1:]
print(word)
```

**Expected output:**

```
Jython
```

---

## 8.5 Formatting Text Neatly

f-strings can pad a value to a fixed width, which is how you line up columns without counting spaces by hand.

```python
subjects = "Physics"
marks = 82

print(f"{subjects:<15}{marks:>5}")
print(f"{'Chemistry':<15}{76:>5}")
print(f"{'Biology':<15}{91:>5}")
```

**Expected output:**

```
Physics           82
Chemistry         76
Biology           91
```

| Code | Means |
|------|-------|
| `:<15` | Left-aligned, 15 characters wide |
| `:>5` | Right-aligned, 5 characters wide |
| `:^20` | Centred, 20 characters wide |

Numbers read best right-aligned, text left-aligned. The Quiz Game's high-score table uses `{name:<14}` for exactly this.

```python
print(f"{'RESULT':^30}")
print("=" * 30)
```

**Expected output:**

```
            RESULT            
==============================
```

---

## 8.6 Putting It All Together

Create `text_analyser.py`:

```python
# text_analyser.py
# Analyses a sentence typed by the user.

print("=" * 48)
print(f"{'TEXT ANALYSER':^48}")
print("=" * 48)

sentence = input("\nType a sentence: ").strip()

if not sentence:
    sentence = "Python makes text easy to handle"
    print(f"Nothing typed — using: {sentence}")

# --- Basic measurements ---
words = sentence.split()
no_spaces = sentence.replace(" ", "")

# --- Count vowels with a loop ---
vowels = 0
consonants = 0

for letter in sentence.lower():
    if letter.isalpha():
        if letter in "aeiou":
            vowels += 1
        else:
            consonants += 1

# --- Palindrome test ---
cleaned = sentence.lower().replace(" ", "")
is_palindrome = cleaned == cleaned[::-1]

# --- Longest word ---
longest = ""
for word in words:
    if len(word) > len(longest):
        longest = word

print()
print("-" * 48)
print(f"{'Original':<20}{sentence}")
print(f"{'Upper case':<20}{sentence.upper()}")
print(f"{'Reversed':<20}{sentence[::-1]}")
print(f"{'First 10 chars':<20}{sentence[:10]}")
print(f"{'Last 10 chars':<20}{sentence[-10:]}")
print("-" * 48)
print(f"{'Characters':<20}{len(sentence)}")
print(f"{'Without spaces':<20}{len(no_spaces)}")
print(f"{'Words':<20}{len(words)}")
print(f"{'Vowels':<20}{vowels}")
print(f"{'Consonants':<20}{consonants}")
print(f"{'Longest word':<20}{longest} ({len(longest)} letters)")
print(f"{'Palindrome':<20}{is_palindrome}")
print("-" * 48)

print("\nWords, one per line:")
for position in range(len(words)):
    print(f"  {position + 1}. {words[position]}")

print(f"\nRejoined with dashes: {'-'.join(words)}")
```

**Sample run:**

```
================================================
                 TEXT ANALYSER                  
================================================

Type a sentence: Physics is the best subject

------------------------------------------------
Original            Physics is the best subject
Upper case          PHYSICS IS THE BEST SUBJECT
Reversed            tcejbus tseb eht si scisyhP
First 10 chars      Physics is
Last 10 chars       st subject
------------------------------------------------
Characters          27
Without spaces      23
Words               5
Vowels              6
Consonants          17
Longest word        Physics (7 letters)
Palindrome          False
------------------------------------------------

Words, one per line:
  1. Physics
  2. is
  3. the
  4. best
  5. subject

Rejoined with dashes: Physics-is-the-best-subject
```

Notice `if letter in "aeiou"` — `in` checks whether one string appears inside another, so this is a neat way to ask "is this a vowel?" without listing five separate comparisons.

Look carefully at the longest word. Both `Physics` and `subject` have seven letters, and the program reported `Physics` — the one it met **first**. That is because the test is `len(word) > len(longest)`, and seven is not greater than seven, so `subject` never displaced it. Change the `>` to `>=` and the answer becomes `subject`, because now every tie replaces the previous holder. Neither is wrong; you just have to decide which you meant.

> **Try it**: Run it with `Madam` and then with `A man a plan a canal Panama`. Both should report `True` for palindrome. Why does the `.replace(" ", "")` matter for the second one?

---

## Practice Exercises

1. **Initials generator** — Ask for a full name such as `Sita Devi Sharma` and print the initials as `S.D.S.`. Use `.split()`, a loop, and indexing to take the first letter of each word. Make it work whether the user types two names or four.

2. **Email validator** — Ask for an email address and check it looks plausible: it contains exactly one `@`, it has at least one `.` after the `@`, and it does not start or end with `@`. Use `.count()`, `.find()` and slicing. Print a clear message for each failure.

3. **Word frequency** — Ask for a sentence and a word, then report how many times that word appears, ignoring case. Try it on `The cat sat on the mat` searching for `the` — you should get 2. Why does `.count()` on the raw sentence give the wrong answer here?

4. **Marks table** — You are given `data = "Physics:82,Chemistry:76,Biology:91,Maths:88"`. Using `.split()` twice and f-string alignment, print a neat two-column table of subject and marks, then the total. You will need to split on `,` first and then on `:`.

---

## Key Takeaways

- **Indexing** starts at 0. `text[0]` is the first character; `text[-1]` is the last. The last valid index is `len(text) - 1`.
- **Slicing** is `text[start:stop:step]` — start included, stop **excluded**. Leave either out for "from the beginning" or "to the end".
- **`text[::-1]`** reverses a string.
- Indexing raises `IndexError` when out of range; **slicing never does**.
- The essential methods: `.upper()`, `.lower()`, `.strip()`, `.find()`, `.count()`, `.replace()`, `.split()`, `.join()`, `.startswith()`, `.isdigit()`.
- **`.find()` returns `-1`** when the text is not present. `in` is simpler when you only need `True`/`False`.
- **Strings are immutable.** Methods return a **new** string — you must assign the result or it is lost.
- **`.lower()`** on both sides makes a comparison case-insensitive.
- f-string alignment (`:<15`, `:>5`, `:^20`) lines up columns without counting spaces.

Next class we will meet **lists** — collections that, unlike strings, you *can* change, and which finally let us store all those marks instead of overwriting them.
