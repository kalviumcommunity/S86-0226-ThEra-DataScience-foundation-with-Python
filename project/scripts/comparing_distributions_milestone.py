"""
Comparing Distributions Across Multiple Columns Milestone - Pandas Fundamentals
===============================================================================

This script demonstrates the fundamentals of comparing distributions across multiple columns using:
- Summary statistics computation (mean, median, std, min, max)
- describe() for multi-column comparison
- Comparative analysis of central tendency
- Comparative analysis of spread and variability
- Pattern and anomaly identification

Comparing distributions helps you understand how different variables behave relative to each other 
and reveals patterns that single-column analysis cannot show.

This is a key step in Exploratory Data Analysis (EDA) before drawing any insights or conclusions.

Author: Your Name
Date: March 12, 2026
"""

import pandas as pd
import numpy as np

print("=" * 80)
print("COMPARING DISTRIBUTIONS ACROSS MULTIPLE COLUMNS MILESTONE")
print("=" * 80)
print()

# =============================================================================
# INTRODUCTION
# =============================================================================
print("INTRODUCTION: Why Comparing Distributions Matters")
print("-" * 80)
print("""
After loading and inspecting data, comparing distributions is THE NEXT CRITICAL STEP.

Comparing distributions means understanding:
1. How different variables behave relative to each other
2. Which columns have higher or lower central values
3. Which columns vary more or less
4. Unusual patterns that single-column analysis misses

Common beginner issues include:
- Analyzing columns in isolation
- Missing relationships between variables
- Comparing raw values instead of distributions
- Drawing conclusions without context

Most real insights come from comparison, not isolation.

This milestone ensures that:
- You understand how variables differ from each other
- Patterns across columns become visible
- Analysis decisions are more informed
- You avoid misleading conclusions

Think of distribution comparison as putting columns side by side and asking,
"How are these different?"
""")
print()

# =============================================================================
# SECTION 1: Understanding Distributions Across Columns
# =============================================================================
print("=" * 80)
print("SECTION 1: Understanding Distributions Across Columns")
print("=" * 80)
print()

print("1.1 What is a Distribution?")
print("-" * 80)
print("""
A distribution describes how values in a column are spread out.

Key aspects of a distribution:
- Central tendency: Where do most values cluster? (mean, median)
- Spread: How far do values deviate from center? (range, std)
- Shape: Are values symmetric or skewed?
- Outliers: Are there unusual extreme values?

Example intuition:
- Column A: [10, 12, 11, 13, 10] - Low variability, mean ~11
- Column B: [5, 25, 8, 30, 2] - High variability, mean ~14
- Both have different central values AND different spreads

Why comparison matters:
- Context reveals meaning (Is 100 high? Depends on the scale!)
- Patterns emerge across columns (Do related variables move together?)
- Analysis decisions depend on distributions (Should I standardize?)
""")
print()

print("1.2 Creating Sample Data with Multiple Distributions")
print("-" * 80)
print("Creating a dataset with diverse numeric columns for comparison:")
print()

# Create sample data with different distribution characteristics
np.random.seed(42)

# Simulate data with intentionally different distributions
sample_data = {
    'student_id': range(1, 51),
    
    # Test scores - relatively narrow range, high central tendency
    'math_score': np.random.normal(75, 8, 50).clip(50, 100),
    
    # Science scores - similar range but slightly lower mean
    'science_score': np.random.normal(70, 10, 50).clip(40, 100),
    
    # English scores - wider variability
    'english_score': np.random.normal(65, 15, 50).clip(30, 100),
    
    # Attendance percentage - very high values, low variability
    'attendance_pct': np.random.normal(92, 5, 50).clip(75, 100),
    
    # Study hours per week - lower values, moderate variability
    'study_hours': np.random.normal(15, 5, 50).clip(5, 35),
    
    # Assignment completion - percentage with moderate spread
    'assignment_completion': np.random.normal(85, 12, 50).clip(50, 100)
}

df = pd.DataFrame(sample_data)

# Round numeric columns for cleaner display
numeric_cols = ['math_score', 'science_score', 'english_score', 'attendance_pct', 'study_hours', 'assignment_completion']
df[numeric_cols] = df[numeric_cols].round(2)

print("✓ Sample student performance dataset created")
print(f"  - {df.shape[0]} students")
print(f"  - {len(numeric_cols)} numeric measurement columns")
print()

print("First look at the data:")
print("-" * 80)
print(df.head(10))
print()

print("Key observation:")
print("Notice how different columns operate on different scales and ranges.")
print("This is exactly WHY we need to compare distributions, not just raw values.")
print()

# =============================================================================
# SECTION 2: Computing Summary Statistics for Multiple Columns
# =============================================================================
print("=" * 80)
print("SECTION 2: Computing Summary Statistics for Multiple Columns")
print("=" * 80)
print()

print("2.1 Using describe() for Multi-Column Summary")
print("-" * 80)
print("""
The describe() method is the PRIMARY tool for comparing distributions.

What describe() shows for each column:
- count: Number of non-missing values
- mean: Average value (central tendency)
- std: Standard deviation (spread/variability)
- min: Minimum value (lower boundary)
- 25%: First quartile (Q1)
- 50%: Median (middle value)
- 75%: Third quartile (Q3)
- max: Maximum value (upper boundary)

When comparing distributions, focus on:
1. Means - Which columns have higher/lower averages?
2. Standard deviations - Which columns vary more?
3. Ranges (max - min) - Which columns have wider spreads?
4. Medians vs means - Which columns are skewed?
""")
print()

print("Computing summary statistics across all numeric columns:")
print("-" * 80)
summary_stats = df[numeric_cols].describe()
print(summary_stats)
print()

print("INTERPRETATION GUIDE:")
print("-" * 80)
print("""
Read this table COLUMN BY COLUMN, then COMPARE ACROSS columns:

For each column, ask:
- What is the typical value? (mean/median)
- How much do values vary? (std)
- What is the full range? (max - min)
- Is it symmetric? (mean ≈ median) or skewed? (mean ≠ median)

Then COMPARE columns:
- Which has the highest average?
- Which varies the most?
- Which is most consistent?
- Do any columns behave unusually?
""")
print()

# =============================================================================
# SECTION 3: Comparing Central Tendency Across Columns
# =============================================================================
print("=" * 80)
print("SECTION 3: Comparing Central Tendency Across Columns")
print("=" * 80)
print()

print("3.1 Comparing Means")
print("-" * 80)
print("""
Mean (average) is the most common measure of central tendency.
Comparing means tells you which variables tend to be higher or lower.

IMPORTANT: Only compare means when columns measure SIMILAR things.
- Comparing test scores makes sense (same scale)
- Comparing test scores to study hours doesn't (different scales)
""")
print()

print("Mean values for each column:")
print("-" * 80)
means = df[numeric_cols].mean()
print(means)
print()

print("Sorting means from lowest to highest:")
print("-" * 80)
sorted_means = means.sort_values()
print(sorted_means)
print()

print("INTERPRETATION:")
print("-" * 80)
print(f"✓ LOWEST mean: {sorted_means.index[0]} = {sorted_means.iloc[0]:.2f}")
print(f"✓ HIGHEST mean: {sorted_means.index[-1]} = {sorted_means.iloc[-1]:.2f}")
print()
print("Key insights:")
print(f"  - Study hours ({sorted_means['study_hours']:.2f}) has the lowest mean (different scale)")
print(f"  - Among test scores, math_score ({means['math_score']:.2f}) has highest mean")
print(f"  - English_score ({means['english_score']:.2f}) has lowest mean among tests")
print(f"  - Attendance ({means['attendance_pct']:.2f}) is very high (as expected)")
print()

print("3.2 Comparing Medians")
print("-" * 80)
print("""
Median (middle value) is more robust to outliers than mean.
Comparing median to mean reveals skewness in the distribution.

If mean ≈ median: Distribution is roughly symmetric
If mean > median: Distribution is right-skewed (long tail of high values)
If mean < median: Distribution is left-skewed (long tail of low values)
""")
print()

print("Median values for each column:")
print("-" * 80)
medians = df[numeric_cols].median()
print(medians)
print()

print("Comparing Mean vs Median (detecting skewness):")
print("-" * 80)
comparison_df = pd.DataFrame({
    'Mean': means,
    'Median': medians,
    'Difference': means - medians,
    'Skew_Type': ['Symmetric' if abs(m - med) < 1 else 
                  ('Right-skewed' if m > med else 'Left-skewed') 
                  for m, med in zip(means, medians)]
})
print(comparison_df)
print()

print("INTERPRETATION:")
print("-" * 80)
print("""
When mean and median are close, the distribution is roughly balanced.
When they differ significantly, the distribution has a tail pulling the mean away.

Why this matters:
- Symmetric data: Mean is a good summary
- Skewed data: Median may be more representative
- Comparison reveals outlier influence
""")
print()

# =============================================================================
# SECTION 4: Comparing Spread and Variability Across Columns
# =============================================================================
print("=" * 80)
print("SECTION 4: Comparing Spread and Variability Across Columns")
print("=" * 80)
print()

print("4.1 Comparing Standard Deviation")
print("-" * 80)
print("""
Standard deviation measures how spread out values are from the mean.

High std: Values are widely dispersed (high variability)
Low std: Values cluster tightly around the mean (low variability)

Comparing std across columns reveals:
- Which variables are more consistent
- Which variables are more volatile
- Where you might find more or less noise
""")
print()

print("Standard deviation for each column:")
print("-" * 80)
stds = df[numeric_cols].std()
print(stds)
print()

print("Sorting by variability (lowest to highest):")
print("-" * 80)
sorted_stds = stds.sort_values()
print(sorted_stds)
print()

print("INTERPRETATION:")
print("-" * 80)
print(f"✓ MOST CONSISTENT: {sorted_stds.index[0]} (std = {sorted_stds.iloc[0]:.2f})")
print(f"✓ MOST VARIABLE: {sorted_stds.index[-1]} (std = {sorted_stds.iloc[-1]:.2f})")
print()
print("Key insights:")
print(f"  - Attendance has LOW variability (std = {stds['attendance_pct']:.2f}) - students attend consistently")
print(f"  - English scores have HIGH variability (std = {stds['english_score']:.2f}) - performance differs widely")
print(f"  - Math scores have MODERATE variability (std = {stds['math_score']:.2f}) - more consistent performance")
print()
print("Why this matters:")
print("  * Low variability = predictable, stable")
print("  * High variability = diverse outcomes, less predictable")
print("  * Helps decide which variables to focus on in analysis")
print()

print("4.2 Comparing Ranges")
print("-" * 80)
print("""
Range = Maximum - Minimum
Range shows the full span of values in each column.

Wide range: Data covers a broad spectrum
Narrow range: Data is confined to a small interval

Range is simple but informative for quick comparison.
""")
print()

print("Computing range for each column:")
print("-" * 80)
ranges = df[numeric_cols].max() - df[numeric_cols].min()
print(ranges)
print()

print("Comparing full distribution boundaries:")
print("-" * 80)
range_comparison = pd.DataFrame({
    'Min': df[numeric_cols].min(),
    'Max': df[numeric_cols].max(),
    'Range': ranges
})
print(range_comparison)
print()

print("INTERPRETATION:")
print("-" * 80)
print("Range tells you the 'amplitude' of each variable:")
print(f"  - English_score has the widest range ({ranges['english_score']:.2f})")
print(f"  - Attendance has the narrowest range ({ranges['attendance_pct']:.2f})")
print()
print("Why this matters:")
print("  * Wide range may indicate outliers or natural diversity")
print("  * Narrow range may indicate ceiling/floor effects or homogeneity")
print("  * Context matters: A narrow range might be good (attendance) or limiting (test scores)")
print()

print("4.3 Coefficient of Variation (Relative Variability)")
print("-" * 80)
print("""
Coefficient of Variation (CV) = (Standard Deviation / Mean) * 100

CV shows variability RELATIVE to the mean, allowing fair comparison across different scales.

Low CV: Values are consistent relative to average
High CV: Values are highly variable relative to average

Use CV when columns have different scales (e.g., comparing test scores to study hours).
""")
print()

print("Computing Coefficient of Variation:")
print("-" * 80)
cv = (stds / means * 100).sort_values()
print(cv)
print()

print("INTERPRETATION:")
print("-" * 80)
print(f"✓ MOST STABLE (relative to mean): {cv.index[0]} (CV = {cv.iloc[0]:.2f}%)")
print(f"✓ MOST VARIABLE (relative to mean): {cv.index[-1]} (CV = {cv.iloc[-1]:.2f}%)")
print()
print("Why CV matters:")
print("  - Allows fair comparison across different scales")
print(f"  - Study hours has higher CV ({cv['study_hours']:.2f}%) than attendance ({cv['attendance_pct']:.2f}%)")
print("    meaning study hours vary more relative to their typical value")
print()

# =============================================================================
# SECTION 5: Identifying Patterns and Anomalies
# =============================================================================
print("=" * 80)
print("SECTION 5: Identifying Patterns and Anomalies")
print("=" * 80)
print()

print("5.1 Creating a Comprehensive Comparison Table")
print("-" * 80)
print("""
A comparison table consolidates all key statistics in one view.
This is the foundation for pattern detection and anomaly identification.
""")
print()

print("Building comprehensive comparison table:")
print("-" * 80)
comparison_table = pd.DataFrame({
    'Mean': means,
    'Median': medians,
    'Std_Dev': stds,
    'Min': df[numeric_cols].min(),
    'Max': df[numeric_cols].max(),
    'Range': ranges,
    'CV(%)': (stds / means * 100)
}).round(2)

print(comparison_table)
print()

print("5.2 Identifying Interesting Patterns")
print("-" * 80)
print("""
Look for these patterns when comparing distributions:

1. SIMILAR DISTRIBUTIONS: Columns with similar means and spreads
2. CONTRASTING DISTRIBUTIONS: Columns that differ significantly
3. UNUSUAL VARIABILITY: Columns with unexpectedly high/low std
4. SCALE DIFFERENCES: Columns operating on different ranges
5. SKEWNESS PATTERNS: Consistent mean-median differences
""")
print()

print("PATTERN ANALYSIS:")
print("-" * 80)

# Identify test score columns for comparison
test_scores = ['math_score', 'science_score', 'english_score']
print("1. Comparing Test Scores (similar scales):")
print("-" * 80)
print(comparison_table.loc[test_scores])
print()
print("Observations:")
print(f"  ✓ Math has highest mean ({means['math_score']:.2f}), science middle ({means['science_score']:.2f}), english lowest ({means['english_score']:.2f})")
print(f"  ✓ English has highest variability (std={stds['english_score']:.2f}), math most consistent (std={stds['math_score']:.2f})")
print("  ✓ All three have similar ranges (operating on 0-100 scale)")
print()

print("2. Comparing Behavioral Metrics:")
print("-" * 80)
behavioral = ['attendance_pct', 'study_hours', 'assignment_completion']
print(comparison_table.loc[behavioral])
print()
print("Observations:")
print(f"  ✓ Attendance is very high (mean={means['attendance_pct']:.2f}) and consistent (std={stds['attendance_pct']:.2f})")
print(f"  ✓ Study hours operate on different scale (mean={means['study_hours']:.2f}), moderate variability")
print(f"  ✓ Assignment completion similar to test scores (mean={means['assignment_completion']:.2f})")
print()

print("5.3 Detecting Unusual Distributions")
print("-" * 80)
print("""
Unusual distributions warrant further investigation.

Red flags:
- Extremely high or low variability compared to others
- Mean very different from median (strong skew)
- Unexpected ranges or boundaries
- Outliers that significantly affect statistics
""")
print()

print("Anomaly Detection:")
print("-" * 80)

# Identify columns with high CV
high_cv_threshold = 25
high_cv_cols = cv[cv > high_cv_threshold]

if len(high_cv_cols) > 0:
    print(f"Columns with HIGH relative variability (CV > {high_cv_threshold}%):")
    print(high_cv_cols)
    print("  → These columns have high diversity in values")
    print()

# Identify columns with large mean-median difference
mean_median_diff = abs(means - medians)
skewed_threshold = 2
skewed_cols = mean_median_diff[mean_median_diff > skewed_threshold]

if len(skewed_cols) > 0:
    print("Columns with potential skewness (|mean - median| > 2):")
    print(skewed_cols)
    print("  → These distributions may have outliers or asymmetry")
    print()

print("INTERPRETATION:")
print("-" * 80)
print("""
Identifying unusual distributions helps you:
- Focus investigation on interesting variables
- Understand data collection issues
- Make informed decisions about next steps
- Avoid misleading conclusions from averaging skewed data
""")
print()

# =============================================================================
# SECTION 6: Using Comparisons to Guide Analysis
# =============================================================================
print("=" * 80)
print("SECTION 6: Using Comparisons to Guide Analysis")
print("=" * 80)
print()

print("6.1 What Comparisons Tell You About Next Steps")
print("-" * 80)
print("""
Distribution comparisons directly inform analysis decisions:

If columns have SIMILAR distributions:
→ They might be related or measure similar constructs
→ Consider correlation analysis
→ May not need all columns (redundancy)

If columns have DIFFERENT scales:
→ Standardize before comparing (z-scores, normalization)
→ Use relative measures (percentiles, CV)
→ Be careful with direct aggregation

If columns have HIGH variability:
→ Check for outliers or data quality issues
→ Consider what drives the variation
→ May need segmentation or grouping

If columns are SKEWED:
→ Use median instead of mean
→ Consider transformations (log, sqrt)
→ Be cautious with parametric statistics
""")
print()

print("6.2 Summary of Key Findings")
print("-" * 80)
print("Based on our distribution comparison:")
print()
print("CENTRAL TENDENCY:")
print(f"  • Test scores range from {means['english_score']:.1f} (English) to {means['math_score']:.1f} (Math)")
print(f"  • Attendance is consistently high: {means['attendance_pct']:.1f}%")
print(f"  • Average study time: {means['study_hours']:.1f} hours/week")
print()
print("VARIABILITY:")
print(f"  • Most consistent: Attendance (std={stds['attendance_pct']:.2f})")
print(f"  • Most variable: English scores (std={stds['english_score']:.2f})")
print(f"  • All test scores show different levels of variability")
print()
print("PATTERNS:")
print("  • Test scores operate on similar scales (0-100)")
print("  • Study hours on different scale, requires relative comparison")
print("  • No extreme skewness detected")
print()
print("NEXT STEPS:")
print("  • Investigate why English scores vary more than other subjects")
print("  • Explore relationship between study hours and test scores")
print("  • Analyze whether attendance correlates with performance")
print("  • Consider student segmentation based on performance patterns")
print()

# =============================================================================
# SECTION 7: Practice Exercise
# =============================================================================
print("=" * 80)
print("SECTION 7: Practice Exercise")
print("=" * 80)
print()

print("Exercise: Apply distribution comparison to new data")
print("-" * 80)
print()

# Create new dataset with different characteristics
np.random.seed(123)
sales_data = {
    'product_id': range(1, 31),
    'price': np.random.uniform(10, 200, 30),
    'cost': np.random.uniform(5, 150, 30),
    'units_sold': np.random.randint(50, 500, 30),
    'customer_rating': np.random.uniform(3.0, 5.0, 30),
    'discount_pct': np.random.uniform(0, 30, 30)
}

df_sales = pd.DataFrame(sales_data)
df_sales = df_sales.round(2)

print("New dataset: Product Sales Data")
print("-" * 80)
print(df_sales.head())
print()

print("YOUR TASK:")
print("-" * 80)
print("""
Perform a complete distribution comparison analysis:

1. Compute summary statistics for all numeric columns
2. Compare central tendency (means and medians)
3. Compare variability (std dev and ranges)
4. Identify any unusual patterns or anomalies
5. Suggest next steps based on your findings

SOLUTION:
""")
print()

# Solution
print("1. Summary Statistics:")
print("-" * 80)
sales_numeric = ['price', 'cost', 'units_sold', 'customer_rating', 'discount_pct']
print(df_sales[sales_numeric].describe())
print()

print("2. Central Tendency Comparison:")
print("-" * 80)
sales_means = df_sales[sales_numeric].mean()
sales_medians = df_sales[sales_numeric].median()
print(pd.DataFrame({'Mean': sales_means, 'Median': sales_medians}))
print()

print("3. Variability Comparison:")
print("-" * 80)
sales_stds = df_sales[sales_numeric].std()
sales_ranges = df_sales[sales_numeric].max() - df_sales[sales_numeric].min()
print(pd.DataFrame({'Std_Dev': sales_stds, 'Range': sales_ranges}))
print()

print("4. Key Observations:")
print("-" * 80)
print("  • Units_sold operates on much larger scale than other metrics")
print("  • Customer_rating has narrow range (3.0-5.0) as expected for ratings")
print("  • Price and cost have wide ranges, suggesting diverse product mix")
print("  • Discount percentages vary substantially")
print()

print("5. Suggested Next Steps:")
print("-" * 80)
print("  • Calculate profit margin (price - cost) and compare")
print("  • Analyze relationship between discount and units_sold")
print("  • Investigate if customer_rating relates to sales volume")
print("  • Segment products by price range for targeted analysis")
print()

# =============================================================================
# CONCLUSION
# =============================================================================
print("=" * 80)
print("CONCLUSION: Key Takeaways")
print("=" * 80)
print()

print("""
DISTRIBUTIONAL COMPARISON is essential for:
✓ Understanding how variables differ from each other
✓ Identifying patterns and anomalies across columns
✓ Making informed analysis decisions
✓ Adding context to single-column statistics

REMEMBER:
• Compare central tendency (mean, median) to understand typical values
• Compare spread (std, range) to understand variability
• Use relative measures (CV) when scales differ
• Look for patterns, not just individual numbers
• Let comparisons guide your next analytical steps

MOST IMPORTANTLY:
→ Always compare distributions before drawing conclusions
→ Context from comparison prevents misleading insights
→ Multi-column thinking reveals relationships
→ Distribution analysis is the foundation of good EDA
""")
print()

print("=" * 80)
print("MILESTONE COMPLETE!")
print("=" * 80)
print()
print("You now understand how to:")
print("  ✓ Compute summary statistics for multiple columns")
print("  ✓ Compare means, medians, and ranges across columns")
print("  ✓ Identify columns with higher or lower variability")
print("  ✓ Detect unusual distributions conceptually")
print("  ✓ Use comparisons to guide deeper analysis")
print()
print("NEXT STEPS:")
print("  → Practice with your own datasets")
print("  → Try comparing distributions in different domains")
print("  → Learn correlation analysis to quantify relationships")
print("  → Explore visualization for distribution comparison")
print()
