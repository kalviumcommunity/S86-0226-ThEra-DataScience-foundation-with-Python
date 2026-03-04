"""
NumPy Arrays Arithmetic Operations Milestone

This script demonstrates fundamental mathematical operations on NumPy arrays.
NumPy allows you to apply operations to entire arrays at once, making numerical 
computation faster, cleaner, and more expressive than using Python loops or lists.

Learning Objectives:
✓ Perform arithmetic operations on NumPy arrays
✓ Understand element-wise computation
✓ Apply scalar operations to arrays
✓ Compare array math with Python list behavior
✓ Avoid common mistakes with array math

Author: Data Science Foundation Student
Date: March 4, 2026
"""

import numpy as np


# ============================================================================
# SECTION 1: Element-Wise Array Operations
# ============================================================================

def element_wise_operations():
    """
    Demonstrate how NumPy applies arithmetic operations element-by-element.
    
    Key Insight: Element-wise operations apply the operation to corresponding
    elements in two arrays, producing a new array of the same shape.
    """
    
    print("\n" + "="*80)
    print("SECTION 1: ELEMENT-WISE ARRAY OPERATIONS")
    print("="*80)
    
    # Create two arrays of the same shape
    array1 = np.array([10, 20, 30, 40, 50])
    array2 = np.array([2, 4, 5, 5, 10])
    
    print("\n📌 Array 1:", array1)
    print("📌 Array 2:", array2)
    print("   Shape of both arrays: (5,)")
    
    # ADDITION
    print("\n" + "-"*80)
    print("1️⃣  ADDITION: array1 + array2")
    print("-"*80)
    addition_result = array1 + array2
    print(f"   Operation: {array1} + {array2}")
    print(f"   Result:    {addition_result}")
    print("   💡 Each element in array1 is added to the corresponding element in array2")
    
    # SUBTRACTION
    print("\n" + "-"*80)
    print("2️⃣  SUBTRACTION: array1 - array2")
    print("-"*80)
    subtraction_result = array1 - array2
    print(f"   Operation: {array1} - {array2}")
    print(f"   Result:    {subtraction_result}")
    print("   💡 Each element in array2 is subtracted from the corresponding element in array1")
    
    # MULTIPLICATION
    print("\n" + "-"*80)
    print("3️⃣  MULTIPLICATION: array1 * array2")
    print("-"*80)
    multiplication_result = array1 * array2
    print(f"   Operation: {array1} * {array2}")
    print(f"   Result:    {multiplication_result}")
    print("   💡 Corresponding elements are multiplied together")
    print("   ⚠️  NOTE: This is element-wise multiplication, NOT matrix multiplication")
    
    # DIVISION
    print("\n" + "-"*80)
    print("4️⃣  DIVISION: array1 / array2")
    print("-"*80)
    division_result = array1 / array2
    print(f"   Operation: {array1} / {array2}")
    print(f"   Result:    {division_result}")
    print("   💡 Each element in array1 is divided by the corresponding element in array2")
    
    # EXPONENTIATION
    print("\n" + "-"*80)
    print("5️⃣  EXPONENTIATION: array1 ** 2")
    print("-"*80)
    power_result = array1 ** 2
    print(f"   Operation: {array1} ** 2")
    print(f"   Result:    {power_result}")
    print("   💡 Each element is raised to the power of 2")
    
    # FLOOR DIVISION
    print("\n" + "-"*80)
    print("6️⃣  FLOOR DIVISION: array1 // array2")
    print("-"*80)
    floor_div_result = array1 // array2
    print(f"   Operation: {array1} // {array2}")
    print(f"   Result:    {floor_div_result}")
    print("   💡 Division result is rounded down to the nearest integer")
    
    # MODULO
    print("\n" + "-"*80)
    print("7️⃣  MODULO (Remainder): array1 % array2")
    print("-"*80)
    modulo_result = array1 % array2
    print(f"   Operation: {array1} % {array2}")
    print(f"   Result:    {modulo_result}")
    print("   💡 Returns the remainder after division")
    

# ============================================================================
# SECTION 2: Scalar Operations on Arrays
# ============================================================================

def scalar_operations():
    """
    Demonstrate how scalar (single value) operations are broadcast across arrays.
    
    Key Insight: When you apply a scalar to an array, the operation is applied to
    every element in the array. This is called "broadcasting".
    """
    
    print("\n" + "="*80)
    print("SECTION 2: SCALAR OPERATIONS ON ARRAYS")
    print("="*80)
    
    # Create an array
    array = np.array([10, 20, 30, 40, 50])
    scalar = 5
    
    print(f"\n📌 Array:  {array}")
    print(f"📌 Scalar: {scalar}")
    
    # SCALAR ADDITION
    print("\n" + "-"*80)
    print("1️⃣  SCALAR ADDITION: array + scalar")
    print("-"*80)
    scalar_add = array + scalar
    print(f"   Operation: {array} + {scalar}")
    print(f"   Result:    {scalar_add}")
    print("   💡 The scalar {scalar} is added to EACH element: [10+5, 20+5, 30+5, ...]")
    
    # SCALAR SUBTRACTION
    print("\n" + "-"*80)
    print("2️⃣  SCALAR SUBTRACTION: array - scalar")
    print("-"*80)
    scalar_sub = array - scalar
    print(f"   Operation: {array} - {scalar}")
    print(f"   Result:    {scalar_sub}")
    print(f"   💡 The scalar {scalar} is subtracted from EACH element")
    
    # SCALAR MULTIPLICATION
    print("\n" + "-"*80)
    print("3️⃣  SCALAR MULTIPLICATION: array * scalar")
    print("-"*80)
    scalar_mul = array * scalar
    print(f"   Operation: {array} * {scalar}")
    print(f"   Result:    {scalar_mul}")
    print(f"   💡 EACH element is multiplied by {scalar}")
    
    # SCALAR DIVISION
    print("\n" + "-"*80)
    print("4️⃣  SCALAR DIVISION: array / scalar")
    print("-"*80)
    scalar_div = array / scalar
    print(f"   Operation: {array} / {scalar}")
    print(f"   Result:    {scalar_div}")
    print(f"   💡 EACH element is divided by {scalar}")
    
    # REVERSE SCALAR OPERATIONS
    print("\n" + "-"*80)
    print("5️⃣  REVERSE OPERATIONS: scalar - array (order matters!)")
    print("-"*80)
    reverse_sub = scalar - array
    print(f"   Operation: {scalar} - {array}")
    print(f"   Result:    {reverse_sub}")
    print(f"   💡 The scalar is subtracted FROM, not by, each element")
    print(f"      Think of it as: [{scalar}-{array[0]}, {scalar}-{array[1]}, ...]")
    
    # REAL-WORLD EXAMPLE: Temperature Conversion
    print("\n" + "-"*80)
    print("📊 REAL-WORLD EXAMPLE: Temperature Conversion")
    print("-"*80)
    celsius_temps = np.array([0, 10, 20, 30, 40])
    fahrenheit_temps = (celsius_temps * 9/5) + 32
    print(f"\n   Celsius temperatures:    {celsius_temps}°C")
    print(f"   Fahrenheit temperatures: {fahrenheit_temps}°F")
    print("   💡 Formula applied to entire array at once!")
    

# ============================================================================
# SECTION 3: Comparing NumPy Arrays and Python Lists
# ============================================================================

def compare_arrays_and_lists():
    """
    Highlight the critical differences between NumPy array math and Python list math.
    
    Key Insight: Python lists and NumPy arrays have very different behavior for
    arithmetic operations. Understanding these differences is crucial!
    """
    
    print("\n" + "="*80)
    print("SECTION 3: COMPARING NUMPY ARRAYS AND PYTHON LISTS")
    print("="*80)
    
    # Create parallel structures
    python_list1 = [10, 20, 30, 40, 50]
    python_list2 = [2, 4, 5, 5, 10]
    numpy_array1 = np.array(python_list1)
    numpy_array2 = np.array(python_list2)
    
    print(f"\n📌 Python Lists:    {python_list1} and {python_list2}")
    print(f"📌 NumPy Arrays:    {numpy_array1} and {numpy_array2}")
    
    # ADDITION COMPARISON
    print("\n" + "-"*80)
    print("1️⃣  ADDITION BEHAVIOR")
    print("-"*80)
    print("\n   Python Lists: Addition CONCATENATES (joins lists together)")
    list_add = python_list1 + python_list2
    print(f"   {python_list1} + {python_list2}")
    print(f"   Result: {list_add}")
    print(f"   ⚠️  This created a list with {len(list_add)} elements (concatenation)")
    
    print("\n   NumPy Arrays: Addition ADDS ELEMENTS TOGETHER (element-wise)")
    array_add = numpy_array1 + numpy_array2
    print(f"   {numpy_array1} + {numpy_array2}")
    print(f"   Result: {array_add}")
    print(f"   ✓ This adds corresponding elements: [10+2, 20+4, 30+5, ...]")
    
    # MULTIPLICATION COMPARISON
    print("\n" + "-"*80)
    print("2️⃣  MULTIPLICATION BEHAVIOR")
    print("-"*80)
    print("\n   Python Lists: Multiplication REPEATS (duplicates the list)")
    list_mul = python_list1 * 2
    print(f"   {python_list1} * 2")
    print(f"   Result: {list_mul}")
    print(f"   ⚠️  This created a list with {len(list_mul)} elements (repetition)")
    
    print("\n   NumPy Arrays: Multiplication MULTIPLIES ELEMENTS (element-wise)")
    array_mul = numpy_array1 * 2
    print(f"   {numpy_array1} * 2")
    print(f"   Result: {array_mul}")
    print(f"   ✓ This multiplies each element by 2: [10*2, 20*2, 30*2, ...]")
    
    # SUBTRACTION & DIVISION (NOT AVAILABLE FOR LISTS)
    print("\n" + "-"*80)
    print("3️⃣  SUBTRACTION & DIVISION (Only in NumPy)")
    print("-"*80)
    print("\n   Python Lists: Subtraction and division are NOT supported")
    print("   ❌ python_list1 - python_list2  → TypeError!")
    print("   ❌ python_list1 / python_list2  → TypeError!")
    
    print("\n   NumPy Arrays: Subtraction and division work element-wise")
    array_sub = numpy_array1 - numpy_array2
    array_div = numpy_array1 / numpy_array2
    print(f"   {numpy_array1} - {numpy_array2}")
    print(f"   Result: {array_sub}")
    print(f"\n   {numpy_array1} / {numpy_array2}")
    print(f"   Result: {array_div}")
    
    # SUMMARY
    print("\n" + "-"*80)
    print("📊 SUMMARY TABLE: Lists vs Arrays")
    print("-"*80)
    print(f"{'Operation':<20} {'Python List':<30} {'NumPy Array':<30}")
    print("-" * 80)
    print(f"{'l1 + l2':<20} {'Concatenates':<30} {'Adds element-wise':<30}")
    print(f"{'l1 * 2':<20} {'Repeats list':<30} {'Multiplies each element':<30}")
    print(f"{'l1 - l2':<20} {'❌ Not supported':<30} {'Subtracts element-wise':<30}")
    print(f"{'l1 / l2':<20} {'❌ Not supported':<30} {'Divides element-wise':<30}")
    print(f"{'Speed':<20} {'Slower':<30} {'Much faster':<30}")
    
    print("\n💡 KEY TAKEAWAY: Use NumPy arrays for numerical operations, not lists!")
    

# ============================================================================
# SECTION 4: Avoiding Common Mistakes
# ============================================================================

def common_mistakes():
    """
    Identify and explain common errors when working with NumPy arrays.
    
    Key Insight: Shape mismatch and data type issues are the most common problems.
    """
    
    print("\n" + "="*80)
    print("SECTION 4: AVOIDING COMMON MISTAKES")
    print("="*80)
    
    # MISTAKE 1: Shape Mismatch
    print("\n" + "-"*80)
    print("❌ MISTAKE 1: Shape Mismatch")
    print("-"*80)
    print("\n   Problem: Trying to add/subtract arrays with different shapes")
    array1 = np.array([1, 2, 3])
    array2 = np.array([1, 2, 3, 4])
    
    print(f"\n   Array 1 shape: {array1.shape} → {array1}")
    print(f"   Array 2 shape: {array2.shape} → {array2}")
    print(f"\n   ❌ array1 + array2 → ValueError: operands could not be broadcast together")
    print("\n   ✅ Solution: Ensure arrays have the same shape")
    print(f"      array1_resized = array1[:4]  # Keep only first 4 elements")
    array1_resized = array1[:3]  # This works with matching size
    print(f"      Result: {array1_resized} + {array2[:3]} = {array1_resized + array2[:3]}")
    
    # MISTAKE 2: Confusing Array Operations with Matrix Operations
    print("\n" + "-"*80)
    print("❌ MISTAKE 2: Array Multiplication vs Matrix Multiplication")
    print("-"*80)
    print("\n   Problem: Expecting * to perform matrix multiplication (it doesn't)")
    matrix1 = np.array([[1, 2], [3, 4]])
    matrix2 = np.array([[5, 6], [7, 8]])
    
    print(f"\n   Matrix 1:\n{matrix1}")
    print(f"\n   Matrix 2:\n{matrix2}")
    print(f"\n   matrix1 * matrix2 (Element-wise multiplication):")
    print(matrix1 * matrix2)
    print(f"\n   ✅ For matrix multiplication, use: np.dot(matrix1, matrix2)")
    print(f"      or matrix1 @ matrix2")
    print(f"\n   Result of matrix multiplication:")
    print(np.dot(matrix1, matrix2))
    
    # MISTAKE 3: Type Coercion Issues
    print("\n" + "-"*80)
    print("❌ MISTAKE 3: Unexpected Data Type Conversions")
    print("-"*80)
    print("\n   Problem: Operations on mismatched types can cause unexpected results")
    int_array = np.array([1, 2, 3], dtype=int)
    float_array = np.array([1.5, 2.5, 3.5], dtype=float)
    
    print(f"\n   Integer array: {int_array} (dtype: {int_array.dtype})")
    print(f"   Float array:   {float_array} (dtype: {float_array.dtype})")
    
    result = int_array + float_array
    print(f"\n   int_array + float_array = {result}")
    print(f"   Result dtype:             {result.dtype}")
    print(f"\n   ✅ Best practice: Be aware of data types when combining arrays")
    print(f"      Use explicit conversion if needed: np.array([1,2,3], dtype=float)")
    
    # MISTAKE 4: Modifying Original Array (when you didn't intend to)
    print("\n" + "-"*80)
    print("❌ MISTAKE 4: Array Reference vs Copy")
    print("-"*80)
    print("\n   Problem: Operations don't always create new arrays")
    original = np.array([1, 2, 3])
    
    print(f"\n   Original array: {original}")
    
    # Assignment creates a reference, not a copy
    reference = original
    reference[0] = 999
    print(f"   After reference[0] = 999:")
    print(f"   Original array: {original} ← Changed! (it was a reference)")
    
    # Arithmetic operations DO create new arrays
    original2 = np.array([1, 2, 3])
    result = original2 + 10
    print(f"\n   Original array 2: {original2}")
    print(f"   result = original2 + 10")
    print(f"   result = {result}")
    print(f"   Original array 2: {original2} ← Unchanged! (arithmetic created new array)")
    
    print(f"\n   ✅ Solution: Use .copy() to create independent copies")
    copy_array = original2.copy()
    copy_array[0] = 999
    print(f"      copy_array = original2.copy()")
    print(f"      Original array 2: {original2} ← Still unchanged")
    
    # MISTAKE 5: Assuming Loop-Free Code is Always Better
    print("\n" + "-"*80)
    print("ℹ️  BEST PRACTICE: Use NumPy for Numerical Operations")
    print("-"*80)
    print("\n   ❌ DON'T: Use loops for simple array math")
    print("      for i in range(len(array1)):")
    print("          result[i] = array1[i] + array2[i]  # Slow!")
    
    print("\n   ✅ DO: Use NumPy operations")
    print("      result = array1 + array2  # Fast and readable!")
    

# ============================================================================
# SECTION 5: Practical Applications
# ============================================================================

def practical_applications():
    """
    Show real-world examples where array math is essential.
    """
    
    print("\n" + "="*80)
    print("SECTION 5: PRACTICAL APPLICATIONS")
    print("="*80)
    
    # APPLICATION 1: Scaling values
    print("\n" + "-"*80)
    print("📊 APPLICATION 1: Normalizing (Scaling) Data")
    print("-"*80)
    
    # Raw test scores
    test_scores = np.array([45, 67, 89, 92, 78, 55, 88])
    print(f"\n   Raw test scores: {test_scores}")
    
    # Normalize to 0-100 scale if out of range, or scale to percentage
    min_score = test_scores.min()
    max_score = test_scores.max()
    normalized = ((test_scores - min_score) / (max_score - min_score)) * 100
    
    print(f"   Min score: {min_score}, Max score: {max_score}")
    print(f"   Normalized (0-100%): {normalized.astype(int)}")
    
    # APPLICATION 2: Computing statistics
    print("\n" + "-"*80)
    print("📊 APPLICATION 2: Computing Statistics")
    print("-"*80)
    
    daily_sales = np.array([1200, 1500, 1100, 1800, 2000, 1300, 1700])
    print(f"\n   Daily sales (7 days): {daily_sales}")
    
    total_sales = daily_sales.sum()
    average_sales = daily_sales.mean()
    max_sales = daily_sales.max()
    min_sales = daily_sales.min()
    
    print(f"   Total sales:   ${total_sales:,}")
    print(f"   Average sales: ${average_sales:,.0f}")
    print(f"   Highest day:   ${max_sales:,}")
    print(f"   Lowest day:    ${min_sales:,}")
    
    # APPLICATION 3: Element-wise comparisons
    print("\n" + "-"*80)
    print("📊 APPLICATION 3: Element-wise Comparisons")
    print("-"*80)
    
    target = 1500
    print(f"\n   Daily sales: {daily_sales}")
    print(f"   Target:      {target}")
    print(f"\n   Which days exceeded target?")
    exceeded = daily_sales > target
    print(f"   Boolean array: {exceeded}")
    print(f"   Days that exceeded target: {np.sum(exceeded)} out of {len(daily_sales)}")
    print(f"   Amount above/below target: {daily_sales - target}")
    
    # APPLICATION 4: Batch calculations
    print("\n" + "-"*80)
    print("📊 APPLICATION 4: Batch Calculations (e.g., Discount Application)")
    print("-"*80)
    
    original_prices = np.array([99.99, 149.99, 199.99, 79.99, 299.99])
    discount_rate = 0.20  # 20% off
    
    print(f"\n   Original prices: ${original_prices}")
    print(f"   Discount rate:   {discount_rate*100}%")
    
    discount_amount = original_prices * discount_rate
    final_prices = original_prices - discount_amount
    
    print(f"   Discount amounts: ${discount_amount}")
    print(f"   Final prices:     ${final_prices}")
    

# ============================================================================
# MAIN FUNCTION
# ============================================================================

def main():
    """
    Execute all sections of the NumPy array arithmetic milestone.
    """
    
    print("\n")
    print("╔" + "="*78 + "╗")
    print("║" + " "*78 + "║")
    print("║" + "  NUMPY ARRAYS ARITHMETIC OPERATIONS - COMPREHENSIVE MILESTONE".center(78) + "║")
    print("║" + " "*78 + "║")
    print("╚" + "="*78 + "╝")
    
    # Execute all sections
    element_wise_operations()
    scalar_operations()
    compare_arrays_and_lists()
    common_mistakes()
    practical_applications()
    
    # Closing message
    print("\n" + "="*80)
    print("MILESTONE SUMMARY")
    print("="*80)
    print("""
✅ You've learned:
   1. Element-wise operations (add, subtract, multiply, divide, power, etc.)
   2. Scalar operations (broadcasting) on arrays
   3. Differences between NumPy arrays and Python lists
   4. Common mistakes and how to avoid them
   5. Real-world applications of array arithmetic

💡 Key Takeaways:
   • NumPy enables fast, vectorized mathematical operations
   • Element-wise operations apply to corresponding elements
   • Broadcasting applies scalars to every array element
   • NumPy is designed for numerical computation, lists are not
   • Always check array shapes before operations
   • Use NumPy operations instead of loops for better performance

🎯 Next Steps:
   • Practice these operations with your own data
   • Explore more advanced NumPy functions (sum, mean, std, etc.)
   • Apply these skills to real datasets
   • Learn about matrix operations and linear algebra with NumPy
    """)
    print("="*80)


if __name__ == "__main__":
    main()
