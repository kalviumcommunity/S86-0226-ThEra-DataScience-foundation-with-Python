import pandas as pd
import matplotlib.pyplot as plt

print("=" * 60)
print("SCATTER PLOT MILESTONE DEMO")
print("=" * 60)
print()

from pathlib import Path

# ---------------------------------------------------------------------------
# 1. LOAD DATA
# ---------------------------------------------------------------------------
print("1️⃣  Loading a dataset")
print("   (using example CSV provided in project/data/processed)")

project_root = Path(__file__).resolve().parents[1]  # project/ (one level up from scripts/)
file_path = project_root / "data" / "processed" / "example_processed.csv"

try:
    df = pd.read_csv(file_path)
    print("   Loaded DataFrame head:")
    print(df.head())
    print("   Data types:")
    print(df.dtypes)
except Exception as e:
    print("   Error loading file:", e)
    raise

print()

# ---------------------------------------------------------------------------
# 2. SELECT NUMERIC COLUMNS
# ---------------------------------------------------------------------------
print("2️⃣  Selecting numeric columns")
numeric_cols = df.select_dtypes(include="number").columns.tolist()
print("   Numeric columns detected:", numeric_cols)

if len(numeric_cols) < 2:
    raise SystemExit("Need at least two numeric columns to create a scatter plot.")

# Pick the first two numeric columns for plotting.
# In a real analysis you would choose columns with meaningful relationships.
x_col, y_col = numeric_cols[0], numeric_cols[1]
print(f"   Using x-axis: '{x_col}' and y-axis: '{y_col}'")

print()

# ---------------------------------------------------------------------------
# 3. CREATE SCATTER PLOT
# ---------------------------------------------------------------------------
print("3️⃣  Creating a scatter plot")
plt.figure(figsize=(6, 4))
plt.scatter(df[x_col], df[y_col], c="tab:blue", edgecolor="black")
plt.title(f"Scatter plot: {y_col} vs {x_col}")
plt.xlabel(x_col)
plt.ylabel(y_col)
plt.grid(True, linestyle="--", alpha=0.5)

output_path = project_root / "outputs" / "scatter_plot.png"
output_path.parent.mkdir(parents=True, exist_ok=True)
plt.tight_layout()
plt.savefig(output_path)
plt.close()

print(f"   Saved scatter plot to: {output_path}")
print("   Each point represents one row/observation in the dataset.")
print()

# ---------------------------------------------------------------------------
# 4. INTERPRETATION GUIDANCE
# ---------------------------------------------------------------------------
print("4️⃣  Interpreting the scatter plot")
print("   - Positive relationship: points trend upward as x increases")
print("   - Negative relationship: points trend downward as x increases")
print("   - No clear trend: points appear scattered")
print("   - Look for clusters, gaps, or outliers")
print()

print("✅ Milestone complete. View the saved plot to assess relationships between variables.")
print("   In a notebook, you could display the plot inline with plt.show().")
print("=" * 60)
