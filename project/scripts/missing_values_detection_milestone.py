"""
Missing Values Detection Milestone - Pandas Fundamentals
========================================================

This script demonstrates the fundamentals of detecting missing values in Pandas DataFrames using:
- isnull() and isna() for detecting missing values
- notnull() and notna() for detecting non-missing values
- sum() for counting missing values
- any() and all() for checking presence of missing values

Missing data is common in real-world datasets, and detecting it correctly is the first
step before any cleaning, imputation, or analysis.

Author: Your Name
Date: March 9, 2026
"""

import pandas as pd
import numpy as np
import os

print("=" * 80)
print("MISSING VALUES DETECTION MILESTONE - PANDAS FUNDAMENTALS")
print("=" * 80)
print()

# =============================================================================
# INTRODUCTION
# =============================================================================
print("INTRODUCTION: Why Missing Value Detection Matters")
print("-" * 80)
print("""
Missing data is one of the most common challenges in real-world datasets.

Before cleaning, analyzing, or modeling data, you must know:
- WHERE data is missing
- HOW MUCH data is missing
- WHICH columns/rows are affected
- PATTERNS of missingness

The key detection methods are:
1. isnull() / isna() - Detect missing values (returns True for NaN)
2. notnull() / notna() - Detect non-missing values (returns False for NaN)
3. sum() - Count missing values
4. any() - Check if any value is missing
5. all() - Check if all values are missing

Think of missing-value detection as a "data health check."
It prevents:
- Incorrect statistics
- Silent analysis errors
- Wrong assumptions
- Downstream pipeline failures
""")
print()

# =============================================================================
# UNDERSTANDING MISSING VALUES
# =============================================================================
print("=" * 80)
print("SECTION 1: Understanding Missing Values")
print("=" * 80)
print()

print("1.1 What Are Missing Values?")
print("-" * 80)
print("""
Missing values represent the ABSENCE of data.

Common representations:
- NaN (Not a Number) - Pandas/NumPy standard
- None - Python's null object
- Empty strings "" - sometimes used incorrectly
- Placeholder values like -999, "N/A", "Unknown" - domain-specific

Pandas standardizes missing values as NaN for consistency.
""")
print()

print("1.2 How Missing Values Appear")
print("-" * 80)
print("Creating examples of missing values:")
print()

# Example with various missing value representations
example_data = {
    'A': [1, 2, np.nan, 4, 5],
    'B': [np.nan, 2.5, 3.5, np.nan, 5.5],
    'C': ['a', 'b', None, 'd', 'e'],
    'D': [True, False, True, np.nan, False],
    'E': [10, 20, 30, 40, 50]  # No missing values
}

df_example = pd.DataFrame(example_data)
print("Sample DataFrame with missing values:")
print(df_example)
print()

print("Key Observations:")
print("- NaN appears in numeric columns (A, B, D)")
print("- None appears in object column (C) - displayed as NaN")
print("- Column E has no missing values")
print("- Mixed data types can all have missing values")
print()

# =============================================================================
# DETECTING MISSING VALUES
# =============================================================================
print("=" * 80)
print("SECTION 2: Detecting Missing Values")
print("=" * 80)
print()

print("2.1 Using isnull() to Detect Missing Values")
print("-" * 80)
print("""
isnull() returns a boolean DataFrame:
- True where values are missing (NaN)
- False where values exist

Syntax: df.isnull() or df.isna()
Note: isnull() and isna() are identical - use either one
""")
print()

print("Boolean mask showing where values are missing:")
print(df_example.isnull())
print()

print("Interpretation:")
print("- True = Missing value detected")
print("- False = Value exists")
print("- Each cell shows if that specific location has missing data")
print()

print("2.2 Using notnull() to Detect Non-Missing Values")
print("-" * 80)
print("""
notnull() is the opposite of isnull():
- True where values exist
- False where values are missing

Syntax: df.notnull() or df.notna()
""")
print()

print("Boolean mask showing where values exist:")
print(df_example.notnull())
print()

print("Use Case:")
print("- Helpful for filtering rows with complete data")
print("- Identifying valid entries")
print()

# =============================================================================
# COUNTING MISSING VALUES
# =============================================================================
print("=" * 80)
print("SECTION 3: Counting Missing Values")
print("=" * 80)
print()

print("3.1 Count Missing Values Per Column")
print("-" * 80)
print("""
Combining isnull() with sum() counts missing values:
- isnull() creates True/False mask
- sum() treats True as 1, False as 0
- Result: count of missing values per column

Syntax: df.isnull().sum()
""")
print()

missing_counts = df_example.isnull().sum()
print("Missing value counts per column:")
print(missing_counts)
print()

print("Interpretation:")
print(f"- Column A: {missing_counts['A']} missing value(s)")
print(f"- Column B: {missing_counts['B']} missing value(s)")
print(f"- Column C: {missing_counts['C']} missing value(s)")
print(f"- Column D: {missing_counts['D']} missing value(s)")
print(f"- Column E: {missing_counts['E']} missing value(s) - Complete!")
print()

print("3.2 Total Missing Values in Entire DataFrame")
print("-" * 80)
print("Syntax: df.isnull().sum().sum()")
print()

total_missing = df_example.isnull().sum().sum()
print(f"Total missing values in DataFrame: {total_missing}")
print()

print("3.3 Count Non-Missing Values Per Column")
print("-" * 80)
print("Syntax: df.notnull().sum() or df.count()")
print()

non_missing_counts = df_example.notnull().sum()
print("Non-missing value counts per column:")
print(non_missing_counts)
print()

print("Alternative using count():")
print(df_example.count())
print()

# =============================================================================
# IDENTIFYING COLUMNS WITH MISSING DATA
# =============================================================================
print("=" * 80)
print("SECTION 4: Identifying Columns with Missing Data")
print("=" * 80)
print()

print("4.1 Columns That Have ANY Missing Values")
print("-" * 80)
print("""
Using isnull().any() to check if column has at least one missing value:
- Returns True if column has ANY missing values
- Returns False if column is complete

Syntax: df.isnull().any()
""")
print()

columns_with_missing = df_example.isnull().any()
print("Columns with at least one missing value:")
print(columns_with_missing)
print()

# Get list of column names with missing values
missing_columns = columns_with_missing[columns_with_missing].index.tolist()
print(f"Column names with missing data: {missing_columns}")
print()

print("4.2 Columns That Are ALL Missing Values")
print("-" * 80)
print("""
Using isnull().all() to check if column is completely empty:
- Returns True if ALL values in column are missing
- Returns False if column has at least one valid value

Syntax: df.isnull().all()
""")
print()

print("Columns with all values missing:")
print(df_example.isnull().all())
print()

# Create example with completely empty column
df_with_empty_col = df_example.copy()
df_with_empty_col['F'] = np.nan

print("Example with completely empty column F:")
print("\nDataFrame:")
print(df_with_empty_col)
print("\nChecking for completely empty columns:")
print(df_with_empty_col.isnull().all())
print()

# =============================================================================
# INSPECTING ROWS WITH MISSING DATA
# =============================================================================
print("=" * 80)
print("SECTION 5: Inspecting Rows with Missing Data")
print("=" * 80)
print()

print("5.1 Identify Rows with ANY Missing Values")
print("-" * 80)
print("""
Using isnull().any(axis=1) to check rows:
- axis=1 means "check across columns"
- Returns True if row has ANY missing value
- Returns False if row is complete

Syntax: df.isnull().any(axis=1)
""")
print()

rows_with_missing = df_example.isnull().any(axis=1)
print("Rows with at least one missing value:")
print(rows_with_missing)
print()

print(f"Total rows with missing data: {rows_with_missing.sum()}")
print()

print("5.2 View Only Rows with Missing Data")
print("-" * 80)
print("Filter DataFrame to show only rows containing missing values:")
print()

df_with_missing_rows = df_example[df_example.isnull().any(axis=1)]
print(df_with_missing_rows)
print()

print("5.3 View Only Complete Rows (No Missing Values)")
print("-" * 80)
print("Filter DataFrame to show only complete rows:")
print()

df_complete_rows = df_example[df_example.notnull().all(axis=1)]
print(df_complete_rows)
print()

# =============================================================================
# COMPREHENSIVE MISSING VALUES SUMMARY
# =============================================================================
print("=" * 80)
print("SECTION 6: Creating a Comprehensive Missing Values Summary")
print("=" * 80)
print()

print("6.1 Building a Complete Summary Table")
print("-" * 80)
print("""
A comprehensive summary should include:
- Column name
- Total values
- Missing values count
- Missing percentage
- Data type
""")
print()

def missing_values_summary(df):
    """
    Generate a comprehensive summary of missing values in a DataFrame.
    
    Parameters:
    -----------
    df : pandas.DataFrame
        The DataFrame to analyze
    
    Returns:
    --------
    pandas.DataFrame
        Summary with missing value statistics
    """
    # Calculate statistics
    total = df.shape[0]
    missing_count = df.isnull().sum()
    missing_percent = (missing_count / total) * 100
    data_types = df.dtypes
    
    # Create summary DataFrame
    summary = pd.DataFrame({
        'Column': df.columns,
        'Data_Type': data_types.values,
        'Total_Values': total,
        'Missing_Count': missing_count.values,
        'Missing_Percent': missing_percent.values
    })
    
    # Sort by missing count descending
    summary = summary.sort_values('Missing_Count', ascending=False)
    summary = summary.reset_index(drop=True)
    
    return summary

print("Missing Values Summary for Example DataFrame:")
print()
summary = missing_values_summary(df_example)
print(summary)
print()

print("6.2 Filtering Summary to Show Only Problematic Columns")
print("-" * 80)
print("Show only columns with missing values:")
print()

problematic_columns = summary[summary['Missing_Count'] > 0]
print(problematic_columns)
print()

# =============================================================================
# REAL-WORLD EXAMPLE WITH LARGER DATASET
# =============================================================================
print("=" * 80)
print("SECTION 7: Real-World Example - Student Records Dataset")
print("=" * 80)
print()

print("Creating a realistic student records dataset with missing values:")
print()

# Create larger, more realistic dataset
np.random.seed(42)
n_students = 50

student_data = {
    'StudentID': range(1001, 1001 + n_students),
    'Name': [f'Student_{i}' for i in range(1, n_students + 1)],
    'Age': np.random.randint(18, 25, n_students),
    'Gender': np.random.choice(['M', 'F', 'Other', np.nan], n_students, p=[0.45, 0.45, 0.05, 0.05]),
    'Major': np.random.choice(['CS', 'Math', 'Physics', 'Biology', np.nan], n_students, p=[0.3, 0.25, 0.2, 0.2, 0.05]),
    'GPA': np.round(np.random.uniform(2.0, 4.0, n_students), 2),
    'Midterm_Score': np.random.randint(60, 100, n_students),
    'Final_Score': np.random.choice([*np.random.randint(65, 100, 45), *[np.nan]*5]),
    'Attendance_Percent': np.round(np.random.uniform(70, 100, n_students), 1),
    'Email': [f'student{i}@university.edu' if i % 7 != 0 else np.nan for i in range(1, n_students + 1)],
    'Phone': [f'555-{1000+i:04d}' if i % 5 != 0 else np.nan for i in range(1, n_students + 1)]
}

df_students = pd.DataFrame(student_data)

print("Preview of student records dataset:")
print(df_students.head(10))
print()

print("7.1 Quick Missing Values Check")
print("-" * 80)
print("Total missing values:", df_students.isnull().sum().sum())
print()
print("Missing values per column:")
print(df_students.isnull().sum())
print()

print("7.2 Detailed Missing Values Analysis")
print("-" * 80)
summary_students = missing_values_summary(df_students)
print(summary_students)
print()

print("7.3 Key Insights from Analysis")
print("-" * 80)
high_missing = summary_students[summary_students['Missing_Percent'] > 5]
if not high_missing.empty:
    print("Columns with > 5% missing data:")
    print(high_missing[['Column', 'Missing_Count', 'Missing_Percent']])
    print()
    print("⚠️  These columns need attention before analysis!")
else:
    print("✓ No columns have excessive missing data (>5%)")
print()

print("7.4 Sample Rows with Missing Data")
print("-" * 80)
rows_with_missing = df_students[df_students.isnull().any(axis=1)]
print(f"Found {len(rows_with_missing)} rows with missing values")
print("\nFirst 5 rows with missing data:")
print(rows_with_missing.head())
print()

# =============================================================================
# BEST PRACTICES AND COMMON MISTAKES
# =============================================================================
print("=" * 80)
print("SECTION 8: Best Practices and Common Mistakes")
print("=" * 80)
print()

print("✓ BEST PRACTICES")
print("-" * 80)
print("""
1. ALWAYS check for missing values immediately after loading data
   - Use df.isnull().sum() as a quick health check
   
2. Create a comprehensive summary before analysis
   - Know which columns are affected
   - Calculate missing percentages
   
3. Inspect rows with missing data
   - Look for patterns
   - Understand why data might be missing
   
4. Document missing value findings
   - Record in data quality reports
   - Note decisions made about handling
   
5. Never assume data is complete
   - Missing values can appear anywhere
   - Even "clean" datasets have surprises
""")
print()

print("✗ COMMON MISTAKES")
print("-" * 80)
print("""
1. Ignoring missing values
   - Leads to incorrect statistics
   - Causes silent analysis errors
   
2. Confusing empty strings with NaN
   - "" is not the same as NaN
   - Check for both: df.isnull() and df == ""
   
3. Not checking for missing values before analysis
   - Most statistical functions handle NaN differently
   - Results can be misleading
   
4. Assuming missing = zero
   - Missing means "unknown", not "zero"
   - Different statistical implications
   
5. Dropping missing values without inspection
   - May lose important data
   - May introduce bias
   - Detection must come before decisions
""")
print()

# =============================================================================
# PRACTICAL WORKFLOW
# =============================================================================
print("=" * 80)
print("SECTION 9: Recommended Workflow for Missing Value Detection")
print("=" * 80)
print()

print("Step-by-Step Workflow:")
print("-" * 80)
print("""
1. Load your data
   df = pd.read_csv('your_data.csv')

2. Quick overview
   print(df.head())
   print(df.info())

3. Check for missing values
   print(df.isnull().sum())

4. Create detailed summary
   summary = missing_values_summary(df)
   print(summary)

5. Inspect problematic columns
   cols_with_missing = summary[summary['Missing_Count'] > 0]['Column']
   print(df[cols_with_missing].head(20))

6. Look at rows with missing data
   df_missing = df[df.isnull().any(axis=1)]
   print(df_missing)

7. Document findings
   - Which columns have missing data?
   - How much is missing?
   - Are there patterns?

8. Make informed decisions
   - Fill missing values?
   - Drop rows/columns?
   - Keep as-is?
   - Use different analysis method?
""")
print()

# =============================================================================
# SUMMARY AND KEY TAKEAWAYS
# =============================================================================
print("=" * 80)
print("SUMMARY AND KEY TAKEAWAYS")
print("=" * 80)
print()

print("Essential Methods:")
print("-" * 80)
print("• isnull() / isna()    - Detect missing values (returns True for NaN)")
print("• notnull() / notna()  - Detect non-missing values")
print("• sum()                - Count missing values")
print("• any()                - Check if any value is missing")
print("• all()                - Check if all values are missing")
print("• count()              - Count non-missing values")
print()

print("Critical Understanding:")
print("-" * 80)
print("✓ Missing values are ALWAYS present in real-world data")
print("✓ Detection is the FIRST step before any cleaning or analysis")
print("✓ Understanding WHERE and HOW MUCH prevents bad decisions")
print("✓ Never assume data is complete")
print("✓ Document your findings before acting")
print()

print("What's Next:")
print("-" * 80)
print("After detection, you'll learn:")
print("• Handling missing values (dropping, filling, imputation)")
print("• Analyzing patterns of missingness")
print("• Making data-driven decisions about missing data")
print("• Advanced missing value techniques")
print()

print("=" * 80)
print("✓ MISSING VALUES DETECTION MILESTONE COMPLETE")
print("=" * 80)
print()

print("You now understand:")
print("• What missing values represent")
print("• How to detect missing values in DataFrames")
print("• How to count and summarize missing data")
print("• How to identify affected rows and columns")
print("• Why detection matters for data quality")
print()

print("Ready to record your 2-minute video walkthrough!")
print("See VIDEO_WALKTHROUGH_MISSING_VALUES_DETECTION.md for guidelines.")
print()
