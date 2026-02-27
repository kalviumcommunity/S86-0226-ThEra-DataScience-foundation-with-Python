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

## Milestone: Working with Python Lists, Tuples, and Dictionaries

This milestone focuses on mastering Python's core collection data structures—**lists**, **tuples**, and **dictionaries**. Understanding when and how to use each structure is essential for handling real-world data efficiently.

### Learning Objectives

By completing this milestone, you will be able to:
- ✅ Create and use lists, tuples, and dictionaries
- ✅ Access elements using indexing and keys
- ✅ Modify lists and dictionaries correctly
- ✅ Understand immutability in tuples
- ✅ Organize structured data effectively
- ✅ Choose the right data structure for a given task

### Scripts Overview

Four comprehensive Python scripts have been created in the `scripts/` folder to demonstrate all concepts:

#### 1. **working_with_lists.py**
Learn about Python lists—ordered and mutable collections.

**Topics covered:**
- Creating lists with multiple values
- Accessing elements using indexes and slicing
- Modifying, adding, and removing elements
- Iterating over list items
- Common list methods (sort, reverse, count, etc.)
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