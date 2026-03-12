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

## Requirements & Setup

This project requires Python 3.8+ and several data science packages.

### Installing Required Packages

Install all required packages using:

```bash
pip install -r requirements.txt
```

### Required Packages:
- **pandas** (≥1.5.0) - Data manipulation and analysis
- **numpy** (≥1.23.0) - Numerical computing
- **matplotlib** (≥3.6.0) - Data visualization
- **jupyter** (≥1.0.0) - Interactive notebooks (optional)

If you prefer to install packages individually:

```bash
pip install pandas numpy matplotlib jupyter
```

### Verifying Installation

Test your setup by running:

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
print("All packages installed successfully!")
```

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

## Milestone: Identifying and Removing Duplicate Records

This milestone focuses on identifying and removing duplicate records in Pandas DataFrames. Duplicate data is a common data quality issue that can skew analysis, inflate counts, and lead to incorrect conclusions if not handled properly.

Learning how to detect and remove duplicates ensures your dataset represents unique, reliable observations.

### Learning Objectives
By completing this milestone, you will be able to:
- ✅ Identify duplicate rows in a dataset
- ✅ Understand why duplicates occur
- ✅ Remove duplicates using appropriate methods
- ✅ Preserve important data while deduplicating
- ✅ Improve overall data quality

### Why This Matters
Common beginner issues include:
- Counting duplicate records as unique observations
- Inflated metrics and misleading summaries
- Removing duplicates without understanding their impact
- Losing important information during cleanup

Duplicate data silently corrupts analysis results.

This milestone ensures that:
- Each row represents a unique observation
- Aggregations and statistics are accurate
- Data integrity is preserved
- Downstream analysis is trustworthy

Think of deduplication as removing noise from your data.

### What You Are Expected to Do
This is a data cleaning milestone, not an analysis task.

You are expected to:
- Load a DataFrame that may contain duplicates
- Detect duplicate records
- Remove duplicates intentionally
- Inspect the results after removal

No modeling or visualization is required.

### Key Topics Covered

#### 1. Understanding Duplicate Records
Learn what duplicates look like.
- Understand row-level duplication
- Recognize exact vs partial duplicates
- Understand why duplicates occur
- Avoid assumptions about uniqueness

#### 2. Detecting Duplicate Rows
Identify repeated records.
- Detect duplicate rows in a DataFrame
- Identify how many duplicates exist
- Inspect duplicate entries
- Understand boolean duplicate indicators

#### 3. Removing Duplicate Records
Clean the dataset.
- Remove duplicate rows safely
- Choose which duplicates to keep
- Apply deduplication to selected columns if needed
- Understand the effect on dataset size

#### 4. Verifying Deduplication Results
Confirm data quality.
- Compare dataset shape before and after
- Recheck for remaining duplicates
- Ensure important records are retained
- Document what changed

### Demo Scripts

See the following resources for complete demonstrations:

**Python Script:**
```bash
python scripts/duplicate_records_milestone.py
```

**Interactive Notebook:**
```bash
jupyter notebook notebooks/duplicate_records_milestone.ipynb
```

### Key Methods Demonstrated
- `duplicated()` - Detect duplicate rows (returns boolean Series)
- `duplicated(subset=[...])` - Detect duplicates in specific columns
- `duplicated(keep='first')` - Mark all except first occurrence
- `duplicated(keep='last')` - Mark all except last occurrence
- `duplicated(keep=False)` - Mark all duplicate occurrences
- `drop_duplicates()` - Remove duplicate rows
- `drop_duplicates(subset=[...])` - Remove based on specific columns
- `drop_duplicates(keep='first')` - Keep first occurrence
- `drop_duplicates(keep='last')` - Keep last occurrence
- `drop_duplicates(keep=False)` - Remove all duplicate occurrences

### Video Walkthrough Checklist
For your video submission, demonstrate:
- Detecting duplicate rows using `duplicated()`
- Viewing duplicate records
- Removing duplicates with `drop_duplicates()`
- Verifying results after deduplication
- Explaining when to keep first vs last occurrence

---

## Milestone: Standardizing Column Names and Data Formats

This milestone focuses on standardizing column names and data formats in Pandas DataFrames. Inconsistent naming and formatting make datasets harder to understand, combine, and analyze—especially when working with real-world data from multiple sources.

Standardization is a critical step in preparing clean, reliable, and analysis-ready data.

### Learning Objectives
By completing this milestone, you will be able to:
- ✅ Convert column names to a consistent format
- ✅ Remove spaces and special characters from column names
- ✅ Apply predictable naming conventions
- ✅ Standardize simple data formats (text, dates, numbers)
- ✅ Improve dataset usability and readability

### Why This Matters
Common beginner issues include:
- Column names with spaces or mixed casing
- Inconsistent naming across datasets
- Difficulty referencing columns in code
- Errors when merging or transforming data

Messy column names lead to messy code.

This milestone ensures that:
- Column access is simple and predictable
- Code is cleaner and less error-prone
- Datasets are easier to merge and reuse
- Analysis workflows scale better

Think of standardization as setting rules for your data to follow.

### What You Are Expected to Do
This is a data cleaning and formatting milestone, not an analysis task.

You are expected to:
- Load a DataFrame
- Standardize column names
- Apply consistent formatting to selected data
- Inspect results after standardization

No modeling or visualization is required.

### Key Topics Covered

#### 1. Standardizing Column Names
Clean and normalize column headers.
- Convert column names to lowercase
- Replace spaces with underscores
- Remove or handle special characters
- Apply a consistent naming style

#### 2. Choosing Naming Conventions
Be consistent and intentional.
- Use snake_case for column names
- Avoid abbreviations that reduce clarity
- Keep names descriptive but concise
- Apply the same rules across all columns

#### 3. Standardizing Text Data
Normalize string values.
- Convert text to lowercase or uppercase
- Strip extra whitespace
- Ensure consistent category values
- Avoid mixed formats in the same column

#### 4. Standardizing Numeric and Date Formats
Ensure uniform data representation.
- Ensure numeric columns are truly numeric
- Standardize simple date formats conceptually
- Recognize formatting issues early
- Prepare data for downstream processing

### Demo Scripts

See the following resources for complete demonstrations:

**Python Script:**
```bash
python scripts/standardizing_data_milestone.py
```

**Interactive Notebook:**
```bash
jupyter notebook notebooks/standardizing_data_milestone.ipynb
```

### Key Methods Demonstrated

**Column Name Standardization:**
- `df.columns.str.lower()` - Convert to lowercase
- `df.columns.str.replace(' ', '_')` - Replace spaces
- `df.columns.str.replace('[^a-z0-9_]', '', regex=True)` - Remove special chars
- `df.columns.str.strip('_')` - Remove leading/trailing underscores

**Text Standardization:**
- `df['col'].str.lower()` - Convert text to lowercase
- `df['col'].str.upper()` - Convert text to uppercase
- `df['col'].str.title()` - Convert text to title case
- `df['col'].str.strip()` - Remove leading/trailing whitespace

**Data Type Conversion:**
- `pd.to_numeric(df['col'], errors='coerce')` - Convert to numeric
- `pd.to_datetime(df['col'], errors='coerce')` - Convert to datetime

### Reusable Function
Create a standardization function for your projects:
```python
def standardize_column_names(df):
    """Convert column names to snake_case format."""
    df = df.copy()
    df.columns = df.columns.str.lower()
    df.columns = df.columns.str.strip()
    df.columns = df.columns.str.replace(' ', '_')
    df.columns = df.columns.str.replace('[^a-z0-9_]', '', regex=True)
    df.columns = df.columns.str.replace('_+', '_', regex=True)
    df.columns = df.columns.str.strip('_')
    return df
```

### Video Walkthrough Checklist
For your video submission, demonstrate:
- Standardizing messy column names to snake_case
- Converting text data to consistent case
- Stripping whitespace from text columns
- Converting string numbers to numeric type
- Explaining the importance of naming conventions

---

## Milestone: Comparing Distributions Across Multiple Columns

This milestone focuses on **comparing distributions across multiple columns** in a Pandas DataFrame. Comparing distributions helps you understand how different variables behave relative to each other and reveals patterns that single-column analysis cannot show.

This is a key step in Exploratory Data Analysis (EDA) before drawing any insights or conclusions.

### Learning Objectives
By completing this milestone, you will be able to:
- ✅ Compute summary statistics for multiple columns
- ✅ Compare means, medians, and ranges across columns
- ✅ Identify columns with higher or lower variability
- ✅ Detect unusual distributions conceptually
- ✅ Use comparisons to guide deeper analysis

### Why This Matters
Common beginner issues include:
- Analyzing columns in isolation
- Missing relationships between variables
- Comparing raw values instead of distributions
- Drawing conclusions without context

**Most real insights come from comparison, not isolation.**

This milestone ensures that:
- You understand how variables differ from each other
- Patterns across columns become visible
- Analysis decisions are more informed
- You avoid misleading conclusions

Think of distribution comparison as putting columns side by side and asking, "How are these different?"

### What You Are Expected to Do
This is a data understanding milestone, not a modeling task.

You are expected to:
- Load a DataFrame with multiple numeric columns
- Compute summary statistics for each column
- Compare distributions using statistics
- Interpret differences meaningfully

No visualization or modeling is required.

### Key Topics Covered

#### 1. Understanding Distributions Across Columns
Build a comparative mindset.
- Understand what distribution means for a column
- Recognize that each column has its own spread
- Avoid comparing raw values directly
- Focus on patterns, not single numbers

Comparison adds context.

#### 2. Comparing Central Tendency
Look at averages across columns.
- Compare means across multiple columns
- Compare medians to detect skew
- Understand why averages may differ
- Avoid assuming "higher is better"

Central tendency is only one part of the story.

#### 3. Comparing Spread and Variability
Understand how data is distributed.
- Compare ranges across columns
- Compare standard deviation conceptually
- Identify columns with high variability
- Recognize stability vs volatility in data

Spread explains consistency.

#### 4. Identifying Patterns and Anomalies
Detect interesting behavior.
- Identify columns that behave differently
- Notice unusually wide or narrow distributions
- Use statistics to raise questions
- Avoid jumping to conclusions

EDA is about asking better questions.

### Demo Scripts

See the following resources for complete demonstrations:

**Python Script:**
```bash
python scripts/comparing_distributions_milestone.py
```

**Interactive Notebook:**
```bash
jupyter notebook notebooks/comparing_distributions_milestone.ipynb
```

**Complete Documentation:**
See `notebooks/COMPARING_DISTRIBUTIONS_README.md` for comprehensive guide, teaching notes, and assessment ideas.

### Key Methods and Concepts Demonstrated

**Summary Statistics:**
- `df.describe()` - Multi-column summary statistics
- `df.mean()` - Compare average values across columns
- `df.median()` - Compare middle values (robust to outliers)
- `df.std()` - Compare variability/spread
- `df.min()`, `df.max()` - Compare ranges

**Comparison Techniques:**
- Creating comparison tables with multiple metrics
- Sorting columns by statistical measures
- Detecting skewness (mean vs median)
- Computing Coefficient of Variation (CV) for relative comparison
- Building comprehensive comparison DataFrames

**Pattern Detection:**
- Identifying similar vs contrasting distributions
- Detecting unusual variability
- Recognizing scale differences
- Spotting columns that warrant investigation

### Sample Dataset
The milestone uses a **student performance dataset** with intentionally different distributions:

| Column | Mean | Std Dev | Characteristics |
|--------|------|---------|-----------------|
| `math_score` | ~75 | ~8 | High mean, low variability |
| `science_score` | ~70 | ~10 | Moderate mean and variability |
| `english_score` | ~65 | ~15 | Lower mean, high variability |
| `attendance_pct` | ~92 | ~5 | Very high, very consistent |
| `study_hours` | ~15 | ~5 | Different scale, moderate variability |
| `assignment_completion` | ~85 | ~12 | Moderate mean and variability |

This diversity enables meaningful comparison exercises and pattern recognition.

### Key Formulas

**Coefficient of Variation (CV):**
```
CV = (Standard Deviation / Mean) × 100
```
Use CV to compare variability across different scales.

**Range:**
```
Range = Maximum - Minimum
```
Shows the full span of values.

**Detecting Skewness:**
```
If mean ≈ median: Symmetric distribution
If mean > median: Right-skewed (positive skew)
If mean < median: Left-skewed (negative skew)
```

### Practice Exercise
The milestone includes a practice exercise with a **product sales dataset** featuring:
- Price and cost data
- Units sold
- Customer ratings
- Discount percentages

You'll perform a complete distribution comparison analysis and suggest next analytical steps based on your findings.

### Key Takeaways

**Distributional comparison is essential for:**
- Understanding how variables differ from each other
- Identifying patterns and anomalies across columns
- Making informed analysis decisions
- Adding context to single-column statistics

**Remember:**
- Compare central tendency (mean, median) to understand typical values
- Compare spread (std, range) to understand variability
- Use relative measures (CV) when scales differ
- Look for patterns, not just individual numbers
- Let comparisons guide your next analytical steps

**Most importantly:**
- Always compare distributions before drawing conclusions
- Context from comparison prevents misleading insights
- Multi-column thinking reveals relationships
- Distribution analysis is the foundation of good EDA

### Video Walkthrough Checklist
For your video submission, demonstrate:
- Using `describe()` to compare multiple columns at once
- Comparing means and medians across columns
- Identifying which column has highest/lowest variability
- Computing and interpreting Coefficient of Variation
- Explaining when distributions suggest further investigation

---

## Milestone: Visualizing Data Distributions Using Histograms

This milestone focuses on **visualizing data distributions using histograms**. Histograms are one of the most effective ways to understand how values are distributed across a numeric column, revealing patterns that summary statistics alone may hide.

Visualization helps you see the data, not just describe it numerically.

### Learning Objectives
By completing this milestone, you will be able to:
- ✅ Create histograms for single and multiple columns
- ✅ Interpret distribution shape and spread
- ✅ Identify skewed or uneven distributions
- ✅ Detect potential outliers visually
- ✅ Use histograms to guide further analysis

### Why This Matters
Common beginner issues include:
- Relying only on averages without seeing the data
- Missing skewed or multi-modal distributions
- Overlooking outliers that affect analysis
- Misinterpreting summary statistics

**Histograms reveal patterns that numbers alone cannot.**

This milestone ensures that:
- You understand how data is distributed
- Patterns and anomalies become visible
- Statistical results are interpreted in context
- EDA decisions are better informed

Think of histograms as a visual summary of your data's behavior.

### What You Are Expected to Do
This is a data visualization milestone, not a modeling task.

You are expected to:
- Load a dataset into a DataFrame
- Select one or more numeric columns
- Create histograms for those columns
- Interpret what the histograms show

No modeling or advanced visualization is required.

### Key Topics Covered

#### 1. Understanding Histograms
Learn what histograms show.
- Understand bins and frequencies
- Recognize how values are grouped
- Understand range and distribution shape
- Avoid confusing histograms with bar charts

Histograms are for continuous numeric data.

#### 2. Creating a Histogram for a Single Column
Visualize one distribution.
- Select a numeric column
- Create a histogram
- Observe how values are distributed
- Adjust bins conceptually if needed

Single-column histograms build intuition.

#### 3. Interpreting Distribution Shape
Learn to read patterns.
- Identify skewed distributions (right, left)
- Recognize roughly normal distributions
- Notice gaps or clusters
- Understand what shape suggests about the data

Shape tells a story.

#### 4. Comparing Histograms Across Columns
Extend visual comparison.
- Create histograms for multiple columns
- Compare spread and skew visually
- Identify columns with different behavior
- Use visuals to support statistical comparisons

Visual comparison complements statistics.

### Demo Scripts

See the following resources for complete demonstrations:

**Python Script:**
```bash
python scripts/visualizing_histograms_milestone.py
```

**Interactive Notebook:**
```bash
jupyter notebook notebooks/visualizing_histograms_milestone.ipynb
```

### Key Concepts Demonstrated

**Distribution Shapes:**
- **Normal (Bell-Shaped)**: Symmetric around mean, Mean ≈ Median
- **Right-Skewed**: Tail extends right, Mean > Median
- **Left-Skewed**: Tail extends left, Mean < Median
- **Bimodal**: Two distinct peaks, suggests two groups
- **Uniform**: Roughly flat, all values equally likely

**Histogram Components:**
- **Bins**: Intervals dividing the range of values
- **Frequency**: Count of values in each bin
- **Shape**: Overall pattern of the distribution
- **Outliers**: Isolated bars far from main distribution

**Plotting Methods:**
- `df['column'].hist()` - Single column histogram
- `df.hist()` - All numeric columns at once
- Adjusting bins: `hist(bins=20)`
- Adding mean/median lines with `axvline()`

### Sample Dataset
The milestone uses a **student performance dataset** with diverse distribution shapes:

| Column | Distribution Shape | Characteristics |
|--------|-------------------|-----------------|
| `math_score` | Normal (Bell-shaped) | Symmetric, mean ≈ median |
| `study_hours` | Right-skewed | Most values low, few high values |
| `attendance_pct` | Left-skewed | Most values high, few low values |
| `assignment_score` | Bimodal | Two distinct peaks (two groups) |
| `random_metric` | Uniform | Roughly flat distribution |
| `quiz_score` | With outliers | Main cluster with isolated low values |

This diversity helps you practice recognizing different distribution patterns.

### Key Visualizations Created

The milestone generates 7 plots demonstrating:

1. **Single column histogram** - Basic histogram for math scores
2. **Bin comparison** - Same data with 5, 15, and 40 bins
3. **Distribution shapes** - All 6 different distribution types
4. **Outlier detection** - Quiz scores with/without outliers
5. **Score comparison** - Side-by-side test score histograms
6. **All columns grid** - Overview of all distributions
7. **Practice exercise** - Product sales data analysis

### Using Histograms to Guide Analysis

**If distribution is NORMAL (symmetric):**
- → Use mean as summary statistic
- → Can use parametric statistical tests
- → Standard deviation is meaningful
- → Proceed with standard methods

**If distribution is SKEWED:**
- → Use median instead of mean
- → Consider transformation (log, sqrt)
- → Be cautious with parametric tests
- → Report skewness explicitly

**If distribution has OUTLIERS:**
- → Investigate outliers individually
- → Decide: Remove, keep, or analyze separately
- → Use robust statistics (median, IQR)
- → Consider outlier impact on models

**If distribution is BIMODAL:**
- → You may have TWO distinct groups
- → Consider segmentation or clustering
- → Analyze groups separately
- → Investigate what causes the split

**If distribution is UNIFORM:**
- → No clear central tendency
- → All values equally common
- → May indicate data quality issue or special case

### Practice Exercise
The milestone includes a practice exercise with **product sales data** featuring:
- Price (bimodal distribution - two product tiers)
- Units sold (right-skewed - most products sell moderately)
- Customer rating (left-skewed - most ratings high)
- Discount percentage (uniform - no clear pattern)

You'll create histograms, identify shapes, and recommend analysis strategies.

### Best Practices

**Do's ✓**
- Always create histograms BEFORE relying on summary statistics
- Adjust bin count if default doesn't reveal patterns
- Add mean/median lines to show central tendency
- Compare distributions side-by-side
- Look for shape, spread, outliers, and gaps
- Use histograms to decide between mean vs median
- Let visual patterns guide next analytical steps

**Don'ts ✗**
- Don't rely only on mean/std without visualizing
- Don't use too few or too many bins
- Don't confuse histograms with bar charts
- Don't ignore skewness and outliers
- Don't assume all numeric data is normally distributed

### Key Takeaways

**Histograms are essential for:**
- Visualizing how data is distributed
- Identifying shape, skewness, and outliers
- Deciding between mean vs median
- Detecting bimodal or multi-modal patterns
- Guiding statistical analysis decisions

**Remember:**
- Histograms reveal patterns that numbers alone cannot
- Shape determines which statistics and methods to use
- Visual comparison complements statistical comparison  
- Outliers and skewness are visible immediately
- Always visualize before assuming normality

**Most importantly:**
- Never rely on summary statistics alone
- Visualize first, then analyze
- Let distribution shape guide your methods
- Histograms are the foundation of good EDA

### Integration with Other Milestones

This milestone builds on:
- **Comparing Distributions Milestone**: Adds visual analysis to statistical comparison
- **DataFrame Inspection**: Using `describe()` with visual context
- **Missing Values Detection**: Understanding data completeness before plotting

This milestone prepares you for:
- **Box plots**: Additional outlier visualization
- **Scatter plots**: Bivariate relationship visualization
- **Correlation analysis**: Understanding relationships between variables
- **Statistical modeling**: Choosing appropriate models based on distribution

### Video Walkthrough Checklist
For your video submission, demonstrate:
- Creating a basic histogram for a single column
- Comparing different bin sizes (5, 15, 40 bins)
- Identifying distribution shapes (normal, skewed, bimodal)
- Detecting outliers visually in a histogram
- Comparing multiple distributions side-by-side
- Explaining what the histogram shape tells you about using mean vs median

---
