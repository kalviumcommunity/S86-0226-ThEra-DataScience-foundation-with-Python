"""
Working with Python Dictionaries
================================
This script demonstrates core dictionary operations including:
- Creating dictionaries with meaningful keys
- Accessing values using keys
- Modifying or adding key-value pairs
- Understanding dictionary structure and usage
"""

# 1. Creating Dictionaries
print("=" * 50)
print("1. CREATING DICTIONARIES")
print("=" * 50)

# Student information
student = {
    "name": "Alice Johnson",
    "age": 20,
    "major": "Computer Science",
    "gpa": 3.8
}
print(f"Student: {student}")

# Product catalog
product = {
    "id": "P001",
    "name": "Laptop",
    "price": 999.99,
    "in_stock": True
}
print(f"Product: {product}")

# Empty dictionary
empty_dict = {}
print(f"Empty Dictionary: {empty_dict}")

# Using dict() constructor
person = dict(name="Bob", age=25, city="New York")
print(f"Person (using dict()): {person}")

print()

# 2. Accessing Values using Keys
print("=" * 50)
print("2. ACCESSING VALUES")
print("=" * 50)

# Direct key access
print(f"Student name: {student['name']}")
print(f"Student GPA: {student['gpa']}")

# Using get() method (safer)
print(f"Student age: {student.get('age')}")
print(f"Student phone (not exists): {student.get('phone')}")  # Returns None
print(f"Student phone (with default): {student.get('phone', 'Not provided')}")

# Attempting direct access with non-existent key causes error
print("\nTrying to access non-existent key directly...")
try:
    print(student['phone'])
except KeyError as e:
    print(f"❌ Error: KeyError - {e}")
    print("✓ Use .get() method to avoid KeyError")

print()

# 3. Modifying and Adding Key-Value Pairs
print("=" * 50)
print("3. MODIFYING DICTIONARIES")
print("=" * 50)

# Modifying existing values
print(f"Original product price: ${product['price']}")
product['price'] = 899.99
print(f"Updated product price: ${product['price']}")

# Adding new key-value pairs
product['category'] = "Electronics"
product['rating'] = 4.5
print(f"Product after adding category and rating: {product}")

# Using update() method to add/modify multiple items
product.update({
    "brand": "TechBrand",
    "warranty": "2 years",
    "price": 849.99  # Also updates existing key
})
print(f"Product after update(): {product}")

print()

# 4. Removing Key-Value Pairs
print("=" * 50)
print("4. REMOVING ITEMS")
print("=" * 50)

sample_dict = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4
}
print(f"Original dictionary: {sample_dict}")

# Using pop() - removes and returns value
removed_value = sample_dict.pop("b")
print(f"Removed 'b' with value: {removed_value}")
print(f"After pop('b'): {sample_dict}")

# Using popitem() - removes and returns last inserted item
last_item = sample_dict.popitem()
print(f"Removed last item: {last_item}")
print(f"After popitem(): {sample_dict}")

# Using del keyword
del sample_dict["a"]
print(f"After del: {sample_dict}")

# Clearing all items
sample_dict.clear()
print(f"After clear(): {sample_dict}")

print()

# 5. Dictionary Methods and Operations
print("=" * 50)
print("5. DICTIONARY METHODS")
print("=" * 50)

inventory = {
    "apples": 50,
    "bananas": 30,
    "oranges": 45,
    "grapes": 25
}

print(f"Inventory: {inventory}")
print()

# Getting all keys
print(f"Keys: {inventory.keys()}")
print(f"Keys as list: {list(inventory.keys())}")

# Getting all values
print(f"Values: {inventory.values()}")
print(f"Values as list: {list(inventory.values())}")

# Getting all key-value pairs
print(f"Items: {inventory.items()}")
print(f"Items as list: {list(inventory.items())}")

# Length of dictionary
print(f"Number of items: {len(inventory)}")

# Checking if key exists
print(f"Is 'apples' in inventory? {'apples' in inventory}")
print(f"Is 'mangoes' in inventory? {'mangoes' in inventory}")

print()

# 6. Iterating Over Dictionaries
print("=" * 50)
print("6. ITERATING OVER DICTIONARIES")
print("=" * 50)

grades = {
    "Math": 90,
    "Science": 85,
    "English": 88,
    "History": 92
}

# Iterating over keys (default)
print("Subjects (keys only):")
for subject in grades:
    print(f"  - {subject}")

print()

# Iterating over keys explicitly
print("Subjects (using .keys()):")
for subject in grades.keys():
    print(f"  - {subject}")

print()

# Iterating over values
print("Grades (values only):")
for grade in grades.values():
    print(f"  - {grade}")

print()

# Iterating over key-value pairs
print("Subject-Grade pairs:")
for subject, grade in grades.items():
    print(f"  {subject}: {grade}")

print()

# 7. Nested Dictionaries
print("=" * 50)
print("7. NESTED DICTIONARIES")
print("=" * 50)

# Dictionary of students
students = {
    "student1": {
        "name": "Alice",
        "age": 20,
        "grades": [90, 85, 88]
    },
    "student2": {
        "name": "Bob",
        "age": 21,
        "grades": [78, 82, 85]
    },
    "student3": {
        "name": "Charlie",
        "age": 19,
        "grades": [95, 92, 98]
    }
}

print("Students database:")
for student_id, student_info in students.items():
    print(f"\n{student_id}:")
    print(f"  Name: {student_info['name']}")
    print(f"  Age: {student_info['age']}")
    print(f"  Grades: {student_info['grades']}")
    print(f"  Average: {sum(student_info['grades']) / len(student_info['grades']):.2f}")

print()

# 8. Dictionary Comprehension
print("=" * 50)
print("8. DICTIONARY COMPREHENSION")
print("=" * 50)

# Creating a dictionary of squares
squares = {x: x**2 for x in range(1, 6)}
print(f"Squares: {squares}")

# Converting temperature data
temp_celsius = {"morning": 20, "afternoon": 28, "evening": 22}
temp_fahrenheit = {time: (temp * 9/5) + 32 for time, temp in temp_celsius.items()}
print(f"Temperature (Celsius): {temp_celsius}")
print(f"Temperature (Fahrenheit): {temp_fahrenheit}")

# Filtering dictionary
scores = {"Alice": 85, "Bob": 92, "Charlie": 78, "David": 95, "Eve": 88}
high_scorers = {name: score for name, score in scores.items() if score >= 90}
print(f"All scores: {scores}")
print(f"High scorers (>=90): {high_scorers}")

print()

# 9. Real-World Use Cases
print("=" * 50)
print("9. REAL-WORLD USE CASES")
print("=" * 50)

# Use Case 1: Configuration settings
config = {
    "app_name": "MyApp",
    "version": "1.0.0",
    "debug_mode": True,
    "max_connections": 100,
    "timeout": 30
}
print("Application Configuration:")
for key, value in config.items():
    print(f"  {key}: {value}")

print()

# Use Case 2: Word frequency counter
text = "python is great and python is powerful"
words = text.split()
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1
print(f"Text: '{text}'")
print("Word frequency:")
for word, count in word_count.items():
    print(f"  '{word}': {count}")

print()

# Use Case 3: Data transformation (list to dictionary)
student_list = [
    ["Alice", 85],
    ["Bob", 90],
    ["Charlie", 88]
]
student_grades = {name: grade for name, grade in student_list}
print("Student grades (from list to dict):")
print(student_grades)

print()

# 10. Common Dictionary Patterns
print("=" * 50)
print("10. COMMON PATTERNS")
print("=" * 50)

# Default values with setdefault()
inventory_new = {"apples": 10}
print(f"Initial inventory: {inventory_new}")
inventory_new.setdefault("bananas", 0)  # Adds if not exists
inventory_new.setdefault("apples", 20)  # Doesn't change existing
print(f"After setdefault: {inventory_new}")

print()

# Merging dictionaries (Python 3.9+)
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged = dict1 | dict2
print(f"dict1: {dict1}")
print(f"dict2: {dict2}")
print(f"Merged (dict1 | dict2): {merged}")

# Alternative merging (works in older Python versions)
dict3 = {"e": 5}
merged_old = {**dict1, **dict2, **dict3}
print(f"Merged (unpacking): {merged_old}")

print()

# 11. Key Takeaways
print("=" * 50)
print("KEY TAKEAWAYS ABOUT DICTIONARIES")
print("=" * 50)
print("✓ Dictionaries store KEY-VALUE pairs")
print("✓ Dictionaries are UNORDERED (before Python 3.7) / Insertion-ordered (3.7+)")
print("✓ Dictionaries are MUTABLE - can be modified after creation")
print("✓ Keys must be IMMUTABLE (strings, numbers, tuples)")
print("✓ Keys must be UNIQUE - duplicate keys overwrite previous values")
print("✓ Values can be ANY type, including other dictionaries")
print("✓ Use .get() to safely access keys that might not exist")
print("✓ Dictionaries provide FAST lookup by key (O(1) average)")
print("✓ Use dictionaries to model real-world entities with properties")
print("✓ Use dictionaries for mapping relationships (ID -> Name, etc.)")
