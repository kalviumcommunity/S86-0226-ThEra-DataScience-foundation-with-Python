"""
Missing Values Handling Milestone - Pandas Fundamentals
======================================================

This script demonstrates how to handle missing values in Pandas using:
- drop strategies (drop rows/columns with missing data)
- fill strategies (fill missing data with constants or statistics)

The goal is to make informed decisions about when to drop data versus when to
fill missing values, understanding the trade-offs involved.

Author: Your Name
Date: March 10, 2026
"""

import pandas as pd
import numpy as np

print("=" * 80)
print("MISSING VALUES HANDLING MILESTONE - PANDAS FUNDAMENTALS")
print("=" * 80)
print()

# =============================================================================
# 1. SET UP EXAMPLE DATAFRAME WITH MISSING VALUES
# =============================================================================
print("SECTION 1: Create a DataFrame with missing values")
print("-" * 80)
print()

# Create a DataFrame intentionally containing missing values
# (mixed numeric and categorical data to show common patterns)
df = pd.DataFrame({
    "id": [1, 2, 3, 4, 5],
    "age": [25, np.nan, 22, 40, np.nan],
    "score": [88.5, 92.0, np.nan, 75.0, 85.0],
    "level": ["beginner", "intermediate", None, "advanced", "beginner"],
    "passed": [True, True, np.nan, False, True],
})

print("Original DataFrame")
print(df)
print()

print("Missing value counts (per column):")
print(df.isnull().sum())
print()

print("Missing percentage (per column):")
print((df.isnull().mean() * 100).round(1))
print()

# =============================================================================
# 2. DROP MISSING VALUES
# =============================================================================
print("SECTION 2: Dropping missing values")
print("-" * 80)
print()

print("2.1 Drop rows with ANY missing value")
print("(This removes rows where at least one column has NaN)")
df_drop_any = df.dropna()
print("Shape before drop:", df.shape)
print("Shape after drop:", df_drop_any.shape)
print(df_drop_any)
print()

print("2.2 Drop rows only when ALL values are missing")
print("(This is more conservative and rarely drops much in real-world data)")
df_drop_all = df.dropna(how="all")
print("Shape after dropna(how='all'):", df_drop_all.shape)
print(df_drop_all)
print()

print("2.3 Drop rows based on a subset of columns")
print("(Drop rows only if important columns are missing)")
df_drop_subset = df.dropna(subset=["age", "score"])
print("Shape after dropping where age or score is missing:", df_drop_subset.shape)
print(df_drop_subset)
print()

print("2.4 Drop columns with too many missing values")
print("(Keep only columns with at least 60% non-missing values)")
threshold = int(len(df) * 0.6)
df_drop_cols = df.dropna(axis=1, thresh=threshold)
print("Columns before:", list(df.columns))
print("Columns after dropping sparse columns:", list(df_drop_cols.columns))
print(df_drop_cols)
print()

print("KEY TAKEAWAY: Dropping removes data permanently. It may be OK if the missing ")
print("values are rare or if the affected rows/columns are not critical.")
print()

# =============================================================================
# 3. FILLING MISSING VALUES
# =============================================================================
print("SECTION 3: Filling missing values")
print("-" * 80)
print()

print("3.1 Fill all missing values with a constant")
print("(This can be useful for placeholders, but be careful not to distort stats)")
df_fill_const = df.fillna({
    "age": 0,
    "score": 0,
    "level": "Unknown",
    "passed": False,
})
print(df_fill_const)
print()

print("3.2 Fill numeric missing values with summary statistics")
print("- age with median")
print("- score with mean")

age_median = df["age"].median()
score_mean = df["score"].mean()

print(f"Median age: {age_median}")
print(f"Mean score: {score_mean:.2f}")

# Use fillna with a dictionary to apply different values per column
df_fill_stats = df.fillna({
    "age": age_median,
    "score": score_mean,
    # For categorical columns, filling with a meaningful placeholder is usually best
    "level": df["level"].mode().iloc[0],
    "passed": df["passed"].mode().iloc[0],
})

print("DataFrame after filling with simple statistics:")
print(df_fill_stats)
print()

print("3.3 Fill categorical missing values with mode (most frequent value)")
print("(This is a simple, explainable strategy for categorical data)")

level_mode = df["level"].mode().iloc[0]
print(f"Level mode: {level_mode}")

df_fill_categorical = df.copy()
df_fill_categorical["level"] = df_fill_categorical["level"].fillna(level_mode)
print(df_fill_categorical)
print()

print("3.4 Forward / backward fill (useful for time series)")
print("(Carry last valid observation forward/backward)")

# Create a 1D example for forward/backward fill to make behavior clear
series_example = pd.Series([1.0, np.nan, np.nan, 4.0, np.nan, 6.0])
print("Original series:")
print(series_example)
print("Forward fill (ffill):")
print(series_example.ffill())
print("Backward fill (bfill):")
print(series_example.bfill())
print()

print("KEY TAKEAWAY: Filling preserves row/column count but introduces assumptions.")
print("Always think about whether the chosen fill value makes sense for the feature.")
print()

# =============================================================================
# 4. COMPARING DROP VS FILL
# =============================================================================
print("SECTION 4: Comparing drop vs fill")
print("-" * 80)
print()

print("Original missing positions (True means missing):")
print(df.isnull())
print()

print("After dropna():")
print(df_drop_any)
print()

print("After fillna() with statistics:")
print(df_fill_stats)
print()

print("SUMMARY: Dropping removes rows but keeps only fully-observed data.")
print("Filling keeps all rows but changes values where data was missing.")
print("Choose the strategy that best preserves the information you need.")
print()

print("""\
DESIGN NOTES:
- Drop when missingness is rare and you can afford to lose data.
- Fill when you need complete records and can justify the imputation.
- Keep a copy of the original data so you can compare approaches.
""")

print("=" * 80)
print("MISSING VALUES HANDLING MILESTONE COMPLETE")
print("=" * 80)
