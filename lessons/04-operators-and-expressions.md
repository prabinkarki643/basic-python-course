# Class 4: Operators and Expressions — Doing the Maths

> **Time budget**: 45 minutes (≈ 32 min teach + 13 min practice)
> **Prerequisites**: Class 3 (Input, Output and Type Conversion)

You already know `+`, `-`, `*` and `/`. Today we complete the set — including two operators that have no equivalent on your calculator but turn out to be extraordinarily useful — and we learn the rules Python uses to decide what to work out first.

## What You Will Learn

- All seven **arithmetic operators**, including `//`, `%` and `**`
- Shortcut **assignment operators** such as `+=`
- **Comparison operators** and the `bool` values they produce
- The **logical operators** `and`, `or` and `not`
- **Operator precedence** — what Python calculates first, and how to override it

---

## 4.1 Arithmetic Operators

| Operator | Name | Example | Result |
|----------|------|---------|--------|
| `+` | Addition | `7 + 3` | `10` |
| `-` | Subtraction | `7 - 3` | `4` |
| `*` | Multiplication | `7 * 3` | `21` |
| `/` | Division | `7 / 3` | `2.3333333333333335` |
| `//` | Floor division | `7 // 3` | `2` |
| `%` | Modulus (remainder) | `7 % 3` | `1` |
| `**` | Exponent (power) | `7 ** 3` | `343` |

The first three behave exactly as you expect. The other four need a proper look.

```python
print(7 + 3)
print(7 - 3)
print(7 * 3)
print(7 / 3)
print(7 // 3)
print(7 % 3)
print(7 ** 3)
```

**Expected output:**

```
10
4
21
2.3333333333333335
2
1
343
```

---

## 4.2 The Two Divisions

Python has two division operators, and knowing which to reach for is a genuine skill.

### `/` — true division, always a float

```python
print(10 / 2)
print(10 / 3)
print(9 / 3)
```

**Expected output:**

```
5.0
3.3333333333333335
3.0
```

Look at `9 / 3`. Mathematically that is 3 exactly, but Python prints `3.0`. **`/` always produces a `float`**, no matter how neatly the division works out. This surprises everybody once.

### `//` — floor division, throws the fraction away

```python
print(10 // 3)
print(9 // 3)
print(7 // 2)
```

**Expected output:**

```
3
3
3
```

`//` divides and then discards everything after the decimal point. `10 // 3` is 3 remainder 1, and `//` gives you the 3.

It is called *floor* division because it always rounds **downwards**, which matters for negative numbers:

```python
print(-7 // 2)
print(-7 / 2)
```

**Expected output:**

```
-4
-3.5
```

`-3.5` rounded downwards is `-4`, not `-3`. Downwards means towards the more negative number, not towards zero.

> **Tip**: Use `//` when a fraction makes no sense. "How many full 6-seat benches do I need for 40 students?" is `40 // 6`, because two-thirds of a bench does not exist.

### `%` — the remainder, and why it is so useful

`%` — pronounced "modulus" or just "mod" — gives you what is **left over** after division.

```python
print(10 % 3)
print(9 % 3)
print(17 % 5)
print(20 % 4)
```

**Expected output:**

```
1
0
2
0
```

`//` and `%` are two halves of the same sum. For 17 ÷ 5: `17 // 5` is 3 (the whole part) and `17 % 5` is 2 (the leftover). Three fives and two left over.

Modulus solves three problems constantly:

**Is a number even or odd?** An even number divides by 2 with nothing left over.

```python
number = 24
print(number % 2)

number = 25
print(number % 2)
```

**Expected output:**

```
0
1
```

`% 2 == 0` means even. This is the standard test in every programming language there is.

**Is one number an exact multiple of another?**

```python
print(2024 % 4)
print(2023 % 4)
```

**Expected output:**

```
0
3
```

A remainder of `0` means yes. That is the first half of the leap-year rule you will implement next class.

**Splitting a total into units.** Turn 3,725 seconds into hours, minutes and seconds:

```python
total_seconds = 3725

hours = total_seconds // 3600
remaining = total_seconds % 3600
minutes = remaining // 60
seconds = remaining % 60

print(f"{total_seconds} seconds = {hours} h {minutes} min {seconds} s")
```

**Expected output:**

```
3725 seconds = 1 h 2 min 5 s
```

The same pattern converts paisa to rupees, or a number of days into weeks and days.

### `**` — powers

```python
print(2 ** 3)
print(5 ** 2)
print(9 ** 0.5)
print(2 ** 10)
```

**Expected output:**

```
8
25
3.0
1024
```

A power of `0.5` is a square root, so `9 ** 0.5` gives `3.0`. Class 12 introduces `math.sqrt()`, which says the same thing more clearly.

> **Careful**: `**` is the power operator, **not** `^`. In Python `^` is a bitwise operator and `5 ^ 2` gives `7`, which is not remotely what you wanted. This is one of the quietest bugs in this class, because it produces a number rather than an error.

---

## 4.3 Assignment Operators

You have already met `=`. Writing `total = total + 5` is so common that Python offers a shortcut for it.

```python
total = 100
total += 5       # same as: total = total + 5
print(total)

total -= 20      # same as: total = total - 20
print(total)

total *= 2       # same as: total = total * 2
print(total)

total /= 4       # same as: total = total / 4
print(total)
```

**Expected output:**

```
105
85
170
42.5
```

| Operator | Long form | Meaning |
|----------|-----------|---------|
| `+=` | `x = x + 5` | Add to it |
| `-=` | `x = x - 5` | Subtract from it |
| `*=` | `x = x * 5` | Multiply it |
| `/=` | `x = x / 5` | Divide it (gives a float) |
| `//=` | `x = x // 5` | Floor-divide it |
| `%=` | `x = x % 5` | Replace with the remainder |
| `**=` | `x = x ** 5` | Raise it to a power |

`+=` matters more than it looks. It is how you keep a running total inside a loop — the **accumulator pattern** — which is the backbone of Class 6 and of the Quiz Game's scoring.

```python
score = 0
score += 1
score += 1
score += 1
print(f"Score: {score}")
```

**Expected output:**

```
Score: 3
```

`+=` also works on strings, because `+` joins them:

```python
message = "Physics"
message += " and Chemistry"
print(message)
```

**Expected output:**

```
Physics and Chemistry
```

---

## 4.4 Comparison Operators

Comparisons ask a question and answer `True` or `False`. They always produce a `bool`.

| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| `==` | Is equal to | `5 == 5` | `True` |
| `!=` | Is not equal to | `5 != 3` | `True` |
| `>` | Greater than | `5 > 3` | `True` |
| `<` | Less than | `5 < 3` | `False` |
| `>=` | Greater than or equal to | `5 >= 5` | `True` |
| `<=` | Less than or equal to | `5 <= 3` | `False` |

```python
marks = 87

print(marks == 87)
print(marks != 87)
print(marks > 40)
print(marks < 40)
print(marks >= 87)
print(marks <= 86)
```

**Expected output:**

```
True
False
True
False
True
False
```

### `=` versus `==` — the classic mistake

This catches everyone, so say it out loud once:

- **`=`** assigns. `marks = 87` **puts** 87 into marks.
- **`==`** compares. `marks == 87` **asks** whether marks is 87.

> **Common error**: Using `=` where you meant `==` inside an `if` gives `SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?`. Python's error message is unusually helpful here — it guesses correctly almost every time.

### Comparing strings

Strings compare too. Equality is case-sensitive:

```python
print("Physics" == "Physics")
print("Physics" == "physics")
print("Physics" != "Chemistry")
```

**Expected output:**

```
True
False
True
```

`<` and `>` compare strings in dictionary order, which is how sorting a list of names works in Class 9:

```python
print("Aarya" < "Bibek")
print("Chemistry" > "Biology")
```

**Expected output:**

```
True
True
```

### Chaining comparisons

Python lets you write a range check the way Maths does. Most languages do not allow this.

```python
marks = 75

print(60 <= marks <= 80)
print(0 <= marks <= 100)
```

**Expected output:**

```
True
True
```

`60 <= marks <= 80` reads exactly like the Maths and means "marks is between 60 and 80 inclusive". The Quiz Game uses this to check a menu number is in range.

---

## 4.5 Logical Operators

Logical operators combine conditions. There are three.

| Operator | True when | Example |
|----------|-----------|---------|
| `and` | **Both** sides are true | `marks > 40 and attendance > 75` |
| `or` | **At least one** side is true | `is_holiday or is_sunday` |
| `not` | Flips true to false and back | `not is_absent` |

```python
physics = 82
chemistry = 76

print(physics > 40 and chemistry > 40)
print(physics > 90 and chemistry > 40)
print(physics > 90 or chemistry > 40)
print(physics > 90 or chemistry > 90)
print(not physics > 90)
```

**Expected output:**

```
True
False
True
False
True
```

Work through the third one: `physics > 90` is `False`, `chemistry > 40` is `True`. `False or True` is `True`, because `or` only needs one side.

### Truth tables

Worth memorising — they are identical to the logic in your Maths syllabus.

| A | B | `A and B` | `A or B` |
|---|---|-----------|----------|
| `True` | `True` | `True` | `True` |
| `True` | `False` | `False` | `True` |
| `False` | `True` | `False` | `True` |
| `False` | `False` | `False` | `False` |

### A realistic condition

```python
marks = 85
attendance = 80
fees_paid = True

eligible = marks >= 40 and attendance >= 75 and fees_paid
print(f"Eligible for the exam: {eligible}")
```

**Expected output:**

```
Eligible for the exam: True
```

Notice `fees_paid` is used on its own. It is already a `bool`, so writing `fees_paid == True` would be redundant. Say `if fees_paid`, not `if fees_paid == True` — it reads better and professionals will notice.

---

## 4.6 Operator Precedence

Python does not simply work left to right. It follows precedence rules — the same **BODMAS** idea you use in Maths.

```python
print(2 + 3 * 4)
print((2 + 3) * 4)
```

**Expected output:**

```
14
20
```

`*` binds more tightly than `+`, so `3 * 4` happens first. Brackets override everything.

From highest priority to lowest:

| Priority | Operators | Note |
|---------:|-----------|------|
| 1 | `()` | Brackets — always win |
| 2 | `**` | Powers |
| 3 | `*` `/` `//` `%` | Left to right among themselves |
| 4 | `+` `-` | Left to right among themselves |
| 5 | `==` `!=` `>` `<` `>=` `<=` | Comparisons |
| 6 | `not` | |
| 7 | `and` | |
| 8 | `or` | Lowest of all |

Two consequences worth knowing.

**Arithmetic happens before comparison**, so this needs no brackets:

```python
print(2 + 3 > 4)
```

**Expected output:**

```
True
```

`2 + 3` is worked out first, then `5 > 4` is asked.

**`and` binds more tightly than `or`**, which can genuinely bite:

```python
print(True or False and False)
print((True or False) and False)
```

**Expected output:**

```
True
False
```

The first line is `True or (False and False)` — Python did the `and` first.

> **Tip**: Do not memorise the whole table. Memorise brackets-then-power-then-multiply-then-add, and put brackets around anything else. `(a > 5) and (b < 10)` is not clumsy — it is clear, and nobody has ever been criticised for a bracket that removed doubt.

---

## 4.7 Putting It All Together

Create `physics_calculator.py`:

```python
# physics_calculator.py
# Works out motion values from user input using the equations of motion.

print("=" * 44)
print("PHYSICS CALCULATOR — EQUATIONS OF MOTION")
print("=" * 44)

initial_velocity = float(input("\nInitial velocity u (m/s): "))
acceleration = float(input("Acceleration a (m/s^2): "))
time = float(input("Time t (s): "))

# v = u + at
final_velocity = initial_velocity + acceleration * time

# s = ut + (1/2)at^2
distance = initial_velocity * time + 0.5 * acceleration * time ** 2

# Kinetic energy for a 1 kg mass: KE = (1/2)mv^2
kinetic_energy = 0.5 * 1 * final_velocity ** 2

print()
print("-" * 44)
print(f"Final velocity v = {final_velocity:.2f} m/s")
print(f"Distance      s = {distance:.2f} m")
print(f"KE (1 kg mass)  = {kinetic_energy:.2f} J")
print("-" * 44)

# --- Checks using comparison and logical operators ---
is_speeding_up = acceleration > 0
is_moving = final_velocity != 0
travelled_far = distance > 100

print()
print(f"Speeding up:      {is_speeding_up}")
print(f"Still moving:     {is_moving}")
print(f"Travelled > 100m: {travelled_far}")
print(f"Fast and far:     {final_velocity > 20 and travelled_far}")

# --- Splitting the time into minutes and seconds ---
whole_seconds = int(time)
minutes = whole_seconds // 60
seconds = whole_seconds % 60
print(f"\nTime {whole_seconds} s is {minutes} min {seconds} s.")
```

**Sample run:**

```
============================================
PHYSICS CALCULATOR — EQUATIONS OF MOTION
============================================

Initial velocity u (m/s): 5
Acceleration a (m/s^2): 2
Time t (s): 90

--------------------------------------------
Final velocity v = 185.00 m/s
Distance      s = 8550.00 m
KE (1 kg mass)  = 17112.50 J
--------------------------------------------

Speeding up:      True
Still moving:     True
Travelled > 100m: True
Fast and far:     True

Time 90 s is 1 min 30 s.
```

Note how `acceleration * time` is worked out before the `+` in the first formula, with no brackets needed — precedence does the right thing for free. And `time ** 2` happens before the `0.5 *`, because `**` outranks `*`.

---

## Practice Exercises

1. **Digit splitter** — Ask for a three-digit number. Using only `//` and `%`, print the hundreds, tens and units digits separately, then their sum. For 472 you should get 4, 7, 2 and a total of 13. Why does `472 // 100` give the hundreds digit?

2. **Predict then check** — Write down your answer for each of these *before* running it. Then run them and explain any you got wrong:

   ```python
   print(17 // 5, 17 % 5, 17 / 5)
   print(2 ** 3 ** 2)
   print(10 - 4 - 3)
   print(True or False and False)
   print(5 ^ 2)
   ```

   The second one is the interesting case — `**` is the one operator that groups right to left.

3. **Eligibility check** — Ask for marks (0–100), attendance percentage and whether fees are paid (the user types `yes` or `no`; compare with `==` to build a bool). Print `True` or `False` for whether the student is eligible: marks at least 40 **and** attendance at least 75 **and** fees paid. Then print whether they are ineligible, using `not`.

4. **Money splitter** — A shopkeeper has a total in paisa, for example 12,345. Using `//` and `%`, work out how many rupees and how many paisa that is, and print it as `Rs. 123 and 45 paisa`. What does `12345 % 100` represent in real life?

---

## Key Takeaways

- Seven arithmetic operators: `+ - * / // % **`.
- **`/` always gives a float**; **`//`** discards the fraction and rounds **downwards**; **`%`** gives the remainder.
- `% 2 == 0` tests for even. `% n == 0` tests for an exact multiple. `//` and `%` together split a total into units.
- **`**`** is the power operator. **`^` is not** — it silently gives a wrong number.
- **`+=`** and friends are shortcuts for "change it by". `+=` is how running totals work.
- Comparisons (`== != > < >= <=`) always produce a **`bool`**. **`=` assigns, `==` compares.**
- Python allows **chained comparisons** like `0 <= marks <= 100`.
- **`and`** needs both sides; **`or`** needs one; **`not`** flips.
- Precedence runs brackets → `**` → `* / // %` → `+ -` → comparisons → `not` → `and` → `or`. When in doubt, add brackets.

Next class we finally make programs that **decide** — using `if`, `elif` and `else` to choose between different paths.
