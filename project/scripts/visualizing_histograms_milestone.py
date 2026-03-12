"""
Visualizing Data Distributions Using Histograms Milestone - Pandas & Matplotlib
================================================================================

This script demonstrates the fundamentals of visualizing data distributions using histograms:
- Understanding what histograms represent
- Creating histograms for single and multiple columns
- Interpreting distribution shape (skewness, normality)
- Identifying outliers and patterns visually
- Comparing distributions across columns using plots

Histograms are one of the most effective ways to understand how values are distributed,
revealing patterns that summary statistics alone may hide.

Visualization helps you see the data, not just describe it numerically.

Author: Your Name
Date: March 12, 2026
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

# Set plotting style for better-looking charts
plt.style.use('default')

print("=" * 80)
print("VISUALIZING DATA DISTRIBUTIONS USING HISTOGRAMS MILESTONE")
print("=" * 80)
print()

# =============================================================================
# INTRODUCTION
# =============================================================================
print("INTRODUCTION: Why Histograms Matter")
print("-" * 80)
print("""
After computing summary statistics, visualization is THE NEXT ESSENTIAL STEP.

Histograms reveal:
1. How values are distributed across the range
2. Whether data is symmetric or skewed
3. Presence of outliers or unusual gaps
4. Multi-modal patterns (multiple peaks)

Common beginner issues include:
- Relying only on averages without seeing the data
- Missing skewed or multi-modal distributions
- Overlooking outliers that affect analysis
- Misinterpreting summary statistics

Histograms reveal patterns that numbers alone cannot.

This milestone ensures that:
- You understand how data is distributed
- Patterns and anomalies become visible
- Statistical results are interpreted in context
- EDA decisions are better informed

Think of histograms as a visual summary of your data's behavior.
""")
print()

# =============================================================================
# SECTION 1: Understanding Histograms
# =============================================================================
print("=" * 80)
print("SECTION 1: Understanding Histograms")
print("=" * 80)
print()

print("1.1 What is a Histogram?")
print("-" * 80)
print("""
A histogram is a graphical representation of the distribution of numeric data.

Key components:
- X-axis: Range of values divided into intervals (bins)
- Y-axis: Frequency (count) or density of values in each bin
- Bars: Height represents how many values fall in each interval

Example intuition:
- If you have test scores: [65, 70, 72, 75, 78, 80, 82, 85, 88, 90]
- A histogram groups these into bins (e.g., 60-70, 70-80, 80-90)
- Bar height shows how many scores fall in each range

Histogram vs Bar Chart:
╔══════════════════════════════════════════════════════════════════════╗
║ Histogram: Continuous numeric data, bins are intervals              ║
║ Bar Chart: Categorical data, bars represent distinct categories     ║
╚══════════════════════════════════════════════════════════════════════╝

Why histograms matter:
- Reveal the SHAPE of the distribution
- Show WHERE values cluster
- Identify GAPS or OUTLIERS
- Detect SKEWNESS (asymmetry)
- Provide context for mean/median
""")
print()

print("1.2 Understanding Bins")
print("-" * 80)
print("""
Bins are intervals that divide the range of values.

Key concepts:
- Too few bins: Loss of detail, distribution looks overly smooth
- Too many bins: Too noisy, hard to see overall pattern
- Default (often 10-30): Usually a good starting point

Example:
Data range: 0 to 100
10 bins: [0-10), [10-20), [20-30), ..., [90-100]
Each bar shows count of values in that interval

The choice of bins affects what patterns you see!
""")
print()

# =============================================================================
# SECTION 2: Creating Sample Data
# =============================================================================
print("=" * 80)
print("SECTION 2: Creating Sample Data with Diverse Distributions")
print("=" * 80)
print()

print("Creating a dataset with intentionally different distribution shapes:")
print("-" * 80)

# Create sample data with different distribution characteristics
np.random.seed(42)

sample_data = {
    'student_id': range(1, 101),
    
    # Roughly normal distribution (symmetric, bell-shaped)
    'math_score': np.random.normal(75, 10, 100).clip(0, 100),
    
    # Right-skewed distribution (tail on the right)
    'study_hours': np.random.exponential(10, 100).clip(0, 50),
    
    # Left-skewed distribution (tail on the left)
    'attendance_pct': 100 - np.random.exponential(5, 100).clip(0, 25),
    
    # Bimodal distribution (two peaks)
    'assignment_score': np.concatenate([
        np.random.normal(60, 5, 50),
        np.random.normal(85, 5, 50)
    ]),
    
    # Uniform distribution (roughly flat)
    'random_metric': np.random.uniform(0, 100, 100),
    
    # Distribution with outliers
    'quiz_score': np.concatenate([
        np.random.normal(80, 8, 95),
        np.array([20, 25, 30, 35, 40])  # Low outliers
    ])
}

df = pd.DataFrame(sample_data)

# Round numeric columns
numeric_cols = ['math_score', 'study_hours', 'attendance_pct', 
                'assignment_score', 'random_metric', 'quiz_score']
df[numeric_cols] = df[numeric_cols].round(2)

print("✓ Sample dataset created with 100 students")
print(f"✓ {len(numeric_cols)} numeric columns with diverse distributions")
print()

print("Preview of the data:")
print("-" * 80)
print(df.head(10))
print()

print("Summary statistics:")
print("-" * 80)
print(df[numeric_cols].describe())
print()

# =============================================================================
# SECTION 3: Creating a Histogram for a Single Column
# =============================================================================
print("=" * 80)
print("SECTION 3: Creating a Histogram for a Single Column")
print("=" * 80)
print()

print("3.1 Basic Histogram with Pandas")
print("-" * 80)
print("""
Pandas provides a simple .hist() method to create histograms.

Syntax: df['column'].hist()

This creates a quick histogram with default settings.
""")
print()

print("Example: Creating a histogram for math_score")
print("-" * 80)

# Create figure
fig, ax = plt.subplots(figsize=(8, 5))
df['math_score'].hist(ax=ax, bins=15, edgecolor='black', alpha=0.7, color='skyblue')
ax.set_xlabel('Math Score', fontsize=11)
ax.set_ylabel('Frequency (Count)', fontsize=11)
ax.set_title('Distribution of Math Scores', fontsize=13, fontweight='bold')
ax.grid(axis='y', alpha=0.3)

# Save the plot
plt.tight_layout()
plt.savefig('../outputs/histogram_single_math_score.png', dpi=100, bbox_inches='tight')
print("✓ Histogram saved: outputs/histogram_single_math_score.png")
plt.close()

print()
print("INTERPRETATION:")
print("-" * 80)
print("""
What to look for in the histogram:
1. CENTER: Where is the peak? (Around 75 for math scores)
2. SPREAD: How wide is the distribution? (Spans roughly 50-95)
3. SHAPE: Is it symmetric? (Roughly bell-shaped/normal)
4. OUTLIERS: Any isolated bars far from the rest? (None visible)
5. GAPS: Any empty bins? (No major gaps)

This histogram shows a roughly normal (bell-shaped) distribution.
Most students score around 75, with fewer at the extremes.
""")
print()

print("3.2 Comparing Different Bin Sizes")
print("-" * 80)
print("""
The number of bins affects how much detail you see.

Too few bins: Oversimplified, loses detail
Too many bins: Too granular, hard to see pattern
Just right: Reveals shape without noise

Let's create the same histogram with different bin counts.
""")
print()

# Create figure with multiple subplots
fig, axes = plt.subplots(1, 3, figsize=(15, 4))

bin_counts = [5, 15, 40]
for ax, bins in zip(axes, bin_counts):
    df['math_score'].hist(ax=ax, bins=bins, edgecolor='black', alpha=0.7, color='skyblue')
    ax.set_xlabel('Math Score', fontsize=10)
    ax.set_ylabel('Frequency', fontsize=10)
    ax.set_title(f'Bins = {bins}', fontsize=12, fontweight='bold')
    ax.grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.savefig('../outputs/histogram_bin_comparison.png', dpi=100, bbox_inches='tight')
print("✓ Bin comparison saved: outputs/histogram_bin_comparison.png")
plt.close()

print()
print("INTERPRETATION:")
print("-" * 80)
print("""
5 bins:   Too coarse - can't see the bell shape clearly
15 bins:  Good balance - shows normal distribution well
40 bins:  Too granular - lots of noise, harder to see overall shape

Best practice: Start with default (10-20 bins), adjust if needed.
""")
print()

# =============================================================================
# SECTION 4: Interpreting Distribution Shape
# =============================================================================
print("=" * 80)
print("SECTION 4: Interpreting Distribution Shape")
print("=" * 80)
print()

print("4.1 Common Distribution Shapes")
print("-" * 80)
print("""
Different shapes reveal different data characteristics:

1. NORMAL (BELL-SHAPED):
   - Symmetric around the mean
   - Most values near center, fewer at extremes
   - Mean ≈ Median
   - Example: Test scores, heights, measurement errors

2. RIGHT-SKEWED (POSITIVE SKEW):
   - Tail extends to the right
   - Most values clustered on left, few high values
   - Mean > Median (pulled by high values)
   - Example: Income, response times, study hours

3. LEFT-SKEWED (NEGATIVE SKEW):
   - Tail extends to the left
   - Most values clustered on right, few low values
   - Mean < Median (pulled by low values)
   - Example: Age at retirement, test scores with ceiling effect

4. BIMODAL:
   - Two distinct peaks
   - Suggests two different groups/populations
   - Example: Mixed beginner/advanced students, weekday/weekend patterns

5. UNIFORM:
   - Roughly flat across the range
   - All values equally likely
   - Example: Random numbers, well-distributed categories
""")
print()

print("4.2 Visualizing Different Distribution Shapes")
print("-" * 80)

# Create figure with multiple distribution shapes
fig, axes = plt.subplots(2, 3, figsize=(15, 8))
axes = axes.ravel()

# Define columns and their expected shapes
distributions = [
    ('math_score', 'Roughly Normal\n(Symmetric)', 'skyblue'),
    ('study_hours', 'Right-Skewed\n(Positive Skew)', 'lightcoral'),
    ('attendance_pct', 'Left-Skewed\n(Negative Skew)', 'lightgreen'),
    ('assignment_score', 'Bimodal\n(Two Peaks)', 'plum'),
    ('random_metric', 'Uniform\n(Flat)', 'wheat'),
    ('quiz_score', 'With Outliers\n(Low Values)', 'lightsalmon')
]

for idx, (col, title, color) in enumerate(distributions):
    ax = axes[idx]
    df[col].hist(ax=ax, bins=20, edgecolor='black', alpha=0.75, color=color)
    ax.set_xlabel(col.replace('_', ' ').title(), fontsize=10)
    ax.set_ylabel('Frequency', fontsize=10)
    ax.set_title(title, fontsize=11, fontweight='bold')
    ax.grid(axis='y', alpha=0.3)
    
    # Add mean and median lines
    mean_val = df[col].mean()
    median_val = df[col].median()
    ax.axvline(mean_val, color='red', linestyle='--', linewidth=2, label=f'Mean: {mean_val:.1f}')
    ax.axvline(median_val, color='blue', linestyle='--', linewidth=2, label=f'Median: {median_val:.1f}')
    ax.legend(fontsize=8, loc='upper right')

plt.tight_layout()
plt.savefig('../outputs/histogram_distribution_shapes.png', dpi=100, bbox_inches='tight')
print("✓ Distribution shapes saved: outputs/histogram_distribution_shapes.png")
plt.close()

print()
print("KEY OBSERVATIONS:")
print("-" * 80)

for col, title, _ in distributions:
    mean_val = df[col].mean()
    median_val = df[col].median()
    diff = mean_val - median_val
    
    print(f"\n{col}:")
    print(f"  Mean: {mean_val:.2f}, Median: {median_val:.2f}, Difference: {diff:.2f}")
    
    if abs(diff) < 1:
        print(f"  → Roughly SYMMETRIC (mean ≈ median)")
    elif diff > 1:
        print(f"  → RIGHT-SKEWED (mean > median, tail to the right)")
    else:
        print(f"  → LEFT-SKEWED (mean < median, tail to the left)")

print()

# =============================================================================
# SECTION 5: Identifying Outliers Visually
# =============================================================================
print("=" * 80)
print("SECTION 5: Identifying Outliers Visually")
print("=" * 80)
print()

print("5.1 What Are Outliers?")
print("-" * 80)
print("""
Outliers are values that are significantly different from most other values.

In a histogram, outliers appear as:
- Isolated bars far from the main distribution
- Values in the extreme tails
- Gaps between the main cluster and extreme values

Why outliers matter:
- They affect mean (but not median much)
- They may indicate data quality issues
- They may represent interesting special cases
- They influence statistical models

Histograms help you SEE outliers before deciding what to do with them.
""")
print()

print("5.2 Example: Quiz Scores with Outliers")
print("-" * 80)

# Create detailed histogram for quiz_score showing outliers
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# Histogram with outliers
df['quiz_score'].hist(ax=ax1, bins=25, edgecolor='black', alpha=0.7, color='lightsalmon')
ax1.set_xlabel('Quiz Score', fontsize=11)
ax1.set_ylabel('Frequency', fontsize=11)
ax1.set_title('Quiz Scores - With Outliers', fontsize=13, fontweight='bold')
ax1.axvline(df['quiz_score'].mean(), color='red', linestyle='--', linewidth=2, label=f'Mean: {df["quiz_score"].mean():.1f}')
ax1.axvline(df['quiz_score'].median(), color='blue', linestyle='--', linewidth=2, label=f'Median: {df["quiz_score"].median():.1f}')
ax1.legend(fontsize=10)
ax1.grid(axis='y', alpha=0.3)

# Histogram without extreme outliers (for comparison)
quiz_filtered = df[df['quiz_score'] > 50]['quiz_score']
quiz_filtered.hist(ax=ax2, bins=20, edgecolor='black', alpha=0.7, color='lightgreen')
ax2.set_xlabel('Quiz Score', fontsize=11)
ax2.set_ylabel('Frequency', fontsize=11)
ax2.set_title('Quiz Scores - Outliers Removed (>50)', fontsize=13, fontweight='bold')
ax2.axvline(quiz_filtered.mean(), color='red', linestyle='--', linewidth=2, label=f'Mean: {quiz_filtered.mean():.1f}')
ax2.axvline(quiz_filtered.median(), color='blue', linestyle='--', linewidth=2, label=f'Median: {quiz_filtered.median():.1f}')
ax2.legend(fontsize=10)
ax2.grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.savefig('../outputs/histogram_outliers_comparison.png', dpi=100, bbox_inches='tight')
print("✓ Outlier comparison saved: outputs/histogram_outliers_comparison.png")
plt.close()

print()
print("INTERPRETATION:")
print("-" * 80)
print(f"""
WITH outliers:
  - Mean: {df['quiz_score'].mean():.2f}
  - Median: {df['quiz_score'].median():.2f}
  - You can see isolated bars in the 20-40 range (outliers)
  - Mean is PULLED DOWN by low outliers

WITHOUT outliers (scores > 50):
  - Mean: {quiz_filtered.mean():.2f}
  - Median: {quiz_filtered.median():.2f}
  - Distribution looks more normal
  - Mean and median are closer

Key insight: Histograms help you SEE outliers and understand their impact.
The median ({df['quiz_score'].median():.2f}) is more representative than the mean ({df['quiz_score'].mean():.2f})
when outliers are present.
""")
print()

# =============================================================================
# SECTION 6: Comparing Histograms Across Columns
# =============================================================================
print("=" * 80)
print("SECTION 6: Comparing Histograms Across Columns")
print("=" * 80)
print()

print("6.1 Side-by-Side Comparison")
print("-" * 80)
print("""
Comparing histograms visually complements statistical comparison.

You can see:
- Which columns have wider/narrower spreads
- Which are symmetric vs skewed
- Which have outliers
- How distributions differ in shape

Visual comparison makes patterns obvious.
""")
print()

print("Example: Comparing Test Score Distributions")
print("-" * 80)

# Compare three related columns
test_columns = ['math_score', 'assignment_score', 'quiz_score']
fig, axes = plt.subplots(1, 3, figsize=(15, 4))

for ax, col in zip(axes, test_columns):
    df[col].hist(ax=ax, bins=20, edgecolor='black', alpha=0.7, color='steelblue')
    ax.set_xlabel(col.replace('_', ' ').title(), fontsize=11)
    ax.set_ylabel('Frequency', fontsize=11)
    ax.set_title(f'{col.replace("_", " ").title()}\nMean: {df[col].mean():.1f}, Std: {df[col].std():.1f}', 
                 fontsize=11, fontweight='bold')
    ax.axvline(df[col].mean(), color='red', linestyle='--', linewidth=2, alpha=0.7)
    ax.grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.savefig('../outputs/histogram_score_comparison.png', dpi=100, bbox_inches='tight')
print("✓ Score comparison saved: outputs/histogram_score_comparison.png")
plt.close()

print()
print("VISUAL COMPARISON INSIGHTS:")
print("-" * 80)
print("""
math_score:
  - Roughly normal (symmetric, bell-shaped)
  - Centered around 75
  - No obvious outliers

assignment_score:
  - BIMODAL (two distinct peaks around 60 and 85)
  - Suggests two different student groups
  - Interesting pattern worth investigating

quiz_score:
  - Mostly clustered around 75-85
  - Clear OUTLIERS in the 20-40 range
  - Right side of distribution is cut off (ceiling effect?)

Visual comparison reveals these patterns immediately!
""")
print()

print("6.2 Using .hist() on Entire DataFrame")
print("-" * 80)
print("""
You can create histograms for ALL numeric columns at once:

Syntax: df.hist()

This creates a grid of histograms for quick overview.
""")
print()

# Create histograms for all numeric columns
fig = plt.figure(figsize=(15, 10))
df[numeric_cols].hist(bins=20, figsize=(15, 10), edgecolor='black', alpha=0.7, color='teal')
plt.suptitle('Distribution of All Numeric Columns', fontsize=16, fontweight='bold', y=0.995)
plt.tight_layout()
plt.savefig('../outputs/histogram_all_columns.png', dpi=100, bbox_inches='tight')
print("✓ All columns saved: outputs/histogram_all_columns.png")
plt.close()

print()
print("This gives you a complete visual overview of all distributions at once.")
print()

# =============================================================================
# SECTION 7: Using Histograms to Guide Analysis
# =============================================================================
print("=" * 80)
print("SECTION 7: Using Histograms to Guide Analysis")
print("=" * 80)
print()

print("7.1 What Histograms Tell You About Next Steps")
print("-" * 80)
print("""
Histogram shapes directly inform analysis decisions:

If distribution is NORMAL (symmetric):
→ Mean is a good summary statistic
→ Can use parametric statistical tests
→ Standard deviation is meaningful
→ Proceed with standard analysis methods

If distribution is SKEWED:
→ Use median instead of mean
→ Consider transformation (log, sqrt)
→ Be cautious with parametric tests
→ Report skewness explicitly

If distribution has OUTLIERS:
→ Investigate outliers individually
→ Decide: Remove, keep, or analyze separately
→ Use robust statistics (median, IQR)
→ Consider outlier impact on models

If distribution is BIMODAL:
→ You may have TWO distinct groups
→ Consider segmentation or clustering
→ Analyze groups separately
→ Investigate what causes the split

If distribution is UNIFORM:
→ No clear central tendency
→ All values equally common
→ May indicate data quality issue or special case
""")
print()

print("7.2 Decision Matrix Based on Our Data")
print("-" * 80)
print()

# Create decision matrix
decisions = []
for col in numeric_cols:
    mean_val = df[col].mean()
    median_val = df[col].median()
    std_val = df[col].std()
    
    # Determine shape
    diff = mean_val - median_val
    if abs(diff) < 1:
        shape = "Normal/Symmetric"
        action = "Use mean, standard methods"
    elif diff > 1:
        shape = "Right-Skewed"
        action = "Use median, check for outliers"
    else:
        shape = "Left-Skewed"
        action = "Use median, consider transformation"
    
    # Check for bimodal (simplified check based on our data)
    if col == 'assignment_score':
        shape = "Bimodal"
        action = "Investigate two groups, segment"
    
    # Check for outliers (simplified check)
    if col == 'quiz_score':
        shape += " with outliers"
        action = "Investigate outliers, use median"
    
    decisions.append({
        'Column': col,
        'Shape': shape,
        'Mean': round(mean_val, 1),
        'Median': round(median_val, 1),
        'Recommended Action': action
    })

decision_df = pd.DataFrame(decisions)
print(decision_df.to_string(index=False))
print()

print("7.3 Summary of Insights")
print("-" * 80)
print("""
Based on our histogram analysis:

NORMAL DISTRIBUTIONS (math_score):
✓ Can proceed with standard statistical analysis
✓ Mean is representative
✓ No special treatment needed

SKEWED DISTRIBUTIONS (study_hours, attendance_pct):
⚠ Use median instead of mean for summaries
⚠ Consider log transformation if using in models
⚠ Be aware of tail behavior

BIMODAL DISTRIBUTIONS (assignment_score):
⚠ TWO distinct groups present (low vs high performers)
→ NEXT STEP: Segment students and analyze separately
→ Investigate what distinguishes the two groups

OUTLIER DISTRIBUTIONS (quiz_score):
⚠ Outliers detected (5 students with scores 20-40)
→ NEXT STEP: Investigate these students individually
→ Were these absences? Incomplete submissions? Data errors?
→ Decide whether to include or exclude from analysis

Histograms have guided us to specific, actionable next steps!
""")
print()

# =============================================================================
# SECTION 8: Practice Exercise
# =============================================================================
print("=" * 80)
print("SECTION 8: Practice Exercise")
print("=" * 80)
print()

print("Exercise: Apply histogram analysis to new data")
print("-" * 80)
print()

# Create new dataset
np.random.seed(789)
sales_data = {
    'product_id': range(1, 81),
    'price': np.concatenate([
        np.random.normal(50, 10, 40),
        np.random.normal(150, 20, 40)
    ]),
    'units_sold': np.random.exponential(20, 80).clip(1, 100),
    'customer_rating': np.random.beta(8, 2, 80) * 5,  # Skewed toward 5
    'discount_pct': np.random.uniform(0, 50, 80)
}

df_sales = pd.DataFrame(sales_data).round(2)

print("New dataset: Product Sales Data")
print("-" * 80)
print(df_sales.head())
print()

print("YOUR TASK:")
print("-" * 80)
print("""
Perform a complete histogram analysis:

1. Create histograms for all numeric columns
2. Identify the shape of each distribution
3. Detect any outliers or unusual patterns
4. Compare distributions across columns
5. Suggest next steps based on visual patterns

SOLUTION:
""")
print()

# Solution
sales_numeric = ['price', 'units_sold', 'customer_rating', 'discount_pct']

# Create histograms
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
axes = axes.ravel()

for idx, col in enumerate(sales_numeric):
    ax = axes[idx]
    df_sales[col].hist(ax=ax, bins=20, edgecolor='black', alpha=0.7, color='coral')
    ax.set_xlabel(col.replace('_', ' ').title(), fontsize=11)
    ax.set_ylabel('Frequency', fontsize=11)
    ax.set_title(f'{col.replace("_", " ").title()}\nMean: {df_sales[col].mean():.1f}, Median: {df_sales[col].median():.1f}',
                 fontsize=11, fontweight='bold')
    ax.axvline(df_sales[col].mean(), color='red', linestyle='--', linewidth=2, alpha=0.7, label='Mean')
    ax.axvline(df_sales[col].median(), color='blue', linestyle='--', linewidth=2, alpha=0.7, label='Median')
    ax.legend(fontsize=9)
    ax.grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.savefig('../outputs/histogram_practice_exercise.png', dpi=100, bbox_inches='tight')
print("✓ Practice exercise saved: outputs/histogram_practice_exercise.png")
plt.close()

print()
print("ANALYSIS RESULTS:")
print("-" * 80)

for col in sales_numeric:
    mean_val = df_sales[col].mean()
    median_val = df_sales[col].median()
    print(f"\n{col}:")
    print(f"  Mean: {mean_val:.2f}, Median: {median_val:.2f}")
    
    if 'price' in col:
        print("  → BIMODAL distribution (two price tiers: budget ~$50, premium ~$150)")
        print("  → Action: Segment products by price category")
    elif 'units_sold' in col:
        print("  → RIGHT-SKEWED (most products sell 10-30 units, few sell 60+)")
        print("  → Action: Use median for typical sales, investigate high sellers")
    elif 'rating' in col:
        print("  → LEFT-SKEWED (most ratings are high, around 4-5 stars)")
        print("  → Action: Ratings are generally positive, focus on low-rated products")
    elif 'discount' in col:
        print("  → UNIFORM (discounts evenly distributed 0-50%)")
        print("  → Action: No clear discount pattern, explore correlation with sales")

print()
print("RECOMMENDED NEXT STEPS:")
print("-" * 80)
print("  1. Segment products into budget vs premium categories (based on price)")
print("  2. Analyze relationship between discount_pct and units_sold")
print("  3. Investigate low-rated products (rating < 3.5)")
print("  4. Identify best-selling products (units_sold > 60)")
print("  5. Check if premium products have higher ratings")
print()

# =============================================================================
# SECTION 9: Best Practices and Common Mistakes
# =============================================================================
print("=" * 80)
print("SECTION 9: Best Practices and Common Mistakes")
print("=" * 80)
print()

print("Best Practices:")
print("-" * 80)
print("""
✓ Always create histograms BEFORE relying on summary statistics
✓ Adjust bin count if the default doesn't reveal patterns clearly
✓ Add mean/median lines to show central tendency
✓ Compare distributions side-by-side when analyzing relationships
✓ Look for shape, spread, outliers, and gaps
✓ Use histograms to decide between mean vs median
✓ Let visual patterns guide your next analytical steps
✓ Save plots with descriptive names for documentation
""")
print()

print("Common Mistakes:")
print("-" * 80)
print("""
✗ Relying only on mean/std without visualizing
✗ Using too few or too many bins (losing detail or adding noise)
✗ Confusing histograms with bar charts
✗ Ignoring skewness and outliers
✗ Not comparing distributions when analyzing relationships
✗ Forgetting to label axes clearly
✗ Drawing conclusions from summary stats without checking shape
✗ Assuming all numeric data is normally distributed
""")
print()

# =============================================================================
# CONCLUSION
# =============================================================================
print("=" * 80)
print("CONCLUSION: Key Takeaways")
print("=" * 80)
print()

print("""
HISTOGRAMS are essential for:
✓ Visualizing how data is distributed
✓ Identifying shape, skewness, and outliers
✓ Deciding between mean vs median
✓ Detecting bimodal or multi-modal patterns
✓ Guiding statistical analysis decisions

REMEMBER:
• Histograms reveal patterns that numbers alone cannot
• Shape determines which statistics and methods to use
• Visual comparison complements statistical comparison
• Outliers and skewness are visible immediately
• Always visualize before assuming normality

MOST IMPORTANTLY:
→ Never rely on summary statistics alone
→ Visualize first, then analyze
→ Let distribution shape guide your methods
→ Histograms are the foundation of good EDA
""")
print()

print("=" * 80)
print("MILESTONE COMPLETE!")
print("=" * 80)
print()
print("You now understand how to:")
print("  ✓ Create histograms for single and multiple columns")
print("  ✓ Interpret distribution shape and spread")
print("  ✓ Identify skewed or uneven distributions")
print("  ✓ Detect potential outliers visually")
print("  ✓ Use histograms to guide further analysis")
print()
print("PLOTS CREATED:")
print("  → outputs/histogram_single_math_score.png")
print("  → outputs/histogram_bin_comparison.png")
print("  → outputs/histogram_distribution_shapes.png")
print("  → outputs/histogram_outliers_comparison.png")
print("  → outputs/histogram_score_comparison.png")
print("  → outputs/histogram_all_columns.png")
print("  → outputs/histogram_practice_exercise.png")
print()
print("NEXT STEPS:")
print("  → Open the saved plots to review patterns")
print("  → Practice with your own datasets")
print("  → Learn box plots for additional outlier detection")
print("  → Explore correlation analysis between columns")
print()
