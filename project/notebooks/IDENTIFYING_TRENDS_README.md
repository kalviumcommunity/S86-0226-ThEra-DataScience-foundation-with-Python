# Identifying Trends Over Time Using Line Plots - Milestone

## 📈 Overview

This milestone focuses on identifying trends over time using line plots. Line plots are one of the most effective ways to analyze time-based data, helping you observe patterns, trends, and changes across a continuous timeline.

**Understanding trends over time is essential for time-series analysis and data-driven decision-making.**

## 🎯 Learning Objectives

By completing this milestone, you will be able to:

- ✓ **Understand** what time-series data represents
- ✓ **Visualize** data changes over time using line plots
- ✓ **Identify** upward, downward, or stable trends
- ✓ **Interpret** patterns such as spikes or drops
- ✓ **Build intuition** for temporal analysis
- ✓ **Create** line plots for time-based data
- ✓ **Detect** anomalies or sudden shifts
- ✓ **Use** line plots as part of exploratory data analysis

## 💡 Why This Matters

Common beginner issues include:
- ❌ Treating time-based data like unordered data
- ❌ Missing long-term trends due to lack of visualization
- ❌ Overreacting to short-term fluctuations
- ❌ Misinterpreting seasonality or noise

**Time adds context that static analysis cannot capture.**

This milestone ensures that:
- ✅ You analyze data in the correct temporal order
- ✅ Trends become visually clear
- ✅ Insights are based on patterns, not snapshots
- ✅ Decisions are better informed over time

> **Think of line plots as a story of how data evolves.**

---

## 📚 Understanding Time-Based Data

### What Makes Data Temporal?

Time-series data has unique characteristics:

#### 1. **Temporal Ordering**
- Data points are ordered by time
- **Order matters!** Cannot be shuffled
- Past influences future (temporal dependency)

#### 2. **Time Intervals**
- **Regular**: Daily, weekly, monthly (evenly spaced)
- **Irregular**: Events, transactions (unevenly spaced)
- Important for analysis method selection

#### 3. **Common Patterns**
- **Trend**: Long-term increase or decrease
- **Seasonality**: Regular, predictable patterns
- **Cycles**: Irregular, longer-term fluctuations
- **Noise**: Random, unpredictable variation

#### 4. **Why Line Plots?**
- Show continuity between points
- Emphasize temporal flow
- Make trends visually obvious
- Highlight changes and patterns

### Time-Series vs. Other Data Types

| Data Type | Description | Example |
|-----------|-------------|---------|
| **Static** | Single snapshot in time | Survey results |
| **Cross-sectional** | Multiple subjects at one time | Census data |
| **Time-series** | One subject tracked over time | Daily stock prices |
| **Panel** | Multiple subjects over time | Customer behavior tracking |

---

## 🚀 Getting Started

### Prerequisites

Ensure you have the following libraries installed:

```bash
pip install pandas numpy matplotlib seaborn
```

### Files Provided

1. **`identifying_trends_milestone.py`** - Python script with complete examples
2. **`identifying_trends_milestone.ipynb`** - Jupyter notebook (interactive)
3. **`IDENTIFYING_TRENDS_README.md`** - This file

---

## 📖 What You Are Expected to Do

This is a **data visualization milestone**, not a modeling task.

You are expected to:

### 1. Understanding Time-Based Data
- ✓ Identify time or date columns
- ✓ Understand the importance of ordering
- ✓ Recognize regular vs irregular time intervals
- ✓ Treat time as a continuous dimension

**Correct ordering is critical.**

### 2. Creating Line Plots
- ✓ Select a time column for the x-axis
- ✓ Select a numeric column for the y-axis
- ✓ Create a clear line plot
- ✓ Label axes appropriately

**Line plots emphasize continuity.**

### 3. Identifying Trends
- ✓ Identify upward or downward trends
- ✓ Recognize stable or flat patterns
- ✓ Distinguish long-term trends from noise
- ✓ Avoid conclusions based on single points

**Trends emerge over time.**

### 4. Spotting Changes and Anomalies
- ✓ Identify sudden spikes or drops
- ✓ Observe periods of volatility
- ✓ Consider possible explanations conceptually
- ✓ Use visuals to raise questions

**Visualization highlights anomalies.**

---

## 💻 Running the Code

### Option 1: Python Script

```bash
cd project/scripts
python identifying_trends_milestone.py
```

The script will:
- Create sample time-series data with various patterns
- Generate multiple line plot visualizations
- Demonstrate trend identification techniques
- Show anomaly detection methods
- Save plots to `project/outputs/` folder

### Option 2: Jupyter Notebook (Recommended)

```bash
cd project/notebooks
jupyter notebook identifying_trends_milestone.ipynb
```

The notebook provides:
- Interactive cells you can modify
- Step-by-step explanations
- Practice exercises
- Visual output inline

---

## 📊 Key Concepts Covered

### 1. Basic Line Plot

```python
import matplotlib.pyplot as plt
import pandas as pd

# Ensure data is sorted by date (CRITICAL!)
df_sorted = df.sort_values('Date')

plt.figure(figsize=(14, 6))
plt.plot(df_sorted['Date'], df_sorted['Sales'], linewidth=2)
plt.xlabel('Date')
plt.ylabel('Sales ($)')
plt.title('Daily Sales Over Time')
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

### 2. Adding Trend Lines

```python
# Calculate linear trend
x_numeric = np.arange(len(df_sorted))
z = np.polyfit(x_numeric, df_sorted['Sales'], 1)
p = np.poly1d(z)

plt.plot(df_sorted['Date'], df_sorted['Sales'], label='Actual')
plt.plot(df_sorted['Date'], p(x_numeric), '--', label='Trend')
plt.legend()
```

### 3. Moving Averages

```python
# Calculate moving averages
df['MA_7'] = df['Sales'].rolling(window=7).mean()
df['MA_30'] = df['Sales'].rolling(window=30).mean()
df['MA_90'] = df['Sales'].rolling(window=90).mean()

# Plot all
plt.plot(df['Date'], df['Sales'], alpha=0.5, label='Original')
plt.plot(df['Date'], df['MA_30'], linewidth=2, label='30-Day MA')
plt.legend()
```

### 4. Anomaly Detection

```python
# Z-score method
rolling_mean = df['Sales'].rolling(window=30).mean()
rolling_std = df['Sales'].rolling(window=30).std()
z_score = (df['Sales'] - rolling_mean) / rolling_std
anomalies = df[abs(z_score) > 3]  # 3 standard deviations

# Visualize
plt.scatter(anomalies['Date'], anomalies['Sales'], 
            color='red', s=100, label='Anomalies')
```

---

## 🔍 Identifying Different Types of Trends

### 1. **Upward Trend** 📈
- Values generally increase over time
- Positive slope
- Example: Growing sales, increasing website traffic

### 2. **Downward Trend** 📉
- Values generally decrease over time
- Negative slope
- Example: Customer churn, declining market share

### 3. **Stable/Flat Trend** ➡️
- Values remain relatively constant
- Near-zero slope
- Example: Consistent production output

### 4. **Cyclical Pattern** 🔄
- Regular ups and downs
- Repeating patterns
- Example: Seasonal sales, weekly traffic

### 5. **Volatile/Noisy** ⚡
- Rapid, irregular changes
- High variance
- Example: Stock prices, sensor data

---

## 📈 Moving Averages Explained

Moving averages smooth out noise to reveal underlying trends:

| Window | Purpose | Use Case |
|--------|---------|----------|
| **7-Day MA** | Weekly patterns | Short-term fluctuations |
| **30-Day MA** | Monthly trends | Reduce daily volatility |
| **90-Day MA** | Quarterly trends | Long-term direction |

### Why Use Moving Averages?

✓ Remove noise to see the underlying trend  
✓ Identify when trends change direction  
✓ Compare short-term vs long-term behavior  
✓ Make better decisions based on sustained patterns  

---

## 🚨 Understanding Anomalies

Anomalies are data points that deviate significantly from expected patterns.

### Types of Anomalies:

#### 1. **Special Events**
- Promotions, sales, marketing campaigns
- Holidays or seasonal events
- Product launches
- **Action**: Document and track for future reference

#### 2. **Operational Issues**
- System outages or failures
- Supply chain disruptions
- Data collection errors
- **Action**: Investigate and fix root cause

#### 3. **External Factors**
- Economic events
- Weather extremes
- Competitor actions
- **Action**: Monitor and adapt strategy

#### 4. **Natural Volatility**
- Random variation (not all anomalies are meaningful)
- Expected fluctuation in volatile systems
- **Action**: Distinguish signal from noise

### Before Taking Action on Anomalies:

- ✅ What happened on that date?
- ✅ Is there a reasonable explanation?
- ✅ Is this a one-time event or pattern?
- ✅ Should corrective action be taken?
- ✅ Can this be prevented in the future?

> **⚠️ WARNING**: Never blindly remove anomalies without investigation!

---

## 📊 Comparing Multiple Time Series

### Separate Plots (Different Scales)

Use when variables have vastly different ranges:

```python
fig, axes = plt.subplots(3, 1, figsize=(14, 12))
axes[0].plot(df['Date'], df['Sales'])
axes[1].plot(df['Date'], df['Traffic'])
axes[2].plot(df['Date'], df['Signups'])
```

### Normalized Plots (Same Scale)

Use to compare relative trends:

```python
# Normalize to 0-100
for col in ['Sales', 'Traffic', 'Signups']:
    normalized = 100 * (df[col] - df[col].min()) / (df[col].max() - df[col].min())
    plt.plot(df['Date'], normalized, label=col)
plt.legend()
```

---

## 🎥 Video Walkthrough Requirements (~2 Minutes)

Record a short screen-capture video demonstrating trend visualization.

### Your video MUST include:
1. ✅ Creating a line plot using time-based data
2. ✅ Explaining the observed trend (upward, downward, stable)
3. ✅ Pointing out notable changes or patterns
4. ✅ Explaining why line plots are suitable for time analysis

### Video Guidelines:
- Duration: Approximately 2 minutes
- Screen-facing and clearly visible
- Clear audio explanation
- Show code and resulting visualizations
- Highlight key insights from the trend analysis

---

## 📝 Submission Guidelines

1. ✅ Submit your work as a **Pull Request** (if required)
2. ✅ Submit the **video link** as instructed
3. ✅ Video should be approximately **2 minutes**
4. ✅ Video must be **screen-facing** and clearly visible

---

## ⚠️ Important Notes

- ✓ **Always sort** data by time before plotting
- ✓ Use line plots **only for ordered data**
- ✓ Avoid **cluttering** plots with too many lines
- ✓ Combine **visuals with contextual understanding**
- ✓ **No forecasting** or modeling is required for this milestone
- ✓ Focus on **interpretation**, not prediction

---

## 📚 Additional Resources (Bonus Content)

This section is optional for learners who want to explore further:

### Documentation:
- [Pandas Line Plot Documentation](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.line.html)
- [Matplotlib Time Series](https://matplotlib.org/stable/gallery/text_labels_and_annotations/date.html)
- [Seaborn Time Series Tutorial](https://seaborn.pydata.org/tutorial/relational.html)

### Understanding Time Series:
- [Understanding Time Series: Analyzing Data Trends Over Time](https://towardsdatascience.com/time-series-analysis-in-python-an-introduction-70d5a5b1d52a)
- [Understanding and Using Line Charts](https://www.storytellingwithdata.com/blog/2020/2/19/line-charts)
- [Time Series Decomposition](https://otexts.com/fpp2/decomposition.html)

### Advanced Topics:
- [Detecting Anomalies in Time Series](https://towardsdatascience.com/time-series-anomaly-detection-with-python-7a53e0c38d5e)
- [Moving Averages Explained](https://www.investopedia.com/terms/m/movingaverage.asp)
- [Seasonality and Trend Analysis](https://machinelearningmastery.com/decompose-time-series-data-trend-seasonality/)

---

## 🎯 Practice Exercises

### Exercise 1: Basic Trend Identification
1. Load time-series data (use sample or your own)
2. Create a line plot
3. Add a trend line
4. Identify if the trend is upward, downward, or stable

### Exercise 2: Moving Averages
1. Calculate 7-day, 30-day, and 90-day moving averages
2. Plot all three on the same chart
3. Compare how smoothing affects trend visibility
4. Write 3 observations about the differences

### Exercise 3: Anomaly Detection
1. Use Z-score method to detect anomalies
2. Visualize anomalies on the line plot
3. Investigate dates of anomalies
4. Provide possible explanations for each

### Exercise 4: Multi-Series Comparison
1. Select 3 different time series
2. Create normalized comparison plot
3. Identify which variables move together
4. Document correlations or patterns

### Exercise 5: Seasonality Analysis
1. Extract monthly or weekly patterns
2. Plot average values by time period
3. Identify peak and low periods
4. Explain seasonal behavior

---

## ✅ Checklist for Completion

Before submitting, ensure you have:

- [ ] Understood time-series data characteristics
- [ ] Created at least one basic line plot
- [ ] Added trend lines to visualizations
- [ ] Used moving averages to smooth data
- [ ] Detected and explained anomalies
- [ ] Compared multiple time series
- [ ] Analyzed seasonal patterns (if applicable)
- [ ] Recorded a 2-minute video walkthrough
- [ ] Saved all visualizations to `outputs/` folder
- [ ] Completed practice exercises (optional)
- [ ] Documented key insights and findings

---

## 🏆 Success Criteria

You have successfully completed this milestone when you can:

1. **Explain** why ordering matters in time-series data
2. **Create** clear, labeled line plots for temporal analysis
3. **Identify** trends (upward, downward, stable) and patterns
4. **Detect** and interpret anomalies appropriately
5. **Compare** multiple time series effectively
6. **Use** moving averages to reveal underlying trends
7. **Apply** line plots as part of your EDA workflow
8. **Communicate** temporal insights clearly

---

## 🤝 Getting Help

If you encounter issues:

1. Review the sample code in the notebook
2. Check the Python script comments
3. Refer to the documentation links
4. Ask your instructor or peers
5. Review the video examples provided

---

## 💡 Tips for Success

### Data Preparation:
- Always check data types (ensure dates are datetime objects)
- Handle missing values appropriately
- Remove duplicates if necessary
- Verify temporal ordering

### Visualization:
- Choose appropriate time granularity (hourly, daily, weekly, monthly)
- Use consistent date formatting
- Add gridlines for easier reading
- Rotate x-axis labels if needed (45 degrees)
- Use colors purposefully, not randomly

### Interpretation:
- Look beyond individual data points
- Consider both short-term and long-term trends
- Search for patterns: seasonality, cycles, anomalies
- Ask "why?" when you see changes
- Combine visualization with domain knowledge

### Common Pitfalls to Avoid:
- ❌ Plotting unsorted data
- ❌ Ignoring scale differences when comparing
- ❌ Overreacting to single data points
- ❌ Confusing correlation with causation
- ❌ Removing anomalies without investigation
- ❌ Using too many lines on one plot

---

## 🎉 Congratulations!

**Identifying trends over time using line plots is a core EDA skill.** This milestone ensures you can analyze and interpret how data evolves across time before moving into forecasting or deeper time-series analysis.

**Time tells a story - now you know how to read it!** ⏰📈✨

---

*This milestone is part of the Data Science Foundation with Python course.*
