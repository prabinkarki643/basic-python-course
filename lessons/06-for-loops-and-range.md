# Class 6: Loops Part 1 — `for` and `range()`

> **Time budget**: 45 minutes (≈ 32 min teach + 13 min practice)
> **Prerequisites**: Class 5 (Making Decisions)

Computers are extraordinarily good at doing the same thing thousands of times without getting bored. Today you learn how to ask them to. This is the single biggest jump in power you will make on this course.

## What You Will Learn

- What a **loop** is and why repetition is the point of programming
- The **`for`** loop and how it walks through a collection
- **`range()`** in all three of its forms
- The **accumulator pattern** — building up a total inside a loop
- Combining a loop with an `if` to count and filter

---

## 6.1 Why Loops Exist

Print the numbers 1 to 5 with what you know so far:

```python
print(1)
print(2)
print(3)
print(4)
print(5)
```

Tedious, but manageable. Now print 1 to 1000. You are not typing a thousand lines, and if you did, changing the format would mean editing all thousand.

A **loop** runs the same block of code repeatedly:

```python
for number in range(1, 6):
    print(number)
```

**Expected output:**

```
1
2
3
4
5
```

Two lines. Change `6` to `1001` and it prints a thousand numbers. That is the whole argument for loops.

> **Analogy**: A loop is a running track. You run the same lap over and over, and something changes each time round — the lap counter. When the counter reaches its limit, you stop and walk off.

---

## 6.2 The `for` Loop

```python
for number in range(1, 6):
    print(number)
```

| Piece | What it does |
|-------|--------------|
| `for` | Starts the loop |
| `number` | The **loop variable** — holds a different value each time round |
| `in` | Keyword joining the variable to the thing being walked through |
| `range(1, 6)` | The collection of values to walk through |
| `:` | Required, exactly as with `if` |
| indented block | The **body** — runs once per value |

The loop variable is created by the loop and updated automatically. You do not set it yourself. You can name it anything — `number`, `i`, `student`, `mark` — and a descriptive name is always better than `i`.

### Looping over a string

`range()` is not the only thing a `for` loop can walk through. Any collection works, and a string is a collection of characters:

```python
for letter in "PYTHON":
    print(letter)
```

**Expected output:**

```
P
Y
T
H
O
N
```

The loop ran six times because the string has six characters. This is why a `for` loop is sometimes called a "for-each" loop — it does something *for each* item.

### The body can be several lines

```python
for number in range(1, 4):
    print(f"Number: {number}")
    print(f"Squared: {number ** 2}")
    print("-" * 15)
```

**Expected output:**

```
Number: 1
Squared: 1
---------------
Number: 2
Squared: 4
---------------
Number: 3
Squared: 9
---------------
```

All three lines are indented, so all three run each time round. As with `if`, indentation decides what belongs to the loop.

---

## 6.3 `range()` in Detail

`range()` generates a sequence of whole numbers. It takes one, two or three arguments.

### One argument — `range(stop)`

Starts at **0** and stops **before** the number you give.

```python
for i in range(5):
    print(i)
```

**Expected output:**

```
0
1
2
3
4
```

Five numbers, but they run 0 to 4. `range(5)` means "five values starting from zero", not "up to five".

> **Careful**: `range(5)` never produces 5. The end value is always **excluded**. This trips up every beginner at least once, and it is deliberate — it makes `range(len(something))` line up perfectly with positions in a list, which you will see in Class 9.

### Two arguments — `range(start, stop)`

```python
for i in range(1, 6):
    print(i)
```

**Expected output:**

```
1
2
3
4
5
```

Starts at `start`, stops **before** `stop`. To count 1 to 5, write `range(1, 6)`.

### Three arguments — `range(start, stop, step)`

The third argument is how much to jump each time.

```python
for i in range(0, 21, 5):
    print(i)
```

**Expected output:**

```
0
5
10
15
20
```

A negative step counts **backwards**:

```python
for i in range(10, 0, -1):
    print(i)

print("Lift off!")
```

**Expected output:**

```
10
9
8
7
6
5
4
3
2
1
Lift off!
```

To count down to 1, stop at `0` — because the stop value is excluded either way.

### A summary

| Written as | Produces | Notes |
|-----------|----------|-------|
| `range(5)` | 0, 1, 2, 3, 4 | Starts at 0 |
| `range(1, 6)` | 1, 2, 3, 4, 5 | Stop is excluded |
| `range(0, 21, 5)` | 0, 5, 10, 15, 20 | Steps of 5 |
| `range(10, 0, -1)` | 10, 9, ... 1 | Counts down |
| `range(2, 11, 2)` | 2, 4, 6, 8, 10 | Even numbers |

> **Tip**: `range()` does not build the whole list in memory. `range(1000000)` is instant and takes almost no space, because it works the numbers out one at a time as the loop asks for them.

---

## 6.4 The Accumulator Pattern

This is the most important pattern in this class. You will use it in every program you write from now on, including the Quiz Game's scoring.

The idea: create a variable **before** the loop, then update it **inside** the loop.

### Adding up

```python
total = 0

for number in range(1, 11):
    total += number

print(f"Sum of 1 to 10 = {total}")
```

**Expected output:**

```
Sum of 1 to 10 = 55
```

Follow the value of `total`: it starts at 0, then becomes 1, 3, 6, 10, 15, 21, 28, 36, 45, 55. Each time round the loop it grows by the current number.

The two rules that make it work:

1. **Set the starting value before the loop.** Put `total = 0` inside the loop and it resets to zero every time round, so the answer is always the last number.
2. **Use `+=` inside the loop.** Plain `=` would overwrite rather than add.

### Counting

To count things rather than add them, add 1 each time instead:

```python
count = 0

for number in range(1, 21):
    if number % 3 == 0:
        count += 1

print(f"Multiples of 3 between 1 and 20: {count}")
```

**Expected output:**

```
Multiples of 3 between 1 and 20: 6
```

There is the `if`-inside-a-loop combination — the loop visits every number, the `if` decides which ones count. This is precisely how the Quiz Game counts correct answers.

### Multiplying — the factorial

For multiplying, start at **1**, not 0. Anything multiplied by zero stays zero.

```python
number = 5
factorial = 1

for i in range(1, number + 1):
    factorial *= i

print(f"{number}! = {factorial}")
```

**Expected output:**

```
5! = 120
```

`range(1, number + 1)` gives 1, 2, 3, 4, 5. The `+ 1` is there because the stop value is excluded — a correction you will write constantly.

### Finding the largest

Start with the first value, then replace it whenever you meet something bigger:

```python
marks = 0

for value in range(1, 8):
    current = value * 13 % 97
    if current > marks:
        marks = current

print(f"Largest value found: {marks}")
```

**Expected output:**

```
Largest value found: 91
```

Class 9 gives you `max()` to do this in one word, but knowing the manual version means you can adapt it — for instance, to find the largest value that is also even.

---

## 6.5 Putting It All Together

Create `marks_analyser.py`:

```python
# marks_analyser.py
# Reads marks for a whole class and reports on them.

print("=" * 44)
print("CLASS MARKS ANALYSER")
print("=" * 44)

student_count = int(input("\nHow many students? "))

total = 0
passed = 0
failed = 0
highest = 0

for student_number in range(1, student_count + 1):
    marks = float(input(f"Marks for student {student_number}: "))

    total += marks

    if marks >= 40:
        passed += 1
    else:
        failed += 1

    if marks > highest:
        highest = marks

average = total / student_count

print()
print("-" * 44)
print(f"Students entered: {student_count}")
print(f"Total marks:      {total:.1f}")
print(f"Class average:    {average:.2f}")
print(f"Highest mark:     {highest:.1f}")
print(f"Passed:           {passed}")
print(f"Failed:           {failed}")
print(f"Pass rate:        {passed / student_count * 100:.1f}%")
print("-" * 44)

print("\nMarks bar chart:")
for student_number in range(1, student_count + 1):
    print(f"Student {student_number}")
```

**Sample run:**

```
============================================
CLASS MARKS ANALYSER
============================================

How many students? 5
Marks for student 1: 82
Marks for student 2: 35
Marks for student 3: 91
Marks for student 4: 67
Marks for student 5: 28

--------------------------------------------
Students entered: 5
Total marks:      303.0
Class average:    60.60
Highest mark:     91.0
Passed:           3
Failed:           2
Pass rate:        60.0%
--------------------------------------------

Marks bar chart:
Student 1
Student 2
Student 3
Student 4
Student 5
```

Four accumulators run side by side in one loop — `total` adds, `passed` and `failed` count, and `highest` tracks a maximum. All four are set up before the loop and updated inside it.

The bar chart at the bottom is deliberately incomplete. It cannot draw real bars yet, because we did not store the individual marks — each new `marks` value overwrote the last. **Class 9 introduces lists**, which fix exactly this, and you will come back and finish this program.

> **Try it**: Run it with 1 student. Does the pass rate still work? Now try 0 students — what happens, and can you see why?

---

## Practice Exercises

1. **Multiplication table** — Ask for a number and print its table from 1 to 10, formatted as `7 x 3 = 21`. Then extend it: ask for the number *and* how far to go, so the user can ask for the 7 times table up to 20.

2. **Sum of even numbers** — Using a single loop, print the sum of all even numbers from 1 to 100. Do it twice: once with `range(1, 101)` and an `if`, and once with `range(2, 101, 2)` and no `if` at all. Both should give 2550. Which version do you find clearer, and why?

3. **Countdown with a twist** — Print a countdown from 10 to 1, but replace every multiple of 3 with the word `FIZZ`. Your output should start `10, FIZZ, 8, 7, FIZZ, 5, ...`. You will need a loop, an `if`/`else` and `%`.

4. **Compound interest** — A student deposits Rs. 10,000 at 8% interest per year. Using a loop, print the balance at the end of each year for 10 years, to two decimal places. Each year the balance becomes `balance * 1.08`. In which year does it first pass Rs. 20,000?

---

## Key Takeaways

- A **loop** repeats a block of code, so you write it once and run it many times.
- **`for variable in collection:`** runs the body once per item, updating the loop variable automatically.
- A `for` loop can walk through a **`range()`** or a **string** — and, from Class 9, a list.
- **`range(stop)`** starts at 0; **`range(start, stop)`** starts where you say; **`range(start, stop, step)`** jumps. A negative step counts down.
- **The stop value is always excluded.** To include `n`, write `range(1, n + 1)`.
- The **accumulator pattern**: create the variable **before** the loop, update it **inside** with `+=`. Start at `0` for sums and counts, at `1` for products.
- An **`if` inside a loop** lets you count or filter — the loop visits everything, the `if` decides what matters.

Next class we will meet the **`while`** loop, for when you do not know in advance how many times you need to repeat — and learn to break out of a loop early.
