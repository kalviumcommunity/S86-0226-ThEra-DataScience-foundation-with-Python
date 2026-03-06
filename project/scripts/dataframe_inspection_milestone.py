"""
DataFrame Inspection Milestone - Pandas Fundamentals
=====================================================

This script demonstrates the fundamentals of inspecting Pandas DataFrames using:
- head() for previewing data
- info() for understanding structure and data types
- describe() for summarizing numeric data

These three methods provide a complete snapshot of your data before any analysis.

Author: Your Name
Date: March 6, 2026
"""

import pandas as pd
import numpy as np
import os

print("=" * 80)
print("DATAFRAME INSPECTION MILESTONE - PANDAS FUNDAMENTALS")
print("=" * 80)
print()

# =============================================================================
# INTRODUCTION
# =============================================================================
print("INTRODUCTION: Why DataFrame Inspection Matters")
print("-" * 80)
print("""
After loading data, inspection is THE MOST IMPORTANT step before any analysis.

The three essential inspection methods are:
1. head() - Preview the actual data rows
2. info() - Understand structure, types, and missing values
3. describe() - Get statistical summaries of numeric columns

These methods answer critical questions:
- What does my data look like?
- What data types do I have?
- Are there missing values?
- What are the distributions of numeric columns?

Think of inspection as "reading before analyzing."
""")
print()

# =============================================================================
# LOAD SAMPLE DATA
# =============================================================================
print("=" * 80)
print("LOADING SAMPLE DATA")
print("=" * 80)
print()

# Load existing CSV files
raw_data_path = '../data/raw/example_raw.csv'
processed_data_path = '../data/processed/example_processed.csv'

df_raw = pd.read_csv(raw_data_path)
df_processed = pd.read_csv(processed_data_path)

print("✓ Sample datasets loaded")
print()

# Create a more comprehensive sample dataset for better demonstration
print("Creating a comprehensive sample dataset for demonstration...")
np.random.seed(42)

sample_data = {
    'student_id': range(1, 21),
    'name': [f'Student_{i}' for i in range(1, 21)],
    'age': np.random.randint(18, 25, 20),
    'grade': np.random.choice(['A', 'B', 'C', 'D'], 20),
    'score': np.random.randint(60, 100, 20),
    'attendance': np.random.uniform(70, 100, 20),
    'passed': np.random.choice([True, False], 20, p=[0.8, 0.2]),
    'notes': ['Good' if i % 3 == 0 else np.nan for i in range(20)]
}

df_sample = pd.DataFrame(sample_data)
print("✓ Comprehensive sample dataset created")
print()

# =============================================================================
# SECTION 1: Inspecting Data with head()
# =============================================================================
print("=" * 80)
print("SECTION 1: Inspecting Data with head()")
print("=" * 80)
print()

print("What is head()?")
print("-" * 80)
print("""
head() displays the FIRST FEW ROWS of a DataFrame.

Purpose:
- Get a quick visual preview of the data
- See column names in context
- Check data alignment
- Verify data loaded correctly
- Understand the format of values

Default: Shows first 5 rows
You can specify: head(n) to show first n rows
""")
print()

print("Example 1: Using head() with default settings (5 rows)")
print("-" * 80)
print(df_sample.head())
print()

print("Example 2: Using head(10) to see more rows")
print("-" * 80)
print(df_sample.head(10))
print()

print("Example 3: Using head(3) to see fewer rows")
print("-" * 80)
print(df_sample.head(3))
print()

print("What head() tells you:")
print("-" * 80)
print("""
✓ Column names - What variables do you have?
✓ Sample values - What does the data actually look like?
✓ Data format - Are values numbers, text, dates?
✓ Missing values - Can you see any NaN values?
✓ Data alignment - Are values in the right columns?

IMPORTANT: head() shows SAMPLE data, not ALL data.
Don't make conclusions about the entire dataset from head() alone!
""")
print()

print("Comparing with tail() - Last rows")
print("-" * 80)
print("tail() shows the LAST few rows (useful to check end of data)")
print(df_sample.tail())
print()

# =============================================================================
# SECTION 2: Inspecting Structure with info()
# =============================================================================
print("=" * 80)
print("SECTION 2: Inspecting Structure with info()")
print("=" * 80)
print()

print("What is info()?")
print("-" * 80)
print("""
info() provides a CONCISE SUMMARY of the DataFrame structure.

Information provided:
- Total number of rows and columns
- Column names
- Non-null counts (how many non-missing values)
- Data types (dtype)
- Memory usage

This is your "health check" for the DataFrame.
""")
print()

print("Example: Using info() on sample dataset")
print("-" * 80)
df_sample.info()
print()

print("Understanding the info() output:")
print("-" * 80)
print("""
1. RANGEINDEX: Shows the index (0 to n-1)
   - "RangeIndex: 20 entries, 0 to 19" means 20 rows

2. DATA COLUMNS: Lists each column with details
   - Column name
   - Non-Null Count: How many values are NOT missing
   - Dtype: The data type

3. DTYPES: Summary of data types
   - int64: Integer numbers
   - float64: Decimal numbers
   - object: Text/strings or mixed types
   - bool: Boolean (True/False)

4. MEMORY USAGE: How much RAM the DataFrame uses

KEY INSIGHT: Non-Null Count vs Total Rows
If Non-Null Count < Total Rows → Missing values exist!
""")
print()

print("Example: Identifying missing values with info()")
print("-" * 80)
print(f"Total rows in dataset: {len(df_sample)}")
print("\nColumn non-null counts:")
for col in df_sample.columns:
    non_null = df_sample[col].notna().sum()
    missing = len(df_sample) - non_null
    print(f"  {col}: {non_null} non-null ({missing} missing)")
print()

print("Why info() is critical:")
print("-" * 80)
print("""
✓ Reveals data types - Ensures columns are correct type
✓ Shows missing values - Identifies data quality issues
✓ Memory usage - Important for large datasets
✓ Quick overview - Fast way to understand structure

COMMON ISSUES CAUGHT BY info():
- Numbers stored as 'object' (string) instead of int/float
- Date columns stored as 'object' instead of datetime
- Missing values you didn't know about
- Wrong number of columns after loading
""")
print()

# =============================================================================
# SECTION 3: Summarizing Data with describe()
# =============================================================================
print("=" * 80)
print("SECTION 3: Summarizing Data with describe()")
print("=" * 80)
print()

print("What is describe()?")
print("-" * 80)
print("""
describe() provides STATISTICAL SUMMARIES of numeric columns.

Statistics provided:
- count: Number of non-missing values
- mean: Average value
- std: Standard deviation (spread)
- min: Minimum value
- 25%: First quartile (25th percentile)
- 50%: Median (50th percentile)
- 75%: Third quartile (75th percentile)
- max: Maximum value

This gives you numeric context at a glance.
""")
print()

print("Example: Using describe() on sample dataset")
print("-" * 80)
print(df_sample.describe())
print()

print("Understanding the describe() output:")
print("-" * 80)
print("""
ROW MEANINGS:

count: How many non-missing values
  - If count < total rows → missing values exist
  - Should match info() non-null count

mean: Average value
  - Center of the distribution
  - Sensitive to outliers

std: Standard deviation
  - How spread out the values are
  - Low std = values are similar
  - High std = values vary widely

min/max: Range boundaries
  - Check for impossible values (e.g., negative age)
  - Identify potential outliers

25%, 50%, 75%: Quartiles
  - 50% is the median (middle value)
  - Quartiles show distribution shape
  - Less sensitive to outliers than mean

EXAMPLE INTERPRETATION:
If mean >> median → Data is right-skewed (outliers pulling mean up)
If mean << median → Data is left-skewed (outliers pulling mean down)
""")
print()

print("Example: Interpreting specific columns")
print("-" * 80)
print("\nAge column analysis:")
age_stats = df_sample['age'].describe()
print(age_stats)
print(f"\nInterpretation:")
print(f"  - Average age: {age_stats['mean']:.1f} years")
print(f"  - Age range: {age_stats['min']:.0f} to {age_stats['max']:.0f}")
print(f"  - Most students between {age_stats['25%']:.0f} and {age_stats['75%']:.0f} years")
print()

print("\nScore column analysis:")
score_stats = df_sample['score'].describe()
print(score_stats)
print(f"\nInterpretation:")
print(f"  - Average score: {score_stats['mean']:.1f}")
print(f"  - Score range: {score_stats['min']:.0f} to {score_stats['max']:.0f}")
print(f"  - Middle 50% scored between {score_stats['25%']:.0f} and {score_stats['75%']:.0f}")
print()

print("describe() for non-numeric columns:")
print("-" * 80)
print("By default, describe() only shows numeric columns.")
print("Use describe(include='all') to include non-numeric columns:")
print()
print(df_sample.describe(include='all'))
print()

print("Why describe() is essential:")
print("-" * 80)
print("""
✓ Quick statistics - Understand distributions instantly
✓ Spot outliers - Extreme min/max values stand out
✓ Check ranges - Verify values are reasonable
✓ Detect issues - Impossible values become obvious
✓ Plan analysis - Know what you're working with

COMMON ISSUES CAUGHT BY describe():
- Negative values where they shouldn't exist (age, price)
- Extreme outliers (max >> typical values)
- Zero variance (std = 0, all values the same)
- Missing values (count < total rows)
""")
print()

# =============================================================================
# SECTION 4: Knowing When to Use Each Method
# =============================================================================
print("=" * 80)
print("SECTION 4: When to Use Each Inspection Method")
print("=" * 80)
print()

print("Method Comparison Guide:")
print("-" * 80)
print("""
METHOD   | PURPOSE              | WHEN TO USE
---------|----------------------|----------------------------------------
head()   | Visual preview       | - First look at data
         |                      | - Check data alignment
         |                      | - See actual values
         |                      | - Verify column names in context
---------|----------------------|----------------------------------------
info()   | Structural summary   | - Check data types
         |                      | - Find missing values
         |                      | - Verify column count
         |                      | - Understand memory usage
---------|----------------------|----------------------------------------
describe()| Numeric statistics  | - Understand distributions
         |                      | - Find outliers
         |                      | - Check value ranges
         |                      | - Get quick summaries
---------|----------------------|----------------------------------------

RECOMMENDED WORKFLOW:
1. Load data
2. Use head() - Quick visual check
3. Use info() - Structural health check
4. Use describe() - Numeric understanding
5. Start analysis with confidence
""")
print()

print("Demonstration: Complete inspection workflow")
print("-" * 80)
print("\nDataset: Student Performance Data")
print()

print("STEP 1: Quick preview with head()")
print("-" * 40)
print(df_sample.head(3))
print()

print("STEP 2: Structural check with info()")
print("-" * 40)
df_sample.info()
print()

print("STEP 3: Numeric summary with describe()")
print("-" * 40)
print(df_sample.describe())
print()

print("STEP 4: Draw initial conclusions")
print("-" * 40)
print("""
From inspection, we now know:
✓ Dataset has 20 students (rows) and 8 variables (columns)
✓ Column types: 3 numeric, 3 text/boolean, 1 with missing values
✓ Age range: 18-24 years
✓ Score range: 60-100
✓ Some missing values in 'notes' column
✓ Most students passed (passed = True)

We can now proceed with cleaning or analysis with confidence!
""")
print()

# =============================================================================
# SECTION 5: Best Practices and Common Patterns
# =============================================================================
print("=" * 80)
print("SECTION 5: Best Practices for DataFrame Inspection")
print("=" * 80)
print()

print("Best Practice #1: ALWAYS inspect after loading")
print("-" * 80)
print("""
# Good practice
df = pd.read_csv('data.csv')
df.head()      # Quick look
df.info()      # Structure check
df.describe()  # Numeric summary

# Bad practice
df = pd.read_csv('data.csv')
# Immediately start analysis without inspection ❌
""")
print()

print("Best Practice #2: Use all three methods together")
print("-" * 80)
print("""
Each method reveals different aspects:
- head() shows WHAT the data looks like
- info() shows HOW the data is structured
- describe() shows WHAT the numbers mean

Don't rely on just one method!
""")
print()

print("Best Practice #3: Check for common issues")
print("-" * 80)
print("""
After inspection, ask yourself:
□ Are data types correct? (info)
□ Are there missing values? (info, describe)
□ Do value ranges make sense? (describe)
□ Are column names what I expect? (head)
□ Is the data aligned properly? (head)
□ Are there obvious outliers? (describe)
""")
print()

print("Best Practice #4: Document your observations")
print("-" * 80)
print("""
After inspection, note:
- Number of rows and columns
- Data types of key columns
- Missing value counts
- Unexpected patterns
- Issues to address in cleaning

This helps plan your next steps!
""")
print()

# =============================================================================
# PRACTICAL EXAMPLES
# =============================================================================
print("=" * 80)
print("SECTION 6: Practical Examples")
print("=" * 80)
print()

print("Example 1: Inspecting raw data")
print("-" * 80)
print("\nDataset: example_raw.csv")
print()
print("Step 1 - Preview:")
print(df_raw.head())
print("\nStep 2 - Structure:")
df_raw.info()
print("\nStep 3 - Statistics:")
print(df_raw.describe())
print()

print("Example 2: Inspecting processed data")
print("-" * 80)
print("\nDataset: example_processed.csv")
print()
print("Step 1 - Preview:")
print(df_processed.head())
print("\nStep 2 - Structure:")
df_processed.info()
print("\nStep 3 - Statistics:")
print(df_processed.describe())
print()

# =============================================================================
# COMMON MISTAKES TO AVOID
# =============================================================================
print("=" * 80)
print("COMMON MISTAKES TO AVOID")
print("=" * 80)
print("""
❌ MISTAKE #1: Skipping inspection entirely
   → Always inspect before analysis

❌ MISTAKE #2: Only using head()
   → Use all three methods (head, info, describe)

❌ MISTAKE #3: Assuming data types are correct
   → Check with info() - numbers might be stored as strings

❌ MISTAKE #4: Ignoring missing values
   → Check non-null counts in info()

❌ MISTAKE #5: Not checking value ranges
   → Use describe() to spot impossible values

❌ MISTAKE #6: Drawing conclusions from head() alone
   → head() shows SAMPLE, not entire dataset

❌ MISTAKE #7: Forgetting to check the tail()
   → Data issues often appear at the end

✅ BEST PRACTICE: Use head(), info(), and describe() TOGETHER
   This gives you a complete picture of your data!
""")
print()

# =============================================================================
# VERIFICATION CHECKLIST
# =============================================================================
print("=" * 80)
print("INSPECTION VERIFICATION CHECKLIST")
print("=" * 80)
print("""
After inspecting any DataFrame, verify:

USING head():
☐ Column names are correct
☐ Sample values look reasonable
☐ Data is aligned properly (values in right columns)
☐ You understand what each column represents

USING info():
☐ Number of rows matches expectations
☐ Number of columns matches expectations
☐ Data types are appropriate for each column
☐ Missing values are identified (non-null count < total)
☐ No unexpected 'object' types for numeric columns

USING describe():
☐ Value ranges make sense (no negative ages, etc.)
☐ Means and medians are reasonable
☐ Min/max values are plausible
☐ No extreme outliers (unless expected)
☐ Standard deviations indicate reasonable spread

OVERALL:
☐ You understand the structure of your data
☐ You know what cleaning is needed
☐ You're ready to proceed with confidence
""")
print()

# =============================================================================
# CONCLUSION
# =============================================================================
print("=" * 80)
print("DATAFRAME INSPECTION MILESTONE COMPLETED!")
print("=" * 80)
print("""
You have learned:
✓ How to use head() to preview data rows
✓ How to use info() to understand structure and types
✓ How to use describe() to summarize numeric columns
✓ When to use each inspection method
✓ How to combine all three for complete inspection
✓ Best practices for data inspection

Key Takeaway:
ALWAYS INSPECT BEFORE ANALYSIS!

The three essential methods:
1. head() - What does it look like?
2. info() - How is it structured?
3. describe() - What do the numbers tell me?

Next steps:
- Practice inspection on different datasets
- Learn data cleaning techniques
- Explore advanced inspection methods
- Build the habit of thorough inspection

Remember: "Inspecting data is like reading before writing—essential!"
""")
print()

print("=" * 80)
print("Thank you for completing the DataFrame Inspection Milestone!")
print("=" * 80)
