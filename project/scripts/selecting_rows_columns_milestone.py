"""
Selecting Rows and Columns Milestone - Pandas DataFrame Indexing
==================================================================

This script demonstrates selecting rows and columns in Pandas DataFrames using:
- Column selection by name
- Row selection by position (iloc)
- Row selection by label (loc)
- Combined row and column selection
- Slicing techniques

Precise data selection is foundational for all data analysis tasks.

Author: Your Name
Date: March 9, 2026
"""

import pandas as pd
import numpy as np

print("=" * 80)
print("SELECTING ROWS AND COLUMNS MILESTONE - PANDAS INDEXING")
print("=" * 80)
print()

# =============================================================================
# INTRODUCTION
# =============================================================================
print("INTRODUCTION: Why Selection Matters")
print("-" * 80)
print("""
Selecting the right subset of data is critical for:
- Inspection and exploration
- Data cleaning and transformation
- Feature engineering
- Analysis of specific segments

Common beginner mistakes include:
- Confusing positional (.iloc) vs label-based (.loc) indexing
- Selecting wrong rows or columns accidentally
- Using chained indexing (can cause errors)
- Writing unclear selection logic

This milestone teaches PRECISE and INTENTIONAL data selection.
""")
print()

# =============================================================================
# CREATE SAMPLE DATAFRAME
# =============================================================================
print("STEP 1: Creating Sample DataFrame")
print("-" * 80)

# Create a sample dataset with multiple columns and meaningful indices
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Henry'],
    'Age': [25, 30, 35, 28, 32, 29, 27, 31],
    'Department': ['Sales', 'IT', 'HR', 'Sales', 'IT', 'HR', 'Sales', 'IT'],
    'Salary': [50000, 65000, 60000, 52000, 68000, 58000, 51000, 67000],
    'Experience': [2, 5, 8, 3, 6, 4, 2, 7],
    'City': ['New York', 'Boston', 'Chicago', 'New York', 'Boston', 'Chicago', 'New York', 'Boston']
}

df = pd.DataFrame(data)

print("Sample DataFrame created:")
print(df)
print()
print(f"Shape: {df.shape} (rows, columns)")
print()

# =============================================================================
# SECTION 1: SELECTING COLUMNS BY NAME
# =============================================================================
print("=" * 80)
print("SECTION 1: Selecting Columns by Name")
print("=" * 80)
print()

print("1.1 Selecting a Single Column")
print("-" * 80)
print("""
To select a single column, use bracket notation with the column name.
Returns a pandas Series (one-dimensional).

Syntax: df['column_name']
""")

# Select single column
name_column = df['Name']
print("Selected 'Name' column:")
print(name_column)
print(f"\nType: {type(name_column)}")
print()

print("1.2 Selecting Multiple Columns")
print("-" * 80)
print("""
To select multiple columns, use bracket notation with a LIST of column names.
Returns a pandas DataFrame (two-dimensional).

Syntax: df[['column1', 'column2', 'column3']]
Note the DOUBLE brackets: outer for indexing, inner for the list.
""")

# Select multiple columns
subset = df[['Name', 'Age', 'Department']]
print("Selected 'Name', 'Age', and 'Department' columns:")
print(subset)
print(f"\nType: {type(subset)}")
print()

print("1.3 Selecting Non-Adjacent Columns")
print("-" * 80)
print("You can select columns in any order:")
selected_cols = df[['Salary', 'Name', 'City']]
print(selected_cols)
print()

print("KEY TAKEAWAYS - Column Selection:")
print("- Single column: df['column'] → Returns Series")
print("- Multiple columns: df[['col1', 'col2']] → Returns DataFrame")
print("- Columns can be selected in any order")
print("- Column names are case-sensitive")
print()

# =============================================================================
# SECTION 2: SELECTING ROWS BY POSITION (iloc)
# =============================================================================
print("=" * 80)
print("SECTION 2: Selecting Rows by Position (iloc)")
print("=" * 80)
print()

print("""
iloc = integer location based indexing
Uses POSITIONAL indexing (0-based, like Python lists)

Syntax: df.iloc[row_position]
        df.iloc[start:stop]  # stop is EXCLUSIVE

Use iloc when:
- You want the first/last N rows
- You're working with positions, not labels
- You want basic slicing behavior
""")
print()

print("2.1 Selecting a Single Row by Position")
print("-" * 80)
first_row = df.iloc[0]
print("First row (position 0):")
print(first_row)
print(f"\nType: {type(first_row)}")
print()

third_row = df.iloc[2]
print("Third row (position 2):")
print(third_row)
print()

print("2.2 Selecting Multiple Rows by Position")
print("-" * 80)
print("First 3 rows (positions 0, 1, 2):")
first_three = df.iloc[0:3]  # Stop position 3 is EXCLUSIVE
print(first_three)
print()

print("Rows at positions 1, 3, 5:")
specific_rows = df.iloc[[1, 3, 5]]
print(specific_rows)
print()

print("2.3 Slicing Rows with iloc")
print("-" * 80)
print("Rows from position 2 to 5 (exclusive):")
middle_rows = df.iloc[2:5]
print(middle_rows)
print()

print("Last 3 rows using negative indexing:")
last_three = df.iloc[-3:]
print(last_three)
print()

print("Every other row:")
every_other = df.iloc[::2]
print(every_other)
print()

print("KEY TAKEAWAYS - iloc:")
print("- Uses integer positions (0-based)")
print("- Slicing stop position is EXCLUSIVE")
print("- Supports negative indexing")
print("- Syntax: df.iloc[rows]")
print()

# =============================================================================
# SECTION 3: SELECTING ROWS BY LABEL (loc)
# =============================================================================
print("=" * 80)
print("SECTION 3: Selecting Rows by Label (loc)")
print("=" * 80)
print()

print("""
loc = label-based indexing
Uses INDEX LABELS (not positions)

Syntax: df.loc[row_label]
        df.loc[start:stop]  # stop is INCLUSIVE

Use loc when:
- Your DataFrame has meaningful index labels
- You want to select by specific identifiers
- You need label-based slicing
""")
print()

# Create a DataFrame with custom index labels
print("3.1 Creating DataFrame with Custom Index Labels")
print("-" * 80)
df_labeled = df.copy()
df_labeled.index = ['EMP001', 'EMP002', 'EMP003', 'EMP004', 'EMP005', 'EMP006', 'EMP007', 'EMP008']
print("DataFrame with employee ID as index:")
print(df_labeled)
print()

print("3.2 Selecting a Single Row by Label")
print("-" * 80)
employee = df_labeled.loc['EMP003']
print("Employee EMP003:")
print(employee)
print()

print("3.3 Selecting Multiple Rows by Label")
print("-" * 80)
print("Employees EMP002, EMP004, EMP007:")
selected_employees = df_labeled.loc[['EMP002', 'EMP004', 'EMP007']]
print(selected_employees)
print()

print("3.4 Slicing Rows with loc")
print("-" * 80)
print("Slice from EMP003 to EMP006 (INCLUSIVE):")
employee_range = df_labeled.loc['EMP003':'EMP006']
print(employee_range)
print("\nNote: Unlike iloc, loc slicing is INCLUSIVE of the stop label.")
print()

print("KEY TAKEAWAYS - loc:")
print("- Uses index labels (not positions)")
print("- Slicing stop label is INCLUSIVE")
print("- Requires meaningful index labels")
print("- Syntax: df.loc[labels]")
print()

# =============================================================================
# SECTION 4: SELECTING ROWS AND COLUMNS TOGETHER
# =============================================================================
print("=" * 80)
print("SECTION 4: Selecting Rows and Columns Together")
print("=" * 80)
print()

print("""
Both iloc and loc can select rows AND columns simultaneously.

Syntax: df.iloc[rows, columns]
        df.loc[row_labels, column_labels]

This is the MOST POWERFUL selection technique.
""")
print()

print("4.1 Using iloc for Rows and Columns")
print("-" * 80)
print("First 3 rows, first 3 columns:")
subset_iloc = df.iloc[0:3, 0:3]
print(subset_iloc)
print()

print("Rows 1-4, columns 'Name' and 'Salary' (using column positions 0 and 3):")
subset_mixed = df.iloc[1:5, [0, 3]]
print(subset_mixed)
print()

print("4.2 Using loc for Rows and Columns")
print("-" * 80)
print("Select specific employees and specific columns:")
subset_loc = df_labeled.loc[['EMP001', 'EMP003', 'EMP005'], ['Name', 'Salary', 'City']]
print(subset_loc)
print()

print("Slice rows and select specific columns:")
subset_loc_slice = df_labeled.loc['EMP002':'EMP005', ['Name', 'Age', 'Department']]
print(subset_loc_slice)
print()

print("4.3 Selecting All Rows, Specific Columns with loc")
print("-" * 80)
print("All rows, only 'Name' and 'Salary' columns:")
all_rows_subset = df_labeled.loc[:, ['Name', 'Salary']]
print(all_rows_subset)
print()

print("4.4 Selecting Specific Rows, All Columns with loc")
print("-" * 80)
print("Employees EMP002 and EMP006, all columns:")
specific_rows_all_cols = df_labeled.loc[['EMP002', 'EMP006'], :]
print(specific_rows_all_cols)
print()

print("KEY TAKEAWAYS - Combined Selection:")
print("- Syntax: df.iloc[rows, columns] or df.loc[rows, columns]")
print("- Use : to select all rows or all columns")
print("- Can combine slicing and explicit lists")
print("- This is the preferred way for complex selections")
print()

# =============================================================================
# SECTION 5: PRACTICAL EXAMPLES AND BEST PRACTICES
# =============================================================================
print("=" * 80)
print("SECTION 5: Practical Examples and Best Practices")
print("=" * 80)
print()

print("5.1 Filtering with Boolean Indexing")
print("-" * 80)
print("Select rows where Age > 28:")
age_filter = df[df['Age'] > 28]
print(age_filter)
print()

print("Select rows where Department is 'IT' and salary > 60000:")
it_high_salary = df[(df['Department'] == 'IT') & (df['Salary'] > 60000)]
print(it_high_salary)
print()

print("5.2 Selecting Columns with Conditions")
print("-" * 80)
print("Names and salaries of employees in Sales:")
sales_subset = df.loc[df['Department'] == 'Sales', ['Name', 'Salary']]
print(sales_subset)
print()

print("5.3 Best Practices")
print("-" * 80)
print("""
DO:
✓ Use .iloc for positional indexing
✓ Use .loc for label-based indexing
✓ Be explicit: df.loc[rows, columns]
✓ Verify your selection immediately
✓ Use meaningful column names

DON'T:
✗ Chain indexing: df['col'][0] (can cause SettingWithCopyWarning)
✗ Mix iloc and loc concepts
✗ Assume default integer index is meaningful
✗ Select without verifying results
""")
print()

# =============================================================================
# SECTION 6: COMMON MISTAKES TO AVOID
# =============================================================================
print("=" * 80)
print("SECTION 6: Common Mistakes to Avoid")
print("=" * 80)
print()

print("Mistake 1: Confusing iloc and loc")
print("-" * 80)
print("df.iloc[0] gets the FIRST row (position)")
print("df.loc[0] gets the row with INDEX LABEL 0 (may not be the first row!)")
print()

print("Mistake 2: Forgetting iloc slicing is exclusive")
print("-" * 80)
print("df.iloc[0:3] gets rows at positions 0, 1, 2 (NOT 3)")
print("df.loc['A':'C'] gets rows labeled 'A', 'B', 'C' (INCLUDES 'C')")
print()

print("Mistake 3: Single vs Double Brackets")
print("-" * 80)
print("df['Name'] returns a Series")
print("df[['Name']] returns a DataFrame")
print()

# =============================================================================
# SUMMARY
# =============================================================================
print("=" * 80)
print("MILESTONE SUMMARY")
print("=" * 80)
print("""
You have learned:

1. Column Selection:
   - Single column: df['column'] → Series
   - Multiple columns: df[['col1', 'col2']] → DataFrame

2. Row Selection by Position (iloc):
   - Positional indexing (0-based)
   - Slicing is EXCLUSIVE: df.iloc[0:3]
   - Use for: first N rows, last N rows, positional access

3. Row Selection by Label (loc):
   - Label-based indexing
   - Slicing is INCLUSIVE: df.loc['A':'C']
   - Use for: meaningful index labels, specific identifiers

4. Combined Selection:
   - df.iloc[rows, columns] for positional
   - df.loc[row_labels, column_labels] for labels
   - Use : to select all rows or all columns

5. Best Practices:
   - Always verify your selection
   - Be explicit with .iloc or .loc
   - Avoid chained indexing
   - Use readable column names

Next Steps:
- Practice with real datasets
- Combine with boolean filtering
- Use selection in data cleaning workflows
- Record your video walkthrough demonstrating these concepts
""")
print()

print("=" * 80)
print("MILESTONE COMPLETE!")
print("=" * 80)
