# Functions Milestone - Video Walkthrough Guide

## What to Cover in Your ~2 Minute Video

### 1. Introduction (10 seconds)
- State your name and that you're demonstrating Python functions
- Mention the file: `functions_milestone.py`

### 2. Defining a Function (30 seconds)
Show and explain:
```python
def greet_person(name):
    """Greet a person by their name."""
    print(f"Hello, {name}! Welcome to Python programming.")
```

**Key Points to Mention:**
- Use `def` keyword to define functions
- Function name should be descriptive
- Parameters go in parentheses
- Indented code is the function body

### 3. Calling a Function (20 seconds)
Show and explain:
```python
greet_person("Alice")
greet_person("Bob")
```

**Key Points to Mention:**
- Call functions by name with parentheses
- Pass arguments in the correct order
- Functions execute when called

### 4. Parameters and Arguments (30 seconds)
Show and explain:
```python
def calculate_rectangle_area(length, width):
    area = length * width
    print(f"Area = {area}")
    return area

result = calculate_rectangle_area(5, 3)
```

**Key Points to Mention:**
- Parameters are placeholders in the function definition
- Arguments are actual values passed when calling
- Functions can return values

### 5. Function Scope (30 seconds)
Show and explain:
```python
global_var = "I am global"

def demonstrate_scope():
    local_var = "I am local"
    print(f"Inside: {global_var}, {local_var}")

demonstrate_scope()
print(f"Outside: {global_var}")
# local_var wouldn't work here!
```

**Key Points to Mention:**
- Global variables accessible everywhere
- Local variables only exist inside functions
- Prevents variable conflicts

### 6. Conclusion (10 seconds)
- Summarize: Functions make code reusable, organized, and maintainable
- State that all milestone objectives are met

## Recording Tips

✅ **DO:**
- Show your code clearly on screen
- Run the code and show output
- Speak clearly and at a moderate pace
- Highlight key lines of code as you explain
- Test at least one function live

❌ **DON'T:**
- Rush through the material
- Use too much technical jargon
- Show your face (screen-facing required)
- Go over 2.5 minutes

## Quick Test Checklist

Before recording, verify you can:
- ✅ Define a function with `def`
- ✅ Call a function
- ✅ Pass arguments to a function
- ✅ Explain function execution flow
- ✅ Demonstrate local vs global scope

## File Location
Your main script: `project/scripts/functions_milestone.py`

Run it with: `python functions_milestone.py`
