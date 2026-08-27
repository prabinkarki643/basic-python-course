# Class 7: Loops Part 2 — `while`, `break` and `continue`

> **Time budget**: 45 minutes (≈ 32 min teach + 13 min practice)
> **Prerequisites**: Class 6 (Loops Part 1 — `for` and `range()`)

A `for` loop is perfect when you know how many times to repeat. But how many guesses will a player need? How many times will a user type an invalid answer? You cannot know. Today we meet the loop that runs until something becomes true.

## What You Will Learn

- The **`while`** loop, and when to choose it over `for`
- **Infinite loops** — how to cause one, and how to escape
- **`break`** to leave a loop early and **`continue`** to skip one turn
- The **`while True`** pattern for validating user input
- **Nested loops** for printing patterns

---

## 7.1 The `while` Loop

A `while` loop repeats **as long as a condition stays true**.

```python
count = 1

while count <= 5:
    print(count)
    count += 1

print("Done.")
```

**Expected output:**

```
1
2
3
4
5
Done.
```

Here is the cycle Python follows:

1. Check the condition `count <= 5`
2. If `True`, run the body
3. Go back to step 1
4. If `False`, skip the body and carry on after the loop

### `for` versus `while`

| Use a `for` loop when | Use a `while` loop when |
|-----------------------|-------------------------|
| You know how many times | You do not know how many times |
| You are walking through a collection | You are waiting for a condition to change |
| Counting to a fixed number | Repeating until the user says stop |
| `for i in range(10):` | `while not finished:` |

The loop above is better written as a `for` — the count is known. `while` earns its place when the number of repetitions depends on something that happens *during* the loop.

```python
balance = 10000
year = 0

while balance < 20000:
    balance *= 1.08
    year += 1

print(f"Balance passed Rs. 20,000 in year {year} (Rs. {balance:.2f})")
```

**Expected output:**

```
Balance passed Rs. 20,000 in year 10 (Rs. 21589.25)
```

Nobody knew it would take ten years until the loop ran. That is a `while` loop doing something a `for` loop cannot do cleanly.

---

## 7.2 Infinite Loops

If the condition never becomes false, the loop never stops.

```python
count = 1

while count <= 5:
    print(count)
```

There is no `count += 1`, so `count` stays 1 forever. This prints `1` until you stop it.

**To stop a runaway program, press `Ctrl + C` in the terminal.** Learn that now — you will need it today.

Every `while` loop needs three things. Miss any one and it runs forever:

1. A variable **set up before** the loop
2. A **condition** that can become false
3. Something **inside the body that changes** the variable

```python
count = 1              # 1. set up
while count <= 5:      # 2. condition that can end
    print(count)
    count += 1         # 3. change — without this it never ends
```

> **Common error**: Ninety per cent of accidental infinite loops are a missing `count += 1`. Before running a `while` loop, find the line that moves the condition towards being false. If you cannot find it, you have not written it.

---

## 7.3 `break` — Leaving Early

`break` stops the loop immediately, wherever you are in it.

```python
for number in range(1, 11):
    if number == 6:
        break
    print(number)

print("Stopped.")
```

**Expected output:**

```
1
2
3
4
5
Stopped.
```

When `number` reached 6, `break` fired and the loop ended. The numbers 6 to 10 were never printed, and the `print(number)` for 6 never ran.

`break` works in `for` loops and `while` loops alike. It is how you stop searching once you have found what you were looking for:

```python
target = 37
found_at = 0

for number in range(1, 101):
    if number * number > target:
        found_at = number
        break

print(f"The first number whose square exceeds {target} is {found_at}.")
```

**Expected output:**

```
The first number whose square exceeds 37 is 7.
```

Without `break` the loop would grind through all 100 numbers pointlessly, and `found_at` would end up as 100.

---

## 7.4 `continue` — Skipping One Turn

`continue` skips the **rest of the current turn** and jumps straight to the next one. The loop carries on.

```python
for number in range(1, 11):
    if number % 2 == 0:
        continue
    print(number)
```

**Expected output:**

```
1
3
5
7
9
```

For each even number, `continue` fired and the `print` was skipped. The loop did not stop — it simply moved on.

| Keyword | Effect |
|---------|--------|
| `break` | Leave the loop entirely. Nothing more runs. |
| `continue` | Abandon this turn only. Go straight to the next one. |

> **Careful**: `continue` inside a `while` loop is dangerous if the line that updates your counter comes *after* it. The `continue` skips the update, the condition never changes, and you have an infinite loop. In a `while` loop, update the counter **before** any `continue`.

---

## 7.5 The `while True` Pattern

This is the most useful pattern in today's class, and it is exactly how the Quiz Game refuses to accept a bad answer.

`while True:` is deliberately infinite — the condition is the literal value `True`, which never changes. You escape with `break`.

```python
while True:
    answer = input("Type 'yes' to continue: ")

    if answer == "yes":
        break

    print("That was not 'yes'. Try again.")

print("Thank you.")
```

**Sample run:**

```
Type 'yes' to continue: no
That was not 'yes'. Try again.
Type 'yes' to continue: maybe
That was not 'yes'. Try again.
Type 'yes' to continue: yes
Thank you.
```

The loop keeps asking until the user gets it right. You could not write this with a `for` loop, because you have no idea how many attempts they will need.

### Validating a number in a range

```python
while True:
    marks = float(input("Enter marks (0-100): "))

    if 0 <= marks <= 100:
        break

    print("Marks must be between 0 and 100.")

print(f"Accepted: {marks}")
```

**Sample run:**

```
Enter marks (0-100): 150
Marks must be between 0 and 100.
Enter marks (0-100): -20
Marks must be between 0 and 100.
Enter marks (0-100): 87
Accepted: 87.0
```

There is the chained comparison from Class 4, guarding real input.

> **Tip**: A `while True` loop with no `break` anywhere inside it is always a bug. When you type `while True:`, immediately type the `break` line as well, then fill in the middle.

### A menu

```python
while True:
    print("\n1. Say hello")
    print("2. Say goodbye")
    print("3. Quit")

    choice = input("Choose: ")

    if choice == "1":
        print("Hello!")
    elif choice == "2":
        print("Goodbye!")
    elif choice == "3":
        print("Closing.")
        break
    else:
        print("Not a valid choice.")
```

**Sample run:**

```

1. Say hello
2. Say goodbye
3. Quit
Choose: 1
Hello!

1. Say hello
2. Say goodbye
3. Quit
Choose: 3
Closing.
```

Compare `choice` with `"1"` in quotes, not `1`. Remember Class 3 — `input()` always gives a string.

---

## 7.6 Nested Loops

A loop inside a loop. The inner one runs completely for every single turn of the outer one.

```python
for i in range(1, 4):
    for j in range(1, 4):
        print(f"i={i}, j={j}")
    print("--- outer turn finished ---")
```

**Expected output:**

```
i=1, j=1
i=1, j=2
i=1, j=3
--- outer turn finished ---
i=2, j=1
i=2, j=2
i=2, j=3
--- outer turn finished ---
i=3, j=1
i=3, j=2
i=3, j=3
--- outer turn finished ---
```

Three outer turns × three inner turns = nine lines. The inner loop restarts from the beginning each time.

### Patterns

Nested loops are how you print shapes. The `end=""` argument tells `print` **not** to start a new line, so the stars build up along one row.

```python
for row in range(1, 6):
    for star in range(row):
        print("*", end="")
    print()
```

**Expected output:**

```
*
**
***
****
*****
```

Row 1 prints one star, row 2 prints two, and so on, because the inner `range(row)` gets bigger each time. The bare `print()` after the inner loop ends the line.

### A full multiplication grid

```python
for row in range(1, 6):
    for column in range(1, 6):
        product = row * column
        print(f"{product:4}", end="")
    print()
```

**Expected output:**

```
   1   2   3   4   5
   2   4   6   8  10
   3   6   9  12  15
   4   8  12  16  20
   5  10  15  20  25
```

`{product:4}` pads each number to four characters wide, which is what keeps the columns lined up. That is the same f-string formatting idea as `:.2f`, applied to width instead of decimals.

---

## 7.7 Putting It All Together

Create `number_guessing_game.py`. This is a real game, and it uses almost everything from the last three classes.

```python
# number_guessing_game.py
# The computer picks a number and you try to guess it.

SECRET = 42
MAX_GUESSES = 5

print("=" * 44)
print("NUMBER GUESSING GAME")
print("=" * 44)
print(f"\nI am thinking of a number between 1 and 100.")
print(f"You have {MAX_GUESSES} guesses.")

guesses_used = 0
has_won = False

while guesses_used < MAX_GUESSES:
    guesses_used += 1
    remaining = MAX_GUESSES - guesses_used

    guess = int(input(f"\nGuess {guesses_used}: "))

    if guess < 1 or guess > 100:
        print("That is outside 1 to 100 — that guess was wasted.")
        continue

    if guess == SECRET:
        has_won = True
        break

    if guess < SECRET:
        print("Too low.")
    else:
        print("Too high.")

    if remaining > 0:
        print(f"{remaining} guesses left.")

print()
print("-" * 44)

if has_won:
    print(f"Correct! The number was {SECRET}.")
    print(f"You found it in {guesses_used} guesses.")

    if guesses_used == 1:
        print("Extraordinary luck.")
    elif guesses_used <= 3:
        print("Excellent guessing.")
    else:
        print("You got there in the end.")
else:
    print(f"Out of guesses. The number was {SECRET}.")

print("-" * 44)
```

**Sample run:**

```
============================================
NUMBER GUESSING GAME
============================================

I am thinking of a number between 1 and 100.
You have 5 guesses.

Guess 1: 50
Too high.
4 guesses left.

Guess 2: 25
Too low.
3 guesses left.

Guess 3: 37
Too low.
2 guesses left.

Guess 4: 43
Too high.
1 guesses left.

Guess 5: 42

--------------------------------------------
Correct! The number was 42.
You found it in 5 guesses.
You got there in the end.
--------------------------------------------
```

Three things worth studying:

- `guesses_used += 1` comes **before** the `continue`. If it came after, an out-of-range guess would skip the increment and the loop would run forever.
- `has_won` is a `bool` flag set up before the loop. After the loop ends we cannot tell *why* it ended — the flag remembers for us. This is a standard and very useful trick.
- `SECRET` is in capitals because it never changes, following the convention from Class 2.

In Class 12 you will replace `SECRET = 42` with `random.randint(1, 100)` and the game becomes genuinely unpredictable.

---

## Practice Exercises

1. **Sum until zero** — Keep asking the user for numbers and adding them to a running total. When they enter `0`, stop and print the total and how many numbers they entered. Which loop type is right here, and why could you not use a `for`?

2. **Password retry** — Set `PASSWORD = "triton123"`. Give the user three attempts to type it. Print "Access granted" on success and "Account locked" after three failures. Use a `while` loop, a counter and `break`.

3. **Multiplication table grid** — Using nested loops, print the full 10 × 10 multiplication table with columns lined up, and a header row of numbers 1 to 10 across the top. You will need `end=""` and width formatting like `{value:4}`.

4. **Trace the output** — Work out what this prints *before* you run it, then check. Explain in one sentence why 3 and 7 are treated differently:

   ```python
   for n in range(1, 11):
       if n == 3:
           continue
       if n == 7:
           break
       print(n)
   ```

---

## Key Takeaways

- **`while condition:`** repeats for as long as the condition stays true — use it when you do not know the number of repetitions in advance.
- Every `while` loop needs a variable **set up before**, a condition that **can** become false, and a **change inside** the body. Miss the change and it runs forever.
- **`Ctrl + C`** stops a runaway program.
- **`break`** leaves the loop immediately; **`continue`** skips the rest of this turn only.
- In a `while` loop, update your counter **before** any `continue`, or you will loop forever.
- **`while True:` … `break`** is the standard pattern for validating user input. Always write the `break` at the same time as the `while True`.
- **Nested loops** run the inner loop completely for each turn of the outer one — the basis of grids and patterns.
- **`print("x", end="")`** prints without moving to a new line.
- A **`bool` flag** set before the loop lets you remember afterwards why the loop ended.

Next class we will look properly at **strings** — slicing them, searching them, and transforming them with Python's built-in string methods.
