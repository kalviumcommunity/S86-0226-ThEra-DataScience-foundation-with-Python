"""
Choosing the Right Data Structure
=================================
This script demonstrates when to use Lists, Tuples, and Dictionaries
by comparing their characteristics and showing appropriate use cases.
"""

# 1. Quick Comparison Table
print("=" * 80)
print("1. CHARACTERISTICS COMPARISON")
print("=" * 80)

comparison_data = [
    ["Characteristic", "List", "Tuple", "Dictionary"],
    ["-" * 15, "-" * 20, "-" * 20, "-" * 20],
    ["Ordered", "✓ Yes", "✓ Yes", "✓ Yes (3.7+)"],
    ["Mutable", "✓ Yes", "✗ No (Immutable)", "✓ Yes"],
    ["Indexed", "✓ By position [0,1,2]", "✓ By position [0,1,2]", "✓ By key ['name']"],
    ["Duplicates", "✓ Allowed", "✓ Allowed", "✗ Keys must be unique"],
    ["Syntax", "[1, 2, 3]", "(1, 2, 3)", "{'a': 1, 'b': 2}"],
    ["Performance", "Good", "Better (faster)", "Best for lookups"],
    ["Memory", "More", "Less", "Most"],
]

for row in comparison_data:
    print(f"{row[0]:<16} | {row[1]:<20} | {row[2]:<20} | {row[3]:<20}")

print()

# 2. When to Use Lists
print("=" * 80)
print("2. WHEN TO USE LISTS")
print("=" * 80)

print("✓ Use lists when you need:")
print("  • A collection that will change over time (add/remove items)")
print("  • To maintain order of elements")
print("  • To access items by numeric position")
print("  • Similar items in a sequence")
print()

print("GOOD EXAMPLES:")
print()

# Example 1: Shopping cart (items frequently added/removed)
shopping_cart = []
print("Shopping Cart (dynamic list):")
shopping_cart.append("Laptop")
shopping_cart.append("Mouse")
shopping_cart.append("Keyboard")
print(f"  Items: {shopping_cart}")
shopping_cart.remove("Mouse")  # Changed mind
print(f"  After removing Mouse: {shopping_cart}")
print()

# Example 2: Task list (items can be completed and removed)
tasks = ["Buy groceries", "Call dentist", "Finish homework", "Go to gym"]
print(f"Task List: {tasks}")
tasks.append("Read a book")  # New task
print(f"Added new task: {tasks}")
completed_task = tasks.pop(0)  # Complete first task
print(f"Completed: '{completed_task}'")
print(f"Remaining tasks: {tasks}")
print()

# Example 3: Sensor readings (continuously growing data)
temperature_readings = [22.5, 23.1, 22.8, 23.5, 24.0]
print(f"Temperature Readings: {temperature_readings}")
temperature_readings.append(24.3)  # New reading
print(f"After new reading: {temperature_readings}")
print(f"Average: {sum(temperature_readings) / len(temperature_readings):.2f}°C")
print()

print("-" * 80)

# 3. When to Use Tuples
print("=" * 80)
print("3. WHEN TO USE TUPLES")
print("=" * 80)

print("✓ Use tuples when you need:")
print("  • Data that should NOT change (immutability protects data)")
print("  • To return multiple values from a function")
print("  • As dictionary keys (immutable)")
print("  • Slightly better performance and less memory")
print("  • Fixed collection of items")
print()

print("GOOD EXAMPLES:")
print()

# Example 1: Coordinates (should not change)
location = (40.7128, -74.0060)  # New York City coordinates
print(f"NYC Coordinates (fixed): {location}")
print(f"  Latitude: {location[0]}, Longitude: {location[1]}")
print()

# Example 2: RGB color values (standard format)
red_color = (255, 0, 0)
blue_color = (0, 0, 255)
print(f"Red color RGB: {red_color}")
print(f"Blue color RGB: {blue_color}")
print()

# Example 3: Database record (shouldn't be modified accidentally)
employee_record = ("E001", "John Doe", "Engineering", 75000)
emp_id, name, department, salary = employee_record  # Unpacking
print(f"Employee Record: {employee_record}")
print(f"  ID: {emp_id}, Name: {name}, Dept: {department}, Salary: ${salary}")
print()

# Example 4: Function returning multiple values
def get_statistics(numbers):
    return min(numbers), max(numbers), sum(numbers) / len(numbers)

data = [10, 20, 30, 40, 50]
minimum, maximum, average = get_statistics(data)
print(f"Statistics for {data}:")
print(f"  Min: {minimum}, Max: {maximum}, Average: {average}")
print()

# Example 5: Tuples as dictionary keys
city_coordinates = {
    (40.7128, -74.0060): "New York",
    (51.5074, -0.1278): "London",
    (35.6762, 139.6503): "Tokyo"
}
print("City lookup by coordinates:")
for coords, city in city_coordinates.items():
    print(f"  {coords} -> {city}")
print()

print("-" * 80)

# 4. When to Use Dictionaries
print("=" * 80)
print("4. WHEN TO USE DICTIONARIES")
print("=" * 80)

print("✓ Use dictionaries when you need:")
print("  • Key-value associations (mapping)")
print("  • Fast lookup by meaningful keys (not just numbers)")
print("  • To represent structured data (objects/entities)")
print("  • Flexible attribute-based access")
print("  • To count or group items")
print()

print("GOOD EXAMPLES:")
print()

# Example 1: User profile (structured entity with properties)
user_profile = {
    "username": "alice_smith",
    "email": "alice@example.com",
    "age": 28,
    "is_premium": True,
    "join_date": "2024-01-15"
}
print("User Profile:")
for key, value in user_profile.items():
    print(f"  {key}: {value}")
print()

# Example 2: Configuration settings (named settings)
app_config = {
    "host": "localhost",
    "port": 8080,
    "debug": True,
    "max_connections": 100
}
print(f"Application Config: {app_config}")
print(f"  Server will run on {app_config['host']}:{app_config['port']}")
print()

# Example 3: Word frequency counter
text = "python is powerful and python is fun"
word_count = {}
for word in text.split():
    word_count[word] = word_count.get(word, 0) + 1
print(f"Text: '{text}'")
print("Word Frequency:")
for word, count in word_count.items():
    print(f"  '{word}': {count}")
print()

# Example 4: Grade book (student name -> grade mapping)
gradebook = {
    "Alice": 92,
    "Bob": 87,
    "Charlie": 95,
    "Diana": 88
}
print("Gradebook:")
for student, grade in gradebook.items():
    print(f"  {student}: {grade}")
print(f"  Bob's grade: {gradebook['Bob']}")
print()

print("-" * 80)

# 5. Decision Tree - Choosing the Right Structure
print("=" * 80)
print("5. DECISION TREE")
print("=" * 80)

decision_tree = """
START: What data structure should I use?
│
├─ Do you need KEY-VALUE pairs?
│  │
│  ├─ YES → Use DICTIONARY
│  │         Examples: user profiles, configs, word counts, mappings
│  │
│  └─ NO → Continue...
│
├─ Will the data CHANGE (add/remove/modify)?
│  │
│  ├─ YES → Use LIST
│  │         Examples: shopping cart, task list, growing data
│  │
│  └─ NO → Use TUPLE
│            Examples: coordinates, RGB colors, constants, function returns
"""

print(decision_tree)
print()

# 6. Common Mistakes and Corrections
print("=" * 80)
print("6. COMMON MISTAKES")
print("=" * 80)

print("❌ MISTAKE 1: Using a list when data shouldn't change")
print("Bad:  coordinates = [40.7128, -74.0060]  # Can be modified accidentally")
print("Good: coordinates = (40.7128, -74.0060)  # Protected from changes")
print()

print("❌ MISTAKE 2: Using a tuple when you need to modify data")
print("Bad:  shopping_cart = ('item1', 'item2')  # Can't add more items")
print("Good: shopping_cart = ['item1', 'item2']  # Can add/remove items")
print()

print("❌ MISTAKE 3: Using list with numeric indices instead of dictionary")
print("Bad:  student = ['Alice', 20, 'CS']  # What does [1] mean?")
print("Good: student = {'name': 'Alice', 'age': 20, 'major': 'CS'}  # Clear!")
print()

print("❌ MISTAKE 4: Trying to use a list as dictionary key")
print("Bad:  locations = {[40.71, -74.00]: 'NYC'}  # ERROR: lists are mutable")
print("Good: locations = {(40.71, -74.00): 'NYC'}  # Tuples work!")
print()

# 7. Practical Scenarios
print("=" * 80)
print("7. PRACTICAL SCENARIOS - WHICH TO USE?")
print("=" * 80)

scenarios = [
    {
        "scenario": "Store student names in a class",
        "answer": "LIST",
        "reason": "Students may be added or removed from class"
    },
    {
        "scenario": "Store a person's birth date (year, month, day)",
        "answer": "TUPLE",
        "reason": "Birth date never changes, fixed 3 values"
    },
    {
        "scenario": "Store product details (name, price, quantity)",
        "answer": "DICTIONARY",
        "reason": "Named attributes make code clearer and more maintainable"
    },
    {
        "scenario": "Store GPS coordinates (latitude, longitude)",
        "answer": "TUPLE",
        "reason": "Fixed pair of values that shouldn't change"
    },
    {
        "scenario": "Store items in a shopping cart",
        "answer": "LIST",
        "reason": "Items will be added and removed frequently"
    },
    {
        "scenario": "Store configuration file settings",
        "answer": "DICTIONARY",
        "reason": "Settings accessed by name, not position"
    },
    {
        "scenario": "Store days of the week",
        "answer": "TUPLE",
        "reason": "Fixed set of values that never change"
    }
]

for i, scenario in enumerate(scenarios, 1):
    print(f"{i}. Scenario: {scenario['scenario']}")
    print(f"   Answer: {scenario['answer']}")
    print(f"   Reason: {scenario['reason']}")
    print()

# 8. Performance Comparison
print("=" * 80)
print("8. PERFORMANCE CONSIDERATIONS")
print("=" * 80)

import time

# Test data
test_size = 1000000
test_data = range(test_size)

# List creation time
start = time.time()
test_list = list(test_data)
list_time = time.time() - start

# Tuple creation time
start = time.time()
test_tuple = tuple(test_data)
tuple_time = time.time() - start

# Dictionary creation time
start = time.time()
test_dict = {i: i for i in test_data}
dict_time = time.time() - start

print(f"Creating {test_size} elements:")
print(f"  List:       {list_time:.4f} seconds")
print(f"  Tuple:      {tuple_time:.4f} seconds (faster)")
print(f"  Dictionary: {dict_time:.4f} seconds")
print()

# Memory usage
import sys
sample_list = [1, 2, 3, 4, 5]
sample_tuple = (1, 2, 3, 4, 5)
sample_dict = {0: 1, 1: 2, 2: 3, 3: 4, 4: 5}

print(f"Memory usage for 5 elements:")
print(f"  List:       {sys.getsizeof(sample_list)} bytes")
print(f"  Tuple:      {sys.getsizeof(sample_tuple)} bytes (smallest)")
print(f"  Dictionary: {sys.getsizeof(sample_dict)} bytes")
print()

# 9. Summary and Best Practices
print("=" * 80)
print("9. SUMMARY & BEST PRACTICES")
print("=" * 80)

summary = """
┌──────────────────────────────────────────────────────────────────────────┐
│                           CHOOSING DATA STRUCTURES                        │
├──────────────────────────────────────────────────────────────────────────┤
│                                                                           │
│  📋 USE LISTS WHEN:                                                       │
│     • You need to add/remove items frequently                            │
│     • Order matters and you access by position                           │
│     • Working with similar items in sequence                             │
│                                                                           │
│  📌 USE TUPLES WHEN:                                                      │
│     • Data should not change (immutability)                              │
│     • Returning multiple values from functions                           │
│     • Need to use as dictionary keys                                     │
│     • Want better performance/memory efficiency                          │
│                                                                           │
│  📚 USE DICTIONARIES WHEN:                                                │
│     • You need key-value associations                                    │
│     • Fast lookup by meaningful identifiers                              │
│     • Representing objects with properties                               │
│     • Counting, grouping, or mapping data                                │
│                                                                           │
│  💡 BEST PRACTICES:                                                       │
│     • Choose based on how data will be used, not just stored             │
│     • Prefer tuples for data integrity                                   │
│     • Use dictionaries for clarity with named attributes                 │
│     • Lists are your default for dynamic sequences                       │
│                                                                           │
└──────────────────────────────────────────────────────────────────────────┘
"""

print(summary)

print("\n✅ Understanding these differences will make you a better Python programmer!")
