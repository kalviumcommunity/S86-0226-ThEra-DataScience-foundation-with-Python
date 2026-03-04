"""
NumPy Demo Video Script (~2 Minutes)

A concise demonstration of NumPy array fundamentals for video recording.
This script is optimized for a 2-minute walkthrough covering:
- Importing NumPy
- Creating arrays from lists
- Inspecting array properties
- Basic array operations

Author: Your Name
Date: March 4, 2026
"""

import numpy as np

print("=" * 60)
print("NUMPY ARRAYS - VIDEO DEMONSTRATION")
print("=" * 60)
print()

# ============================================================================
# 1. IMPORTING NUMPY
# ============================================================================

print("1️⃣  Importing NumPy")
print("   import numpy as np")
print("   → NumPy is imported with the alias 'np' by convention")
print()

# ============================================================================
# 2. CREATING ARRAYS FROM PYTHON LISTS
# ============================================================================

print("2️⃣  Creating Arrays from Python Lists")
print()

# 1D array
print("   Creating a 1D array:")
my_list = [10, 20, 30, 40, 50]
my_array = np.array(my_list)
print(f"   Python list: {my_list}")
print(f"   NumPy array: {my_array}")
print()

# 2D array
print("   Creating a 2D array:")
nested_list = [[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9]]
array_2d = np.array(nested_list)
print(f"   2D array:")
print(array_2d)
print()

# ============================================================================
# 3. INSPECTING ARRAY PROPERTIES
# ============================================================================

print("3️⃣  Inspecting Array Properties")
print()

print(f"   Shape: {array_2d.shape} → (3 rows, 3 columns)")
print(f"   Data type: {array_2d.dtype}")
print(f"   Dimensions: {array_2d.ndim}D")
print(f"   Total elements: {array_2d.size}")
print()

# ============================================================================
# 4. BASIC ARRAY OPERATIONS
# ============================================================================

print("4️⃣  Basic Array Operations")
print()

# Element-wise operations
numbers = np.array([5, 10, 15, 20])
print(f"   Array: {numbers}")
print(f"   Array * 2 = {numbers * 2} (element-wise multiplication)")
print(f"   Array + 10 = {numbers + 10} (element-wise addition)")
print()

# Array arithmetic
array_a = np.array([1, 2, 3, 4])
array_b = np.array([10, 20, 30, 40])
print(f"   Array A: {array_a}")
print(f"   Array B: {array_b}")
print(f"   A + B = {array_a + array_b} (element-wise addition)")
print()

# Statistical operations
data = np.array([12, 18, 24, 30, 36])
print(f"   Data: {data}")
print(f"   Mean: {data.mean()}")
print(f"   Sum: {data.sum()}")
print(f"   Max: {data.max()}")
print()

# ============================================================================
# 5. ARRAYS VS LISTS COMPARISON
# ============================================================================

print("5️⃣  Why Use Arrays Instead of Lists?")
print()

print("   Python list behavior:")
list_x = [1, 2, 3]
print(f"   {list_x} * 2 = {list_x * 2} → Replicates the list")
print()

print("   NumPy array behavior:")
array_x = np.array([1, 2, 3])
print(f"   {array_x} * 2 = {array_x * 2} → Multiplies each element")
print()

print("   💡 Arrays are optimized for numerical operations!")
print()

# ============================================================================
# CONCLUSION
# ============================================================================

print("=" * 60)
print("✅ KEY TAKEAWAYS")
print("=" * 60)
print("• NumPy arrays are created from Python lists using np.array()")
print("• Arrays have properties: shape, dtype, ndim, size")
print("• Arrays support element-wise operations automatically")
print("• Arrays are faster and more efficient than lists for numbers")
print("• NumPy is the foundation for Pandas and data science")
print()
print("🎯 Milestone Complete: Ready for real-world data analysis!")
print("=" * 60)
