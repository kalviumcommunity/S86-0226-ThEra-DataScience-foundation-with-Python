# Video Walkthrough Guide (~2 Minutes)

This guide will help you create your video submission for the Python Collections milestone.

## Video Structure

### Introduction (15 seconds)
"Hi! Today I'll demonstrate Python's three core collection data structures: Lists, Tuples, and Dictionaries, and explain when to use each one."

---

## 1. Lists Example (30 seconds)

### What to Show:
Run `collections_demo.py` or demonstrate live:

```python
# Create a list
shopping_cart = ["Laptop", "Mouse", "Keyboard"]
print(f"Shopping Cart: {shopping_cart}")

# Add an item
shopping_cart.append("Monitor")
print(f"After adding: {shopping_cart}")

# Remove an item
shopping_cart.remove("Mouse")
print(f"After removing: {shopping_cart}")

# Modify an item
shopping_cart[0] = "Gaming Laptop"
print(f"After modifying: {shopping_cart}")
```

### What to Say:
"Lists are mutable and ordered. I can add, remove, and modify items. Use lists when your collection will change, like a shopping cart or task list."

---

## 2. Tuples Example (30 seconds)

### What to Show:

```python
# Create a tuple
coordinates = (40.7128, -74.0060)
print(f"NYC Coordinates: {coordinates}")

# Try to modify (will fail)
try:
    coordinates[0] = 50.0
except TypeError as e:
    print(f"Error: {e}")
    print("Tuples are IMMUTABLE!")

# Tuple unpacking
latitude, longitude = coordinates
print(f"Lat: {latitude}, Lon: {longitude}")
```

### What to Say:
"Tuples are immutable - they cannot be changed after creation. See? When I try to modify it, I get an error. Use tuples for data that shouldn't change, like coordinates or dates."

---

## 3. Dictionaries Example (30 seconds)

### What to Show:

```python
# Create a dictionary
student = {
    "name": "Alice",
    "age": 20,
    "major": "Computer Science",
    "gpa": 3.8
}
print(f"Student: {student}")

# Access by key
print(f"Name: {student['name']}")

# Modify a value
student['gpa'] = 3.9
print(f"Updated GPA: {student['gpa']}")

# Add new key-value pair
student['email'] = "alice@example.com"
print(f"Added email: {student['email']}")
```

### What to Say:
"Dictionaries store key-value pairs. I can access, modify, and add data using meaningful keys instead of numeric positions. Use dictionaries for structured data like user profiles or configuration settings."

---

## 4. Comparison and Use Cases (15 seconds)

### What to Show:
Display this comparison (from `collections_demo.py`):

```python
# Same data, different structures
person_list = ["Bob", 25, "Engineer"]          # Unclear what index means
person_tuple = ("Bob", 25, "Engineer")         # Protected from changes
person_dict = {"name": "Bob", "age": 25, "job": "Engineer"}  # Self-documenting
```

### What to Say:
"Here's the same data in each structure. Lists are for dynamic data, tuples protect data from changes, and dictionaries make code self-documenting with named keys."

---

## 5. Conclusion (5 seconds)

### What to Say:
"Choose lists for changing collections, tuples for fixed data, and dictionaries for key-value mappings. Thanks for watching!"

---

## Quick Tips for Recording

✅ **Screen Setup:**
- Use a terminal or Python IDE with large font (16pt or higher)
- Zoom in so text is clearly visible
- Use dark mode or light mode with good contrast

✅ **Recording:**
- Speak clearly and at a steady pace
- Show output after each operation
- Use the `collections_demo.py` script or type live
- Keep it under 2 minutes

✅ **What to Avoid:**
- Don't go into advanced topics
- Don't rush through explanations
- Don't use tiny font sizes
- Don't forget to show the actual OUTPUT

---

## Recommended Script to Run

The easiest approach is to run:
```bash
python scripts/collections_demo.py
```

And explain each section as it appears on screen.

Alternatively, create your own examples following the structure above.

---

## Submission Checklist

- [ ] Video covers Lists with operations (create, add, remove, modify)
- [ ] Video shows Tuple immutability behavior
- [ ] Video demonstrates Dictionary key-value access
- [ ] Video explains differences between structures
- [ ] Video shows when to use each structure
- [ ] Video is approximately 2 minutes long
- [ ] Video is screen-facing and clearly visible
- [ ] Audio is clear and understandable

---

Good luck with your video! 🎥
