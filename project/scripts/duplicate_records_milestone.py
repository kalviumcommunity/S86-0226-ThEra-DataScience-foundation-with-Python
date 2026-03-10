"""
Identifying and Removing Duplicate Records Milestone - Pandas Fundamentals
===========================================================================

This script demonstrates the fundamentals of identifying and removing duplicate records using:
- duplicated() for detecting duplicate rows
- drop_duplicates() for removing duplicate rows
- Understanding subset and keep parameters
- Verifying deduplication results

Duplicate data is a common data quality issue that can skew analysis, inflate counts,
and lead to incorrect conclusions if not handled properly.

Author: Your Name
Date: March 10, 2026
"""

import pandas as pd
import numpy as np
import os

print("=" * 80)
print("IDENTIFYING AND REMOVING DUPLICATE RECORDS MILESTONE")
print("=" * 80)
print()

# =============================================================================
# INTRODUCTION
# =============================================================================
print("INTRODUCTION: Why Duplicate Detection and Removal Matters")
print("-" * 80)
print("""
Duplicate data is one of the most common data quality issues in real-world datasets.

Duplicates can cause:
- Inflated counts and misleading summaries
- Incorrect statistical measures
- Biased analysis results
- Wasted computational resources

Before analyzing data, you must:
- DETECT where duplicates exist
- UNDERSTAND why they exist
- REMOVE them intentionally and safely
- VERIFY the results after deduplication

The key methods for duplicate handling are:
1. duplicated() - Detect duplicate rows (returns boolean Series)
2. drop_duplicates() - Remove duplicate rows
3. subset - Specify which columns to consider
4. keep - Choose which duplicate to keep ('first', 'last', False)

Think of deduplication as removing noise so each row represents a unique observation.
It ensures:
- Each record represents unique information
- Aggregations and statistics are accurate
- Data integrity is preserved
- Downstream analysis is trustworthy
""")
print()

# =============================================================================
# UNDERSTANDING DUPLICATE RECORDS
# =============================================================================
print("=" * 80)
print("SECTION 1: Understanding Duplicate Records")
print("=" * 80)
print()

print("1.1 What Are Duplicate Records?")
print("-" * 80)
print("""
Duplicate records are rows that have identical values across:
- ALL columns (exact duplicates), OR
- SPECIFIC columns (partial duplicates)

Common causes of duplicates:
- Data entry errors (same person entered twice)
- System glitches (records saved multiple times)
- Data merging (combining datasets with overlapping records)
- Lack of unique identifiers
- Historical snapshots (same entity at different times)

Types of duplicates:
1. Exact duplicates - All column values are identical
2. Partial duplicates - Only some columns match (e.g., same name, different address)
3. Intentional duplicates - Valid repeated observations (e.g., multiple purchases by same customer)

Not all duplicates should be removed - understand context first!
""")
print()

print("1.2 Creating Sample Data with Duplicates")
print("-" * 80)
print("Creating a dataset with various duplicate scenarios:")
print()

# Create sample data with duplicates
np.random.seed(42)

sample_data = {
    'customer_id': [101, 102, 103, 101, 104, 105, 103, 106, 102, 107],
    'name': ['Alice', 'Bob', 'Charlie', 'Alice', 'David', 'Eve', 'Charlie', 'Frank', 'Bob', 'Grace'],
    'email': ['alice@email.com', 'bob@email.com', 'charlie@email.com', 'alice@email.com', 
              'david@email.com', 'eve@email.com', 'charlie@email.com', 'frank@email.com', 
              'bob@email.com', 'grace@email.com'],
    'purchase_amount': [100, 150, 200, 100, 175, 225, 200, 130, 150, 190],
    'purchase_date': ['2026-01-15', '2026-01-16', '2026-01-17', '2026-01-15', 
                      '2026-01-18', '2026-01-19', '2026-01-17', '2026-01-20',
                      '2026-01-16', '2026-01-21']
}

df = pd.DataFrame(sample_data)
print("Sample customer purchase dataset:")
print(df)
print()

print("Observations:")
print("- customer_id 101 appears twice (rows 0 and 3) - EXACT duplicate")
print("- customer_id 102 appears twice (rows 1 and 8) - EXACT duplicate")
print("- customer_id 103 appears twice (rows 2 and 6) - EXACT duplicate")
print("- These could be duplicate entries or legitimate multiple purchases")
print()

print(f"Dataset shape: {df.shape[0]} rows, {df.shape[1]} columns")
print()

# =============================================================================
# DETECTING DUPLICATE ROWS
# =============================================================================
print("=" * 80)
print("SECTION 2: Detecting Duplicate Rows")
print("=" * 80)
print()

print("2.1 Using duplicated() to Detect Duplicates")
print("-" * 80)
print("""
duplicated() returns a boolean Series:
- True where rows are duplicates
- False where rows are unique (or first occurrence)

By default:
- Considers ALL columns
- Marks subsequent duplicates as True (keeps 'first' occurrence)

Syntax: df.duplicated()
""")
print()

print("Boolean mask showing duplicate rows:")
duplicate_mask = df.duplicated()
print(duplicate_mask)
print()

print("Interpretation:")
print("- False (rows 0-2, 4-7, 9) = First occurrence or unique rows")
print("- True (rows 3, 8, 6) = Duplicate rows")
print()

print("2.2 Counting Duplicate Rows")
print("-" * 80)
print("How many duplicate rows exist?")
print()

num_duplicates = df.duplicated().sum()
print(f"Number of duplicate rows: {num_duplicates}")
print(f"Number of unique rows: {len(df) - num_duplicates}")
print(f"Percentage of duplicates: {(num_duplicates / len(df)) * 100:.1f}%")
print()

print("2.3 Viewing Duplicate Rows")
print("-" * 80)
print("Filtering to see only the duplicate rows:")
print()

duplicate_rows = df[df.duplicated()]
print("Duplicate rows (subsequent occurrences):")
print(duplicate_rows)
print()

print("To see ALL occurrences (including first):")
print("Use: df[df.duplicated(keep=False)]")
print()

all_duplicate_occurrences = df[df.duplicated(keep=False)]
print("All rows that have duplicates (including first occurrences):")
print(all_duplicate_occurrences)
print()

print("Key difference:")
print("- duplicated() marks only subsequent duplicates")
print("- duplicated(keep=False) marks ALL duplicate occurrences")
print()

# =============================================================================
# DETECTING DUPLICATES IN SPECIFIC COLUMNS
# =============================================================================
print("=" * 80)
print("SECTION 3: Detecting Duplicates in Specific Columns")
print("=" * 80)
print()

print("3.1 Duplicates Based on Subset of Columns")
print("-" * 80)
print("""
Often, you want to check duplicates based on specific columns only.
Use the 'subset' parameter to specify which columns to consider.

Syntax: df.duplicated(subset=['col1', 'col2'])
""")
print()

print("Example: Find duplicates based on customer_id only")
print()

duplicate_by_id = df.duplicated(subset=['customer_id'])
print("Duplicates based on customer_id:")
print(duplicate_by_id)
print()

num_id_duplicates = duplicate_by_id.sum()
print(f"Number of rows with duplicate customer_id: {num_id_duplicates}")
print()

print("View duplicate customer_ids:")
print(df[duplicate_by_id])
print()

print("3.2 Duplicates Based on Multiple Columns")
print("-" * 80)
print("Example: Find duplicates based on name AND email")
print()

duplicate_by_name_email = df.duplicated(subset=['name', 'email'])
print("Duplicates based on name + email:")
print(duplicate_by_name_email)
print()

print(f"Number of rows with duplicate name+email: {duplicate_by_name_email.sum()}")
print()

print("3.3 Understanding the 'keep' Parameter")
print("-" * 80)
print("""
The 'keep' parameter controls which occurrence is marked as duplicate:
- keep='first' (default) - Mark duplicates except first occurrence
- keep='last' - Mark duplicates except last occurrence
- keep=False - Mark ALL duplicates (including first)
""")
print()

print("Compare different 'keep' options:")
print()

print("keep='first' (default):")
print(df.duplicated(keep='first'))
print()

print("keep='last':")
print(df.duplicated(keep='last'))
print()

print("keep=False (all occurrences):")
print(df.duplicated(keep=False))
print()

# =============================================================================
# REMOVING DUPLICATE RECORDS
# =============================================================================
print("=" * 80)
print("SECTION 4: Removing Duplicate Records")
print("=" * 80)
print()

print("4.1 Using drop_duplicates() to Remove Duplicates")
print("-" * 80)
print("""
drop_duplicates() removes duplicate rows from DataFrame.

Key parameters:
- subset: Columns to consider for identifying duplicates
- keep: Which occurrence to keep ('first', 'last', False)
- inplace: Whether to modify original DataFrame (default False)

Syntax: df.drop_duplicates()
Returns: New DataFrame with duplicates removed
""")
print()

print("Original DataFrame:")
print(f"Shape: {df.shape}")
print(df)
print()

# Remove exact duplicates (all columns)
df_deduplicated = df.drop_duplicates()

print("After removing exact duplicates:")
print(f"Shape: {df_deduplicated.shape}")
print(df_deduplicated)
print()

print(f"Rows removed: {len(df) - len(df_deduplicated)}")
print()

print("4.2 Removing Duplicates Based on Specific Columns")
print("-" * 80)
print("Example: Remove duplicates based on customer_id only")
print("(Keep first occurrence of each customer)")
print()

df_unique_customers = df.drop_duplicates(subset=['customer_id'])

print("After removing duplicates by customer_id:")
print(f"Shape: {df_unique_customers.shape}")
print(df_unique_customers)
print()

print(f"Original rows: {len(df)}")
print(f"Unique customers: {len(df_unique_customers)}")
print(f"Duplicate customer entries removed: {len(df) - len(df_unique_customers)}")
print()

print("4.3 Choosing Which Duplicate to Keep")
print("-" * 80)
print("Example: Keep LAST occurrence instead of first")
print()

df_keep_last = df.drop_duplicates(subset=['customer_id'], keep='last')

print("Keeping last occurrence of each customer_id:")
print(df_keep_last)
print()

print("Comparison:")
print("- Keep 'first': Rows 0, 1, 2, 4, 5, 6, 7, 9")
print("- Keep 'last': Rows 3, 8, 6, 4, 5, 7, 9")
print("Notice rows 0→3, 1→8, 2→6 are replaced with their last occurrences")
print()

print("4.4 Removing All Duplicates (Keep None)")
print("-" * 80)
print("Example: Remove ALL occurrences of duplicated rows")
print("Use keep=False to remove both/all occurrences")
print()

df_no_duplicates = df.drop_duplicates(subset=['customer_id'], keep=False)

print("After removing ALL duplicate occurrences:")
print(df_no_duplicates)
print()

print(f"Rows remaining: {len(df_no_duplicates)}")
print("Only rows with unique customer_id values remain")
print()

# =============================================================================
# PRACTICAL SCENARIOS
# =============================================================================
print("=" * 80)
print("SECTION 5: Practical Duplicate Handling Scenarios")
print("=" * 80)
print()

print("5.1 Scenario: Cleaning Customer Database")
print("-" * 80)
print("Remove duplicate customers based on email (most reliable identifier)")
print()

# Create realistic customer data
customer_data = {
    'customer_id': [1001, 1002, 1003, 1004, 1005, 1006],
    'name': ['Alice Smith', 'Alice Smith', 'Bob Jones', 'Charlie Brown', 'Bob Jones', 'Diana Prince'],
    'email': ['alice@email.com', 'alice@email.com', 'bob@email.com', 'charlie@email.com', 
              'bobjones@email.com', 'diana@email.com'],
    'phone': ['111-1111', '111-1111', '222-2222', '333-3333', '444-4444', '555-5555'],
    'registration_date': ['2026-01-01', '2026-01-15', '2026-01-10', '2026-01-20', 
                          '2026-02-01', '2026-02-05']
}

df_customers = pd.DataFrame(customer_data)

print("Original customer database:")
print(df_customers)
print()

print("Checking for duplicates based on email:")
email_duplicates = df_customers.duplicated(subset=['email'])
print(f"Duplicate emails found: {email_duplicates.sum()}")
print()

# Clean by keeping most recent registration (last occurrence)
df_customers_clean = df_customers.drop_duplicates(subset=['email'], keep='last')

print("Cleaned customer database (keeping most recent registration):")
print(df_customers_clean)
print()

print(f"Original: {len(df_customers)} customers")
print(f"Cleaned: {len(df_customers_clean)} customers")
print(f"Duplicates removed: {len(df_customers) - len(df_customers_clean)}")
print()

print("5.2 Scenario: Transaction Log Deduplication")
print("-" * 80)
print("Identify and remove duplicate transactions")
print()

# Create transaction data with duplicates
transaction_data = {
    'transaction_id': ['TXN001', 'TXN002', 'TXN003', 'TXN001', 'TXN004', 'TXN005', 'TXN003'],
    'customer_id': [101, 102, 103, 101, 104, 105, 103],
    'amount': [50.00, 75.00, 100.00, 50.00, 60.00, 120.00, 100.00],
    'date': ['2026-03-01', '2026-03-01', '2026-03-02', '2026-03-01', 
             '2026-03-02', '2026-03-03', '2026-03-02'],
    'status': ['completed', 'completed', 'completed', 'completed', 
               'completed', 'completed', 'completed']
}

df_transactions = pd.DataFrame(transaction_data)

print("Transaction log with duplicates:")
print(df_transactions)
print()

print("Checking for duplicate transaction_ids:")
txn_duplicates = df_transactions.duplicated(subset=['transaction_id'])
print(f"Duplicate transactions found: {txn_duplicates.sum()}")
print()

print("Viewing duplicate transactions:")
print(df_transactions[df_transactions.duplicated(subset=['transaction_id'], keep=False)])
print()

# Remove duplicates keeping first occurrence
df_transactions_clean = df_transactions.drop_duplicates(subset=['transaction_id'], keep='first')

print("Cleaned transaction log:")
print(df_transactions_clean)
print()

print(f"Original transactions: {len(df_transactions)}")
print(f"Unique transactions: {len(df_transactions_clean)}")
print(f"Duplicate transactions removed: {len(df_transactions) - len(df_transactions_clean)}")
print()

# =============================================================================
# VERIFYING DEDUPLICATION RESULTS
# =============================================================================
print("=" * 80)
print("SECTION 6: Verifying Deduplication Results")
print("=" * 80)
print()

print("6.1 Compare Dataset Shapes")
print("-" * 80)
print("Before and after comparison:")
print()

print(f"Original DataFrame: {df.shape}")
print(f"Deduplicated DataFrame: {df_deduplicated.shape}")
print(f"Rows removed: {df.shape[0] - df_deduplicated.shape[0]}")
print(f"Columns (should be same): {df.shape[1]} → {df_deduplicated.shape[1]}")
print()

print("6.2 Recheck for Remaining Duplicates")
print("-" * 80)
print("Verify no duplicates remain:")
print()

remaining_duplicates = df_deduplicated.duplicated().sum()
print(f"Duplicates remaining: {remaining_duplicates}")

if remaining_duplicates == 0:
    print("✓ SUCCESS: No duplicates remain")
else:
    print("⚠ WARNING: Duplicates still present")
print()

print("6.3 Verify Specific Column Uniqueness")
print("-" * 80)
print("Check if customer_id is now unique:")
print()

unique_customer_ids = df_unique_customers['customer_id'].nunique()
total_rows = len(df_unique_customers)

print(f"Unique customer_ids: {unique_customer_ids}")
print(f"Total rows: {total_rows}")

if unique_customer_ids == total_rows:
    print("✓ SUCCESS: Each row has unique customer_id")
else:
    print("⚠ WARNING: Some customer_ids are still duplicated")
print()

print("6.4 Compare Record Counts")
print("-" * 80)
print("Statistical verification:")
print()

print("Original dataset:")
print(df['customer_id'].value_counts().sort_index())
print()

print("Deduplicated dataset:")
print(df_unique_customers['customer_id'].value_counts().sort_index())
print()

# =============================================================================
# BEST PRACTICES AND COMMON PITFALLS
# =============================================================================
print("=" * 80)
print("SECTION 7: Best Practices and Common Pitfalls")
print("=" * 80)
print()

print("7.1 Best Practices")
print("-" * 80)
print("""
✓ DO:
1. ALWAYS check for duplicates before analysis
2. Understand WHY duplicates exist before removing them
3. Use subset parameter to specify relevant columns
4. Choose keep parameter intentionally (first/last/False)
5. Verify results after deduplication
6. Document what was removed and why
7. Keep original data backup before removing duplicates
8. Consider domain context (some duplicates may be valid)

Example workflow:
1. Load data
2. Inspect for duplicates (duplicated())
3. Count duplicates (duplicated().sum())
4. View duplicates (df[df.duplicated()])
5. Decide removal strategy
6. Remove duplicates (drop_duplicates())
7. Verify results (check shape, recount duplicates)
""")
print()

print("7.2 Common Pitfalls")
print("-" * 80)
print("""
✗ DON'T:
1. Remove duplicates without understanding their source
2. Assume all duplicates are errors (could be valid data)
3. Remove duplicates on wrong columns
4. Forget to assign result (drop_duplicates doesn't modify in-place by default)
5. Remove duplicates before checking data quality
6. Ignore timestamp/date columns when choosing which to keep
7. Fail to verify deduplication results

Common mistakes:

Mistake 1: Not assigning result
❌ df.drop_duplicates()  # Does nothing!
✓ df = df.drop_duplicates()  # Correct
✓ df.drop_duplicates(inplace=True)  # Also correct

Mistake 2: Wrong subset columns
❌ df.drop_duplicates(subset=['name'])  # May remove valid different people with same name
✓ df.drop_duplicates(subset=['email'])  # Better unique identifier

Mistake 3: Not considering timestamps
❌ df.drop_duplicates(subset=['customer_id'], keep='first')  # May keep older data
✓ df.sort_values('date').drop_duplicates(subset=['customer_id'], keep='last')  # Keeps most recent
""")
print()

print("7.3 When NOT to Remove Duplicates")
print("-" * 80)
print("""
Duplicates are NOT always errors. Consider keeping them when:

1. Time-series data: Same entity at different times
   Example: Customer purchases - multiple orders by same person

2. Multi-level data: Intentional repetition
   Example: Students in multiple classes

3. Event logs: Each row is an event occurrence
   Example: Website visits - same user visiting multiple times

4. Many-to-many relationships: Valid data structure
   Example: Books and authors - books can have multiple authors

Always understand your data structure before removing duplicates!
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
1. UNDERSTANDING DUPLICATES
   - What duplicate records are
   - Why they occur
   - Types of duplicates (exact vs partial)

2. DETECTING DUPLICATES
   - Using duplicated() to identify duplicate rows
   - Counting duplicates with sum()
   - Viewing duplicate records
   - Understanding keep parameter (first/last/False)

3. REMOVING DUPLICATES
   - Using drop_duplicates() to remove duplicates
   - Specifying subset of columns to check
   - Choosing which occurrence to keep
   - Understanding inplace parameter

4. VERIFYING RESULTS
   - Comparing dataset shapes before/after
   - Rechecking for remaining duplicates
   - Verifying column uniqueness
   - Statistical verification

5. BEST PRACTICES
   - Always investigate before removing
   - Use appropriate subset columns
   - Choose keep strategy intentionally
   - Verify results thoroughly
   - Document deduplication decisions
""")
print()

print("Key Methods Summary:")
print("-" * 80)
print("""
duplicated()              - Detect duplicate rows (returns boolean Series)
duplicated(subset=[...])  - Detect duplicates in specific columns
duplicated(keep='first')  - Mark all except first occurrence
duplicated(keep='last')   - Mark all except last occurrence
duplicated(keep=False)    - Mark all duplicate occurrences

drop_duplicates()         - Remove duplicate rows
drop_duplicates(subset=[...])  - Remove based on specific columns
drop_duplicates(keep='first')  - Keep first occurrence
drop_duplicates(keep='last')   - Keep last occurrence
drop_duplicates(keep=False)    - Remove all duplicate occurrences
drop_duplicates(inplace=True)  - Modify DataFrame in place
""")
print()

print("=" * 80)
print("Next Steps:")
print("-" * 80)
print("""
Now that you can identify and remove duplicates:

1. Practice on real datasets with duplicate records
2. Learn about missing value handling
3. Explore data validation techniques
4. Combine duplicate detection with other data quality checks
5. Build complete data cleaning pipelines

Remember: Deduplication is a critical step in data quality assurance!
""")
print("=" * 80)
print("END OF MILESTONE")
print("=" * 80)
