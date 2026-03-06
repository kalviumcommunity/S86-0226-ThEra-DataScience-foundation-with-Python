# DataFrame Inspection Milestone - README

## 🔍 Inspecting Pandas DataFrames with head(), info(), and describe()

This milestone teaches the critical skill of DataFrame inspection—the most important step after loading data. Before any cleaning, transformation, or analysis, you must understand what your data looks like, how it's structured, and what the numbers mean.

---

## 📁 Files Created

### 1. **Main Script**
[`scripts/dataframe_inspection_milestone.py`](scripts/dataframe_inspection_milestone.py)

**Comprehensive demonstration of:**
- Why inspection matters
- Using head() for visual previews
- Using info() for structural understanding
- Using describe() for statistical summaries
- When to use each method
- Best practices and common mistakes
- Complete inspection workflow

**To run:**
```bash
cd project/scripts
python dataframe_inspection_milestone.py
```

### 2. **Completion Documentation**
[`INSPECTION_MILESTONE_COMPLETION.md`](INSPECTION_MILESTONE_COMPLETION.md)

**Detailed documentation including:**
- All learning objectives achieved
- Method-by-method breakdown
- Interpretation guides
- Verification checklist
- Real-world applications
- Skills demonstrated

### 3. **Video Walkthrough Guide**
[`VIDEO_WALKTHROUGH_INSPECTION.md`](VIDEO_WALKTHROUGH_INSPECTION.md)

**Complete guide for your 2-minute video:**
- Detailed timeline and script
- What to show and say for each method
- Technical setup checklist
- Interpretation tips
- Recording best practices
- Submission instructions

---

## 🎯 Learning Objectives

### ✅ What You Will Master

1. **Using head() for Previews**
   - View first/last rows of data
   - Verify data loaded correctly
   - Check column names and values
   - Understand data format

2. **Using info() for Structure**
   - Identify data types
   - Find missing values
   - Check row/column counts
   - Understand memory usage

3. **Using describe() for Statistics**
   - Get summary statistics
   - Understand distributions
   - Spot outliers
   - Check value ranges

4. **Building Inspection Habits**
   - Know when to use each method
   - Follow systematic workflow
   - Combine methods effectively
   - Inspect before analyzing

---

## 🚀 Quick Start

### Prerequisites
```python
# Ensure pandas is installed
pip install pandas numpy
```

### Basic Inspection Workflow
```python
import pandas as pd

# 1. Load data
df = pd.read_csv('data.csv')

# 2. Visual preview
df.head()        # First 5 rows
df.tail()        # Last 5 rows

# 3. Structural check
df.info()        # Data types, missing values

# 4. Statistical summary
df.describe()    # Numeric statistics
```

### The Three Essential Questions
| Question | Method | Purpose |
|----------|--------|---------|
| What does it look like? | `head()` | Visual preview |
| How is it structured? | `info()` | Types and missing values |
| What do the numbers mean? | `describe()` | Statistical summary |

---

## 📊 Method Reference Guide

### head() - Visual Preview

**Purpose:** See actual data rows

**Usage:**
```python
df.head()       # First 5 rows (default)
df.head(10)     # First 10 rows
df.head(3)      # First 3 rows
df.tail()       # Last 5 rows
```

**What It Reveals:**
- Column names in context
- Sample values and formats
- Missing values (NaN)
- Data alignment

**When to Use:**
- First look at data
- Verify loading
- Check column names
- See value formats

---

### info() - Structure Check

**Purpose:** Understand DataFrame structure

**Usage:**
```python
df.info()                    # Standard info
df.info(verbose=True)        # Detailed info
df.info(memory_usage='deep') # Detailed memory usage
```

**What It Reveals:**
- Total rows and columns
- Column data types (dtype)
- Non-null counts (missing values)
- Memory usage
- Index information

**Key Dtypes:**
- `int64` - Integer numbers
- `float64` - Decimal numbers
- `object` - Text/strings or mixed
- `bool` - True/False values
- `datetime64` - Dates and times

**When to Use:**
- Check data types
- Find missing values
- Verify column count
- Identify type issues

---

### describe() - Statistical Summary

**Purpose:** Summarize numeric columns

**Usage:**
```python
df.describe()                # Numeric columns only
df.describe(include='all')   # All columns
df['column'].describe()      # Single column
```

**Statistics Provided:**
- `count` - Non-missing values
- `mean` - Average value
- `std` - Standard deviation
- `min` - Minimum value
- `25%` - First quartile
- `50%` - Median (middle value)
- `75%` - Third quartile
- `max` - Maximum value

**What It Reveals:**
- Value distributions
- Outliers (extreme min/max)
- Data spread (std)
- Missing values (count)

**When to Use:**
- Understand numeric distributions
- Check value ranges
- Spot outliers
- Verify data reasonableness

---

## 💡 Interpretation Guide

### Reading info() Output

```python
df.info()

# Output interpretation:
# RangeIndex: 20 entries, 0 to 19    → 20 rows total
# Data columns (total 8 columns):    → 8 columns total
#
# Column      Non-Null Count  Dtype  
# age         20 non-null     int64  → Complete, no missing
# score       20 non-null     int64  → Complete, no missing  
# notes       15 non-null     object → 5 missing values!
```

**Key Insight:** If Non-Null Count < Total Rows → Missing values exist

### Reading describe() Output

```python
df['age'].describe()

# Output interpretation:
# count    20.0    → 20 non-missing values
# mean     21.5    → Average age is 21.5
# std       2.1    → Most ages within ±2.1 of mean
# min      18.0    → Youngest is 18
# 25%      20.0    → 25% are under 20
# 50%      21.5    → Median (middle value) is 21.5
# 75%      23.0    → 75% are under 23
# max      24.0    → Oldest is 24
```

**Distribution Clues:**
- If `mean ≈ 50%` → Symmetric distribution
- If `mean >> 50%` → Right-skewed (outliers pull mean up)
- If `mean << 50%` → Left-skewed (outliers pull mean down)

---

## 🔧 Common Use Cases

### Use Case 1: First Look at New Dataset
```python
# Quick 3-step inspection
df.head()        # What's in here?
df.info()        # What types? Any missing?
df.describe()    # What are the numbers like?
```

### Use Case 2: Check for Missing Values
```python
df.info()  # Look at Non-Null Count column
# If Non-Null Count < total rows → missing values
```

### Use Case 3: Verify Data Types
```python
df.info()  # Check Dtype column
# Numbers should be int64/float64, not object
# Dates should be datetime64, not object
```

### Use Case 4: Detect Outliers
```python
df.describe()  # Check min/max values
# If min/max seem extreme → investigate outliers
```

### Use Case 5: Understand Column Contents
```python
df.head(20)  # See more samples
# Get better sense of what each column represents
```

---

## ⚠️ Common Issues and Solutions

| Issue | Detection | Solution |
|-------|-----------|----------|
| **Wrong data type** | `info()` shows 'object' for numbers | Convert with `astype()` or reload with `dtype` |
| **Missing values** | Non-null count < total in `info()` | Handle with dropna(), fillna(), or imputation |
| **Outliers** | Extreme min/max in `describe()` | Investigate, transform, or remove |
| **All values same** | `std = 0` in `describe()` | Check data quality or remove constant column |
| **Impossible values** | Negative age/price in `describe()` | Clean or investigate data source |
| **Mixed types in column** | `object` dtype with expected numbers | Clean and convert to proper type |

---

## 📋 Inspection Checklist

### After Using head()
- [ ] Column names are correct
- [ ] Sample values look reasonable
- [ ] Data appears aligned (values in right columns)
- [ ] Format of values understood
- [ ] No obvious visual errors

### After Using info()
- [ ] Row count matches expectations
- [ ] Column count matches expectations
- [ ] All data types are appropriate
- [ ] Missing values identified
- [ ] No unexpected 'object' types for numeric columns

### After Using describe()
- [ ] Value ranges make sense
- [ ] No impossible values (negative ages, etc.)
- [ ] Means and medians are reasonable
- [ ] Min/max are plausible
- [ ] Outliers noted (if any)

### Overall
- [ ] Understand the structure
- [ ] Know what cleaning is needed
- [ ] Ready to proceed with confidence

---

## 🎥 Video Walkthrough (~ 2 Minutes)

### What to Include

**1. Introduction (20 sec)**
- Why inspection is critical
- Three methods overview

**2. head() Demo (30 sec)**
- Execute `df.head()`
- Explain what you see
- Point out column names and values

**3. info() Demo (30 sec)**
- Execute `df.info()`
- Highlight row/column count
- Point out data types
- Mention non-null counts

**4. describe() Demo (30 sec)**
- Execute `df.describe()`
- Interpret statistics
- Mention what they reveal

**5. Conclusion (10 sec)**
- Recap three methods
- Emphasize using together

**See [`VIDEO_WALKTHROUGH_INSPECTION.md`](VIDEO_WALKTHROUGH_INSPECTION.md) for complete guide.**

---

## 💻 Code Examples

### Example 1: Complete Inspection
```python
import pandas as pd

# Load data
df = pd.read_csv('data/raw/example_raw.csv')

print("=" * 50)
print("VISUAL PREVIEW")
print("=" * 50)
print(df.head())

print("\n" + "=" * 50)
print("STRUCTURAL CHECK")
print("=" * 50)
df.info()

print("\n" + "=" * 50)
print("STATISTICAL SUMMARY")
print("=" * 50)
print(df.describe())
```

### Example 2: Check for Missing Values
```python
# Method 1: Using info()
df.info()  # Look at Non-Null Count

# Method 2: Count missing per column
print(df.isnull().sum())

# Method 3: Show percentage missing
print((df.isnull().sum() / len(df)) * 100)
```

### Example 3: Inspect Specific Columns
```python
# Single column statistics
print(df['age'].describe())

# Multiple columns
print(df[['age', 'score']].describe())

# Non-numeric column info
print(df['grade'].value_counts())
```

---

## 🎓 Best Practices

### DO ✅
- **Always inspect after loading** - Make it automatic
- **Use all three methods** - Each reveals different information
- **Interpret the output** - Don't just run commands
- **Check for anomalies** - Look for weird values
- **Document findings** - Note issues for cleaning
- **Compare head() and tail()** - Check data consistency

### DON'T ❌
- **Skip inspection** - Never analyze without inspecting
- **Use only head()** - It's not enough alone
- **Ignore data types** - Wrong types cause errors
- **Overlook missing values** - They affect analysis
- **Assume ranges are correct** - Verify with describe()
- **Forget to check the end** - Issues hide at the tail

---

## 🌟 Why This Matters

### In Real Projects
- **Prevents Silent Errors** - Catches issues before they propagate
- **Saves Time** - Early detection vs debugging later
- **Informs Decisions** - Know what cleaning is needed
- **Builds Confidence** - Understand your data deeply
- **Professional Standard** - Expected in industry

### Common Scenarios
1. **Data Science Interview** - "Walk me through this dataset"
2. **Team Collaboration** - "Here's what we're working with"
3. **Project Planning** - "What preprocessing do we need?"
4. **Quality Assurance** - "Is this data reliable?"
5. **Documentation** - "Dataset characteristics are..."

---

## 📚 Quick Reference Card

```python
# === INSPECTION CHEAT SHEET ===

# Visual Preview
df.head()           # First 5 rows
df.head(n)          # First n rows
df.tail()           # Last 5 rows
df.sample(n)        # Random n rows

# Structure
df.info()           # Types, missing values
df.shape            # (rows, columns)
df.columns          # Column names
df.dtypes           # Data types
df.index            # Index info

# Statistics
df.describe()       # Numeric summary
df.describe(include='all')  # All columns
df['col'].describe()        # Single column

# Missing Values
df.isnull().sum()   # Count missing per column
df.info()           # Non-Null Count shows missing

# Unique Values
df['col'].unique()  # All unique values
df['col'].nunique() # Count of unique values
df['col'].value_counts()  # Frequency of values
```

---

## 🎯 Learning Outcomes

After completing this milestone, you will:

- ✅ Use `head()` to preview DataFrame contents
- ✅ Use `info()` to understand structure and data types
- ✅ Use `describe()` to summarize numeric data
- ✅ Detect data issues early (types, missing, outliers)
- ✅ Follow systematic inspection workflow
- ✅ Interpret inspection outputs confidently
- ✅ Build strong data inspection habits

---

## 📝 Submission Checklist

- [ ] Run `dataframe_inspection_milestone.py` successfully
- [ ] Review `INSPECTION_MILESTONE_COMPLETION.md`
- [ ] Record 2-minute video following guide
- [ ] Video demonstrates all three methods
- [ ] Video explains what each reveals
- [ ] Video is screen-facing and clearly visible
- [ ] Audio is clear and understandable
- [ ] Submit video link as instructed
- [ ] Submit Pull Request (if required)

---

## 🔥 Pro Tips

### Efficiency Tips
- **Combine methods**: Run head(), info(), describe() in sequence
- **Use notebooks**: Jupyter makes inspection interactive
- **Save outputs**: Document findings for reference
- **Create functions**: Wrap inspection workflow for reuse

### Advanced Techniques
```python
# Quick full inspection
def inspect_df(df):
    print("Shape:", df.shape)
    print("\nPreview:")
    print(df.head())
    print("\nInfo:")
    df.info()
    print("\nStatistics:")
    print(df.describe())
    print("\nMissing Values:")
    print(df.isnull().sum())
    
# Use it
inspect_df(df)
```

---

## 🎬 Next Steps

### Immediate Practice
1. Load different datasets
2. Practice all three methods
3. Interpret outputs
4. Identify issues
5. Document observations

### Continue Learning
- Data cleaning based on inspection findings
- Handling missing values
- Converting data types
- Outlier treatment
- Advanced inspection techniques

---

## 📖 Additional Resources

### Official Documentation
- [pandas.DataFrame.head](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.head.html)
- [pandas.DataFrame.info](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.info.html)
- [pandas.DataFrame.describe](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html)

### Related Topics
- Missing value analysis
- Data type conversions
- Outlier detection
- Data quality assessment

---

## ❓ FAQ

**Q: Do I always need to use all three methods?**  
A: Yes! Each reveals different critical information. Together they give complete picture.

**Q: What if describe() shows nothing?**  
A: You might have no numeric columns. Use `describe(include='all')` for all columns.

**Q: How do I know if my data types are correct?**  
A: Check with info(). Numbers should be int64/float64, dates should be datetime64.

**Q: Can I use these on large datasets?**  
A: Yes! These methods are fast even on large DataFrames. They're optimized for performance.

**Q: What's the difference between count in describe() and non-null in info()?**  
A: They show the same thing—number of non-missing values. Both help identify missing data.

---

## 🏁 Conclusion

DataFrame inspection with `head()`, `info()`, and `describe()` is non-negotiable. These three methods provide a fast, complete snapshot of any dataset.

**Remember the Three Questions:**
1. **What does it look like?** → `head()`
2. **How is it structured?** → `info()`
3. **What do the numbers mean?** → `describe()`

Make inspection automatic. Every time you load data, inspect it. This habit will save you countless hours and prevent numerous errors throughout your Data Science career.

---

**Milestone Status:** ✅ **READY FOR COMPLETION**

**Next Action:** Run the script, record your video, and submit!

---

*"Inspecting data is like reading the manual before assembling furniture—essential and enlightening."*
