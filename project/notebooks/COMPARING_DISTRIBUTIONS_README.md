# Comparing Distributions Across Multiple Columns - Milestone Documentation

## Overview

This milestone focuses on **comparing distributions across multiple columns** in a Pandas DataFrame. This is a critical step in Exploratory Data Analysis (EDA) that helps you understand how different variables behave relative to each other and reveals patterns that single-column analysis cannot show.

## Learning Objectives

By completing this milestone, you will be able to:

1. ✓ Compute summary statistics for multiple columns
2. ✓ Compare means, medians, and ranges across columns
3. ✓ Identify columns with higher or lower variability
4. ✓ Detect unusual distributions conceptually
5. ✓ Use comparisons to guide deeper analysis

## Why This Matters

### Common Beginner Issues:
- Analyzing columns in isolation
- Missing relationships between variables
- Comparing raw values instead of distributions
- Drawing conclusions without context

### Key Insight:
**Most real insights come from comparison, not isolation.**

This milestone ensures that:
- You understand how variables differ from each other
- Patterns across columns become visible
- Analysis decisions are more informed
- You avoid misleading conclusions

## Files Included

### 1. Python Script: `comparing_distributions_milestone.py`
**Location:** `project/scripts/comparing_distributions_milestone.py`

A comprehensive, self-contained Python script with:
- Detailed explanations of distribution concepts
- Sample dataset creation (student performance data)
- Step-by-step comparisons with interpretations
- Practice exercise with solutions
- 700+ lines of educational content

**Run the script:**
```bash
cd project/scripts
python comparing_distributions_milestone.py
```

### 2. Jupyter Notebook: `comparing_distributions_milestone.ipynb`
**Location:** `project/notebooks/comparing_distributions_milestone.ipynb`

An interactive notebook with:
- Same content as Python script but in notebook format
- Code cells for experimentation
- Practice exercises with TODO sections
- Markdown explanations for better readability

**Open in Jupyter:**
```bash
cd project/notebooks
jupyter notebook comparing_distributions_milestone.ipynb
```

## What You Will Learn

### Section 1: Understanding Distributions Across Columns
- What a distribution represents
- Why comparison adds context
- How to build a comparative mindset

### Section 2: Computing Summary Statistics
- Using `describe()` for multi-column analysis
- Interpreting count, mean, std, min, quartiles, max
- Reading statistics tables effectively

### Section 3: Comparing Central Tendency
- **Comparing Means**: Which variables tend higher/lower
- **Comparing Medians**: Detecting skewness and outlier effects
- **Mean vs Median**: Understanding distribution symmetry

### Section 4: Comparing Spread and Variability
- **Standard Deviation**: Measuring consistency across columns
- **Ranges**: Understanding full span of values
- **Coefficient of Variation (CV)**: Relative variability for different scales

### Section 5: Identifying Patterns and Anomalies
- Creating comprehensive comparison tables
- Detecting similar vs contrasting distributions
- Identifying unusual variability
- Recognizing scale differences

### Section 6: Using Comparisons to Guide Analysis
- How distributions inform next steps
- When to standardize data
- When to use median vs mean
- Decision-making based on patterns

## Key Concepts Explained

### 1. Distribution Components
```
Distribution = Central Tendency + Spread + Shape + Outliers

- Central Tendency: mean, median (where values cluster)
- Spread: std, range (how far values deviate)
- Shape: symmetric vs skewed
- Outliers: unusual extreme values
```

### 2. Why Compare Distributions?
```
Context Reveals Meaning:
- Is 100 high? Depends on the scale!
- Does a column vary a lot? Compared to what?
- Is the mean representative? Check the spread!
```

### 3. Statistical Measures Used

| Measure | Purpose | Interpretation |
|---------|---------|----------------|
| **Mean** | Average value | Typical value (affected by outliers) |
| **Median** | Middle value | Typical value (robust to outliers) |
| **Std Dev** | Variability | How spread out values are |
| **Range** | Full span | Maximum - Minimum |
| **CV** | Relative variability | (Std/Mean) × 100, for comparing different scales |

## Sample Dataset

The milestone uses a **student performance dataset** with intentionally different distributions:

| Column | Scale | Mean | Std Dev | Characteristics |
|--------|-------|------|---------|-----------------|
| `math_score` | 0-100 | ~75 | ~8 | High mean, low variability |
| `science_score` | 0-100 | ~70 | ~10 | Moderate mean and variability |
| `english_score` | 0-100 | ~65 | ~15 | Lower mean, high variability |
| `attendance_pct` | 0-100 | ~92 | ~5 | Very high, very consistent |
| `study_hours` | 0-35 | ~15 | ~5 | Different scale, moderate variability |
| `assignment_completion` | 0-100 | ~85 | ~12 | Moderate mean and variability |

This diversity allows you to practice meaningful comparisons across different contexts.

## Expected Outcomes

After completing this milestone, you should be able to:

### ✓ Computational Skills
- Use `df.describe()` to get multi-column summaries
- Calculate means, medians, std dev for comparison
- Compute ranges and coefficient of variation
- Create comprehensive comparison tables

### ✓ Analytical Skills
- Identify which columns have higher/lower central values
- Determine which columns are more consistent or variable
- Detect skewness by comparing mean vs median
- Spot unusual distributions that warrant investigation

### ✓ Decision-Making Skills
- Know when to standardize data
- Choose appropriate summary statistics (mean vs median)
- Identify which variables to focus on
- Formulate data-driven questions for deeper analysis

## Practice Exercise

The milestone includes a practice exercise with a **product sales dataset**:
- Price and cost data
- Units sold
- Customer ratings
- Discount percentages

You'll perform a complete distribution comparison analysis and suggest next analytical steps.

## Common Patterns to Look For

### 1. Similar Distributions
```python
# Example: Two test scores with similar stats
math_score:    mean=75, std=8
science_score: mean=73, std=9

→ Might measure similar constructs
→ Consider correlation analysis
→ Possible redundancy
```

### 2. Different Scales
```python
# Example: Test scores vs study hours
test_score:  mean=75,  std=10,  CV=13%
study_hours: mean=15,  std=5,   CV=33%

→ Can't compare raw values directly
→ Use CV for relative comparison
→ Standardize if combining
```

### 3. High Variability
```python
# Example: English scores vary widely
english_score: std=15 (high)
math_score:    std=8  (low)

→ English performance more diverse
→ Investigate drivers of variation
→ May need segmentation
```

### 4. Skewed Distributions
```python
# Example: Mean ≠ Median
column_A: mean=50, median=45  (right-skewed)
column_B: mean=70, median=70  (symmetric)

→ Column_A has outliers pulling mean up
→ Median more representative for Column_A
→ Be careful with parametric statistics
```

## Tips for Success

### Do's ✓
- Compare statistics across columns, not just raw values
- Use describe() as your starting point
- Calculate CV when comparing different scales
- Look for patterns, not just individual numbers
- Let comparisons raise questions for investigation

### Don'ts ✗
- Don't compare columns in isolation
- Don't assume "higher is better" without context
- Don't ignore scale differences
- Don't draw conclusions from means alone (check spread!)
- Don't forget to check for skewness

## Integration with Other Milestones

This milestone builds on:
- **DataFrame Inspection Milestone**: Using `describe()` basics
- **Missing Values Detection**: Understanding data completeness
- **Selecting Rows and Columns**: Subsetting for comparisons

This milestone prepares you for:
- **Correlation Analysis**: Quantifying relationships
- **Data Visualization**: Visual distribution comparison
- **Feature Engineering**: Creating new variables based on patterns
- **Statistical Testing**: Hypothesis testing across groups

## Notes for Instructors

### Teaching Emphasis:
1. **Comparative Thinking**: Always ask "compared to what?"
2. **Context Matters**: Numbers mean little without comparison
3. **Pattern Detection**: Look beyond individual statistics
4. **Informed Decisions**: Let data guide next steps

### Common Student Mistakes:
- Focusing on one column at a time
- Forgetting about scale differences
- Ignoring variability (only looking at means)
- Not checking mean vs median

### Assessment Ideas:
- Give students a new dataset and ask for distribution comparison
- Ask them to identify which column is most/least variable
- Request interpretation of CV differences
- Have them suggest analysis next steps based on patterns

## Additional Resources

### Further Reading:
- Pandas documentation: `DataFrame.describe()`
- Statistics review: Measures of central tendency and spread
- Coefficient of variation: When and why to use it
- Skewness and kurtosis: Understanding distribution shape

### Next Steps:
- Practice with real-world datasets
- Learn visualization techniques (histograms, box plots)
- Study correlation and covariance
- Explore statistical hypothesis testing

## Summary

This milestone teaches you to:
- **Compare**, not just compute
- **Interpret** statistics in context
- **Detect** patterns across variables
- **Guide** analysis based on distributions

Remember: **Most insights come from comparison, not isolation.**

---

**Author:** Data Science Foundation with Python  
**Date:** March 12, 2026  
**Difficulty:** Intermediate  
**Prerequisites:** DataFrame basics, `describe()` method, basic statistics  
**Estimated Time:** 1-2 hours
