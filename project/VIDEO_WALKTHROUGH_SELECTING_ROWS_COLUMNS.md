# Video Walkthrough Guide: Selecting Rows and Columns

## Overview
This guide will help you create a professional and comprehensive video walkthrough demonstrating DataFrame selection techniques in Pandas.

**Target Duration**: 2 minutes  
**Required**: Screen recording with clear audio narration

---

## Pre-Recording Checklist

### ✅ Technical Setup
- [ ] Screen recording software ready (OBS, Zoom, Loom, etc.)
- [ ] Audio tested and clear
- [ ] Python environment activated
- [ ] Jupyter Notebook or script ready
- [ ] Font size increased for visibility (14pt+ recommended)
- [ ] Close unnecessary applications/notifications
- [ ] Test recording 10 seconds to check quality

### ✅ Content Preparation
- [ ] Review script/notebook: `selecting_rows_columns_milestone.py` or `.ipynb`
- [ ] Practice run-through (don't read verbatim, be natural)
- [ ] Prepare sample DataFrame
- [ ] Know your examples by heart
- [ ] Have timing outline ready

---

## Video Structure (~120 seconds)

### Part 1: Introduction (15 seconds)

**What to Say:**
```
"Hi! Today I'm demonstrating DataFrame selection in Pandas—a critical skill for 
data analysis. I'll show you column selection, positional indexing with iloc, 
label-based indexing with loc, and combined selections. Let's get started!"
```

**What to Show:**
- Your prepared notebook or script
- Sample DataFrame displayed

---

### Part 2: Column Selection (20 seconds)

**What to Demonstrate:**

```python
# Single column - returns Series
df['Name']

# Multiple columns - returns DataFrame  
df[['Name', 'Age', 'Department']]
```

**What to Say:**
```
"First, column selection. Single brackets return a Series—one column. 
Double brackets return a DataFrame—multiple columns. Notice the difference 
in output types."
```

**Key Points to Emphasize:**
- Single vs double brackets
- Series vs DataFrame return types
- Columns can be in any order

---

### Part 3: Row Selection with iloc (30 seconds)

**What to Demonstrate:**

```python
# Single row by position
df.iloc[0]

# First 3 rows - stop is exclusive
df.iloc[0:3]

# Last 3 rows
df.iloc[-3:]

# Specific rows
df.iloc[[1, 3, 5]]
```

**What to Say:**
```
"iloc is for positional indexing. zero-based, like Python lists. 
iloc[0] gets the first row. Slicing like 0:3 gets rows 0, 1, and 2—
the stop position is exclusive. You can use negative indexing too."
```

**Key Points to Emphasize:**
- Position-based (0-indexed)
- Slicing is EXCLUSIVE
- Negative indexing works
- Use for "first N" or "last N" operations

---

### Part 4: Row Selection with loc (30 seconds)

**What to Demonstrate:**

```python
# Create labeled DataFrame
df_labeled = df.copy()
df_labeled.index = ['EMP001', 'EMP002', 'EMP003', ...]

# Single row by label
df_labeled.loc['EMP003']

# Multiple rows by label
df_labeled.loc[['EMP001', 'EMP003', 'EMP005']]

# Slicing - INCLUSIVE
df_labeled.loc['EMP002':'EMP005']
```

**What to Say:**
```
"loc is for label-based indexing. First, I'll add meaningful labels—employee IDs. 
Then I can select by those labels. The key difference: loc slicing is INCLUSIVE. 
EMP002 through EMP005 includes EMP005, unlike iloc."
```

**Key Points to Emphasize:**
- Uses index labels, not positions
- Slicing is INCLUSIVE
- Requires meaningful indices
- Use for specific identifiers

---

### Part 5: Combined Row and Column Selection (20 seconds)

**What to Demonstrate:**

```python
# iloc with rows and columns
df.iloc[0:3, 0:2]

# loc with rows and columns
df_labeled.loc['EMP001':'EMP003', ['Name', 'Salary']]

# All rows, specific columns
df.loc[:, ['Name', 'Department']]
```

**What to Say:**
```
"Both iloc and loc can select rows AND columns together. The syntax is 
iloc[rows, columns] or loc[rows, columns]. Use a colon to select all 
rows or all columns. This is the most powerful selection method."
```

**Key Points to Emphasize:**
- Syntax: `df.loc[rows, columns]`
- Can combine with slicing
- Colon means "all"

---

### Part 6: Best Practices & Conclusion (15 seconds)

**What to Say:**
```
"Quick recap: Use iloc for positions, loc for labels. Remember iloc slicing 
is exclusive, loc is inclusive. Always verify your selections. These skills 
are foundational for all data analysis. Thanks for watching!"
```

**What to Show:**
- Quick side-by-side comparison if time permits
- Final summary slide (optional)

---

## Script Timing Breakdown

| Section | Duration | Cumulative |
|---------|----------|------------|
| Introduction | 0:15 | 0:15 |
| Column Selection | 0:20 | 0:35 |
| iloc Selection | 0:30 | 1:05 |
| loc Selection | 0:30 | 1:35 |
| Combined Selection | 0:20 | 1:55 |
| Conclusion | 0:15 | 2:10 |

**Total**: ~2:00-2:10 (within acceptable range)

---

## Speaking Tips

### ✅ DO:
- Speak clearly and at moderate pace
- Show enthusiasm—this makes content engaging
- Pause briefly after running each code cell
- Highlight key differences (exclusive vs inclusive)
- Use your cursor to point at important output
- Be conversational, not robotic

### ❌ DON'T:
- Rush through content
- Read code line-by-line (explain concepts instead)
- Apologize for mistakes (just re-record if needed)
- Use filler words excessively ("um", "uh")
- Mumble or speak too quietly

---

## Visual Best Practices

### Screen Setup
- **Zoom Level**: 125-150% for readability
- **Theme**: Light theme for better visibility (or high-contrast dark)
- **Window Layout**: Full screen or large window
- **Output**: Ensure DataFrame output is not truncated

### Code Display
- Use clear, readable font (14pt minimum)
- Run cells so output is visible
- Highlight changes (cursor or selection)
- Keep notebook clean (no error cells)

### Narration and Cursor
- Move cursor deliberately to draw attention
- Point at specific values in output
- Highlight important differences
- Use selection to emphasize code sections

---

## Common Mistakes to Avoid

### Content Mistakes
1. **Confusing iloc and loc in explanation**
   - Solution: Clearly state "iloc uses positions, loc uses labels"

2. **Not showing output clearly**
   - Solution: Pause after each cell execution

3. **Going too fast**
   - Solution: Practice timing, speak deliberately

4. **Forgetting to emphasize key differences**
   - Solution: Explicitly state "exclusive vs inclusive"

### Technical Mistakes
1. **Audio issues**: Test recording first
2. **Screen too small**: Zoom to 125%+
3. **Notifications popping up**: Enable Do Not Disturb
4. **Code errors**: Test-run everything first

---

## Example Opening Script

### Option 1 (Professional)
```
"Hello! I'm [Your Name], and today I'll demonstrate selecting rows and columns 
in Pandas DataFrames. This is a fundamental skill for data analysis and cleaning. 
I'll cover four main techniques: column selection, positional indexing with iloc, 
label-based indexing with loc, and combined selections. Let's dive in!"
```

### Option 2 (Casual)
```
"Hey there! Today's milestone is all about selecting data in Pandas—one of the 
most important skills you'll use every single day. I'll show you how to grab 
exactly the rows and columns you need, using iloc for positions and loc for 
labels. Ready? Let's go!"
```

### Option 3 (Direct)
```
"This video demonstrates Pandas DataFrame selection. You'll learn column selection, 
iloc for positional indexing, loc for label-based indexing, and how to combine them. 
These techniques are essential for all data manipulation tasks."
```

---

## Example Closing Script

### Option 1 (Summary)
```
"To recap: Use iloc for positional access, loc for label-based access. Remember 
that iloc slicing excludes the stop position, while loc includes it. Always verify 
your selections before proceeding with analysis. Thanks for watching!"
```

### Option 2 (Call to Action)
```
"That's it! Practice these selection techniques—they're the foundation of everything 
else in Pandas. Try different datasets, experiment with boolean indexing, and make 
sure you're comfortable with both iloc and loc. Good luck!"
```

---

## Recording Workflow

### Step-by-Step Process

1. **Setup** (5 minutes)
   - Open notebook/script
   - Increase font size
   - Close distractions
   - Test audio

2. **Practice Run** (3-4 minutes)
   - Run through without recording
   - Time yourself
   - Adjust if over/under 2 minutes

3. **Record** (2 minutes)
   - Start recording
   - Follow your outline
   - Show code and output clearly
   - Speak naturally

4. **Review** (2 minutes)
   - Watch the recording
   - Check audio quality
   - Verify code is visible
   - Re-record if necessary

5. **Export & Submit** (2 minutes)
   - Export in required format (MP4 recommended)
   - Upload to specified platform
   - Submit link as instructed

---

## Quality Checklist

### Before Submitting

- [ ] Video is approximately 2 minutes
- [ ] Audio is clear throughout
- [ ] Code is readable (font size sufficient)
- [ ] All required concepts covered:
  - [ ] Column selection
  - [ ] iloc selection
  - [ ] loc selection
  - [ ] Combined selection
  - [ ] When to use each method
- [ ] Output is visible and not truncated
- [ ] No long pauses or dead air
- [ ] Professional presentation
- [ ] File format is correct
- [ ] Video uploads successfully

---

## Sample Code for Video

### Complete Demo Script

```python
import pandas as pd

# Create sample data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 35, 28, 32],
    'Department': ['Sales', 'IT', 'HR', 'Sales', 'IT'],
    'Salary': [50000, 65000, 60000, 52000, 68000]
}
df = pd.DataFrame(data)
print("Sample DataFrame:")
print(df)

# 1. Column Selection
print("\n1. Column Selection:")
print(df['Name'])                    # Series
print(df[['Name', 'Age']])          # DataFrame

# 2. iloc - Positional Selection
print("\n2. iloc (Positional):")
print(df.iloc[0])                    # First row
print(df.iloc[0:3])                  # First 3 rows
print(df.iloc[-2:])                  # Last 2 rows

# 3. loc - Label-based Selection
print("\n3. loc (Label-based):")
df_labeled = df.copy()
df_labeled.index = ['EMP001', 'EMP002', 'EMP003', 'EMP004', 'EMP005']
print(df_labeled.loc['EMP003'])
print(df_labeled.loc['EMP001':'EMP003'])  # Inclusive!

# 4. Combined Selection
print("\n4. Combined Selection:")
print(df.iloc[0:3, 0:2])                    # iloc
print(df_labeled.loc[:, ['Name', 'Salary']]) # loc
```

---

## Submission Guidelines

### File Requirements
- **Format**: MP4 or MOV (MP4 preferred)
- **Duration**: 1:45 - 2:15 (approximately 2 minutes)
- **Resolution**: Minimum 720p (1080p recommended)
- **Audio**: Clear narration throughout
- **Size**: Check submission platform limits

### Where to Submit
- Follow instructor's specific submission instructions
- Upload to designated platform (YouTube, Google Drive, etc.)
- Submit link through assignment portal
- Ensure video is accessible (unlisted or public as required)

---

## Troubleshooting

### Common Issues

**Issue**: Video exceeds 2 minutes
- **Solution**: Speak slightly faster, cut unnecessary pauses

**Issue**: Audio not clear
- **Solution**: Use headset microphone, reduce background noise

**Issue**: Code not readable
- **Solution**: Increase font to 16pt+, use full screen

**Issue**: Forgot to show something
- **Solution**: Don't panic—re-record the section and edit, or do full re-take

---

## Final Tips

### Make it Personal
- Show your genuine understanding
- Don't just read code—explain concepts
- Express why selection matters in real workflows

### Technical Excellence
- Clear audio is MORE important than perfect delivery
- Visible code is MORE important than fancy editing
- Concise content is MORE important than extra details

### Remember
- Everyone makes mistakes—perfection isn't required
- Clarity and comprehension are the goals
- Your enthusiasm makes the content engaging

---

**Good luck with your recording! You've got this! 🎥✨**
