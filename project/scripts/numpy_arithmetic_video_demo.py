"""
NumPy Array Arithmetic Operations - Video Walkthrough Script (~2 Minutes)

A concise, easy-to-follow demonstration perfect for screen capture recording.
This script covers the core concepts of array arithmetic in a clear, visual way.

Key Points to Narrate During Recording:
1. Import NumPy and create arrays
2. Demonstrate element-wise operations
3. Show scalar operations
4. Highlight NumPy vs list differences
5. Show real-world application

Author: Data Science Foundation Student
Date: March 4, 2026
"""

import numpy as np


def print_section(title, number):
    """Print a formatted section header."""
    print("\n" + "="*70)
    print(f"{number}. {title}")
    print("="*70)


def print_operation(description, result=None):
    """Pretty print an operation."""
    print(f"\n📊 {description}")
    if result is not None:
        print(f"   Result: {result}")


# ============================================================================
# VIDEO SCRIPT START - ~2 Minutes
# ============================================================================

print("\n" + "╔" + "="*68 + "╗")
print("║" + "  NUMPY ARRAY ARITHMETIC OPERATIONS - VIDEO DEMO".center(68) + "║")
print("║" + "  (~2 Minutes)".center(68) + "║")
print("╚" + "="*68 + "╝")

# PART 1: Setup and Array Creation (15 seconds)
print_section("IMPORTING NUMPY AND CREATING ARRAYS", 1)
print("\nNarration: 'First, we import NumPy and create two simple arrays.'")

import_code = "import numpy as np"
print(f"\nCode: {import_code}")

print("\n\nNow let's create two arrays with numbers:")
array1 = np.array([10, 20, 30, 40, 50])
array2 = np.array([2, 4, 5, 5, 10])

print(f"\narray1 = np.array([10, 20, 30, 40, 50])")
print(f"Result: {array1}")
print(f"\narray2 = np.array([2, 4, 5, 5, 10])")
print(f"Result: {array2}")

print("\nNarration: 'Both arrays have 5 elements - they're compatible for operations.'")


# PART 2: Element-Wise Operations (45 seconds)
print_section("ELEMENT-WISE ARITHMETIC OPERATIONS", 2)

print("\nNarration: 'NumPy applies operations to each pair of elements.'")

# Addition
addition = array1 + array2
print_operation("ADDITION: array1 + array2", addition)
print("   Calculation: [10+2, 20+4, 30+5, 40+5, 50+10]")

# Subtraction
subtraction = array1 - array2
print_operation("SUBTRACTION: array1 - array2", subtraction)
print("   Calculation: [10-2, 20-4, 30-5, 40-5, 50-10]")

# Multiplication
multiplication = array1 * array2
print_operation("MULTIPLICATION: array1 * array2", multiplication)
print("   Calculation: [10*2, 20*4, 30*5, 40*5, 50*10]")

# Division
division = array1 / array2
print_operation("DIVISION: array1 / array2", division)
print("   Calculation: [10/2, 20/4, 30/5, 40/5, 50/10]")

print("\nNarration: 'Each operation applies element-by-element. Very different from lists!'")


# PART 3: Scalar Operations (30 seconds)
print_section("SCALAR OPERATIONS (Applying a Single Value)", 3)

print("\nNarration: 'Now let's apply a single number to an entire array.'")

scalar = 5
print(f"\narray = {array1}")
print(f"scalar = {scalar}")

# Scalar addition
scalar_add = array1 + scalar
print_operation("ADD SCALAR: array1 + 5", scalar_add)
print("   Applied to ALL elements: [10+5, 20+5, 30+5, 40+5, 50+5]")

# Scalar multiplication
scalar_mul = array1 * scalar
print_operation("MULTIPLY SCALAR: array1 * 5", scalar_mul)
print("   Applied to ALL elements: [10*5, 20*5, 30*5, 40*5, 50*5]")

print("\nNarration: 'The scalar operation broadcasts to every element automatically.'")


# PART 4: NumPy vs Python Lists (25 seconds)
print_section("WHY NUMPY BEATS PYTHON LISTS", 4)

print("\nNarration: 'Let's see why NumPy is better for math than lists.'")

python_list1 = [10, 20, 30]
python_list2 = [2, 4, 5]
numpy_arr1 = np.array([10, 20, 30])
numpy_arr2 = np.array([2, 4, 5])

print(f"\nPython lists: {python_list1} + {python_list2}")
list_result = python_list1 + python_list2
print(f"Result: {list_result}")
print("   ⚠️  CONCATENATED! (not added)")

print(f"\nNumPy arrays: {numpy_arr1} + {numpy_arr2}")
array_result = numpy_arr1 + numpy_arr2
print(f"Result: {array_result}")
print("   ✅ ADDED! (element-wise)")

print("\nNarration: 'Lists concatenate; NumPy adds. This is crucial for data analysis!'")


# PART 5: Real-World Example (15 seconds)
print_section("REAL-WORLD EXAMPLE: TEMPERATURE CONVERSION", 5)

print("\nNarration: 'Here's a practical example: converting temperatures.'")

celsius = np.array([0, 10, 20, 30, 40])
print(f"\nTemperatures in Celsius: {celsius}°C")

# Conversion formula: F = (C × 9/5) + 32
fahrenheit = (celsius * 9/5) + 32
print(f"Conversion: F = (C × 9/5) + 32")
print(f"\nTemperatures in Fahrenheit: {fahrenheit}°F")

print("\nNarration: 'The formula applied to all 5 temperatures instantly!")
print("            That's the power of vectorized operations.'")


# CLOSING
print("\n" + "="*70)
print("KEY TAKEAWAYS")
print("="*70)

print(f"""
✅ NumPy operates element-wise on arrays with the same shape
✅ Scalar operations broadcast to all array elements
✅ NumPy is designed for numerical computation (unlike lists)
✅ Code is concise, readable, and extremely fast
✅ Perfect for data analysis and scientific computing

Next: Apply these operations to real datasets!
""")

print("="*70)
print("END OF VIDEO DEMO")
print("="*70)

# ============================================================================
# TIME MARKERS FOR VIDEO EDITING
# ============================================================================

print("""

VIDEO EDITING TIME MARKERS:
─────────────────────────────────────────
0:00 - 0:15   Section 1: Setup and imports
0:15 - 1:00   Section 2: Element-wise operations (+, -, *, /)
1:00 - 1:30   Section 3: Scalar operations
1:30 - 1:55   Section 4: NumPy vs Python lists comparison
1:55 - 2:10   Section 5: Real-world temperature example
2:10 - 2:20   Summary and key takeaways
─────────────────────────────────────────

NARRATION TIPS:
• Speak clearly and at a moderate pace
• Explain what's happening on screen
• Highlight key differences between operations
• Emphasize the element-wise concept
• Show output clearly
""")
