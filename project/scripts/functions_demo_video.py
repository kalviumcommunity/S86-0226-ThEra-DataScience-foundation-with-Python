"""
Functions Milestone - Video Demo Script
========================================
A concise demonstration of Python functions for video walkthrough.
"""

# ============================================================================
# 1. DEFINING A FUNCTION
# ============================================================================
print("1. DEFINING A FUNCTION")
print("-" * 40)

def greet_person(name):
    """Greet a person by their name."""
    print(f"Hello, {name}! Welcome to Python programming.")

print("Function 'greet_person' has been defined.")
print()


# ============================================================================
# 2. CALLING A FUNCTION
# ============================================================================
print("2. CALLING A FUNCTION")
print("-" * 40)

print("Before calling the function...")
greet_person("Alice")
print("After calling the function.")
print()


# ============================================================================
# 3. PASSING ARGUMENTS
# ============================================================================
print("3. PASSING ARGUMENTS")
print("-" * 40)

def add_numbers(num1, num2):
    """Add two numbers and return the result."""
    result = num1 + num2
    return result

# Calling with different arguments
sum1 = add_numbers(10, 20)
sum2 = add_numbers(100, 250)

print(f"10 + 20 = {sum1}")
print(f"100 + 250 = {sum2}")
print()


# ============================================================================
# 4. FUNCTION SCOPE
# ============================================================================
print("4. FUNCTION SCOPE")
print("-" * 40)

global_var = "I am global"

def show_scope():
    """Demonstrate local and global variables."""
    local_var = "I am local"
    print(f"Inside function - Global: {global_var}")
    print(f"Inside function - Local: {local_var}")

show_scope()
print(f"Outside function - Global: {global_var}")
print("Outside function - Local variable doesn't exist here!")
print()


# ============================================================================
# 5. PRACTICAL EXAMPLE
# ============================================================================
print("5. PRACTICAL EXAMPLE - Student Grade Analysis")
print("-" * 40)

def calculate_average(grade1, grade2, grade3):
    """Calculate average of three grades."""
    return (grade1 + grade2 + grade3) / 3

def analyze_student(name, g1, g2, g3):
    """Analyze a student's performance."""
    avg = calculate_average(g1, g2, g3)
    print(f"\nStudent: {name}")
    print(f"Grades: {g1}, {g2}, {g3}")
    print(f"Average: {avg:.2f}")
    
    if avg >= 90:
        print("Performance: Excellent! ⭐")
    elif avg >= 80:
        print("Performance: Very Good ✓")
    else:
        print("Performance: Good")

# Analyzing students
analyze_student("Emma", 92, 88, 95)
analyze_student("John", 85, 82, 87)

print("\n" + "=" * 40)
print("DEMO COMPLETE!")
print("=" * 40)
