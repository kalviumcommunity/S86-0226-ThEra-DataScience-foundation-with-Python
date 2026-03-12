# Visualizing Data Distributions Using Boxplots - Milestone

## 📊 Overview

This milestone focuses on visualizing data distributions using boxplots. Boxplots provide a compact summary of a dataset's distribution, making it easy to compare spread, central tendency, and potential outliers across one or more numeric columns.

**Boxplots complement histograms** by highlighting quartiles and outliers clearly.

## 🎯 Learning Objectives

By completing this milestone, you will be able to:

- ✓ **Understand** what a boxplot represents
- ✓ **Visualize** distribution spread using quartiles
- ✓ **Identify** median and interquartile range (IQR)
- ✓ **Detect** potential outliers visually
- ✓ **Compare** distributions across multiple columns
- ✓ **Create** boxplots for numeric columns
- ✓ **Interpret** median, quartiles, and range
- ✓ **Use** boxplots as part of EDA (Exploratory Data Analysis)

## 💡 Why This Matters

Common beginner issues include:
- ❌ Missing outliers when relying only on averages
- ❌ Difficulty comparing distributions across columns
- ❌ Over-reliance on histograms for all insights
- ❌ Misinterpreting spread and variability

**Boxplots summarize distributions clearly and comparably.**

This milestone ensures that:
- ✅ You can spot outliers quickly
- ✅ Distribution spread is easy to compare
- ✅ Central tendency is clearly visible
- ✅ EDA decisions are more informed

> **Think of boxplots as a side-by-side comparison tool for distributions.**

---

## 📚 Understanding Boxplots

### Components of a Boxplot

A boxplot consists of several key components:

#### 1. **The Box (Interquartile Range - IQR)**
- **Bottom edge**: Q1 (25th percentile)
- **Top edge**: Q3 (75th percentile)
- **Box height**: IQR = Q3 - Q1 (middle 50% of data)

#### 2. **The Median Line**
- Line inside the box
- Shows the middle value (50th percentile)
- **Different from mean** (average)

#### 3. **The Whiskers**
- Extend from box to 1.5 × IQR
- **Lower whisker**: Q1 - 1.5 × IQR (but not below minimum data point)
- **Upper whisker**: Q3 + 1.5 × IQR (but not above maximum data point)

#### 4. **Outliers**
- Individual points beyond whiskers
- Potential anomalies or extreme values
- **NOT always errors - need context!**

### Visual Representation

```
    Maximum (within 1.5*IQR)
           ↓
    ───────┬───────
           │
    ┌──────┴──────┐
    │             │  ← Q3 (75th percentile)
    │      ─      │  ← Median (50th percentile)
    │             │
    └──────┬──────┘  ← Q1 (25th percentile)
           │
    ───────┴───────
           ↑
    Minimum (within 1.5*IQR)

    ● ● = Outliers
```

---

## 🚀 Getting Started

### Prerequisites

Ensure you have the following libraries installed:

```bash
pip install pandas numpy matplotlib seaborn
```

### Files Provided

1. **`visualizing_boxplots_milestone.py`** - Python script with complete examples
2. **`visualizing_boxplots_milestone.ipynb`** - Jupyter notebook (interactive)
3. **`VISUALIZING_BOXPLOTS_README.md`** - This file

---

## 📖 What You Are Expected to Do

This is a **data visualization milestone**, not a modeling task.

You are expected to:

### 1. Understanding Boxplots
- ✓ Understand median, quartiles, and IQR
- ✓ Recognize whiskers and their meaning
- ✓ Identify outliers visually
- ✓ Avoid confusing boxplots with bar charts

**Each component conveys key information.**

### 2. Creating a Boxplot for a Single Column
- ✓ Select a numeric column
- ✓ Create a boxplot
- ✓ Identify median and spread
- ✓ Note any visible outliers

**Single-column boxplots build intuition.**

### 3. Comparing Boxplots Across Columns
- ✓ Create boxplots for multiple columns
- ✓ Compare medians and variability
- ✓ Identify columns with wider spread
- ✓ Spot columns with more outliers

**Comparison is a major strength of boxplots.**

### 4. Interpreting Outliers Carefully
- ✓ Identify points beyond whiskers
- ✓ Understand that outliers are not always errors
- ✓ Avoid removing outliers blindly
- ✓ Use boxplots to ask better questions

**Outliers need context, not assumptions.**

---

## 💻 Running the Code

### Option 1: Python Script

```bash
cd project/scripts
python visualizing_boxplots_milestone.py
```

The script will:
- Create sample data with intentional outliers
- Generate multiple boxplot visualizations
- Save plots to `project/outputs/` folder
- Display comprehensive explanations

### Option 2: Jupyter Notebook (Recommended)

```bash
cd project/notebooks
jupyter notebook visualizing_boxplots_milestone.ipynb
```

The notebook provides:
- Interactive cells you can modify
- Step-by-step explanations
- Practice exercises
- Visual output inline

---

## 📊 Key Concepts Covered

### 1. Single Column Boxplot
```python
import matplotlib.pyplot as plt

plt.boxplot(df['Age'], patch_artist=True)
plt.ylabel('Age')
plt.title('Age Distribution')
plt.show()
```

### 2. Multiple Column Comparison
```python
df[['Age', 'Income', 'Experience']].boxplot(figsize=(12, 6))
plt.show()
```

### 3. Outlier Detection
```python
q1 = df['Income'].quantile(0.25)
q3 = df['Income'].quantile(0.75)
iqr = q3 - q1
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

outliers = df[(df['Income'] < lower_bound) | (df['Income'] > upper_bound)]
```

### 4. Using Seaborn
```python
import seaborn as sns

sns.boxplot(data=df, y='Salary', palette='Set2')
plt.show()
```

---

## 🔍 Interpreting Outliers

### Types of Outliers

#### 1. **Data Entry Errors**
- Typos (e.g., age = 150 instead of 15)
- Wrong units (e.g., meters vs. centimeters)
- **Action**: Verify and correct if confirmed as errors

#### 2. **Genuine Extreme Values**
- High earners in income data
- Athletes in physical performance data
- **Action**: Keep them! They represent real phenomena

#### 3. **Different Populations**
- Part-time vs. full-time workers
- Different age groups mixed together
- **Action**: Consider separate analysis or grouping

#### 4. **Measurement Errors**
- Instrument malfunction
- Recording mistakes
- **Action**: Investigate root cause

### Before Removing Outliers:
- ✅ Understand the domain context
- ✅ Investigate the cause
- ✅ Document your decision
- ✅ Consider separate analysis with/without outliers

> **⚠️ WARNING**: Never blindly remove outliers without investigation!

---

## 📈 Boxplot vs Histogram

### Boxplot Strengths:
- ✓ Quick outlier identification
- ✓ Easy comparison across groups
- ✓ Clear quartile visualization
- ✓ Compact representation

### Histogram Strengths:
- ✓ Shows distribution shape (normal, skewed, bimodal)
- ✓ Frequency information
- ✓ Detailed view of data density
- ✓ Reveals modality (number of peaks)

> **Best Practice**: Use both together for comprehensive EDA!

---

## 🎥 Video Walkthrough Requirements (~2 Minutes)

Record a short screen-capture video demonstrating boxplot visualization.

### Your video MUST include:
1. ✅ Creating a boxplot for a numeric column
2. ✅ Explaining median and quartiles
3. ✅ Identifying outliers
4. ✅ Comparing boxplots across columns (if applicable)

### Video Guidelines:
- Duration: Approximately 2 minutes
- Screen-facing and clearly visible
- Clear audio explanation
- Show code and resulting visualizations

---

## 📝 Submission Guidelines

1. ✅ Submit your work as a **Pull Request** (if required)
2. ✅ Submit the **video link** as instructed
3. ✅ Video should be approximately **2 minutes**
4. ✅ Video must be **screen-facing** and clearly visible

---

## ⚠️ Important Notes

- ✓ Use boxplots **only for numeric data**
- ✓ Combine boxplots with **summary statistics**
- ✓ Do **not** assume outliers are mistakes
- ✓ Use visuals to **guide further analysis**
- ✓ **No modeling** or advanced styling is required for this milestone

---

## 📚 Additional Resources (Bonus Content)

This section is optional for learners who want to explore further:

### Documentation:
- [Pandas Boxplot Documentation](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.boxplot.html)
- [Matplotlib Boxplot Guide](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.boxplot.html)
- [Seaborn Boxplot Tutorial](https://seaborn.pydata.org/generated/seaborn.boxplot.html)

### Understanding Boxplots:
- [Understanding Box Plots](https://towardsdatascience.com/understanding-boxplots-5e2df7bcbd51)
- [When to Use Box Plots](https://chartio.com/learn/charts/box-plot-complete-guide/)

### Interpreting Outliers:
- [Detecting and Treating Outliers](https://www.analyticsvidhya.com/blog/2021/05/detecting-and-treating-outliers/)
- [To Remove or Not to Remove Outliers](https://www.statisticshowto.com/statistics-basics/remove-outliers/)

---

## 🎯 Practice Exercises

### Exercise 1: Basic Boxplot
1. Load the `example_raw.csv` from `data/raw/`
2. Create a boxplot for any numeric column
3. Identify and count the outliers

### Exercise 2: Comparison
1. Select 3 numeric columns
2. Create side-by-side boxplots
3. Write 3 observations about the distributions

### Exercise 3: Outlier Investigation
1. Identify outliers in a column
2. Investigate if they are errors or genuine values
3. Document your findings

### Exercise 4: Standardization
1. Take two columns with different scales
2. Create standardized boxplots (z-scores)
3. Compare the variability fairly

---

## ✅ Checklist for Completion

Before submitting, ensure you have:

- [ ] Understood all components of a boxplot
- [ ] Created a single-column boxplot
- [ ] Created multi-column comparison boxplots
- [ ] Identified and interpreted outliers
- [ ] Compared distributions across columns
- [ ] Recorded a 2-minute video walkthrough
- [ ] Saved all visualizations to `outputs/` folder
- [ ] Completed the practice exercises (optional)
- [ ] Documented your findings

---

## 🏆 Success Criteria

You have successfully completed this milestone when you can:

1. **Explain** what each part of a boxplot represents
2. **Create** boxplots using matplotlib or seaborn
3. **Identify** outliers and their potential causes
4. **Compare** multiple distributions side-by-side
5. **Decide** when to use boxplots vs. histograms
6. **Apply** boxplots as part of your EDA workflow

---

## 🤝 Getting Help

If you encounter issues:

1. Review the sample code in the notebook
2. Check the Python script comments
3. Refer to the documentation links
4. Ask your instructor or peers
5. Review the video examples provided

---

## 🎉 Congratulations!

Visualizing data distributions using boxplots is a **powerful EDA skill**. This milestone ensures you can summarize and compare numeric distributions clearly before moving deeper into analysis.

**Keep practicing and happy analyzing!** 📊✨

---

*This milestone is part of the Data Science Foundation with Python course.*
