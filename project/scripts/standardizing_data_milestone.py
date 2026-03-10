"""
Standardizing Column Names and Data Formats Milestone - Pandas Fundamentals
============================================================================

This script demonstrates the fundamentals of standardizing column names and data formats using:
- String manipulation methods for column names
- str.lower(), str.upper(), str.strip() for text standardization
- replace() for consistent formatting
- to_numeric() and to_datetime() for data type standardization

Inconsistent naming and formatting make datasets harder to understand, combine, and analyze.
Standardization is a critical step in preparing clean, reliable, and analysis-ready data.

Author: Your Name
Date: March 10, 2026
"""

import pandas as pd
import numpy as np
import re

print("=" * 80)
print("STANDARDIZING COLUMN NAMES AND DATA FORMATS MILESTONE")
print("=" * 80)
print()

# =============================================================================
# INTRODUCTION
# =============================================================================
print("INTRODUCTION: Why Standardization Matters")
print("-" * 80)
print("""
Inconsistent column names and data formats are common issues in real-world datasets.

Problems caused by inconsistency:
- Column names with spaces require bracket notation
- Mixed casing makes column access error-prone
- Special characters cause parsing issues
- Inconsistent data formats lead to comparison errors
- Merging datasets becomes difficult

Before analyzing data, you must:
- CLEAN column names to a consistent format
- NORMALIZE text data (case, whitespace, categories)
- STANDARDIZE data types (numeric, dates, text)
- VERIFY consistency across the dataset

The key concepts for standardization are:
1. Column Name Cleaning - lowercase, underscores, no special chars
2. Naming Conventions - snake_case, descriptive, consistent
3. Text Standardization - case, whitespace, categorical values
4. Data Type Standardization - ensure correct types

Think of standardization as setting rules for your data to follow.
It ensures:
- Column access is simple and predictable
- Code is cleaner and less error-prone
- Datasets are easier to merge and reuse
- Analysis workflows scale better
""")
print()

# =============================================================================
# UNDERSTANDING THE PROBLEM
# =============================================================================
print("=" * 80)
print("SECTION 1: Understanding Inconsistent Data")
print("=" * 80)
print()

print("1.1 Common Column Name Issues")
print("-" * 80)
print("""
Real-world datasets often have messy column names:

Common problems:
- Mixed casing: "Customer Name", "customer_ID", "PRODUCT_code"
- Spaces: "Order Date", "Total Amount", "Shipping Address"
- Special characters: "Price($)", "Discount%", "Email@domain"
- Inconsistent separators: "first-name", "last_name", "middleName"
- Leading/trailing spaces: " City ", "Country  "
- Numbers and abbreviations: "Column1", "Col2", "qty", "amt"

Why this matters:
- df.Customer Name  # ❌ Syntax error
- df['Customer Name']  # ✓ Works, but inconvenient
- df.customer_name  # ✓✓ Clean and Pythonic
""")
print()

print("1.2 Creating Sample Data with Inconsistent Names and Formats")
print("-" * 80)
print("Creating a dataset with common real-world issues:")
print()

# Create messy dataset that mimics real-world data
messy_data = {
    'Customer Name': ['Alice Smith', 'bob jones', 'CHARLIE BROWN', ' David Lee ', 'eve WILSON'],
    'Email Address': ['ALICE@EMAIL.COM', 'bob@email.com', 'Charlie@Email.com', 'david@email.com  ', '  eve@email.com'],
    'Product Code': ['PRD-001', 'prd-002', 'PRD-003', 'Prd-004', 'prd-005'],
    'Order Date': ['2026-01-15', '01/16/2026', '2026-01-17', '01-18-2026', '2026/01/19'],
    'Total Amount': ['$100.00', '150', '$200.50', '175.00', '$225'],
    'Quantity Ordered': ['5', '10', '3', '7', '12'],
    'Shipping City': ['New York', 'new york', 'NEW YORK', 'Los Angeles', 'los angeles'],
    'Status': ['Completed', 'COMPLETED', 'completed', 'Pending', 'pending'],
    ' Price($) ': [20.00, 30.00, 66.83, 25.00, 18.75],  # Leading/trailing spaces and special chars
    'Discount%': [10, 5, 15, 0, 20]
}

df_messy = pd.DataFrame(messy_data)

print("Original messy DataFrame:")
print(df_messy)
print()

print("Column names:")
print(df_messy.columns.tolist())
print()

print("Issues identified:")
print("- Column names have spaces: 'Customer Name', 'Email Address'")
print("- Column names have special characters: ' Price($) ', 'Discount%'")
print("- Column names have leading/trailing spaces: ' Price($) '")
print("- Mixed casing in column names")
print("- Text data has inconsistent casing: 'ALICE@EMAIL.COM' vs 'bob@email.com'")
print("- Text data has extra whitespace: ' David Lee ', 'david@email.com  '")
print("- City names are inconsistent: 'New York', 'new york', 'NEW YORK'")
print("- Status values are inconsistent: 'Completed', 'COMPLETED', 'completed'")
print("- Amount column has mixed formats: '$100.00', '150', '$200.50'")
print("- Date formats are inconsistent: '2026-01-15', '01/16/2026', '2026/01/19'")
print()

# =============================================================================
# STANDARDIZING COLUMN NAMES
# =============================================================================
print("=" * 80)
print("SECTION 2: Standardizing Column Names")
print("=" * 80)
print()

print("2.1 Converting Column Names to Lowercase")
print("-" * 80)
print("""
First step: Convert all column names to lowercase.

Benefits:
- Eliminates case sensitivity issues
- Makes column access predictable
- Reduces naming conflicts

Method: Use str.lower() on column names
Syntax: df.columns = df.columns.str.lower()
""")
print()

# Make a copy to work with
df_clean = df_messy.copy()

print("Original column names:")
print(df_clean.columns.tolist())
print()

# Convert to lowercase
df_clean.columns = df_clean.columns.str.lower()

print("After converting to lowercase:")
print(df_clean.columns.tolist())
print()

print("2.2 Replacing Spaces with Underscores")
print("-" * 80)
print("""
Second step: Replace spaces with underscores.

Benefits:
- Enables dot notation access: df.customer_name instead of df['customer name']
- Follows Python naming conventions
- Makes code cleaner and more readable

Method: Use str.replace() on column names
Syntax: df.columns = df.columns.str.replace(' ', '_')
""")
print()

# Replace spaces with underscores
df_clean.columns = df_clean.columns.str.replace(' ', '_')

print("After replacing spaces with underscores:")
print(df_clean.columns.tolist())
print()

print("2.3 Removing Special Characters")
print("-" * 80)
print("""
Third step: Remove or replace special characters.

Common special characters to remove: $ % @ # ( ) - (at start/end)

Method: Use str.replace() with regex or strip()
Syntax: df.columns = df.columns.str.replace('[^a-zA-Z0-9_]', '', regex=True)
""")
print()

# Remove special characters (keep only letters, numbers, underscores)
df_clean.columns = df_clean.columns.str.replace('[^a-z0-9_]', '', regex=True)

print("After removing special characters:")
print(df_clean.columns.tolist())
print()

print("2.4 Removing Leading/Trailing Underscores")
print("-" * 80)
print("""
Fourth step: Clean up leading/trailing underscores created during cleaning.

Method: Use str.strip() on column names
Syntax: df.columns = df.columns.str.strip('_')
""")
print()

# Remove leading/trailing underscores
df_clean.columns = df_clean.columns.str.strip('_')

print("After removing leading/trailing underscores:")
print(df_clean.columns.tolist())
print()

print("2.5 Complete Column Name Standardization Function")
print("-" * 80)
print("""
Best practice: Create a reusable function for column standardization.
""")
print()

def standardize_column_names(df):
    """
    Standardize DataFrame column names to snake_case format.
    
    Transformations applied:
    1. Convert to lowercase
    2. Strip leading/trailing whitespace
    3. Replace spaces with underscores
    4. Remove special characters (keep letters, numbers, underscores)
    5. Replace multiple underscores with single underscore
    6. Remove leading/trailing underscores
    
    Parameters:
    df (DataFrame): DataFrame with columns to standardize
    
    Returns:
    DataFrame: DataFrame with standardized column names
    """
    df = df.copy()
    
    # Convert to lowercase
    df.columns = df.columns.str.lower()
    
    # Strip whitespace
    df.columns = df.columns.str.strip()
    
    # Replace spaces with underscores
    df.columns = df.columns.str.replace(' ', '_')
    
    # Remove special characters (keep alphanumeric and underscores)
    df.columns = df.columns.str.replace('[^a-z0-9_]', '', regex=True)
    
    # Replace multiple underscores with single underscore
    df.columns = df.columns.str.replace('_+', '_', regex=True)
    
    # Remove leading/trailing underscores
    df.columns = df.columns.str.strip('_')
    
    return df

print("Function to standardize column names:")
print()
print("""
def standardize_column_names(df):
    df = df.copy()
    df.columns = df.columns.str.lower()
    df.columns = df.columns.str.strip()
    df.columns = df.columns.str.replace(' ', '_')
    df.columns = df.columns.str.replace('[^a-z0-9_]', '', regex=True)
    df.columns = df.columns.str.replace('_+', '_', regex=True)
    df.columns = df.columns.str.strip('_')
    return df
""")
print()

# Apply the function to original messy data
df_standardized = standardize_column_names(df_messy)

print("Before standardization:")
print(df_messy.columns.tolist())
print()

print("After standardization:")
print(df_standardized.columns.tolist())
print()

print("Comparison:")
for old, new in zip(df_messy.columns, df_standardized.columns):
    print(f"  '{old}' → '{new}'")
print()

# =============================================================================
# CHOOSING NAMING CONVENTIONS
# =============================================================================
print("=" * 80)
print("SECTION 3: Choosing Naming Conventions")
print("=" * 80)
print()

print("3.1 Common Naming Conventions")
print("-" * 80)
print("""
Choose a consistent style and stick with it.

Common conventions:

1. snake_case (Recommended for Python/Pandas)
   - All lowercase
   - Words separated by underscores
   - Examples: customer_name, order_date, total_amount

2. camelCase
   - First word lowercase, subsequent words capitalized
   - Examples: customerName, orderDate, totalAmount

3. PascalCase
   - All words capitalized
   - Examples: CustomerName, OrderDate, TotalAmount

4. kebab-case
   - All lowercase, words separated by hyphens
   - Examples: customer-name, order-date (avoid in Pandas)

For Pandas DataFrames: Use snake_case
- Follows Python conventions (PEP 8)
- Enables dot notation access
- Most compatible with data science tools
""")
print()

print("3.2 Best Practices for Column Names")
print("-" * 80)
print("""
Guidelines for good column names:

✓ DO:
1. Use snake_case consistently
2. Keep names descriptive but concise
3. Use full words, avoid unclear abbreviations
4. Use consistent terminology across datasets
5. Start with a letter (not a number)
6. Use singular nouns for entity attributes

✗ DON'T:
1. Mix naming conventions (customer_name vs orderDate)
2. Use spaces or special characters
3. Use reserved Python keywords (class, type, list)
4. Make names too long (max 20-25 characters)
5. Use ambiguous abbreviations (amt, qty, num)
6. Mix singular and plural inconsistently

Examples:

❌ Bad names:
'Cust Name', 'ord-date', 'TotalAmt', 'qty', 'Column1', 'email address '

✓ Good names:
'customer_name', 'order_date', 'total_amount', 'quantity', 'order_id', 'email_address'
""")
print()

print("3.3 Improving Column Names - Examples")
print("-" * 80)

# Create examples of name improvements
name_improvements = {
    'Original Name': [
        'Cust ID', 'CustName', 'e-mail', 'phone#', 'DOB',
        'Qty', 'amt', 'prc', 'Order Date', 'Status Code'
    ],
    'Improved Name': [
        'customer_id', 'customer_name', 'email', 'phone_number', 'date_of_birth',
        'quantity', 'amount', 'price', 'order_date', 'status_code'
    ],
    'Reason': [
        'Remove abbreviation, use underscore',
        'Convert to snake_case',
        'Remove hyphen, use standard name',
        'Remove special character, be descriptive',
        'Use full words, snake_case',
        'Use full word "quantity"',
        'Use full word "amount"',
        'Use full word "price"',
        'Use snake_case',
        'Use snake_case'
    ]
}

df_improvements = pd.DataFrame(name_improvements)
print("Column name improvement examples:")
print(df_improvements.to_string(index=False))
print()

# =============================================================================
# STANDARDIZING TEXT DATA
# =============================================================================
print("=" * 80)
print("SECTION 4: Standardizing Text Data")
print("=" * 80)
print()

print("4.1 Converting Text to Consistent Case")
print("-" * 80)
print("""
Text data should have consistent casing within each column.

Common approaches:
- Lowercase for emails, usernames, codes
- Uppercase for country codes, abbreviations
- Title Case for names, cities
- Original case for proper nouns (when appropriate)

Method: Use .str.lower(), .str.upper(), or .str.title()
Syntax: df['column'] = df['column'].str.lower()
""")
print()

# Work with standardized column names
df_format = df_standardized.copy()

print("Original email addresses (inconsistent case):")
print(df_format['email_address'])
print()

# Standardize email to lowercase
df_format['email_address'] = df_format['email_address'].str.lower()

print("After converting to lowercase:")
print(df_format['email_address'])
print()

print("Original product codes (inconsistent case):")
print(df_format['product_code'])
print()

# Standardize product codes to uppercase
df_format['product_code'] = df_format['product_code'].str.upper()

print("After converting to uppercase:")
print(df_format['product_code'])
print()

print("Original customer names (inconsistent case):")
print(df_format['customer_name'])
print()

# Standardize names to title case
df_format['customer_name'] = df_format['customer_name'].str.title()

print("After converting to title case:")
print(df_format['customer_name'])
print()

print("4.2 Removing Extra Whitespace")
print("-" * 80)
print("""
Extra whitespace can cause comparison and matching issues.

Types of whitespace to remove:
- Leading spaces: "  text"
- Trailing spaces: "text  "
- Multiple internal spaces: "text    text"

Method: Use .str.strip() and .str.replace()
Syntax: 
  df['column'] = df['column'].str.strip()  # Remove leading/trailing
  df['column'] = df['column'].str.replace('\\s+', ' ', regex=True)  # Normalize internal
""")
print()

print("Before stripping whitespace:")
print(repr(df_format['customer_name'].iloc[3]))  # Show with quotes
print(repr(df_format['email_address'].iloc[3]))
print()

# Strip leading and trailing whitespace from all text columns
text_columns = ['customer_name', 'email_address', 'shipping_city', 'status']
for col in text_columns:
    df_format[col] = df_format[col].str.strip()

print("After stripping whitespace:")
print(repr(df_format['customer_name'].iloc[3]))
print(repr(df_format['email_address'].iloc[3]))
print()

print("4.3 Standardizing Categorical Values")
print("-" * 80)
print("""
Categorical columns should have consistent values.

Common issues:
- Mixed case: "Completed", "completed", "COMPLETED"
- Variations: "NY", "New York", "new york"
- Misspellings: "Californa" vs "California"

Solution:
1. Convert to consistent case
2. Use replace() for variations
3. Create a mapping dictionary for complex cases
""")
print()

print("Original status values (inconsistent):")
print(df_format['status'].value_counts())
print()

# Standardize status values
df_format['status'] = df_format['status'].str.lower()
df_format['status'] = df_format['status'].str.strip()

print("After standardization (lowercase, stripped):")
print(df_format['status'].value_counts())
print()

print("Original city values (inconsistent):")
print(df_format['shipping_city'].value_counts())
print()

# Standardize city values (title case for consistency)
df_format['shipping_city'] = df_format['shipping_city'].str.title()
df_format['shipping_city'] = df_format['shipping_city'].str.strip()

print("After standardization (title case, stripped):")
print(df_format['shipping_city'].value_counts())
print()

# =============================================================================
# STANDARDIZING NUMERIC AND DATE FORMATS
# =============================================================================
print("=" * 80)
print("SECTION 5: Standardizing Numeric and Date Formats")
print("=" * 80)
print()

print("5.1 Understanding Data Types")
print("-" * 80)
print("""
Check current data types before standardization.

Method: Use .dtypes or .info()
""")
print()

print("Current data types:")
print(df_format.dtypes)
print()

print("5.2 Standardizing Numeric Columns")
print("-" * 80)
print("""
Numeric columns should have numeric data types for calculations.

Common issues:
- Currency symbols: "$100.00"
- Commas in large numbers: "1,000,000"
- Percentage signs: "15%"
- Text in numeric columns: "N/A", "Unknown"

Solution:
1. Remove non-numeric characters
2. Convert to numeric using pd.to_numeric()
3. Handle errors appropriately
""")
print()

print("Original 'total_amount' column (mixed formats):")
print(df_format['total_amount'])
print(f"Data type: {df_format['total_amount'].dtype}")
print()

# Clean and convert total_amount to numeric
# Remove $ signs and convert to float
df_format['total_amount_clean'] = df_format['total_amount'].astype(str).str.replace('$', '', regex=False)
df_format['total_amount_clean'] = pd.to_numeric(df_format['total_amount_clean'], errors='coerce')

print("After cleaning and converting to numeric:")
print(df_format['total_amount_clean'])
print(f"Data type: {df_format['total_amount_clean'].dtype}")
print()

print("Original 'quantity_ordered' column:")
print(df_format['quantity_ordered'])
print(f"Data type: {df_format['quantity_ordered'].dtype}")
print()

# Convert quantity to integer
df_format['quantity_ordered'] = pd.to_numeric(df_format['quantity_ordered'], errors='coerce')
df_format['quantity_ordered'] = df_format['quantity_ordered'].astype('Int64')  # Nullable integer

print("After converting to integer:")
print(df_format['quantity_ordered'])
print(f"Data type: {df_format['quantity_ordered'].dtype}")
print()

print("5.3 Understanding Date Format Issues")
print("-" * 80)
print("""
Date columns should be in a consistent format for time-based operations.

Common issues:
- Mixed formats: "2026-01-15", "01/16/2026", "2026/01/19"
- Text dates: "January 15, 2026"
- Different separators: "-", "/", "."
- Ambiguous formats: "01-02-2026" (MM-DD-YYYY or DD-MM-YYYY?)

Solution:
1. Identify the format variations
2. Use pd.to_datetime() with appropriate format specifier
3. Or use pd.to_datetime() with infer_datetime_format=True
4. Handle errors with errors='coerce'

Note: Full datetime conversion is covered in detail in dedicated lessons.
For this milestone, we focus on recognizing and understanding the issues.
""")
print()

print("Original 'order_date' column (mixed formats):")
print(df_format['order_date'])
print(f"Data type: {df_format['order_date'].dtype}")
print()

print("These dates have different formats:")
print("- '2026-01-15' - ISO format (YYYY-MM-DD)")
print("- '01/16/2026' - US format (MM/DD/YYYY)")
print("- '2026-01-17' - ISO format (YYYY-MM-DD)")
print("- '01-18-2026' - US format with dashes (MM-DD-YYYY)")
print("- '2026/01/19' - ISO-like with slashes (YYYY/MM/DD)")
print()

print("Converting to datetime (Pandas will infer format):")
df_format['order_date_clean'] = pd.to_datetime(df_format['order_date'], errors='coerce')

print(df_format['order_date_clean'])
print(f"Data type: {df_format['order_date_clean'].dtype}")
print()

print("Now dates are standardized and can be used for date operations.")
print()

# =============================================================================
# COMPLETE STANDARDIZATION WORKFLOW
# =============================================================================
print("=" * 80)
print("SECTION 6: Complete Standardization Workflow")
print("=" * 80)
print()

print("6.1 Before and After Comparison")
print("-" * 80)

print("BEFORE - Original messy dataset:")
print(df_messy.head())
print()
print("Column names:")
print(df_messy.columns.tolist())
print()
print("Data types:")
print(df_messy.dtypes)
print()

print("AFTER - Standardized dataset:")
# Create final clean version
df_final = df_format[['customer_name', 'email_address', 'product_code', 'order_date_clean', 
                       'total_amount_clean', 'quantity_ordered', 'shipping_city', 'status', 
                       'price', 'discount']].copy()

# Rename cleaned columns
df_final = df_final.rename(columns={
    'order_date_clean': 'order_date',
    'total_amount_clean': 'total_amount'
})

print(df_final.head())
print()
print("Column names:")
print(df_final.columns.tolist())
print()
print("Data types:")
print(df_final.dtypes)
print()

print("6.2 Verification Checklist")
print("-" * 80)
print("""
After standardization, verify:

✓ Column Names:
  - All lowercase
  - Spaces replaced with underscores
  - No special characters
  - Consistent naming convention
  - No leading/trailing underscores

✓ Text Data:
  - Consistent case within each column
  - No leading/trailing whitespace
  - Categorical values are uniform
  - No unexpected variations

✓ Numeric Data:
  - Correct data types (int, float)
  - No text in numeric columns
  - No currency symbols or formatting

✓ Date Data:
  - Converted to datetime type
  - Consistent format
  - Valid dates (no parsing errors)
""")
print()

# Perform verification
print("Verification Results:")
print()

print("1. Column Names Check:")
all_lowercase = all(col.islower() for col in df_final.columns)
no_spaces = all(' ' not in col for col in df_final.columns)
no_special = all(col.replace('_', '').isalnum() for col in df_final.columns)

print(f"   All lowercase: {all_lowercase}")
print(f"   No spaces: {no_spaces}")
print(f"   No special characters: {no_special}")
print()

print("2. Text Data Check:")
for col in ['customer_name', 'email_address', 'product_code', 'shipping_city', 'status']:
    has_leading_trailing_space = df_final[col].str.strip().equals(df_final[col])
    print(f"   {col} - No leading/trailing spaces: {has_leading_trailing_space}")
print()

print("3. Numeric Data Check:")
numeric_cols = ['total_amount', 'quantity_ordered', 'price', 'discount']
for col in numeric_cols:
    is_numeric = pd.api.types.is_numeric_dtype(df_final[col])
    print(f"   {col} - Is numeric: {is_numeric}")
print()

print("4. Date Data Check:")
is_datetime = pd.api.types.is_datetime64_any_dtype(df_final['order_date'])
print(f"   order_date - Is datetime: {is_datetime}")
print()

# =============================================================================
# PRACTICAL EXAMPLES
# =============================================================================
print("=" * 80)
print("SECTION 7: Practical Examples")
print("=" * 80)
print()

print("7.1 Standardizing a Real-World CSV")
print("-" * 80)
print("""
Common workflow when loading external data:

1. Load data
2. Inspect column names and data types
3. Standardize column names
4. Standardize text data
5. Convert data types
6. Verify results
7. Save cleaned data
""")
print()

# Create example function for complete workflow
def clean_dataframe(df):
    """
    Apply complete standardization to a DataFrame.
    
    Steps:
    1. Standardize column names
    2. Strip whitespace from text columns
    3. Standardize text case in appropriate columns
    4. Identify and report data type issues
    
    Parameters:
    df (DataFrame): Input DataFrame
    
    Returns:
    DataFrame: Cleaned DataFrame
    """
    df = df.copy()
    
    # 1. Standardize column names
    df = standardize_column_names(df)
    
    # 2. Strip whitespace from all object columns
    text_columns = df.select_dtypes(include=['object']).columns
    for col in text_columns:
        if df[col].dtype == 'object':
            df[col] = df[col].astype(str).str.strip()
    
    # 3. Report on data types
    print(f"Cleaned DataFrame shape: {df.shape}")
    print(f"Column names: {df.columns.tolist()}")
    print(f"Data types:\n{df.dtypes}")
    
    return df

print("Example: Applying complete cleaning workflow")
print()

# Apply to original messy data
df_cleaned = clean_dataframe(df_messy)
print()

print("Cleaned DataFrame preview:")
print(df_cleaned.head())
print()

# =============================================================================
# BEST PRACTICES AND COMMON PITFALLS
# =============================================================================
print("=" * 80)
print("SECTION 8: Best Practices and Common Pitfalls")
print("=" * 80)
print()

print("8.1 Best Practices")
print("-" * 80)
print("""
✓ DO:
1. Standardize column names FIRST, before any analysis
2. Use a consistent naming convention throughout
3. Create reusable functions for repetitive cleaning
4. Document your cleaning decisions
5. Keep a copy of the original data
6. Verify results after each transformation
7. Consider creating a data dictionary
8. Test your cleaning process on sample data first

Column naming:
✓ Use snake_case for Python/Pandas
✓ Be descriptive but concise (15-25 chars max)
✓ Avoid abbreviations unless universally understood
✓ Use consistent terminology across similar datasets

Text standardization:
✓ Choose case based on data type (emails → lowercase, names → title case)
✓ Strip whitespace before and after other transformations
✓ Standardize categorical values to reduce cardinality
✓ Document how you handle special cases

Data type conversion:
✓ Convert numeric columns to numeric types
✓ Convert date columns to datetime types
✓ Handle errors gracefully (errors='coerce')
✓ Validate data after conversion
""")
print()

print("8.2 Common Pitfalls")
print("-" * 80)
print("""
✗ DON'T:
1. Mix naming conventions in the same dataset
2. Leave spaces or special characters in column names
3. Forget to strip whitespace (causes silent matching failures)
4. Convert data types without handling errors
5. Standardize without understanding the data context
6. Lose information during cleaning (document changes)
7. Assume all text should be lowercase (names, proper nouns)
8. Skip verification after cleaning

Common mistakes:

Mistake 1: Inconsistent column standardization
❌ df.columns = df.columns.str.lower()  # Only lowercase, spaces remain
✓ df = standardize_column_names(df)  # Complete standardization

Mistake 2: Not stripping whitespace
❌ df['city'] = df['city'].str.lower()  # "New York" != "New York " (trailing space)
✓ df['city'] = df['city'].str.strip().str.lower()  # Correct order

Mistake 3: Losing data during conversion
❌ df['price'] = df['price'].str.replace('$', '').astype(float)  # Crashes on missing
✓ df['price'] = pd.to_numeric(df['price'].str.replace('$', ''), errors='coerce')

Mistake 4: Wrong case for data type
❌ df['name'] = df['name'].str.lower()  # "john smith" looks unprofessional
✓ df['name'] = df['name'].str.title()  # "John Smith" is more appropriate

Mistake 5: Abbreviating column names too much
❌ 'cust_nm', 'ord_dt', 'qty', 'amt'  # Hard to understand
✓ 'customer_name', 'order_date', 'quantity', 'amount'  # Clear and readable
""")
print()

print("8.3 When to Apply Different Standardizations")
print("-" * 80)
print("""
Choose standardization based on data type and usage:

Emails, URLs, usernames:
→ Lowercase (case-insensitive matching)

Names, cities, countries:
→ Title Case (readable, professional)

Product codes, ticket IDs:
→ Uppercase (standard convention)

Categories/status values:
→ Lowercase (easier filtering, grouping)

Free text/comments:
→ Keep original (preserve user intent)

Column names:
→ Always snake_case (Python convention)
""")
print()

# =============================================================================
# SUMMARY
# =============================================================================
print("=" * 80)
print("MILESTONE COMPLETE: KEY TAKEAWAYS")
print("=" * 80)
print()

print("What You Learned:")
print("-" * 80)
print("""
1. STANDARDIZING COLUMN NAMES
   - Convert to lowercase
   - Replace spaces with underscores
   - Remove special characters
   - Apply consistent snake_case convention
   - Create reusable standardization functions

2. CHOOSING NAMING CONVENTIONS
   - Use snake_case for Python/Pandas
   - Keep names descriptive but concise
   - Avoid unclear abbreviations
   - Apply consistent rules across all columns

3. STANDARDIZING TEXT DATA
   - Convert text to consistent case (lower, upper, title)
   - Strip leading/trailing whitespace
   - Normalize categorical values
   - Ensure consistency within columns

4. STANDARDIZING NUMERIC AND DATE FORMATS
   - Identify data type issues
   - Remove currency symbols and formatting
   - Convert to appropriate numeric types
   - Understand date format inconsistencies
   - Use pd.to_numeric() and pd.to_datetime()

5. VERIFICATION AND BEST PRACTICES
   - Always verify after transformation
   - Document cleaning decisions
   - Keep original data backup
   - Use reusable functions
   - Test on sample data first
""")
print()

print("Key Methods Summary:")
print("-" * 80)
print("""
Column name standardization:
  df.columns.str.lower()              - Convert columns to lowercase
  df.columns.str.replace(' ', '_')    - Replace spaces with underscores
  df.columns.str.replace('[^a-z0-9_]', '', regex=True)  - Remove special chars
  df.columns.str.strip('_')           - Remove leading/trailing underscores

Text standardization:
  df['col'].str.lower()               - Convert text to lowercase
  df['col'].str.upper()               - Convert text to uppercase
  df['col'].str.title()               - Convert text to title case
  df['col'].str.strip()               - Remove leading/trailing whitespace
  df['col'].str.replace('\\s+', ' ')  - Normalize internal whitespace

Data type conversion:
  pd.to_numeric(df['col'], errors='coerce')      - Convert to numeric
  pd.to_datetime(df['col'], errors='coerce')     - Convert to datetime
  df['col'].astype('type')                       - Convert to specific type
""")
print()

print("=" * 80)
print("Next Steps:")
print("-" * 80)
print("""
Now that you can standardize column names and data formats:

1. Practice on messy real-world datasets
2. Create your own cleaning functions library
3. Learn about advanced text cleaning (regex)
4. Explore data validation techniques
5. Study datetime manipulation in depth
6. Build automated data cleaning pipelines

Remember: Clean, standardized data is the foundation of good analysis!
""")
print("=" * 80)
print("END OF MILESTONE")
print("=" * 80)
