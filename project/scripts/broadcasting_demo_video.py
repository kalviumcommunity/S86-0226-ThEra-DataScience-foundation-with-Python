"""
NumPy Broadcasting Demo Video Script (~2 Minutes)

A concise demonstration of NumPy broadcasting fundamentals for video recording.
This script is optimized for a 2-minute walkthrough covering:
- Broadcasting with scalars
- Broadcasting between 1D arrays
- Broadcasting between 2D and 1D arrays
- Understanding broadcasting rules

Author: Your Name
Date: March 5, 2026
"""

import numpy as np

print("=" * 60)
print("NUMPY BROADCASTING - VIDEO DEMONSTRATION")
print("=" * 60)
print()

# ============================================================================
# 1. BROADCASTING WITH SCALARS (Simplest Case)
# ============================================================================

print("1️⃣  Broadcasting with Scalars")
print("   → The scalar is applied to every element")
print()

array = np.array([10, 20, 30, 40, 50])
scalar = 5

print(f"   Array: {array}")
print(f"   Scalar: {scalar}")
print()

print(f"   Array + Scalar = {array + scalar}")
print(f"   Array * Scalar = {array * scalar}")
print(f"   Array - Scalar = {array - scalar}")
print()

print("   💡 The scalar '5' is broadcast to match the array shape")
print("   💡 No loops needed—NumPy handles it automatically")
print()

# ============================================================================
# 2. BROADCASTING BETWEEN 1D ARRAYS
# ============================================================================

print("2️⃣  Broadcasting Between 1D Arrays")
print("   → Arrays are aligned and expanded as needed")
print()

# Column vector (3, 1)
col_vector = np.array([[1],
                       [2],
                       [3]])

# Row vector (1, 4)
row_vector = np.array([[10, 20, 30, 40]])

print("   Column vector (3, 1):")
print(col_vector)
print(f"   Shape: {col_vector.shape}")
print()

print("   Row vector (1, 4):")
print(row_vector)
print(f"   Shape: {row_vector.shape}")
print()

result = col_vector + row_vector
print("   Column + Row = Broadcasting!")
print(result)
print(f"   Result shape: {result.shape} (3, 4)")
print()

print("   💡 Column vector is broadcast across columns")
print("   💡 Row vector is broadcast down rows")
print()

# ============================================================================
# 3. BROADCASTING BETWEEN 2D AND 1D ARRAYS
# ============================================================================

print("3️⃣  Broadcasting Between 2D and 1D Arrays")
print("   → Common real-world pattern")
print()

# 2D array
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# 1D array
vector = np.array([10, 20, 30])

print("   2D Matrix (3, 3):")
print(matrix)
print(f"   Shape: {matrix.shape}")
print()

print(f"   1D Vector (3,): {vector}")
print(f"   Shape: {vector.shape}")
print()

result = matrix + vector
print("   Matrix + Vector = Broadcasting!")
print(result)
print(f"   Result shape: {result.shape}")
print()

print("   💡 Vector is added to each row of the matrix")
print("   💡 [10, 20, 30] is broadcast across all 3 rows")
print()

# ============================================================================
# 4. UNDERSTANDING BROADCASTING RULES
# ============================================================================

print("4️⃣  Understanding Broadcasting Rules")
print("   → Shapes are compared from right to left")
print()

print("   Rule 1: Compare shapes from the rightmost dimension")
print("   Rule 2: Dimensions are compatible if:")
print("           • They are equal, OR")
print("           • One of them is 1")
print()

# Example 1: Compatible shapes
print("   ✅ Compatible Example:")
a = np.array([[1, 2, 3]])  # Shape (1, 3)
b = np.array([[10], [20]])  # Shape (2, 1)
print(f"   Array A shape: {a.shape}")
print(f"   Array B shape: {b.shape}")
result = a + b
print(f"   Result shape: {result.shape} (2, 3)")
print("   → Both dimensions can be broadcast")
print()

# Example 2: Simple row operation
print("   ✅ Row-wise Operation:")
data = np.array([[100, 200, 300],
                 [400, 500, 600],
                 [700, 800, 900]])
row_subtract = np.array([50, 100, 150])

print("   Data (3, 3):")
print(data)
print(f"   Subtract vector (3,): {row_subtract}")
result = data - row_subtract
print("   Result:")
print(result)
print()

# ============================================================================
# 5. PRACTICAL BROADCASTING EXAMPLES
# ============================================================================

print("5️⃣  Practical Broadcasting Examples")
print()

# Normalizing data (centering)
print("   Example: Centering data (subtract mean)")
dataset = np.array([[10, 20, 30],
                    [40, 50, 60],
                    [70, 80, 90]])

print("   Dataset:")
print(dataset)
print()

# Calculate mean of each column
column_means = dataset.mean(axis=0)
print(f"   Column means: {column_means}")
print(f"   Shape: {column_means.shape}")
print()

# Subtract mean from each column (broadcasting!)
centered = dataset - column_means
print("   Centered data (each column now has mean ≈ 0):")
print(centered)
print()

print("   💡 Broadcasting made this operation clean and efficient")
print("   💡 No loops, no manual iteration—just NumPy magic!")
print()

# ============================================================================
# 6. SHAPE INSPECTION BEFORE OPERATIONS
# ============================================================================

print("6️⃣  Always Check Shapes Before Broadcasting")
print("   → Avoid errors by inspecting shapes first")
print()

x = np.array([1, 2, 3, 4])
y = np.array([[10], [20], [30]])

print(f"   Array X shape: {x.shape} (4,)")
print(f"   Array Y shape: {y.shape} (3, 1)")
print()

print("   Can we broadcast X + Y?")
print("   → X: (4,) Y: (3, 1)")
print("   → Comparing: 4 vs 3 (rightmost dimensions)")
print("   → ❌ Incompatible! Shapes don't align")
print()

print("   Fix: Reshape X to match compatible dimensions")
x_reshaped = x.reshape(1, 4)
print(f"   X reshaped: {x_reshaped.shape} (1, 4)")
result = y + x_reshaped
print(f"   Now Y (3,1) + X (1,4) → Result shape: {result.shape}")
print()

# ============================================================================
# SUMMARY
# ============================================================================

print("=" * 60)
print("SUMMARY")
print("=" * 60)
print()
print("✅ Broadcasting allows operations on different-shaped arrays")
print("✅ Scalars broadcast to any array shape automatically")
print("✅ Arrays are aligned from the rightmost dimension")
print("✅ Dimensions of size 1 can be stretched to match")
print("✅ Always inspect shapes before operations")
print("✅ Broadcasting is efficient—no data is copied")
print()
print("🎯 Broadcasting is a core NumPy concept that makes")
print("   your code shorter, faster, and more expressive!")
print()
print("=" * 60)
