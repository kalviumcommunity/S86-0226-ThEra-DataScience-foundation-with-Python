"""
NumPy Array Arithmetic Operations - Quick Reference Guide

A compact, easy-to-remember guide for array arithmetic operations.
Print this or keep it handy while coding!

Author: Data Science Foundation Student
Date: March 4, 2026
"""

import numpy as np


print("""
╔════════════════════════════════════════════════════════════════════════════╗
║                  NUMPY ARRAY ARITHMETIC - QUICK REFERENCE                  ║
╚════════════════════════════════════════════════════════════════════════════╝


1️⃣  ELEMENT-WISE OPERATIONS (Arrays of same shape)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Operation          Syntax              Example
───────────────────────────────────────────────────────────────────────────
Addition           a + b               [1,2,3] + [4,5,6] = [5,7,9]
Subtraction        a - b               [10,20,30] - [1,2,3] = [9,18,27]
Multiplication     a * b               [2,3,4] * [5,6,7] = [10,18,28]
Division           a / b               [10,20,30] / [2,4,5] = [5,5,6]
Floor Division     a // b              [10,20,30] // [3,3,3] = [3,6,10]
Modulo (Remainder) a % b               [10,20,30] % [3,3,3] = [1,2,0]
Power              a ** b              [2,3,4] ** 2 = [4,9,16]


2️⃣  SCALAR OPERATIONS (Single value to array)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Operation          Syntax              Example
───────────────────────────────────────────────────────────────────────────
Add scalar         a + 5               [1,2,3] + 5 = [6,7,8]
Subtract scalar    a - 5               [10,20,30] - 5 = [5,15,25]
Multiply scalar    a * 5               [1,2,3] * 5 = [5,10,15]
Divide by scalar   a / 2               [10,20,30] / 2 = [5,10,15]
Power by scalar    a ** 2              [2,3,4] ** 2 = [4,9,16]
Reverse subtract   5 - a               5 - [1,2,3] = [4,3,2]
Reverse divide     100 / a             100 / [4,5,10] = [25,20,10]


3️⃣  CREATION AND BASIC USAGE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Create from list:     a = np.array([1, 2, 3, 4, 5])
Create 2D array:      a = np.array([[1,2,3], [4,5,6]])
Create with range:    a = np.arange(0, 10, 2)  # [0,2,4,6,8]
Create with zeros:    a = np.zeros(5)  # [0,0,0,0,0]
Create with ones:     a = np.ones(5)  # [1,1,1,1,1]
Create linspace:      a = np.linspace(0, 10, 5)  # 5 values from 0 to 10


4️⃣  INSPECTION AND PROPERTIES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Property           Syntax              Example
───────────────────────────────────────────────────────────────────────────
Shape              a.shape             (5,) for 1D, (3,4) for 2D
Data type          a.dtype             int64, float64, etc.
Number of elements a.size              5 for a 5-element array
Number of dims     a.ndim              1 for 1D, 2 for 2D
Get element        a[0]                First element
Get range          a[0:3]              First three elements
Get column (2D)    a[:, 0]             First column of 2D array


5️⃣  COMMON FUNCTIONS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Function           Syntax              Description
───────────────────────────────────────────────────────────────────────────
Sum                a.sum()             Total of all elements
Mean               a.mean()            Average of all elements
Min                a.min()             Smallest element
Max                a.max()             Largest element
Std Dev            a.std()             Standard deviation
Square root        np.sqrt(a)          Square root of each element
Absolute value     np.abs(a)           Absolute value of elements


6️⃣  COMMON MISTAKES & SOLUTIONS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

❌ Mistake                              ✅ Solution
─────────────────────────────────────────────────────────────────────────
Arrays have different shapes           Reshape or ensure same shape
Confusing * with matrix multiply (@)   Use @ for matrix multiplication
Not knowing result type changes        Check dtype after operations
Modifying original when you didn't want Use .copy() to make independent copy
Using loops instead of vectorization   Use NumPy operations directly


7️⃣  LISTS vs NUMPY ARRAYS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Operation              List Behavior              NumPy Behavior
─────────────────────────────────────────────────────────────────────────
list + [1,2,3]        Concatenation (joins)      Element-wise addition
list * 3              Repetition (duplicates)    Multiplication by scalar
list - another        ❌ Not supported           Element-wise subtraction
list / 2              ❌ Not supported           Element-wise division
Speed                 Slower (loops internally)  Much faster (optimized)
Memory                More memory per element    Compact & efficient


8️⃣  PRACTICAL RECIPES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

NORMALIZE DATA (0-1 range):
   normalized = (data - data.min()) / (data.max() - data.min())

CONVERT CELSIUS TO FAHRENHEIT:
   fahrenheit = (celsius * 9/5) + 32

APPLY DISCOUNT:
   discounted_price = original_price * (1 - discount_rate)

SCALE VALUES:
   scaled = values * scale_factor

HANDLE PERCENTAGE CHANGE:
   percentage_change = (new_value - old_value) / old_value * 100

STANDARDIZE DATA (mean=0, std=1):
   standardized = (data - data.mean()) / data.std()


9️⃣  REAL-WORLD EXAMPLE: QUARTERLY SALES ANALYSIS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

""")

# Real example
q1_sales = np.array([15000, 18000, 22000])  # Jan, Feb, Mar
q2_sales = np.array([20000, 25000, 28000])  # Apr, May, Jun

print(f"Q1 Sales: {q1_sales}")
print(f"Q2 Sales: {q2_sales}")

difference = q2_sales - q1_sales
percent_growth = (difference / q1_sales) * 100
total_growth = q2_sales.sum() - q1_sales.sum()
avg_q1 = q1_sales.mean()
avg_q2 = q2_sales.mean()

print(f"\nMonth-by-month difference: {difference}")
print(f"Percent growth: {percent_growth.astype(int)}%")
print(f"Total growth Q1→Q2: ${total_growth:,}")
print(f"Average Q1: ${avg_q1:,.0f}, Average Q2: ${avg_q2:,.0f}")

print(f"""

🔟  KEY PRINCIPLES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. Element-wise: Operations apply to corresponding elements
2. Broadcasting: Scalars apply to all elements
3. Compatible shapes: Arrays must have matching shapes for operations
4. Type coercion: Operations may change data types (int → float)
5. No loops needed: Use NumPy operations for speed and clarity
6. Use @ for matrix math: * is element-wise, @ is matrix multiplication
7. Check your shapes: Most errors come from shape mismatches


╔════════════════════════════════════════════════════════════════════════════╗
║                                                                            ║
║  REMEMBER: NumPy is built for numerical computation. Use it instead of     ║
║            loops and lists for anything mathematical!                      ║
║                                                                            ║
╚════════════════════════════════════════════════════════════════════════════╝
""")
