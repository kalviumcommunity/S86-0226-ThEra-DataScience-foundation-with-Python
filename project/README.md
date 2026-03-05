# Data Science Project Structure

This project follows a standard, professional folder structure to ensure clarity, reproducibility, and ease of collaboration.

## Folder Overview

- `data/` — Store all raw and processed datasets here. **Do not modify raw data.**
- `notebooks/` — Jupyter notebooks for exploration, analysis, and reporting.
- `scripts/` — Standalone Python scripts for data processing, modeling, or automation.
- `outputs/` — Generated results, figures, and model outputs. Never overwrite raw data.

## Best Practices
- Keep code, data, and outputs separate.
- Use clear, consistent folder names.
- Avoid deeply nested folders.
- Make paths predictable for easy collaboration.

This structure helps your project scale, remain organized, and be easy for others to understand and review.

---


## Milestone: Using for and while Loops for Iterative Data Processing

This milestone focuses on using **for** and **while** loops to perform iterative data processing in Python. Loops allow you to repeat operations efficiently, which is essential when working with collections, sequences, and repeated logic in real-world programs.

### Learning Objectives

By completing this milestone, you will be able to:
- ✅ Write for loops to process sequences and collections
- ✅ Write while loops for condition-based repetition
- ✅ Control loops using break and continue
- ✅ Recognize and fix infinite loop scenarios
- ✅ Use loops confidently in data workflows

### Why This Matters
Common beginner issues include:
- Writing repetitive code instead of loops
- Creating infinite loops accidentally
- Using the wrong loop type for a task
- Difficulty understanding loop flow

This milestone ensures that:
- Your code is concise and maintainable
- Repetitive tasks are handled cleanly
- Iteration logic behaves predictably
- Data processing becomes scalable

Think of loops as automation tools—this lesson teaches you how to use them safely and effectively.

### What You Are Expected to Do
This is a Python iteration milestone, not a data analysis task.

You are expected to:
- Write for loops and while loops
- Iterate over lists or ranges
- Use conditions to control loop execution
- Print outputs to observe loop behavior
No datasets or advanced libraries are required.

#### 1. Using for Loops for Iteration
Learn how for loops work.
You should:
- Iterate over a range of numbers
- Observe loop execution order
- Use loop variables meaningfully
for loops are ideal for known sequences.

#### 2. Using while Loops for Condition-Based Repetition
Learn how while loops work.
You should:

#### 3. Controlling Loop Flow
Manage loop execution safely.
- Keep loop flow readable
Control statements prevent errors and inefficiency.

#### 4. Avoiding Infinite Loops
- Test loops with small examples
- Stop execution safely if needed
Preventing infinite loops saves time and frustration.

#### 5. Video Walkthrough (~2 Minutes)
For your video, demonstrate:
- A for loop iterating over a range and a list
#### Demo Script
See `scripts/loops_milestone.py` for a complete demonstration of all these concepts:

```bash
python scripts/loops_milestone.py
## Milestone: Working with Python Lists, Tuples, and Dictionaries

This milestone focuses on mastering Python's core collection data structures—**lists**, **tuples**, and **dictionaries**. Understanding when and how to use each structure is essential for handling real-world data efficiently.

### Learning Objectives
- ✅ Modify lists and dictionaries correctly
- ✅ Understand immutability in tuples
- ✅ Organize structured data effectively
- ✅ Choose the right data structure for a given task

#### 1. **working_with_lists.py**
Learn about Python lists—ordered and mutable collections.

**Topics covered:**
- Creating lists with multiple values
- List comprehensions

**Run the script:**
```bash
python scripts/working_with_lists.py
```

#### 2. **working_with_tuples.py**
Learn about Python tuples—ordered but immutable collections.

**Topics covered:**
- Creating tuples with fixed values
- Accessing elements using indexes
- Demonstrating immutability behavior
- Tuple unpacking and packing
- When to use tuples over lists
- Performance and memory benefits

**Run the script:**
```bash
python scripts/working_with_tuples.py
```

#### 3. **working_with_dictionaries.py**
Learn about Python dictionaries—key-value pair collections.
**Topics covered:**
- Creating dictionaries with meaningful keys
- Accessing values using keys safely (.get() method)
- Modifying and adding key-value pairs
- Dictionary methods (keys, values, items)
- Iterating over dictionaries
- Nested dictionaries and dictionary comprehensions

**Run the script:**
```bash
python scripts/working_with_dictionaries.py
```

#### 4. **choosing_data_structures.py**
Learn when to use each data structure by understanding their trade-offs.

**Topics covered:**
- Characteristic comparison table
- When to use lists vs tuples vs dictionaries
- Decision tree for choosing the right structure
- Common mistakes and how to avoid them
- Practical scenarios with explanations
- Performance and memory considerations

**Run the script:**
```bash
python scripts/choosing_data_structures.py
```

### Quick Reference: When to Use Each Structure

| Structure | Use When | Mutable? | Syntax Example |
|-----------|----------|----------|----------------|
| **List** | Collection will change (add/remove items) | ✅ Yes | `[1, 2, 3]` |
| **Tuple** | Data should NOT change (immutability) | ❌ No | `(1, 2, 3)` |
| **Dictionary** | Key-value associations needed | ✅ Yes | `{'a': 1, 'b': 2}` |

### Running All Scripts

To see all demonstrations in sequence, run each script:

```bash
# Run from the project root directory
python scripts/working_with_lists.py
python scripts/working_with_tuples.py
python scripts/working_with_dictionaries.py
python scripts/choosing_data_structures.py
```

### Video Walkthrough Checklist

For your video submission (~2 minutes), demonstrate:

- ✅ A **list** example showing creation and operations (add, remove, modify)
- ✅ A **tuple** example demonstrating immutability behavior
- ✅ A **dictionary** example with key-value access and modification
- ✅ Explanation of differences between structures
- ✅ When to use each structure (use cases)

You can use any of the provided scripts or create your own examples.

### Key Takeaways

#### Lists
- Ordered, mutable, and allow duplicates
- Use for dynamic collections that change over time
- Examples: shopping cart, task list, sensor readings

#### Tuples
- Ordered, immutable, and allow duplicates
- Use for data that should not change
- Examples: coordinates, RGB colors, database records

#### Dictionaries
- Key-value pairs with unique keys
- Use for named attributes and fast lookups
- Examples: user profiles, configuration settings, word counts

---

## Previous Milestone: Data Organization

To satisfy the assignment requirements, the following steps have been completed:

1. **Separated data stages** into `data/raw/` (original datasets) and
   `data/processed/` (cleaned or derived tables). Each folder contains a
   `.gitkeep` placeholder to track empty directories.
2. **Added a sample raw file** (`example_raw.csv`) to demonstrate immutability.
3. **Created a demonstration script** (`scripts/organize_data_demo.py`) that
   reads from raw, writes processed output, and saves an artifact in `outputs/`.
4. **Updated this README** to explain the reasoning and point users at the
   example script and folder layout.

### Key principles illustrated

- Raw data is never modified; scripts only read from `data/raw`.
- Processed datasets are written to `data/processed` with clear names.
- Output artifacts (reports, plots, models) belong in `outputs/`.
- Workflows should be one-directional: raw → processed → outputs.

By following this organization, you avoid accidental overwrites, maintain
reproducibility, and make it easier for others (or future you) to follow
your work.

---


---

## Milestone: Structuring Python Code for Readability and Reuse

This milestone focuses on organizing Python code for clarity, modularity, and maintainability. Well-structured code is easier to understand, debug, and extend, supporting collaboration and future development.

### Learning Objectives

By completing this milestone, you will be able to:
- ✅ Structure Python scripts clearly with logical sections
- ✅ Group related logic and use functions to reduce repetition
- ✅ Separate setup, logic, and execution for clean code flow
- ✅ Write code that is easy to read, reuse, and maintain

### Why This Matters

Unstructured code leads to confusion, bugs, and slow development. This milestone ensures your scripts:
- Have a clear, predictable structure
- Group logic for reusability
- Are easier to debug and extend

### What You Are Expected to Do

- Organize code into logical sections (imports, variables, functions, execution)
- Use functions to avoid repetition
- Keep top-level execution minimal and readable
- Focus on readability over cleverness

### Demo Script

See `scripts/readability_milestone.py` for a complete demonstration of code structuring, naming conventions, and readability best practices:

```bash
python scripts/readability_milestone.py
```

Key principles illustrated:
- Place imports at the top
- Group variable definitions logically
- Separate helper functions from execution logic
- Maintain a clear top-to-bottom flow
- Use descriptive names and comments
- Avoid deeply nested or repetitive code

By following these practices, your code will be easier to maintain, scale, and share with others.

---

## Milestone: Understanding Array Shape, Dimensions, and Index Positions in NumPy

This milestone focuses on understanding array shape, dimensions, and index positions in NumPy. Correctly interpreting how data is laid out in an array is essential for accessing values safely, avoiding index errors, and writing correct numerical code.

### Learning Objectives
By completing this milestone, you will be able to:
- ✅ Interpret array shapes confidently
- ✅ Understand dimensions and axes
- ✅ Access elements using proper indexing
- ✅ Navigate rows and columns correctly
- ✅ Prevent index-related bugs

### Why This Matters
Common beginner issues include:
- Index errors due to incorrect positions
- Confusion between rows and columns
- Misunderstanding array dimensions
- Incorrect assumptions about array layout

This milestone ensures that:
- You understand how data is stored in arrays
- You can access and manipulate data correctly
- Your code behaves predictably
- You are ready for slicing and reshaping later

### What You Are Expected to Do
This is a NumPy fundamentals milestone, not a data analysis task.

You are expected to:
- Inspect array shape and dimensions
- Work with 1D and 2D arrays
- Access elements using index positions
- Print results to observe behavior

### Demo Script
See `scripts/numpy_milestone.py` for a complete demonstration of all these concepts:

```bash
python scripts/numpy_milestone.py
```

### Key Concepts Demonstrated
- Understanding array shape and what each number means
- Identifying 1D, 2D, and higher-dimensional arrays
- Using `.shape` and `.ndim` to inspect arrays
- Accessing elements in 1D and 2D arrays using correct index positions
- Visualizing array layout and mapping index positions to values
- Avoiding common indexing mistakes (zero-based indexing, out-of-range errors)

### Video Walkthrough Checklist
For your video submission, demonstrate:
- Inspecting array shape and dimensions
- Accessing elements in 1D and 2D arrays
- Visualizing array layout and index mapping
- Explaining how to avoid index errors

---

## Milestone: Performing Basic Mathematical Operations on NumPy Arrays

This milestone focuses on performing basic mathematical operations on NumPy arrays. NumPy allows you to apply operations to entire arrays at once, making numerical computation faster, cleaner, and more expressive than using Python loops or lists.

### Learning Objectives
By completing this milestone, you will be able to:
- ✅ Add, subtract, multiply, and divide NumPy arrays
- ✅ Apply scalar operations across arrays
- ✅ Understand element-wise behavior clearly
- ✅ Avoid common mistakes with array math
- ✅ Use NumPy for efficient numerical computation

### Why This Matters
Common beginner issues include:
- Using loops for simple numerical operations
- Expecting Python list math to behave like NumPy
- Writing verbose, inefficient code
- Confusion around how operations are applied

NumPy addresses these problems directly, ensuring your numerical code is concise, readable, and efficient.

### What You Are Expected to Do
This is a NumPy fundamentals milestone, not a data analysis task.

You are expected to:
- Create NumPy arrays
- Perform basic arithmetic operations
- Observe element-wise behavior
- Print results to verify correctness

### Demo Script
See `scripts/numpy_milestone.py` for a complete demonstration of all these concepts:

```bash
python scripts/numpy_milestone.py
```

### Key Concepts Demonstrated
- Element-wise array operations (addition, subtraction, multiplication, division)
- Scalar operations on arrays (applying a single value to all elements)
- Comparison of NumPy array math with Python list behavior
- Common mistakes: shape mismatches, data type errors, and how to interpret them

### Video Walkthrough Checklist
For your video submission, demonstrate:
- Adding, subtracting, multiplying, and dividing arrays
- Applying scalar operations
- Comparing array and list math
- Showing and explaining common mistakes and errors

---
