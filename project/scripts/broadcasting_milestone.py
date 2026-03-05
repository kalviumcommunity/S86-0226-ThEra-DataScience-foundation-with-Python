"""
NumPy Broadcasting Milestone

This script guides you through understanding NumPy broadcasting with 
simple, intuitive examples. Complete each section to master broadcasting.

Broadcasting allows NumPy to perform operations on arrays of different 
shapes without explicit loops, making code shorter, faster, and more expressive.

Author: Your Name
Date: March 5, 2026
"""

import numpy as np

print("\n" + "=" * 70)
print(" " * 15 + "NUMPY BROADCASTING MILESTONE")
print("=" * 70 + "\n")

# ============================================================================
# SECTION 1: BROADCASTING WITH SCALARS
# ============================================================================

print("━" * 70)
print("SECTION 1: Broadcasting with Scalars")
print("━" * 70)
print("""
Task: Create small NumPy arrays and perform operations with scalars.
Goal: Understand how scalars are broadcast to every element automatically.
\n""")

# TODO 1: Create a 1D array with values [5, 10, 15, 20, 25]
array_1 = np.array([5, 10, 15, 20, 25])
print("1️⃣  Array created:")
print(f"   {array_1}")
print(f"   Shape: {array_1.shape}\n")

# TODO 2: Add 100 to every element using broadcasting
result_add = array_1 + 100
print("2️⃣  Adding scalar 100 to array:")
print(f"   Original: {array_1}")
print(f"   Result:   {result_add}")
print("   💡 The scalar 100 was broadcast to every element\n")

# TODO 3: Multiply every element by 3 using broadcasting
result_mult = array_1 * 3
print("3️⃣  Multiplying array by scalar 3:")
print(f"   Original: {array_1}")
print(f"   Result:   {result_mult}")
print("   💡 No loops needed—broadcasting handles it!\n")

# TODO 4: Compare with loop-based approach (conceptually)
print("4️⃣  Without broadcasting (using loops):")
print("   result = []")
print("   for value in array:")
print("       result.append(value + 100)")
print("   → More code, slower, less readable\n")

print("   ✅ Broadcasting is NumPy's superpower!\n")
input("Press Enter to continue to Section 2...")

# ============================================================================
# SECTION 2: BROADCASTING BETWEEN 1D ARRAYS
# ============================================================================

print("\n" + "━" * 70)
print("SECTION 2: Broadcasting Between 1D Arrays")
print("━" * 70)
print("""
Task: Combine arrays of different lengths using broadcasting.
Goal: Understand shape alignment rules and when broadcasting succeeds.
\n""")

# TODO 5: Create a column vector (3, 1)
column_vec = np.array([[10],
                       [20],
                       [30]])
print("5️⃣  Column vector created:")
print(column_vec)
print(f"   Shape: {column_vec.shape} (3 rows, 1 column)\n")

# TODO 6: Create a row vector (1, 4)
row_vec = np.array([[1, 2, 3, 4]])
print("6️⃣  Row vector created:")
print(row_vec)
print(f"   Shape: {row_vec.shape} (1 row, 4 columns)\n")

# TODO 7: Add column and row vectors (broadcasting!)
print("7️⃣  Broadcasting column + row:")
print(f"   Column shape: {column_vec.shape}")
print(f"   Row shape:    {row_vec.shape}")
print("   → Can these shapes broadcast?\n")

result_broadcast = column_vec + row_vec
print("   Result:")
print(result_broadcast)
print(f"   Result shape: {result_broadcast.shape} (3, 4)\n")

print("   💡 Column vector expanded across columns")
print("   💡 Row vector expanded down rows")
print("   💡 Result is a grid of all combinations!\n")

# TODO 8: Try incompatible shapes
print("8️⃣  Example of incompatible shapes:")
incompatible_a = np.array([1, 2, 3])      # Shape (3,)
incompatible_b = np.array([10, 20])       # Shape (2,)
print(f"   Array A shape: {incompatible_a.shape}")
print(f"   Array B shape: {incompatible_b.shape}")
print("   → These shapes are INCOMPATIBLE")
print("   → Would cause: ValueError: operands could not be broadcast\n")

print("   ✅ Always check shapes before operations!\n")
input("Press Enter to continue to Section 3...")

# ============================================================================
# SECTION 3: BROADCASTING BETWEEN 2D AND 1D ARRAYS
# ============================================================================

print("\n" + "━" * 70)
print("SECTION 3: Broadcasting Between 2D and 1D Arrays")
print("━" * 70)
print("""
Task: Combine a 2D array (matrix) with a 1D array (vector).
Goal: Apply broadcasting across rows or columns—most common pattern!
\n""")

# TODO 9: Create a 3x3 matrix
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
print("9️⃣  Matrix created:")
print(matrix)
print(f"   Shape: {matrix.shape}\n")

# TODO 10: Create a 1D vector
vector = np.array([100, 200, 300])
print("🔟 Vector created:")
print(f"   {vector}")
print(f"   Shape: {vector.shape}\n")

# TODO 11: Add vector to matrix (row-wise broadcasting)
print("1️⃣1️⃣ Adding vector to each row of matrix:")
print(f"   Matrix shape: {matrix.shape}")
print(f"   Vector shape: {vector.shape}")
print("   → Vector will be broadcast to each row\n")

result_row_broadcast = matrix + vector
print("   Result:")
print(result_row_broadcast)
print(f"   Shape: {result_row_broadcast.shape}\n")

print("   💡 Vector [100, 200, 300] was added to each row")
print("   💡 This is the most common broadcasting pattern!\n")

# TODO 12: Column-wise broadcasting (reshape vector first)
vector_col = vector.reshape(3, 1)
print("1️⃣2️⃣ Adding vector to each column (reshape to 3x1):")
print(f"   Reshaped vector shape: {vector_col.shape}")
print(vector_col)
print()

result_col_broadcast = matrix + vector_col
print("   Result:")
print(result_col_broadcast)
print(f"   Shape: {result_col_broadcast.shape}\n")

print("   💡 Shape matters! Reshape controls broadcasting direction\n")
input("Press Enter to continue to Section 4...")

# ============================================================================
# SECTION 4: UNDERSTANDING BROADCASTING RULES
# ============================================================================

print("\n" + "━" * 70)
print("SECTION 4: Understanding Broadcasting Rules")
print("━" * 70)
print("""
Task: Learn how NumPy determines if shapes can broadcast.
Goal: Predict outcomes before running code—develop shape intuition!
\n""")

print("📌 Broadcasting Rules (Simple Version):")
print("   1. Compare shapes from RIGHT to LEFT (trailing dimensions)")
print("   2. Dimensions are compatible if:")
print("      • They are exactly equal, OR")
print("      • One of them is 1 (can be stretched)")
print("   3. If compatible, the result shape takes the max of each dimension\n")

# TODO 13: Example 1 - Compatible shapes
print("1️⃣3️⃣ Example 1: Compatible Shapes")
shape_a = np.array([[1, 2, 3]])  # Shape (1, 3)
shape_b = np.array([[10], [20], [30]])  # Shape (3, 1)

print(f"   Array A: {shape_a.shape} → (1, 3)")
print(f"   Array B: {shape_b.shape} → (3, 1)")
print("\n   Analysis:")
print("   • Compare rightmost: 3 vs 1 → Compatible (1 can stretch)")
print("   • Compare next: 1 vs 3 → Compatible (1 can stretch)")
print("   • Result shape: (3, 3) ✅\n")

result_shapes = shape_a + shape_b
print("   Result:")
print(result_shapes)
print(f"   Result shape: {result_shapes.shape}\n")

# TODO 14: Example 2 - Predict before computing
print("1️⃣4️⃣ Example 2: Predict the Result")
pred_a = np.array([[[1, 2]]])  # Shape (1, 1, 2)
pred_b = np.array([[10, 20]])  # Shape (1, 2)

print(f"   Array A shape: {pred_a.shape}")
print(f"   Array B shape: {pred_b.shape}")
print("\n   🤔 What will the result shape be?")
print("   → Compare right to left: 2 vs 2 ✅, 1 vs 1 ✅, 1 vs missing (treated as 1) ✅")
print("   → Predicted result shape: (1, 1, 2)\n")

result_pred = pred_a + pred_b
print(f"   Actual result shape: {result_pred.shape}")
print("   ✅ Prediction was correct!\n")

# TODO 15: Example 3 - Size 1 as expandable
print("1️⃣5️⃣ Example 3: Size 1 Dimensions Are Expandable")
expand_a = np.array([[[1], [2], [3]]])  # Shape (1, 3, 1)
expand_b = np.array([10, 20, 30, 40])    # Shape (4,)

print(f"   Array A shape: {expand_a.shape}")
print(f"   Array B shape: {expand_b.shape}")
print("\n   Analysis:")
print("   • A: (1, 3, 1), B: (4,) → Compare: 1 vs 4 ✅, 3 vs missing ✅, 1 vs missing ✅")
print("   • Result shape: (1, 3, 4)\n")

result_expand = expand_a + expand_b
print(f"   Result shape: {result_expand.shape}")
print("   ✅ Broadcasting expanded both arrays!\n")

input("Press Enter to continue to Section 5...")

# ============================================================================
# SECTION 5: PRACTICAL APPLICATIONS
# ============================================================================

print("\n" + "━" * 70)
print("SECTION 5: Practical Broadcasting Applications")
print("━" * 70)
print("""
Task: Apply broadcasting to real-world data operations.
Goal: See how broadcasting makes data science code clean and efficient!
\n""")

# TODO 16: Centering data (subtract column means)
print("1️⃣6️⃣ Application 1: Centering Data (Zero-Centering)")
dataset = np.array([[10, 20, 30],
                    [40, 50, 60],
                    [70, 80, 90]])

print("   Dataset:")
print(dataset)
print()

column_means = dataset.mean(axis=0)
print(f"   Column means: {column_means}")
print(f"   Mean shape: {column_means.shape}\n")

centered_data = dataset - column_means
print("   Centered data (mean of each column is now ~0):")
print(centered_data)
print()

print("   💡 Broadcasting subtracted means from each column")
print("   💡 Essential for machine learning preprocessing!\n")

# TODO 17: Normalizing rows (divide by row sums)
print("1️⃣7️⃣ Application 2: Normalizing Rows")
data_rows = np.array([[1, 2, 3],
                      [4, 5, 6]])

print("   Data:")
print(data_rows)
print()

row_sums = data_rows.sum(axis=1, keepdims=True)
print(f"   Row sums (keepdims=True): {row_sums.T} → Shape {row_sums.shape}")
print()

normalized_rows = data_rows / row_sums
print("   Normalized (each row sums to 1):")
print(normalized_rows)
print()

print("   💡 keepdims=True preserves dimension for broadcasting")
print("   💡 Used in probability distributions and neural networks!\n")

# TODO 18: Creating a grid (coordinate mesh)
print("1️⃣8️⃣ Application 3: Creating a Coordinate Grid")
x = np.array([[1], [2], [3], [4]])  # Shape (4, 1)
y = np.array([[10, 20, 30]])        # Shape (1, 3)

print(f"   X (column): Shape {x.shape}")
print(f"   Y (row): Shape {y.shape}\n")

grid = x + y
print("   Grid (X + Y):")
print(grid)
print(f"   Shape: {grid.shape}\n")

print("   💡 Creates combinations of X and Y coordinates")
print("   💡 Useful for meshgrids, plotting, and spatial data!\n")

input("Press Enter to continue to Summary...")

# ============================================================================
# SUMMARY AND NEXT STEPS
# ============================================================================

print("\n" + "=" * 70)
print(" " * 22 + "MILESTONE SUMMARY")
print("=" * 70 + "\n")

print("✅ You have successfully completed the NumPy Broadcasting Milestone!\n")

print("📋 What You Learned:")
print("   1. Broadcasting with scalars")
print("   2. Broadcasting between 1D arrays")
print("   3. Broadcasting between 2D and 1D arrays")
print("   4. Broadcasting rules (right-to-left shape comparison)")
print("   5. Practical applications (centering, normalizing, grids)\n")

print("🎯 Key Takeaways:")
print("   • Broadcasting eliminates loops for cleaner, faster code")
print("   • Always inspect shapes before operations")
print("   • Dimensions of size 1 can be stretched")
print("   • Broadcasting is memory-efficient (no copying)")
print("   • Essential for NumPy, Pandas, and machine learning\n")

print("🚀 Next Steps:")
print("   1. Record your ~2 minute video walkthrough")
print("   2. Practice with your own examples")
print("   3. Explore advanced indexing and masking")
print("   4. Move on to Pandas (which uses broadcasting extensively)\n")

print("📹 Video Requirements:")
print("   • Demonstrate scalar-to-array broadcasting")
print("   • Demonstrate 1D-to-2D broadcasting")
print("   • Show shape inspection before operations")
print("   • Explain why broadcasting works")
print("   • Length: ~2 minutes, screen-facing, clear audio\n")

print("=" * 70)
print(" " * 20 + "CONGRATULATIONS! 🎉")
print("=" * 70 + "\n")

print("Broadcasting is a fundamental NumPy skill.")
print("You are now ready for advanced array operations!\n")
