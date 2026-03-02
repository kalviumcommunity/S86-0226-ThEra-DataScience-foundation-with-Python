"""
Functions Milestone - Python Fundamentals
==========================================
This script demonstrates:
1. Defining functions
2. Calling functions
3. Using parameters and arguments
4. Understanding function scope (basics)

Functions help organize code into reusable, logical blocks.
"""

# ============================================================================
# SECTION 1: DEFINING A FUNCTION
# ============================================================================
print("=" * 60)
print("SECTION 1: DEFINING A FUNCTION")
print("=" * 60)

# A simple function with no parameters
def greet():
    """Display a simple greeting message."""
    print("Hello! Welcome to Python Functions.")

# A function that performs a calculation
def calculate_square():
    """Calculate and return the square of 5."""
    number = 5
    square = number ** 2
    print(f"The square of {number} is {square}")

# Calling the functions to see them in action
greet()
calculate_square()
print()


# ============================================================================
# SECTION 2: CALLING A FUNCTION
# ============================================================================
print("=" * 60)
print("SECTION 2: CALLING A FUNCTION")
print("=" * 60)

def display_message():
    """Show how function execution flows."""
    print("Step 2: Inside the function")
    print("Step 3: Function is executing")

print("Step 1: Before calling the function")
display_message()
print("Step 4: After function returns")
print()


# ============================================================================
# SECTION 3: USING PARAMETERS AND ARGUMENTS
# ============================================================================
print("=" * 60)
print("SECTION 3: USING PARAMETERS AND ARGUMENTS")
print("=" * 60)

# Function with a single parameter
def greet_person(name):
    """Greet a person by their name.
    
    Args:
        name: The name of the person to greet
    """
    print(f"Hello, {name}! Welcome to Python programming.")

# Function with multiple parameters
def calculate_rectangle_area(length, width):
    """Calculate the area of a rectangle.
    
    Args:
        length: The length of the rectangle
        width: The width of the rectangle
    """
    area = length * width
    print(f"Rectangle with length {length} and width {width}")
    print(f"Area = {area}")
    return area

# Function that returns a value
def add_numbers(num1, num2):
    """Add two numbers and return the result.
    
    Args:
        num1: First number
        num2: Second number
    
    Returns:
        The sum of num1 and num2
    """
    result = num1 + num2
    return result

# Calling functions with arguments
greet_person("Alice")
greet_person("Bob")
print()

calculate_rectangle_area(5, 3)
calculate_rectangle_area(10, 7)
print()

# Using return values
sum1 = add_numbers(10, 20)
sum2 = add_numbers(100, 250)
print(f"First sum: {sum1}")
print(f"Second sum: {sum2}")
print(f"Total of both sums: {sum1 + sum2}")
print()


# ============================================================================
# SECTION 4: UNDERSTANDING FUNCTION SCOPE (BASICS)
# ============================================================================
print("=" * 60)
print("SECTION 4: UNDERSTANDING FUNCTION SCOPE")
print("=" * 60)

# Global variable
global_var = "I am a global variable"

def demonstrate_scope():
    """Show the difference between local and global variables."""
    # Local variable - only exists inside this function
    local_var = "I am a local variable"
    
    print(f"Inside function - Global variable: {global_var}")
    print(f"Inside function - Local variable: {local_var}")

# Calling the function
demonstrate_scope()
print(f"Outside function - Global variable: {global_var}")
# Uncommenting the next line would cause an error because local_var doesn't exist outside
# print(f"Outside function - Local variable: {local_var}")  # Error!
print()

# Example showing variables with same name in different scopes
counter = 100  # Global counter

def increment_local_counter():
    """Demonstrate local variable shadowing global variable."""
    counter = 0  # This is a LOCAL variable, different from global counter
    counter += 1
    print(f"Inside function - Local counter: {counter}")

increment_local_counter()
print(f"Outside function - Global counter: {counter}")
print()


# ============================================================================
# PRACTICAL EXAMPLES: COMBINING ALL CONCEPTS
# ============================================================================
print("=" * 60)
print("PRACTICAL EXAMPLES: COMBINING ALL CONCEPTS")
print("=" * 60)

def calculate_average(num1, num2, num3):
    """Calculate the average of three numbers.
    
    Args:
        num1, num2, num3: Numbers to average
    
    Returns:
        The average of the three numbers
    """
    total = num1 + num2 + num3
    average = total / 3
    return average

def analyze_grades(student_name, grade1, grade2, grade3):
    """Analyze a student's grades and display results.
    
    Args:
        student_name: Name of the student
        grade1, grade2, grade3: Three test grades
    """
    avg = calculate_average(grade1, grade2, grade3)
    print(f"\nStudent: {student_name}")
    print(f"Grades: {grade1}, {grade2}, {grade3}")
    print(f"Average: {avg:.2f}")
    
    if avg >= 90:
        print("Performance: Excellent!")
    elif avg >= 80:
        print("Performance: Very Good")
    elif avg >= 70:
        print("Performance: Good")
    else:
        print("Performance: Needs Improvement")

# Using the practical functions
analyze_grades("Emma", 92, 88, 95)
analyze_grades("John", 78, 82, 75)
analyze_grades("Sarah", 95, 98, 92)
print()


# ============================================================================
# REAL-WORLD USE CASE: DATA PROCESSING
# ============================================================================
print("=" * 60)
print("REAL-WORLD USE CASE: DATA PROCESSING")
print("=" * 60)

def convert_temperature(celsius):
    """Convert Celsius to Fahrenheit.
    
    Args:
        celsius: Temperature in Celsius
    
    Returns:
        Temperature in Fahrenheit
    """
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def display_temperature_conversion(temp_celsius):
    """Display temperature in both Celsius and Fahrenheit.
    
    Args:
        temp_celsius: Temperature in Celsius
    """
    temp_fahrenheit = convert_temperature(temp_celsius)
    print(f"{temp_celsius}°C = {temp_fahrenheit:.1f}°F")

# Processing multiple temperature conversions
print("Temperature Conversions:")
display_temperature_conversion(0)
display_temperature_conversion(25)
display_temperature_conversion(37)
display_temperature_conversion(100)
print()


# ============================================================================
# FUNCTIONS WITH DEFAULT PARAMETERS (BONUS)
# ============================================================================
print("=" * 60)
print("BONUS: FUNCTIONS WITH DEFAULT PARAMETERS")
print("=" * 60)

def create_profile(name, age, city="Unknown"):
    """Create a user profile with optional city parameter.
    
    Args:
        name: User's name
        age: User's age
        city: User's city (default: "Unknown")
    """
    print(f"Profile: {name}, Age: {age}, City: {city}")

# Calling with and without optional parameter
create_profile("Alice", 25, "New York")
create_profile("Bob", 30)  # Uses default city
print()


# ============================================================================
# KEY TAKEAWAYS
# ============================================================================
print("=" * 60)
print("KEY TAKEAWAYS")
print("=" * 60)
print("""
1. Functions are defined using the 'def' keyword
2. Functions make code reusable and organized
3. Parameters allow functions to accept input
4. Arguments are the actual values passed to functions
5. Local variables exist only inside functions
6. Global variables can be accessed from anywhere
7. Functions can return values using 'return'
8. Good function names describe what they do
9. Functions help reduce code repetition
10. Functions make programs easier to test and maintain
""")

print("=" * 60)
print("MILESTONE COMPLETED SUCCESSFULLY!")
print("=" * 60)
