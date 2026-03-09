# Selecting Rows and Columns Milestone

## Overview
This milestone focuses on mastering DataFrame selection using Pandas indexing and slicing techniques. Precise data selection is foundational for all data analysis tasks.

## Learning Objectives
After completing this milestone, you will be able to:
- Select specific columns from a DataFrame
- Select rows using positional indexing (iloc)
- Select rows using label-based indexing (loc)
- Combine row and column selection
- Understand the difference between iloc and loc
- Avoid common selection mistakes

## Key Concepts Covered

### 1. Column Selection
- **Single column**: `df['column_name']` → Returns Series
- **Multiple columns**: `df[['col1', 'col2']]` → Returns DataFrame
- Columns can be selected in any order

### 2. Row Selection by Position (iloc)
- Uses integer positions (0-based indexing)
- Slicing is **EXCLUSIVE**: `df.iloc[0:3]` gets rows 0, 1, 2 (NOT 3)
- Supports negative indexing: `df.iloc[-3:]` gets last 3 rows
- Use when you need positional access

### 3. Row Selection by Label (loc)
- Uses index labels (not positions)
- Slicing is **INCLUSIVE**: `df.loc['A':'C']` includes 'A', 'B', and 'C'
- Requires meaningful index labels
- Use when working with specific identifiers

### 4. Combined Row and Column Selection
- **Syntax**: `df.iloc[rows, columns]` or `df.loc[rows, columns]`
- Use `:` to select all rows or all columns
- Can combine slicing and explicit lists
- Most powerful and flexible selection method

## Files Included

### Scripts
- **`selecting_rows_columns_milestone.py`**: Complete demonstration script with examples

### Notebooks
- **`selecting_rows_columns_milestone.ipynb`**: Interactive Jupyter notebook

## Quick Reference

### iloc vs loc Comparison

| Feature | iloc | loc |
|---------|------|-----|
| Type | Position-based | Label-based |
| Indexing | Integer (0-based) | Index labels |
| Slicing | Exclusive | Inclusive |
| Example | `df.iloc[0:3]` | `df.loc['A':'C']` |

### Common Selection Patterns

```python
# Column Selection
df['Name']                        # Single column → Series
df[['Name', 'Age']]              # Multiple columns → DataFrame

# Row Selection - Position
df.iloc[0]                        # First row
df.iloc[0:3]                      # First 3 rows (0,1,2)
df.iloc[-3:]                      # Last 3 rows
df.iloc[[1, 3, 5]]               # Specific rows

# Row Selection - Label
df.loc['EMP001']                  # Row with label 'EMP001'
df.loc['A':'D']                   # Rows A through D (inclusive)
df.loc[['EMP001', 'EMP003']]     # Specific labeled rows

# Combined Selection
df.iloc[0:3, 0:2]                # First 3 rows, first 2 columns
df.loc[:, ['Name', 'Age']]       # All rows, specific columns
df.loc['A':'C', 'Name':'Age']    # Slice both rows and columns

# Boolean Indexing
df[df['Age'] > 25]               # Rows where Age > 25
df.loc[df['Age'] > 25, ['Name']] # Names where Age > 25
```

## Best Practices

### ✅ DO:
- Use `.iloc` for positional indexing
- Use `.loc` for label-based indexing
- Be explicit with `df.loc[rows, columns]`
- Verify your selection immediately after making it
- Use meaningful column names

### ❌ DON'T:
- Chain indexing: `df['col'][0]` (can cause SettingWithCopyWarning)
- Mix `iloc` and `loc` concepts
- Assume default integer index is meaningful
- Select data without verifying the results

## Common Mistakes to Avoid

### Mistake 1: Confusing iloc and loc
```python
# WRONG: Mixing concepts
df.iloc['Name']  # iloc uses positions, not labels

# CORRECT:
df.loc[:, 'Name']  # loc can use column labels
df.iloc[:, 0]      # iloc uses column positions
```

### Mistake 2: Forgetting Slicing Behavior
```python
# iloc is EXCLUSIVE
df.iloc[0:3]  # Gets rows 0, 1, 2 (NOT 3)

# loc is INCLUSIVE
df.loc['A':'C']  # Gets rows 'A', 'B', 'C'
```

### Mistake 3: Single vs Double Brackets
```python
df['Name']      # Returns Series
df[['Name']]    # Returns DataFrame with one column
```

## Running the Code

### Run the Script
```bash
python project/scripts/selecting_rows_columns_milestone.py
```

### Run the Notebook
1. Open `project/notebooks/selecting_rows_columns_milestone.ipynb`
2. Execute cells sequentially
3. Experiment with the examples

## Video Walkthrough Requirements

Your video demonstration should include:
1. **Column Selection** - Show single and multiple column selection
2. **iloc Selection** - Demonstrate positional indexing and slicing
3. **loc Selection** - Show label-based indexing with custom indices
4. **Combined Selection** - Select specific rows and columns together
5. **Explanation** - Discuss when to use each approach

**Duration**: ~2 minutes  
**Format**: Screen capture with audio

## Next Steps

After completing this milestone:
1. Practice with real datasets
2. Combine selection with data cleaning
3. Use boolean indexing for filtering
4. Apply in feature engineering workflows

## Why This Matters

Proper data selection:
- Prevents accidental data leaks
- Reduces errors in analysis
- Makes code more readable
- Enables precise data transformations
- Forms the foundation for all data workflows

Most downstream errors in data analysis start with incorrect data selection. Master this skill to ensure your analyses are built on solid foundations.

## Resources

### Official Documentation
- [Pandas Indexing and Selecting Data](https://pandas.pydata.org/docs/user_guide/indexing.html)
- [iloc Documentation](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iloc.html)
- [loc Documentation](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html)

### Additional Learning
- [Pandas iloc vs loc](https://www.datacamp.com/tutorial/pandas-iloc-vs-loc)
- [Common Selection Mistakes](https://realpython.com/pandas-settingwithcopywarning/)

---

**Remember**: Selection is not about memorizing syntax—it's about understanding the logic of positions vs labels and being intentional about what data you extract.
