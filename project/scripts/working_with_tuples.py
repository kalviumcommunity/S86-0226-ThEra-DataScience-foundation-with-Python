"""
Working with Python Tuples
==========================
This script demonstrates core tuple operations including:
- Creating tuples with fixed values
- Accessing elements using indexing
- Observing immutability behavior
- Understanding when tuples are preferred
"""

# 1. Creating Tuples
print("=" * 50)
print("1. CREATING TUPLES")
print("=" * 50)

# Tuple of coordinates (x, y)
coordinates = (10, 20)
print(f"Coordinates: {coordinates}")

# Tuple of RGB color values
color_rgb = (255, 128, 64)
print(f"RGB Color: {color_rgb}")

# Tuple of mixed data types
person_info = ("Alice", 25, "Engineer", True)
print(f"Person Info: {person_info}")

# Single element tuple (note the comma!)
single_element = (42,)
print(f"Single Element Tuple: {single_element}")
print(f"Type: {type(single_element)}")

# Without comma, it's not a tuple
not_a_tuple = (42)
print(f"Not a Tuple: {not_a_tuple}")
print(f"Type: {type(not_a_tuple)}")

# Tuple without parentheses (tuple packing)
packed_tuple = 1, 2, 3, 4
print(f"Packed Tuple: {packed_tuple}")

# Empty tuple
empty_tuple = ()
print(f"Empty Tuple: {empty_tuple}")

print()

# 2. Accessing Elements using Indexes
print("=" * 50)
print("2. ACCESSING ELEMENTS")
print("=" * 50)

days_of_week = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print(f"Days of Week: {days_of_week}")

# Accessing individual elements
print(f"First day: {days_of_week[0]}")
print(f"Last day: {days_of_week[-1]}")
print(f"Middle day: {days_of_week[3]}")

# Slicing tuples
print(f"Weekdays: {days_of_week[0:5]}")
print(f"Weekend: {days_of_week[5:]}")
print(f"First three days: {days_of_week[:3]}")

# Unpacking tuples
monday, tuesday, *rest = days_of_week
print(f"Unpacked - Monday: {monday}, Tuesday: {tuesday}")
print(f"Rest of the days: {rest}")

print()

# 3. Demonstrating Immutability
print("=" * 50)
print("3. IMMUTABILITY BEHAVIOR")
print("=" * 50)

# Tuples cannot be modified
numbers_tuple = (1, 2, 3, 4, 5)
print(f"Original tuple: {numbers_tuple}")

# Attempting to modify will cause an error
print("\nTrying to modify tuple element...")
try:
    numbers_tuple[0] = 10
    print("Modified successfully")
except TypeError as e:
    print(f"❌ Error: {e}")
    print("✓ Tuples are IMMUTABLE - cannot change elements")

# Attempting to append will cause an error
print("\nTrying to append to tuple...")
try:
    numbers_tuple.append(6)
    print("Appended successfully")
except AttributeError as e:
    print(f"❌ Error: {e}")
    print("✓ Tuples don't have append() method")

# Attempting to remove will cause an error
print("\nTrying to remove from tuple...")
try:
    numbers_tuple.remove(3)
    print("Removed successfully")
except AttributeError as e:
    print(f"❌ Error: {e}")
    print("✓ Tuples don't have remove() method")

print("\n✓ Once a tuple is created, its elements cannot be changed, added, or removed")

print()

# 4. Operations You CAN Perform on Tuples
print("=" * 50)
print("4. VALID TUPLE OPERATIONS")
print("=" * 50)

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

# Concatenation - creates a NEW tuple
combined = tuple1 + tuple2
print(f"tuple1: {tuple1}")
print(f"tuple2: {tuple2}")
print(f"Combined (tuple1 + tuple2): {combined}")

# Repetition
repeated = tuple1 * 3
print(f"Repeated (tuple1 * 3): {repeated}")

# Length
print(f"Length of combined: {len(combined)}")

# Count occurrences
sample = (1, 2, 2, 3, 2, 4, 2)
print(f"Sample tuple: {sample}")
print(f"Count of 2: {sample.count(2)}")

# Find index
print(f"Index of 3: {sample.index(3)}")

# Membership testing
print(f"Is 3 in sample? {3 in sample}")
print(f"Is 10 in sample? {10 in sample}")

# Min and Max
numbers = (45, 12, 78, 23, 56)
print(f"Numbers: {numbers}")
print(f"Min: {min(numbers)}")
print(f"Max: {max(numbers)}")
print(f"Sum: {sum(numbers)}")

print()

# 5. Iterating Over Tuples
print("=" * 50)
print("5. ITERATING OVER TUPLES")
print("=" * 50)

months = ("January", "February", "March", "April", "May", "June")

# Simple iteration
print("Months:")
for month in months:
    print(f"  - {month}")

print()

# Iteration with index
print("Months with index:")
for index, month in enumerate(months, start=1):
    print(f"  Month {index}: {month}")

print()

# 6. Tuple Unpacking in Practice
print("=" * 50)
print("6. TUPLE UNPACKING")
print("=" * 50)

# Function returning multiple values (as a tuple)
def get_student_info():
    name = "Bob"
    age = 20
    grade = "A"
    return name, age, grade  # Returns a tuple

# Unpacking the returned tuple
student_name, student_age, student_grade = get_student_info()
print(f"Name: {student_name}")
print(f"Age: {student_age}")
print(f"Grade: {student_grade}")

# Swapping variables using tuple unpacking
x = 10
y = 20
print(f"\nBefore swap: x = {x}, y = {y}")
x, y = y, x  # Tuple packing and unpacking
print(f"After swap: x = {x}, y = {y}")

print()

# 7. When to Use Tuples
print("=" * 50)
print("7. WHEN TO USE TUPLES")
print("=" * 50)

# Tuples for fixed data (database records, API responses)
database_record = ("EMP001", "John Doe", "Engineering", 75000)
print(f"Database Record: {database_record}")

# Tuples as dictionary keys (must be immutable)
locations = {
    (40.7128, -74.0060): "New York",
    (51.5074, -0.1278): "London",
    (35.6762, 139.6503): "Tokyo"
}
print(f"\nLocations dictionary (with tuple keys):")
for coords, city in locations.items():
    print(f"  {coords} -> {city}")

# Tuples for data that shouldn't change
DAYS_IN_WEEK = 7
MONTHS_IN_YEAR = 12
HOURS_IN_DAY = 24
CONFIG = (DAYS_IN_WEEK, MONTHS_IN_YEAR, HOURS_IN_DAY)
print(f"\nConstant Configuration: {CONFIG}")

print()

# 8. Tuples vs Lists - Performance
print("=" * 50)
print("8. TUPLES VS LISTS")
print("=" * 50)

import sys

list_example = [1, 2, 3, 4, 5]
tuple_example = (1, 2, 3, 4, 5)

print(f"List size: {sys.getsizeof(list_example)} bytes")
print(f"Tuple size: {sys.getsizeof(tuple_example)} bytes")
print("✓ Tuples are slightly more memory-efficient")

print()

# 9. Key Takeaways
print("=" * 50)
print("KEY TAKEAWAYS ABOUT TUPLES")
print("=" * 50)
print("✓ Tuples are ORDERED - elements maintain their position")
print("✓ Tuples are IMMUTABLE - cannot be modified after creation")
print("✓ Tuples allow DUPLICATES - same value can appear multiple times")
print("✓ Tuples use INDEXING - access elements by position (0-based)")
print("✓ Tuples are more MEMORY-EFFICIENT than lists")
print("✓ Tuples can be used as DICTIONARY KEYS (lists cannot)")
print("✓ Use tuples when data should NOT change (integrity)")
print("✓ Use tuples for returning multiple values from functions")
print("✓ Use tuples for fixed collections (coordinates, RGB values, etc.)")
