"""
CSV Loading Milestone - Pandas Fundamentals
============================================

This script demonstrates the fundamentals of loading CSV files into Pandas DataFrames.
It covers:
1. Understanding CSV file structure
2. Loading CSV files correctly
3. Inspecting loaded data
4. Recognizing common loading issues

Author: Your Name
Date: March 6, 2026
"""

import pandas as pd
import os

print("=" * 80)
print("CSV LOADING MILESTONE - PANDAS FUNDAMENTALS")
print("=" * 80)
print()

# =============================================================================
# SECTION 1: Understanding CSV Files
# =============================================================================
print("SECTION 1: Understanding CSV Files")
print("-" * 80)
print("""
CSV stands for Comma-Separated Values. It's a simple file format used to store
tabular data (data arranged in rows and columns).

Structure:
- First row typically contains column headers
- Each subsequent row contains data values
- Values are separated by commas (or other delimiters)
- Similar to spreadsheet tables (like Excel)

Example CSV structure:
    id,name,age
    1,Alice,25
    2,Bob,30
    3,Charlie,35
""")
print()

# =============================================================================
# SECTION 2: Loading CSV Files into Pandas
# =============================================================================
print("SECTION 2: Loading CSV Files into Pandas")
print("-" * 80)

# Define file paths
# Always use relative paths from the script location or absolute paths
raw_data_path = '../data/raw/example_raw.csv'
processed_data_path = '../data/processed/example_processed.csv'

# Check if files exist before loading
print("Checking if CSV files exist...")
if os.path.exists(raw_data_path):
    print(f"✓ Found: {raw_data_path}")
else:
    print(f"✗ Not found: {raw_data_path}")

if os.path.exists(processed_data_path):
    print(f"✓ Found: {processed_data_path}")
else:
    print(f"✗ Not found: {processed_data_path}")
print()

# Load the raw CSV file
print("Loading raw CSV file...")
try:
    # pd.read_csv() is the primary method for loading CSV files
    # By default, it assumes the first row contains headers
    df_raw = pd.read_csv(raw_data_path)
    print("✓ Successfully loaded raw data")
except FileNotFoundError:
    print("✗ Error: File not found. Check the file path.")
    df_raw = None
except pd.errors.EmptyDataError:
    print("✗ Error: File is empty.")
    df_raw = None
except Exception as e:
    print(f"✗ Error: {e}")
    df_raw = None
print()

# Load the processed CSV file
print("Loading processed CSV file...")
try:
    df_processed = pd.read_csv(processed_data_path)
    print("✓ Successfully loaded processed data")
except Exception as e:
    print(f"✗ Error: {e}")
    df_processed = None
print()

# =============================================================================
# SECTION 3: Inspecting Loaded Data
# =============================================================================
print("SECTION 3: Inspecting Loaded Data")
print("-" * 80)
print("""
After loading data, ALWAYS inspect it to verify:
- Data loaded correctly
- Column names are as expected
- Row counts are reasonable
- Data types are appropriate
- No obvious formatting issues
""")
print()

if df_raw is not None:
    print("=" * 80)
    print("INSPECTING RAW DATA")
    print("=" * 80)
    
    # 1. Display first few rows
    print("\n1. First 5 rows (df.head()):")
    print(df_raw.head())
    print()
    
    # 2. Display last few rows
    print("2. Last 5 rows (df.tail()):")
    print(df_raw.tail())
    print()
    
    # 3. Show DataFrame shape (rows, columns)
    print(f"3. Shape (rows, columns): {df_raw.shape}")
    print(f"   - Number of rows: {df_raw.shape[0]}")
    print(f"   - Number of columns: {df_raw.shape[1]}")
    print()
    
    # 4. Display column names
    print("4. Column names:")
    print(f"   {list(df_raw.columns)}")
    print()
    
    # 5. Show data types
    print("5. Data types (df.dtypes):")
    print(df_raw.dtypes)
    print()
    
    # 6. Show DataFrame info (comprehensive overview)
    print("6. DataFrame info (df.info()):")
    df_raw.info()
    print()
    
    # 7. Show basic statistics
    print("7. Basic statistics (df.describe()):")
    print(df_raw.describe())
    print()

if df_processed is not None:
    print("=" * 80)
    print("INSPECTING PROCESSED DATA")
    print("=" * 80)
    
    print("\n1. First 5 rows:")
    print(df_processed.head())
    print()
    
    print(f"2. Shape: {df_processed.shape}")
    print()
    
    print("3. Column names:")
    print(f"   {list(df_processed.columns)}")
    print()
    
    print("4. Data types:")
    print(df_processed.dtypes)
    print()
    
    print("5. DataFrame info:")
    df_processed.info()
    print()

# =============================================================================
# SECTION 4: Recognizing Common Loading Issues
# =============================================================================
print("=" * 80)
print("SECTION 4: Recognizing Common Loading Issues")
print("-" * 80)
print("""
Common issues when loading CSV files:

1. INCORRECT FILE PATH
   - Symptom: FileNotFoundError
   - Solution: Verify the path, use absolute paths if needed

2. MISSING HEADERS
   - Symptom: First data row becomes column names
   - Solution: Use pd.read_csv(file, header=None) or specify header row

3. WRONG DELIMITER
   - Symptom: All data appears in one column
   - Solution: Use pd.read_csv(file, delimiter=';') or sep parameter

4. ENCODING ISSUES
   - Symptom: Special characters appear as gibberish
   - Solution: Use pd.read_csv(file, encoding='utf-8' or 'latin-1')

5. QUOTED VALUES WITH COMMAS
   - Symptom: Data splits incorrectly
   - Solution: Pandas usually handles this, but check quotechar parameter

6. EXTRA WHITESPACE
   - Symptom: Column names have spaces or data has leading/trailing spaces
   - Solution: Use skipinitialspace=True or df.columns.str.strip()

7. MIXED DATA TYPES
   - Symptom: Numbers stored as strings
   - Solution: Check dtypes and convert using astype() if needed

8. LARGE FILES
   - Symptom: Memory errors or slow loading
   - Solution: Use chunksize parameter or select specific columns

WHY INSPECTION MATTERS:
- Catches errors early before analysis
- Prevents incorrect conclusions
- Saves time debugging later
- Ensures data integrity
""")
print()

# =============================================================================
# SECTION 5: Best Practices Demonstration
# =============================================================================
print("=" * 80)
print("SECTION 5: Best Practices for CSV Loading")
print("-" * 80)
print()

# Example: Loading with specific parameters
print("Example: Loading CSV with custom parameters")
print("-" * 50)

# Load with specific columns only
if os.path.exists(raw_data_path):
    print("Loading only specific columns...")
    df_subset = pd.read_csv(raw_data_path, usecols=['id', 'value'])
    print("Loaded columns:", list(df_subset.columns))
    print(df_subset)
    print()

# Load with data type specification
if os.path.exists(raw_data_path):
    print("Loading with specified data types...")
    df_typed = pd.read_csv(raw_data_path, dtype={'id': int, 'value': int})
    print("Data types:")
    print(df_typed.dtypes)
    print()

# Load first N rows only
if os.path.exists(raw_data_path):
    print("Loading first 2 rows only (nrows parameter)...")
    df_limited = pd.read_csv(raw_data_path, nrows=2)
    print(df_limited)
    print()

# =============================================================================
# VERIFICATION CHECKLIST
# =============================================================================
print("=" * 80)
print("VERIFICATION CHECKLIST - Always check these after loading:")
print("-" * 80)
print("""
☐ File loaded without errors
☐ Number of rows matches expectations
☐ Number of columns matches expectations
☐ Column names are correct (no typos, no extra spaces)
☐ Data types are appropriate (numbers as int/float, not strings)
☐ First few rows look reasonable
☐ Last few rows look reasonable
☐ No unexpected missing values
☐ Shape makes sense (df.shape)
☐ Info shows expected structure (df.info())
""")
print()

print("=" * 80)
print("CSV LOADING MILESTONE COMPLETED!")
print("=" * 80)
print("""
You have learned:
✓ What CSV files represent
✓ How to load CSV files into Pandas DataFrames
✓ How to inspect loaded data thoroughly
✓ Common issues to watch for
✓ Best practices for safe data loading

Next steps:
- Practice with different CSV files
- Try loading files with different delimiters
- Handle files with missing values
- Work with larger datasets
""")
