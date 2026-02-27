"""
Working with Python Lists
=========================
This script demonstrates core list operations including:
- Creating lists
- Accessing elements using indexing
- Modifying, adding, and removing elements
- Iterating over list items
"""

# 1. Creating Lists
print("=" * 50)
print("1. CREATING LISTS")
print("=" * 50)

# List of programming languages
programming_languages = ["Python", "Java", "JavaScript", "C++", "Ruby"]
print(f"Programming Languages: {programming_languages}")

# List of student scores
student_scores = [85, 92, 78, 95, 88]
print(f"Student Scores: {student_scores}")

# Mixed data type list (though not commonly recommended)
mixed_data = ["Alice", 25, True, 3.14]
print(f"Mixed Data: {mixed_data}")

# Empty list
empty_list = []
print(f"Empty List: {empty_list}")

print()

# 2. Accessing Elements using Indexes
print("=" * 50)
print("2. ACCESSING ELEMENTS")
print("=" * 50)

print(f"First language: {programming_languages[0]}")
print(f"Last language: {programming_languages[-1]}")
print(f"Third language: {programming_languages[2]}")

# Slicing - accessing multiple elements
print(f"First three languages: {programming_languages[0:3]}")
print(f"Languages from index 2 onwards: {programming_languages[2:]}")
print(f"Last two languages: {programming_languages[-2:]}")

print()

# 3. Modifying List Elements
print("=" * 50)
print("3. MODIFYING LISTS")
print("=" * 50)

# Changing an element
print(f"Original scores: {student_scores}")
student_scores[0] = 90
print(f"After modifying first score: {student_scores}")

# Adding elements
# Using append() - adds to the end
programming_languages.append("Go")
print(f"After append 'Go': {programming_languages}")

# Using insert() - adds at specific position
programming_languages.insert(2, "TypeScript")
print(f"After insert 'TypeScript' at index 2: {programming_languages}")

# Using extend() - adds multiple elements
programming_languages.extend(["Rust", "Swift"])
print(f"After extend with 'Rust' and 'Swift': {programming_languages}")

print()

# 4. Removing Elements
print("=" * 50)
print("4. REMOVING ELEMENTS")
print("=" * 50)

# Using remove() - removes by value
programming_languages.remove("Java")
print(f"After removing 'Java': {programming_languages}")

# Using pop() - removes by index and returns the value
removed_item = programming_languages.pop()
print(f"Removed last item: {removed_item}")
print(f"List after pop(): {programming_languages}")

# Removing at specific index
removed_at_index = programming_languages.pop(2)
print(f"Removed item at index 2: {removed_at_index}")
print(f"List after pop(2): {programming_languages}")

# Using del - removes by index
del programming_languages[0]
print(f"After del first item: {programming_languages}")

# Clearing the list
languages_copy = ["A", "B", "C"]
print(f"Before clear: {languages_copy}")
languages_copy.clear()
print(f"After clear: {languages_copy}")

print()

# 5. Iterating Over Lists
print("=" * 50)
print("5. ITERATING OVER LISTS")
print("=" * 50)

fruits = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]

# Simple iteration
print("Fruits:")
for fruit in fruits:
    print(f"  - {fruit}")

print()

# Iteration with index
print("Fruits with index:")
for index, fruit in enumerate(fruits):
    print(f"  {index}: {fruit}")

print()

# 6. Common List Methods and Operations
print("=" * 50)
print("6. COMMON LIST OPERATIONS")
print("=" * 50)

numbers = [5, 2, 9, 1, 7, 3]
print(f"Original numbers: {numbers}")

# Length
print(f"Length of list: {len(numbers)}")

# Sorting
numbers.sort()
print(f"After sort(): {numbers}")

# Sorting in reverse
numbers.sort(reverse=True)
print(f"After sort(reverse=True): {numbers}")

# Reverse
numbers.reverse()
print(f"After reverse(): {numbers}")

# Count occurrences
test_list = [1, 2, 2, 3, 2, 4]
print(f"Count of 2 in {test_list}: {test_list.count(2)}")

# Index of element
print(f"Index of 3 in {numbers}: {numbers.index(3)}")

# Checking membership
print(f"Is 5 in numbers? {5 in numbers}")
print(f"Is 10 in numbers? {10 in numbers}")

print()

# 7. List Comprehension (Bonus)
print("=" * 50)
print("7. LIST COMPREHENSION")
print("=" * 50)

# Creating a list of squares
squares = [x**2 for x in range(1, 6)]
print(f"Squares: {squares}")

# Filtering even numbers
all_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [x for x in all_numbers if x % 2 == 0]
print(f"Even numbers: {even_numbers}")

print()

# 8. Key Takeaways
print("=" * 50)
print("KEY TAKEAWAYS ABOUT LISTS")
print("=" * 50)
print("✓ Lists are ORDERED - elements maintain their position")
print("✓ Lists are MUTABLE - can be modified after creation")
print("✓ Lists allow DUPLICATES - same value can appear multiple times")
print("✓ Lists use INDEXING - access elements by position (0-based)")
print("✓ Lists are DYNAMIC - can grow or shrink as needed")
print("✓ Use lists when you need a collection that changes over time")
