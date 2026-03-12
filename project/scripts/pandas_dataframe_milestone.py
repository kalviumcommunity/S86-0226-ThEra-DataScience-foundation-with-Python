import pandas as pd

print("=" * 60)
print("PANDAS DATAFRAME MILESTONE DEMO")
print("=" * 60)
print()

# ============================================================================
# 1. IMPORT PANDAS
# ============================================================================
print("1️⃣  Importing Pandas")
print("   import pandas as pd")
print("   → Pandas is imported with the alias 'pd' by convention")
print()

# ============================================================================
# 2. CREATE DATAFRAME FROM DICTIONARY
# ============================================================================
print("2️⃣  Creating a DataFrame from a dictionary")

data = {
    "name": ["Alice", "Bob", "Carol"],
    "age": [25, 30, 22],
    "score": [88.5, 92.0, 79.5],
}

df = pd.DataFrame(data)

print("   Dictionary:\n", data)
print("   Resulting DataFrame:\n", df)
print()

print("   Columns:", df.columns)
print("   Shape:", df.shape)
print("   Data types:\n", df.dtypes)
print()

# ============================================================================
# 3. LOAD DATAFRAME FROM FILE
# ============================================================================
print("3️⃣  Loading a DataFrame from a file")
print("   (using example CSV provided in project/data/processed)")

file_path = "S86-0226-ThEra-DataScience-foundation-with-Python/project/data/processed/example_processed.csv"
try:
    df_file = pd.read_csv(file_path)
    print("   Loaded DataFrame head:\n", df_file.head())
    print("   Columns:", df_file.columns)
    print("   Shape:", df_file.shape)
    print("   Data types:\n", df_file.dtypes)
except Exception as e:
    print("   Error loading file:", e)

print()

# ============================================================================
# 4. BASIC INSPECTION
# ============================================================================
print("4️⃣  Inspecting the DataFrame structure")
print("   Use df.head(), df.columns, df.shape, df.dtypes to verify data")
print()

# ============================================================================
# 5. BASIC SUMMARY STATISTICS FOR INDIVIDUAL COLUMNS
# ============================================================================
print("5️⃣  Computing basic summary statistics for individual columns")
print("   Summary statistics help you understand central tendency (mean/median), range, and spread.")
print()

# Choose a single numeric column from the small demo DataFrame
col = "age"
print(f"   Stats for df['{col}'] (small demo DataFrame):")
print(f"     count:  {df[col].count()}")
print(f"     mean:   {df[col].mean():.2f}")
print(f"     median: {df[col].median():.2f}")
print(f"     min:    {df[col].min()}")
print(f"     max:    {df[col].max()}")
print(f"     std:    {df[col].std():.2f}")
print(f"     var:    {df[col].var():.2f}")
print()

# Show how Pandas can compute summaries quickly for all numeric columns
print("   Quick summary for all numeric columns in the small demo DataFrame:")
print(df.describe())
print()

# If the file loaded successfully, compute statistics on its numeric columns.
if "df_file" in locals():
    print("   Summary statistics for numeric columns in the loaded CSV:")
    numeric_cols = df_file.select_dtypes(include="number").columns.tolist()
    print(f"   Numeric columns detected: {numeric_cols}")
    # Display stats for each numeric column with a short description of what to look for
    for col in numeric_cols:
        series = df_file[col]
        print(f"\n   Column: {col}")
        print(f"     count:  {series.count()}")
        print(f"     mean:   {series.mean():.2f}")
        print(f"     median: {series.median():.2f}")
        print(f"     min:    {series.min()}")
        print(f"     max:    {series.max()}")
        print(f"     std:    {series.std():.2f}")
        print(f"     var:    {series.var():.2f}")

    print("\n   You can use these statistics to compare columns, detect outliers, and understand spread.")

print()
print("✅ Milestone demonstration complete. DataFrames created, inspected, and summary statistics computed.")
print("   Use these outputs to practice interpreting mean vs median, spread, and outliers.")
print("=" * 60)
