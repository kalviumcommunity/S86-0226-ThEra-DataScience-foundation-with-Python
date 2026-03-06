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

print("✅ Milestone demonstration complete. DataFrames created and inspected.")
print("   No further cleaning or analysis was performed.")
print("=" * 60)
