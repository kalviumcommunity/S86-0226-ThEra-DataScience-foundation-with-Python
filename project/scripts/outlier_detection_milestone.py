import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

print("=" * 60)
print("OUTLIER DETECTION MILESTONE DEMO")
print("=" * 60)
print()

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

if len(numeric_cols) < 1:
    raise SystemExit("Need at least one numeric column to detect outliers.")

print()

# ---------------------------------------------------------------------------
# 3. VISUAL INSPECTION USING BOXPLOTS
# ---------------------------------------------------------------------------
print("3️⃣  Visual inspection using boxplots")
print("   Boxplots show median, quartiles, and potential outliers beyond whiskers.")

for col in numeric_cols:
    plt.figure(figsize=(6, 4))
    plt.boxplot(df[col], vert=False, patch_artist=True, boxprops=dict(facecolor="lightblue"))
    plt.title(f"Boxplot of {col}")
    plt.xlabel(col)
    plt.grid(True, linestyle="--", alpha=0.5)

    output_path = project_root / "outputs" / f"boxplot_{col}.png"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()

    print(f"   Saved boxplot for {col} to: {output_path}")
    print(f"   - Points beyond whiskers are potential outliers")
    print(f"   - Whiskers typically extend to 1.5 * IQR from Q1/Q3")

print()

# ---------------------------------------------------------------------------
# 4. VISUAL INSPECTION USING SCATTER PLOTS (if multiple numeric columns)
# ---------------------------------------------------------------------------
print("4️⃣  Visual inspection using scatter plots")
if len(numeric_cols) >= 2:
    x_col, y_col = numeric_cols[0], numeric_cols[1]
    plt.figure(figsize=(6, 4))
    plt.scatter(df[x_col], df[y_col], c="tab:blue", edgecolor="black")
    plt.title(f"Scatter plot: {y_col} vs {x_col}")
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.grid(True, linestyle="--", alpha=0.5)

    output_path = project_root / "outputs" / f"scatter_{y_col}_vs_{x_col}.png"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()

    print(f"   Saved scatter plot to: {output_path}")
    print("   - Isolated points far from the main cluster may be outliers")
else:
    print("   Not enough numeric columns for scatter plot (need at least 2).")

print()

# ---------------------------------------------------------------------------
# 5. DETECTING OUTLIERS USING SIMPLE RULES (IQR METHOD)
# ---------------------------------------------------------------------------
print("5️⃣  Detecting outliers using simple rules (IQR method)")
print("   IQR = Q3 - Q1")
print("   Lower bound = Q1 - 1.5 * IQR")
print("   Upper bound = Q3 + 1.5 * IQR")
print("   Values outside these bounds are potential outliers.")

for col in numeric_cols:
    series = df[col]
    Q1 = series.quantile(0.25)
    Q3 = series.quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    outliers = series[(series < lower_bound) | (series > upper_bound)]
    print(f"\n   Column: {col}")
    print(f"     Q1: {Q1:.2f}, Q3: {Q3:.2f}, IQR: {IQR:.2f}")
    print(f"     Lower bound: {lower_bound:.2f}, Upper bound: {upper_bound:.2f}")
    if len(outliers) > 0:
        print(f"     Potential outliers: {outliers.tolist()}")
        print("     - These values are far from the typical range")
        print("     - Check if they are valid observations or data errors")
    else:
        print("     No outliers detected by IQR rule.")

print()

# ---------------------------------------------------------------------------
# 6. INTERPRETATION GUIDANCE
# ---------------------------------------------------------------------------
print("6️⃣  Interpreting outliers carefully")
print("   - Outliers may be valid extreme values (e.g., rare events)")
print("   - They could indicate data entry errors or measurement issues")
print("   - Consider domain knowledge: Does the value make sense?")
print("   - Before removing, investigate why the outlier exists")
print("   - Outliers can provide valuable insights if handled thoughtfully")

print()
print("✅ Milestone complete. Review the saved plots and flagged values.")
print("   Use visuals and rules as starting points for deeper investigation.")
print("=" * 60)
