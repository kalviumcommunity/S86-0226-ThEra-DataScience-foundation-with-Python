"""
NumPy Vectorized Operations Milestone - Assignment Completion

Demonstrates vectorized operations instead of Python loops.
Covers all assignment requirements:
1. Loop-based vs vectorized code comparison
2. Vectorized arithmetic operations
3. Vectorized comparisons and conditions
4. Common vectorization mistakes
"""

import numpy as np
import time


print("=" * 80)
print("NUMPY VECTORIZED OPERATIONS MILESTONE - ASSIGNMENT COMPLETION")
print("=" * 80)

# ============================================================================
# 1. UNDERSTANDING LOOP-BASED VS VECTORIZED CODE
# ============================================================================

print("\n" + "=" * 80)
print("1. LOOP-BASED VS VECTORIZED CODE")
print("=" * 80)

# Loop-based approach
print("\n❌ LOOP-BASED (Slow, Verbose):")
array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
result_loop = []
for i in array:
    result_loop.append(i * 2 + 5)

print(f"Code:\n  result_loop = []\n  for i in array:\n      result_loop.append(i * 2 + 5)")
print(f"Result: {result_loop}")
print(f"Length: 4 lines of code")

# Vectorized approach
print("\n✅ VECTORIZED (Fast, Clean):")
result_vectorized = array * 2 + 5

print(f"Code:\n  result_vectorized = array * 2 + 5")
print(f"Result: {result_vectorized}")
print(f"Length: 1 line of code")

print(f"\n💡 Both produce same output: {np.array_equal(result_loop, result_vectorized)}")
print("   Vectorized is cleaner, faster, and more readable")


# ============================================================================
# 2. APPLYING VECTORIZED ARITHMETIC OPERATIONS
# ============================================================================

print("\n" + "=" * 80)
print("2. VECTORIZED ARITHMETIC OPERATIONS")
print("=" * 80)

prices = np.array([100, 250, 320, 150, 500])
quantities = np.array([5, 2, 8, 3, 1])

# ❌ Loop approach
print("\n❌ LOOP-BASED:")
total_loop = []
for i in range(len(prices)):
    total_loop.append(prices[i] * quantities[i])
print(f"Prices: {prices}")
print(f"Quantities: {quantities}")
print(f"Totals: {total_loop}")
print(f"Code lines: 4")

# ✅ Vectorized approach
print("\n✅ VECTORIZED:")
total_vectorized = prices * quantities
print(f"Prices: {prices}")
print(f"Quantities: {quantities}")
print(f"Totals: {total_vectorized}")
print(f"Code lines: 1")
print(f"Correct: {np.array_equal(total_loop, total_vectorized)}")


# Real-world example: Apply discount
print("\n" + "-" * 80)
print("REAL-WORLD: Apply 20% discount to prices")
print("-" * 80)

original_prices = np.array([99.99, 149.99, 199.99, 79.99, 299.99])

print(f"\n❌ LOOP-BASED:")
discounted_loop = []
for price in original_prices:
    discounted_loop.append(price * 0.8)
print(f"Result: {discounted_loop}")

print(f"\n✅ VECTORIZED:")
discounted_vectorized = original_prices * 0.8
print(f"Result: {discounted_vectorized}")


# ============================================================================
# 3. VECTORIZED COMPARISONS AND CONDITIONS
# ============================================================================

print("\n" + "=" * 80)
print("3. VECTORIZED COMPARISONS AND CONDITIONS")
print("=" * 80)

scores = np.array([45, 67, 89, 92, 78, 55, 88, 72, 91, 65])

# ❌ Loop-based condition checking
print("\n❌ LOOP-BASED: Which scores are above 80?")
high_scores_loop = []
for score in scores:
    if score > 80:
        high_scores_loop.append(score)
print(f"Code: 5 lines (for loop + if condition)")
print(f"Result: {high_scores_loop}")

# ✅ Vectorized comparison
print("\n✅ VECTORIZED: Which scores are above 80?")
boolean_mask = scores > 80
high_scores_vectorized = scores[boolean_mask]
print(f"Code: 2 lines")
print(f"Boolean mask: {boolean_mask}")
print(f"Result: {high_scores_vectorized}")
print(f"Correct: {np.array_equal(high_scores_loop, high_scores_vectorized)}")


# Multiple conditions
print("\n" + "-" * 80)
print("MULTIPLE CONDITIONS: Scores between 70 and 90")
print("-" * 80)

print(f"\n❌ LOOP-BASED:")
filtered_loop = []
for score in scores:
    if score >= 70 and score <= 90:
        filtered_loop.append(score)
print(f"Result: {filtered_loop}")

print(f"\n✅ VECTORIZED:")
condition = (scores >= 70) & (scores <= 90)
filtered_vectorized = scores[condition]
print(f"Result: {filtered_vectorized}")
print(f"Correct: {np.array_equal(filtered_loop, filtered_vectorized)}")


# ============================================================================
# 4. AVOIDING COMMON VECTORIZATION MISTAKES
# ============================================================================

print("\n" + "=" * 80)
print("4. AVOIDING COMMON VECTORIZATION MISTAKES")
print("=" * 80)

# Mistake 1: Shape mismatch
print("\n❌ MISTAKE 1: Shape Mismatch")
a = np.array([1, 2, 3])
b = np.array([1, 2])
print(f"a.shape = {a.shape}, b.shape = {b.shape}")
print(f"a + b → Would cause error (shapes don't match)")
print(f"✅ SOLUTION: Ensure shapes are compatible")

# Mistake 2: Using wrong operator
print("\n❌ MISTAKE 2: Using * instead of @ for matrix multiplication")
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])
print(f"matrix1 * matrix2 (Element-wise, not matrix multiply)")
print(matrix1 * matrix2)
print(f"✅ Use np.dot() or @ for matrix multiplication")
print(np.dot(matrix1, matrix2))

# Mistake 3: When NOT to vectorize (clarity matters)
print("\n❌ MISTAKE 3: Over-complicated vectorization")
print(f"Sometimes a loop is clearer than a complex expression")
print(f"✅ PRINCIPLE: Write for clarity first, optimize if needed")

# Correct vectorization approach
print("\n✅ CORRECT APPROACH:")
values = np.array([1, 2, 3, 4, 5])
squared = values ** 2
print(f"values: {values}")
print(f"squared: {squared}")
print(f"(Simple, clear, and vectorized)")


# ============================================================================
# 5. PERFORMANCE COMPARISON
# ============================================================================

print("\n" + "=" * 80)
print("5. PERFORMANCE COMPARISON")
print("=" * 80)

large_array = np.array(range(1000000))

# Loop-based
start = time.time()
result_loop = []
for val in large_array:
    result_loop.append(val * 2)
loop_time = time.time() - start

# Vectorized
start = time.time()
result_vectorized = large_array * 2
vectorized_time = time.time() - start

print(f"\nOperation: Multiply 1,000,000 elements by 2")
print(f"Loop-based time:    {loop_time:.6f} seconds")
print(f"Vectorized time:    {vectorized_time:.6f} seconds")
print(f"Speed improvement:  {loop_time / vectorized_time:.1f}x faster")
print(f"Correct results:    {np.array_equal(result_loop, result_vectorized)}")


# ============================================================================
# 6. COMPREHENSIVE EXAMPLES
# ============================================================================

print("\n" + "=" * 80)
print("6. COMPREHENSIVE EXAMPLES")
print("=" * 80)

# Example 1: Temperature conversion
print("\n📊 EXAMPLE 1: Temperature Conversion")
celsius = np.array([0, 10, 20, 25, 30, 35, 40])
print(f"Celsius:    {celsius}")

print(f"❌ Loop: for c in celsius: fahrenheit.append(c * 9/5 + 32)")
print(f"✅ Vectorized: fahrenheit = celsius * 9/5 + 32")
fahrenheit = celsius * 9/5 + 32
print(f"Fahrenheit: {fahrenheit}")

# Example 2: Data normalization
print("\n📊 EXAMPLE 2: Data Normalization (0-1 range)")
data = np.array([10, 20, 30, 40, 50])
print(f"Original: {data}")

min_val = data.min()
max_val = data.max()
print(f"❌ Loop: for d in data: normalized.append((d - min) / (max - min))")
print(f"✅ Vectorized: (data - min) / (max - min)")
normalized = (data - min_val) / (max_val - min_val)
print(f"Normalized: {normalized}")

# Example 3: Conditional assignment
print("\n📊 EXAMPLE 3: Replace values based on condition")
values = np.array([5, 15, 25, 35, 45])
print(f"Original: {values}")

print(f"❌ Loop: for i, v in enumerate: if v > 20: values[i] = 0")
print(f"✅ Vectorized: values[values > 20] = 0")
values_copy = values.copy()
values_copy[values_copy > 20] = 0
print(f"After replacing (>20 with 0): {values_copy}")


# ============================================================================
# 7. KEY TAKEAWAYS
# ============================================================================

print("\n" + "=" * 80)
print("KEY TAKEAWAYS")
print("=" * 80)

print("""
✅ VECTORIZED OPERATIONS:
   • Use array operations instead of for loops
   • Cleaner, more readable code
   • Significantly faster (100-1000x)
   • Core NumPy principle

✅ WHEN TO VECTORIZE:
   • Simple arithmetic operations
   • Comparisons and filtering
   • Element-wise transformations
   • Bulk calculations

✅ BEST PRACTICES:
   • Write for clarity first
   • Use vectorized operations when natural
   • Check shapes before combining arrays
   • Understand operator meanings (* vs @)
   • NumPy operations are the preferred approach

✅ EXAMPLES OF VECTORIZATION:
   • array * 2 + 5 (instead of loop)
   • array[array > 20] (instead of if loop)
   • array1 * array2 (instead of element loop)
   • np.sum(array) (instead of loop sum)

✅ PERFORMANCE:
   • Vectorized: 50-1000x faster
   • Less code to write and maintain
   • Easier to understand intent
   • Scales better to large datasets
""")

print("=" * 80)
print("ASSIGNMENT COMPLETION: ALL REQUIREMENTS MET")
print("=" * 80)
