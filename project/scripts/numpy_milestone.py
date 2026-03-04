"""
NumPy Arrays Milestone - Creating Arrays from Python Lists

This script demonstrates the fundamentals of NumPy arrays:
- Converting Python lists to NumPy arrays
- Understanding array properties (shape, dtype, dimensions)
- Performing basic array operations
- Comparing arrays with lists

Author: Your Name
Date: March 4, 2026
"""

import numpy as np


# ============================================================================
# SECTION 1: Understanding NumPy Arrays vs Python Lists
# ============================================================================

def demonstrate_arrays_vs_lists():
    """
    Show the fundamental difference between Python lists and NumPy arrays.
    Arrays are homogeneous (same data type) and optimized for numerical operations.
    """
    
    print("=" * 70)
    print("SECTION 1: NumPy Arrays vs Python Lists")
    print("=" * 70)
    
    # Python list - can contain mixed types
    python_list = [1, 2, 3, 4, 5]
    print("\n📌 Python List:")
    print(f"   List: {python_list}")
    print(f"   Type: {type(python_list)}")
    
    # NumPy array - homogeneous, optimized for numerical operations
    numpy_array = np.array([1, 2, 3, 4, 5])
    print("\n📌 NumPy Array:")
    print(f"   Array: {numpy_array}")
    print(f"   Type: {type(numpy_array)}")
    print(f"   Data type: {numpy_array.dtype}")
    
    print("\n💡 Key Insight: Arrays are faster and more memory-efficient for")
    print("   numerical computations than Python lists.")
    print()


# ============================================================================
# SECTION 2: Creating NumPy Arrays from Lists
# ============================================================================

def create_arrays_from_lists():
    """
    Demonstrate how to create both 1D and multi-dimensional arrays from lists.
    This is the core skill for transitioning from Python lists to NumPy.
    """
    
    print("=" * 70)
    print("SECTION 2: Creating NumPy Arrays from Lists")
    print("=" * 70)
    
    # Creating 1D arrays
    print("\n✅ Creating 1D Arrays:")
    
    # Integer array
    int_array = np.array([10, 20, 30, 40, 50])
    print(f"\n   Integer array: {int_array}")
    print(f"   Data type: {int_array.dtype}")
    
    # Float array
    float_array = np.array([1.5, 2.7, 3.9, 4.1, 5.3])
    print(f"\n   Float array: {float_array}")
    print(f"   Data type: {float_array.dtype}")
    
    # Creating 2D arrays from nested lists
    print("\n✅ Creating 2D Arrays (Multi-dimensional):")
    
    # Simple 2D array (matrix-like structure)
    array_2d = np.array([[1, 2, 3],
                         [4, 5, 6],
                         [7, 8, 9]])
    print(f"\n   2D Array:")
    print(array_2d)
    print(f"   Data type: {array_2d.dtype}")
    
    # Real-world example: student scores across subjects
    print("\n📊 Real-world Example - Student Scores:")
    student_scores = np.array([[85, 90, 78],   # Student 1: Math, Science, English
                               [92, 88, 95],   # Student 2
                               [78, 85, 82]])  # Student 3
    print("   Student scores (rows=students, columns=subjects):")
    print(student_scores)
    print()


# ============================================================================
# SECTION 3: Inspecting Array Properties
# ============================================================================

def inspect_array_properties():
    """
    Understand array structure by examining shape, dimensions, size, and dtype.
    These properties are critical for debugging and data manipulation.
    """
    
    print("=" * 70)
    print("SECTION 3: Inspecting Array Properties")
    print("=" * 70)
    
    # 1D array properties
    print("\n📏 1D Array Properties:")
    array_1d = np.array([5, 10, 15, 20, 25, 30])
    print(f"   Array: {array_1d}")
    print(f"   Shape: {array_1d.shape} → (6 elements in 1 dimension)")
    print(f"   Dimensions (ndim): {array_1d.ndim}")
    print(f"   Size (total elements): {array_1d.size}")
    print(f"   Data type: {array_1d.dtype}")
    
    # 2D array properties
    print("\n📏 2D Array Properties:")
    array_2d = np.array([[10, 20, 30, 40],
                         [50, 60, 70, 80],
                         [90, 100, 110, 120]])
    print(f"   Array:")
    print(f"{array_2d}")
    print(f"   Shape: {array_2d.shape} → (3 rows, 4 columns)")
    print(f"   Dimensions (ndim): {array_2d.ndim}")
    print(f"   Size (total elements): {array_2d.size}")
    print(f"   Data type: {array_2d.dtype}")
    
    # 3D array properties (advanced glimpse)
    print("\n📏 3D Array Properties (Advanced):")
    array_3d = np.array([[[1, 2], [3, 4]],
                         [[5, 6], [7, 8]]])
    print(f"   Shape: {array_3d.shape} → (2 matrices, 2 rows, 2 columns)")
    print(f"   Dimensions (ndim): {array_3d.ndim}")
    print(f"   Size (total elements): {array_3d.size}")
    
    print("\n💡 Key Insight: Shape tells you the structure; dtype tells you")
    print("   what kind of data is stored.")
    print()


# ============================================================================
# SECTION 4: Basic Operations on Arrays
# ============================================================================

# ============================================================================
# SECTION 4A: Accessing Elements and Visualizing Array Layout
# ============================================================================

def access_elements_and_visualize():
    """
    Demonstrate accessing elements in 1D and 2D arrays and visualize their layout.
    """
    print("=" * 70)
    print("SECTION 4A: Accessing Elements and Visualizing Array Layout")
    print("=" * 70)

    # 1D Array
    arr_1d = np.array([10, 20, 30, 40, 50])
    print("\n🔹 1D Array:")
    print(f"   Array: {arr_1d}")
    print("   Index positions:  0   1   2   3   4")
    print("   Values:          10  20  30  40  50")
    print(f"   arr_1d[2] = {arr_1d[2]}  # Access value at index 2")
    print(f"   arr_1d[-1] = {arr_1d[-1]}  # Access last element (negative index)")

    # 2D Array
    arr_2d = np.array([[1, 2, 3],
                       [4, 5, 6],
                       [7, 8, 9]])
    print("\n🔹 2D Array:")
    print(arr_2d)
    print("   Row indices:    0    1    2")
    print("   Col indices:  0  1  2")
    print("   Accessing arr_2d[1, 2] (row 1, col 2):", arr_2d[1, 2])
    print("   Accessing arr_2d[0, 0] (row 0, col 0):", arr_2d[0, 0])
    print("   Accessing arr_2d[-1, -1] (last row, last col):", arr_2d[-1, -1])

    print("\n💡 Visualization:")
    print("   Array as a grid (row, col):")
    print("     [ [1, 2, 3],   # row 0")
    print("       [4, 5, 6],   # row 1")
    print("       [7, 8, 9] ]  # row 2")
    print("   arr_2d[1, 2] → 6 (row 1, col 2)")
    print("   arr_2d[2, 0] → 7 (row 2, col 0)")
    print("   arr_2d[0, 1] → 2 (row 0, col 1)")

    print("\n⚠️  Remember: Indexing is zero-based. arr_2d[3, 0] would cause an IndexError!")
    print()

def basic_array_operations():
    """
    Perform simple arithmetic operations on arrays.
    NumPy performs element-wise operations automatically.
    """
    
    print("=" * 70)
    print("SECTION 4: Basic Operations on Arrays")
    print("=" * 70)
    
    # Element-wise operations
    print("\n➕ Element-wise Arithmetic:")
    
    array_a = np.array([10, 20, 30, 40])
    array_b = np.array([1, 2, 3, 4])
    
    print(f"   Array A: {array_a}")
    print(f"   Array B: {array_b}")
    
    # Addition
    print(f"\n   A + B = {array_a + array_b}")
    
    # Subtraction
    print(f"   A - B = {array_a - array_b}")
    
    # Multiplication
    print(f"   A * B = {array_a * array_b}")
    
    # Division
    print(f"   A / B = {array_a / array_b}")
    
    # Scalar operations
    print("\n🔢 Scalar Operations (Broadcasting):")
    array_c = np.array([5, 10, 15, 20])
    print(f"   Array C: {array_c}")
    print(f"   C * 2 = {array_c * 2}")
    print(f"   C + 10 = {array_c + 10}")
    print(f"   C ** 2 = {array_c ** 2} (squaring each element)")
    
    # Aggregation functions
    print("\n📊 Aggregation Functions:")
    data = np.array([12, 45, 23, 67, 89, 34])
    print(f"   Data: {data}")
    print(f"   Sum: {data.sum()}")
    print(f"   Mean: {data.mean()}")
    print(f"   Max: {data.max()}")
    print(f"   Min: {data.min()}")
    print(f"   Standard deviation: {data.std():.2f}")
    print()


# ============================================================================
# SECTION 5: Arrays vs Lists for Numerical Operations
# ============================================================================

def compare_arrays_and_lists():
    """
    Directly compare how arrays and lists handle numerical operations.
    This highlights why NumPy is preferred for numerical computing.
    """
    
    print("=" * 70)
    print("SECTION 5: Arrays vs Lists - Numerical Operations")
    print("=" * 70)
    
    # Python list behavior
    print("\n⚠️  Python List Behavior:")
    list_a = [1, 2, 3, 4]
    list_b = [10, 20, 30, 40]
    
    print(f"   List A: {list_a}")
    print(f"   List B: {list_b}")
    print(f"   A + B = {list_a + list_b} ← Concatenation, NOT element-wise addition!")
    print(f"   A * 2 = {list_a * 2} ← Replication, NOT multiplication!")
    
    # NumPy array behavior
    print("\n✅ NumPy Array Behavior:")
    array_a = np.array([1, 2, 3, 4])
    array_b = np.array([10, 20, 30, 40])
    
    print(f"   Array A: {array_a}")
    print(f"   Array B: {array_b}")
    print(f"   A + B = {array_a + array_b} ← Element-wise addition!")
    print(f"   A * 2 = {array_a * 2} ← Element-wise multiplication!")
    
    print("\n💡 Key Insight: Arrays provide mathematical operations directly,")
    print("   while lists require loops for element-wise operations.")
    print()


# ============================================================================
# SECTION 6: Practical Use Case - Data Analysis Preparation
# ============================================================================

def practical_use_case():
    """
    Show a practical scenario where arrays are essential for data preparation.
    """
    
    print("=" * 70)
    print("SECTION 6: Practical Use Case - Temperature Data Analysis")
    print("=" * 70)
    
    # Simulated temperature data (in Celsius) for a week
    temperatures_celsius = np.array([22, 24, 19, 25, 23, 20, 21])
    
    print("\n🌡️  Weekly Temperature Data (Celsius):")
    print(f"   Temperatures: {temperatures_celsius}")
    
    # Convert to Fahrenheit using vectorized operation
    temperatures_fahrenheit = (temperatures_celsius * 9/5) + 32
    print(f"\n   Converted to Fahrenheit: {temperatures_fahrenheit}")
    
    # Calculate statistics
    print("\n📊 Temperature Statistics:")
    print(f"   Average: {temperatures_celsius.mean():.2f}°C")
    print(f"   Maximum: {temperatures_celsius.max()}°C")
    print(f"   Minimum: {temperatures_celsius.min()}°C")
    print(f"   Range: {temperatures_celsius.max() - temperatures_celsius.min()}°C")
    
    # Find days above average
    average_temp = temperatures_celsius.mean()
    above_average = temperatures_celsius > average_temp
    print(f"\n   Days above average: {above_average}")
    print(f"   Number of days above average: {above_average.sum()}")
    
    print("\n💡 This operation would require loops with Python lists,")
    print("   but NumPy handles it in a single line!")
    print()


# ============================================================================
# MAIN EXECUTION
# ============================================================================

def run_all_examples():
    """Execute all milestone demonstrations in sequence."""
    
    print("\n" + "=" * 70)
    print("NUMPY ARRAYS MILESTONE - CREATING ARRAYS FROM PYTHON LISTS")
    print("=" * 70)
    print("\nThis demonstration covers:")
    print("  • Understanding NumPy arrays vs Python lists")
    print("  • Creating 1D and 2D arrays from lists")
    print("  • Inspecting array properties (shape, dtype, dimensions)")
    print("  • Performing basic numerical operations")
    print("  • Comparing array and list behaviors")
    print("  • Practical use case for data analysis")
    print()
    
    demonstrate_arrays_vs_lists()
    create_arrays_from_lists()
    inspect_array_properties()
    basic_array_operations()
    access_elements_and_visualize()
    compare_arrays_and_lists()
    practical_use_case()
    
    print("=" * 70)
    print("✅ MILESTONE COMPLETE!")
    print("=" * 70)
    print("\nYou have successfully:")
    print("  ✓ Imported NumPy")
    print("  ✓ Created arrays from Python lists")
    print("  ✓ Inspected array properties")
    print("  ✓ Performed basic operations")
    print("  ✓ Accessed elements and visualized array layout")
    print("  ✓ Understood arrays vs lists")
    print("\nYou're ready to work with real datasets using NumPy!")
    print()


if __name__ == "__main__":
    run_all_examples()
