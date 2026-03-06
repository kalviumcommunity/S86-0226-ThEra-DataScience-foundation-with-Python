# CSV Loading Milestone - README

## 📊 Loading CSV Data into Pandas DataFrames

This milestone covers the fundamental skill of loading CSV files into Pandas DataFrames—an essential first step in any Data Science workflow.

---

## 📁 Files Created

### 1. **Main Script**
[`scripts/csv_loading_milestone.py`](scripts/csv_loading_milestone.py)

**Comprehensive demonstration including:**
- CSV file structure explanation
- Loading CSV files with `pd.read_csv()`
- Thorough data inspection techniques
- Common loading issues and solutions
- Best practices and verification checklist

**To run:**
```bash
cd project/scripts
python csv_loading_milestone.py
```

### 2. **Completion Documentation**
[`CSV_LOADING_MILESTONE_COMPLETION.md`](CSV_LOADING_MILESTONE_COMPLETION.md)

**Detailed documentation of:**
- All learning objectives achieved
- Key concepts mastered
- Code examples and explanations
- Verification checklist
- Next steps for continued learning

### 3. **Video Walkthrough Guide**
[`VIDEO_WALKTHROUGH_CSV_LOADING.md`](VIDEO_WALKTHROUGH_CSV_LOADING.md)

**Complete guide for recording your 2-minute video:**
- Detailed timeline and script
- What to show and say at each step
- Technical setup checklist
- Recording tips and best practices
- Submission instructions

---

## 🎯 Learning Objectives

### ✅ What You Will Learn

1. **Understanding CSV Files**
   - Structure of CSV format
   - Headers vs data rows
   - Delimiter concepts
   - Relationship to spreadsheets

2. **Loading CSV into Pandas**
   - Using `pd.read_csv()` function
   - Handling file paths correctly
   - Basic error handling
   - Creating DataFrames from files

3. **Inspecting Loaded Data**
   - `df.head()` - Preview first rows
   - `df.tail()` - Preview last rows
   - `df.shape` - Get dimensions
   - `df.columns` - View column names
   - `df.dtypes` - Check data types
   - `df.info()` - Comprehensive overview
   - `df.describe()` - Statistical summary

4. **Common Loading Issues**
   - Incorrect file paths
   - Missing headers
   - Wrong delimiters
   - Encoding problems
   - Mixed data types
   - Large file handling

---

## 🚀 Quick Start

### Prerequisites
```python
# Install pandas if not already installed
pip install pandas
```

### Basic Usage
```python
import pandas as pd

# Load CSV file
df = pd.read_csv('data/raw/example_raw.csv')

# Inspect the data
print(df.head())
print(df.shape)
print(df.columns)
print(df.dtypes)
```

### Sample Data Files
- **Raw Data:** `data/raw/example_raw.csv` (2 columns, 3 rows)
- **Processed Data:** `data/processed/example_processed.csv` (3 columns, 3 rows)

---

## 📋 Verification Checklist

After loading any CSV file, always verify:

- [ ] File loaded without errors
- [ ] Row count is as expected
- [ ] Column count is as expected
- [ ] Column names are correct
- [ ] Data types are appropriate
- [ ] First rows look reasonable
- [ ] Last rows look reasonable
- [ ] No unexpected missing values
- [ ] Overall shape makes sense
- [ ] Structure matches expectations

---

## 🎥 Video Walkthrough (~2 Minutes)

### What to Cover in Your Video

1. **Introduction (20 sec)**
   - Explain what CSV files are
   - Why they're important in Data Science

2. **Loading Demo (30 sec)**
   - Import pandas
   - Use `pd.read_csv()`
   - Show successful loading

3. **Inspection (30 sec)**
   - Demonstrate `head()`, `shape`, `columns`, `dtypes`
   - Explain row and column structure

4. **Best Practices (30 sec)**
   - Discuss importance of inspection
   - Mention common issues

5. **Conclusion (10 sec)**
   - Quick summary
   - Key takeaway

**See [`VIDEO_WALKTHROUGH_CSV_LOADING.md`](VIDEO_WALKTHROUGH_CSV_LOADING.md) for detailed guide.**

---

## 💡 Key Concepts

### Why CSV Loading Matters
- **Foundation of Analysis** - All data work starts here
- **Common Format** - CSV is universal
- **Error Prevention** - Proper loading prevents downstream issues
- **Professional Standard** - Expected in industry

### Critical Best Practices
1. **Always Inspect** - Never assume data loaded correctly
2. **Check File Paths** - Verify paths before loading
3. **Verify Headers** - Confirm column names
4. **Check Data Types** - Ensure appropriate types
5. **Catch Errors Early** - Inspect immediately after loading

---

## 🛠️ Common Loading Patterns

### Basic Loading
```python
df = pd.read_csv('file.csv')
```

### Specify Delimiter
```python
df = pd.read_csv('file.txt', delimiter='\t')  # Tab-separated
```

### Load Specific Columns
```python
df = pd.read_csv('file.csv', usecols=['col1', 'col2'])
```

### Specify Data Types
```python
df = pd.read_csv('file.csv', dtype={'id': int, 'value': float})
```

### Handle Missing Values
```python
df = pd.read_csv('file.csv', na_values=['NA', 'NULL', ''])
```

### Load First N Rows
```python
df = pd.read_csv('file.csv', nrows=100)
```

---

## 🔍 Inspection Methods Reference

| Method | Purpose | Example Output |
|--------|---------|----------------|
| `df.head()` | First 5 rows | Tabular preview |
| `df.tail()` | Last 5 rows | Tabular preview |
| `df.shape` | Dimensions | `(100, 5)` |
| `df.columns` | Column names | `['id', 'value']` |
| `df.dtypes` | Data types | `int64, float64` |
| `df.info()` | Overview | Memory, types, nulls |
| `df.describe()` | Statistics | Mean, std, min, max |

---

## ⚠️ Common Issues and Solutions

| Issue | Symptom | Solution |
|-------|---------|----------|
| Wrong path | FileNotFoundError | Check file location |
| Missing headers | First row as data | Use `header=0` or `None` |
| Wrong delimiter | Single column | Use `sep=';'` or `delimiter` |
| Encoding error | Gibberish characters | Try `encoding='utf-8'` |
| Numbers as strings | dtype: object | Specify `dtype` or convert |
| Large file | Memory error | Use `chunksize` or `nrows` |

---

## 📚 Additional Resources

### Official Documentation
- [Pandas read_csv documentation](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)
- [Pandas DataFrame documentation](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)

### Next Steps
- Data cleaning techniques
- Handling missing values
- Data type conversions
- Merging multiple CSV files
- Working with large datasets

---

## 🎓 Skills Demonstrated

By completing this milestone, you demonstrate:

- ✅ Understanding of CSV file format
- ✅ Proficiency with `pd.read_csv()`
- ✅ Ability to inspect DataFrames thoroughly
- ✅ Awareness of common loading pitfalls
- ✅ Application of data loading best practices

---

## 📝 Submission Checklist

- [ ] Run `csv_loading_milestone.py` successfully
- [ ] Review `CSV_LOADING_MILESTONE_COMPLETION.md`
- [ ] Record 2-minute video following guide
- [ ] Ensure video is screen-facing and clearly visible
- [ ] Submit video link as instructed
- [ ] Submit Pull Request (if required)

---

## 🌟 Success Criteria

Your submission should demonstrate:

1. **Technical Competence**
   - Successfully load CSV files
   - Use inspection methods correctly
   - Understand DataFrame structure

2. **Understanding**
   - Explain CSV format clearly
   - Describe row and column structure
   - Articulate why inspection matters

3. **Presentation**
   - Clear video with good audio
   - Visible screen and code
   - Confident explanation

---

## 💬 Tips for Success

### Code Practice
- Run the script multiple times
- Try with different CSV files
- Experiment with parameters
- Practice inspection methods

### Video Recording
- Test audio and video quality first
- Use large, readable fonts
- Speak clearly and confidently
- Keep it concise (~2 minutes)
- Practice before recording

### Conceptual Understanding
- Understand why inspection matters
- Know what each method shows
- Recognize common issues
- Think about real-world applications

---

## 🎯 Learning Outcomes

After completing this milestone, you will be able to:

- ✅ Load external CSV data into Python
- ✅ Create Pandas DataFrames from files
- ✅ Inspect data structure systematically
- ✅ Verify data loaded correctly
- ✅ Identify common loading problems
- ✅ Apply professional data loading practices
- ✅ Prepare data safely for analysis

---

## 📞 Questions or Issues?

If you encounter problems:

1. Check file paths are correct
2. Verify pandas is installed
3. Review error messages carefully
4. Consult the completion documentation
5. Refer to the video walkthrough guide
6. Contact instructor if needed

---

## 🏁 Conclusion

CSV loading is the foundation of Data Science workflows. This milestone ensures you can bring external tabular data into Pandas confidently and safely. 

**Remember:** Always inspect your data after loading. This simple practice prevents countless errors downstream.

**Good luck with your video walkthrough!** 🎥

---

*"Data loading is like opening a door—always look before you walk through."*

**Milestone Status:** ✅ **READY FOR COMPLETION**
