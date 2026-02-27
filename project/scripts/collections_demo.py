"""
Python Collections Demo - Complete Overview
===========================================
This script provides a concise demonstration of all three collection types
for quick understanding and video walkthroughs.

This covers:
- Lists (mutable, ordered)
- Tuples (immutable, ordered)
- Dictionaries (key-value pairs)
"""

print("=" * 80)
print("PYTHON COLLECTIONS DEMONSTRATION")
print("=" * 80)
print()

# ============================================================================
# 1. LISTS - Dynamic Collections
# ============================================================================
print("┌" + "─" * 78 + "┐")
print("│" + " " * 30 + "1. LISTS" + " " * 38 + "│")
print("└" + "─" * 78 + "┘")
print()

# Creating a list
shopping_cart = ["Laptop", "Mouse", "Keyboard"]
print(f"Shopping Cart: {shopping_cart}")
print(f"Type: {type(shopping_cart)}")
print()

# Accessing elements
print(f"First item: {shopping_cart[0]}")
print(f"Last item: {shopping_cart[-1]}")
print()

# Modifying - Lists are MUTABLE
shopping_cart.append("Monitor")  # Add item
print(f"After adding Monitor: {shopping_cart}")

shopping_cart.remove("Mouse")  # Remove item
print(f"After removing Mouse: {shopping_cart}")

shopping_cart[0] = "Gaming Laptop"  # Modify item
print(f"After modifying first item: {shopping_cart}")
print()

# When to use lists
print("✓ Use Lists When:")
print("  • Items will be added, removed, or modified")
print("  • You need a dynamic collection")
print("  • Order matters and you access by position")
print()
print("Example Use Cases: shopping carts, task lists, sensor readings")
print()

# ============================================================================
# 2. TUPLES - Fixed Collections
# ============================================================================
print("┌" + "─" * 78 + "┐")
print("│" + " " * 30 + "2. TUPLES" + " " * 37 + "│")
print("└" + "─" * 78 + "┘")
print()

# Creating a tuple
coordinates = (40.7128, -74.0060)  # NYC coordinates
print(f"NYC Coordinates: {coordinates}")
print(f"Type: {type(coordinates)}")
print()

# Accessing elements
print(f"Latitude: {coordinates[0]}")
print(f"Longitude: {coordinates[1]}")
print()

# Demonstrating immutability
print("Attempting to modify tuple...")
try:
    coordinates[0] = 50.0  # This will fail
except TypeError as e:
    print(f"❌ Error: {e}")
    print("✓ Tuples are IMMUTABLE - cannot be changed after creation")
print()

# Tuple unpacking (common use case)
latitude, longitude = coordinates
print(f"Unpacked - Lat: {latitude}, Lon: {longitude}")
print()

# Multiple values from function (returns tuple)
def get_dimensions():
    width = 1920
    height = 1080
    return width, height  # Returns tuple

width, height = get_dimensions()
print(f"Screen dimensions: {width} x {height}")
print()

# When to use tuples
print("✓ Use Tuples When:")
print("  • Data should NOT change (immutability protects data)")
print("  • Returning multiple values from functions")
print("  • Using as dictionary keys")
print("  • Performance and memory are important")
print()
print("Example Use Cases: coordinates, RGB colors, dates, constant values")
print()

# ============================================================================
# 3. DICTIONARIES - Key-Value Pairs
# ============================================================================
print("┌" + "─" * 78 + "┐")
print("│" + " " * 27 + "3. DICTIONARIES" + " " * 34 + "│")
print("└" + "─" * 78 + "┘")
print()

# Creating a dictionary
student = {
    "name": "Alice Johnson",
    "age": 20,
    "major": "Computer Science",
    "gpa": 3.8
}
print(f"Student: {student}")
print(f"Type: {type(student)}")
print()

# Accessing values by key
print(f"Student Name: {student['name']}")
print(f"Student GPA: {student['gpa']}")
print()

# Safe access using .get()
print(f"Email (using .get()): {student.get('email', 'Not provided')}")
print()

# Modifying - Dictionaries are MUTABLE
student['gpa'] = 3.9  # Modify existing
print(f"After GPA update: {student['gpa']}")

student['email'] = "alice@example.com"  # Add new key
print(f"After adding email: {student['email']}")
print()

# Iterating over dictionary
print("All student information:")
for key, value in student.items():
    print(f"  {key}: {value}")
print()

# When to use dictionaries
print("✓ Use Dictionaries When:")
print("  • You need key-value associations")
print("  • Fast lookup by meaningful names (not just numbers)")
print("  • Representing objects with properties")
print("  • Counting, grouping, or mapping data")
print()
print("Example Use Cases: user profiles, configs, word counts, databases")
print()

# ============================================================================
# 4. SIDE-BY-SIDE COMPARISON
# ============================================================================
print("┌" + "─" * 78 + "┐")
print("│" + " " * 26 + "4. VISUAL COMPARISON" + " " * 31 + "│")
print("└" + "─" * 78 + "┘")
print()

# Same data in different structures
print("Storing the same data in different structures:")
print()

# As a list (positional access)
person_list = ["Bob", 25, "Engineer"]
print(f"List:       {person_list}")
print(f"Access:     person_list[0] = {person_list[0]}")
print(f"Problem:    What does index [1] represent? Not clear!")
print()

# As a tuple (positional access, immutable)
person_tuple = ("Bob", 25, "Engineer")
print(f"Tuple:      {person_tuple}")
print(f"Access:     person_tuple[0] = {person_tuple[0]}")
print(f"Benefit:    Cannot be accidentally modified")
print()

# As a dictionary (named access)
person_dict = {"name": "Bob", "age": 25, "job": "Engineer"}
print(f"Dictionary: {person_dict}")
print(f"Access:     person_dict['name'] = {person_dict['name']}")
print(f"Benefit:    Clear, self-documenting code!")
print()

# ============================================================================
# 5. PRACTICAL EXAMPLE - REAL-WORLD SCENARIO
# ============================================================================
print("┌" + "─" * 78 + "┐")
print("│" + " " * 24 + "5. REAL-WORLD EXAMPLE" + " " * 31 + "│")
print("└" + "─" * 78 + "┘")
print()

print("Scenario: Building a simple gradebook system")
print()

# List of student names (dynamic - students can be added/removed)
student_names = ["Alice", "Bob", "Charlie", "Diana"]
print(f"Students (List): {student_names}")
print("  → Can add/remove students as needed")
print()

# Tuple of subjects (fixed - subjects don't change mid-semester)
subjects = ("Math", "Science", "English", "History")
print(f"Subjects (Tuple): {subjects}")
print("  → Protected from accidental changes")
print()

# Dictionary of student grades (key-value mapping)
gradebook = {
    "Alice": 92,
    "Bob": 87,
    "Charlie": 95,
    "Diana": 88
}
print(f"Gradebook (Dictionary):")
for student, grade in gradebook.items():
    print(f"  {student}: {grade}")
print("  → Easy lookup by student name")
print()

# Adding a new student
student_names.append("Eve")
gradebook["Eve"] = 91
print(f"After adding Eve:")
print(f"  Students: {student_names}")
print(f"  Eve's grade: {gradebook['Eve']}")
print()

# ============================================================================
# 6. DECISION GUIDE
# ============================================================================
print("┌" + "─" * 78 + "┐")
print("│" + " " * 25 + "6. QUICK DECISION GUIDE" + " " * 29 + "│")
print("└" + "─" * 78 + "┘")
print()

decision_guide = """
╔═══════════════════════════════════════════════════════════════════════════╗
║                    WHICH DATA STRUCTURE SHOULD I USE?                     ║
╠═══════════════════════════════════════════════════════════════════════════╣
║                                                                           ║
║  Question 1: Do you need KEY-VALUE pairs?                                ║
║  ├─ YES → Use DICTIONARY                                                 ║
║  └─ NO  → Continue to Question 2                                         ║
║                                                                           ║
║  Question 2: Will the data CHANGE (add/remove/modify)?                   ║
║  ├─ YES → Use LIST                                                       ║
║  └─ NO  → Use TUPLE                                                      ║
║                                                                           ║
╠═══════════════════════════════════════════════════════════════════════════╣
║                              QUICK SUMMARY                                ║
╠═══════════════════════════════════════════════════════════════════════════╣
║                                                                           ║
║  📋 LIST        [1, 2, 3]          Mutable, Ordered        Dynamic data  ║
║  📌 TUPLE       (1, 2, 3)          Immutable, Ordered      Fixed data    ║
║  📚 DICTIONARY  {'a': 1, 'b': 2}   Mutable, Key-Value      Named data    ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
"""

print(decision_guide)

# ============================================================================
# CONCLUSION
# ============================================================================
print()
print("=" * 80)
print("CONCLUSION")
print("=" * 80)
print()
print("✅ Lists are for DYNAMIC collections (shopping carts, task lists)")
print("✅ Tuples are for FIXED data that shouldn't change (coordinates, dates)")
print("✅ Dictionaries are for KEY-VALUE associations (user profiles, configs)")
print()
print("Master these three structures and you'll be able to handle any data!")
print()
print("=" * 80)
print("For more details, run the individual scripts:")
print("  - working_with_lists.py")
print("  - working_with_tuples.py")
print("  - working_with_dictionaries.py")
print("  - choosing_data_structures.py")
print("=" * 80)
