# Video Walkthrough Guide - CSV Loading Milestone

**Duration:** ~2 minutes  
**Topic:** Loading CSV Files into Pandas DataFrames  
**Type:** Screen-capture demonstration  
**Requirements:** Screen-facing, clearly visible, with audio explanation

---

## Video Structure

### Timeline Overview
| Time | Section | Content |
|------|---------|---------|
| 0:00-0:20 | Introduction | What are CSV files and why they matter |
| 0:20-0:50 | Loading Demo | Load CSV file into DataFrame |
| 0:50-1:20 | Inspection | Preview and explain data structure |
| 1:20-1:50 | Best Practices | Discuss inspection importance |
| 1:50-2:00 | Conclusion | Summary and key takeaway |

---

## Detailed Script

### Section 1: Introduction (0:00-0:20)
**What to Show:**
- Open your Python environment (Jupyter, VS Code, or terminal)
- Show the CSV file in a file explorer or text editor

**What to Say:**
> "Hello! Today I'm demonstrating how to load CSV files into Pandas DataFrames. CSV stands for Comma-Separated Values, and it's one of the most common formats for tabular data in Data Science. Think of it like a simplified spreadsheet. Let's get started."

**Key Points:**
- Define CSV briefly
- Mention it's a common format
- Set expectation for the demo

---

### Section 2: Loading Demo (0:20-0:50)
**What to Show:**
```python
import pandas as pd

# Show the file path clearly
df = pd.read_csv('data/raw/example_raw.csv')
```

**What to Say:**
> "First, I import pandas. Then I use the read_csv function to load the file. I'm using a relative path to the CSV file located in the data/raw folder. Notice how simple it is—just one line of code. Pandas automatically reads the first row as column headers and converts the rest into data rows."

**Actions:**
1. Type `import pandas as pd`
2. Type the `read_csv()` command
3. Execute the cell/script
4. Briefly pause to show successful execution

**Key Points:**
- Show the import statement
- Explain `pd.read_csv()` function
- Mention file path
- Note automatic header detection

---

### Section 3: Inspection (0:50-1:20)
**What to Show:**
```python
# Show first few rows
print(df.head())

# Show shape
print(f"Shape: {df.shape}")

# Show column names
print(f"Columns: {list(df.columns)}")

# Show data types
print(df.dtypes)
```

**What to Say:**
> "Now, let's inspect what we loaded. Using head(), I can see the first five rows. The shape tells me I have [X] rows and [Y] columns. The columns are named [list names]. And dtypes shows the data types—here we see integers for our numeric columns. This inspection step is critical because it confirms the data loaded correctly before we do any analysis."

**Actions:**
1. Run `df.head()` and point to headers and values
2. Run `df.shape` and explain rows vs columns
3. Show `df.columns` and read the column names
4. Run `df.dtypes` and mention data types

**Key Points:**
- Demonstrate multiple inspection methods
- Explain what each method shows
- Point to specific parts of output
- Emphasize the structure (rows and columns)

---

### Section 4: Best Practices (1:20-1:50)
**What to Show:**
- Optionally show a common error (e.g., wrong file path)
- Or show `df.info()` for comprehensive overview

**What to Say:**
> "Why is inspection so important? Because common issues like incorrect file paths, wrong delimiters, or missing headers can cause silent errors. If you don't inspect your data right after loading, you might analyze the wrong thing and get incorrect results. Always check your column names, row counts, and data types immediately after loading."

**Actions:**
1. Either demonstrate a common error briefly
2. Or show `df.info()` as a comprehensive check
3. Reinforce the "always inspect" principle

**Key Points:**
- Mention common loading issues
- Emphasize prevention over debugging
- Stress the importance of early verification

---

### Section 5: Conclusion (1:50-2:00)
**What to Show:**
- Your terminal/notebook with completed code visible

**What to Say:**
> "To summarize: CSV loading in Pandas is straightforward—import pandas, use read_csv, and always inspect with head, shape, columns, and dtypes. This foundation ensures your analysis starts correctly. Thanks for watching!"

**Key Points:**
- Quick recap of steps
- Reinforce the workflow
- End confidently

---

## Technical Setup

### Before Recording
- [ ] Clean up your workspace (close unnecessary tabs)
- [ ] Increase font size for visibility (14pt or larger)
- [ ] Prepare the CSV file and script
- [ ] Test run the code to avoid errors
- [ ] Close distracting applications
- [ ] Ensure good lighting (if camera is on)
- [ ] Test audio quality

### Recording Settings
- **Screen Resolution:** 1920×1080 or 1280×720
- **Audio:** Clear microphone, minimal background noise
- **Recording Software:** OBS Studio, Loom, QuickTime, or similar
- **Output Format:** MP4 or MOV
- **Frame Rate:** 30 fps minimum

### During Recording
- Speak clearly and at moderate pace
- Keep cursor visible and use it to point
- Avoid long pauses
- If you make a mistake, keep going or restart
- Show confidence and understanding

---

## Code to Demonstrate

### Recommended Code Sequence
```python
# 1. Import
import pandas as pd

# 2. Load CSV
df = pd.read_csv('data/raw/example_raw.csv')

# 3. Inspect - First rows
print("First 5 rows:")
print(df.head())

# 4. Inspect - Shape
print(f"\nShape: {df.shape}")
print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")

# 5. Inspect - Columns
print(f"\nColumn names: {list(df.columns)}")

# 6. Inspect - Data types
print("\nData types:")
print(df.dtypes)

# 7. Comprehensive overview
print("\nDataFrame info:")
df.info()
```

### Alternative: Interactive Approach
If using Jupyter Notebook, run each command in separate cells to show output clearly.

---

## Common Mistakes to Avoid

### ❌ Don't:
- Rush through the explanation
- Use tiny font sizes
- Skip the inspection step
- Assume everything works without checking
- Make it too technical or complicated
- Record in noisy environment
- Use unclear file paths

### ✅ Do:
- Speak clearly and confidently
- Zoom in or increase font size
- Show each inspection method
- Explain why inspection matters
- Keep it simple and practical
- Use a quiet recording space
- Show full file paths

---

## Video Checklist

### Content Requirements
- [ ] CSV file explanation included
- [ ] `pd.read_csv()` demonstrated
- [ ] Data preview shown (`df.head()`)
- [ ] Column and row structure explained
- [ ] Inspection importance discussed
- [ ] Duration is approximately 2 minutes
- [ ] Screen is clearly visible
- [ ] Audio is clear and audible

### Technical Requirements
- [ ] Screen capture recording
- [ ] Good video quality (720p minimum)
- [ ] Clear audio (no excessive noise)
- [ ] Readable font sizes
- [ ] Smooth transitions
- [ ] No sensitive information visible
- [ ] Proper file format (MP4/MOV)

---

## Submission

### Where to Submit
- Upload video to YouTube (unlisted or public)
- Or use platform specified by instructor (Google Drive, Vimeo, etc.)
- Submit the video link as required

### Video Title
- "CSV Loading Milestone - [Your Name] - Pandas Fundamentals"

### Video Description
```
This video demonstrates loading CSV files into Pandas DataFrames as part of the Data Science Fundamentals course.

Topics covered:
- Understanding CSV file structure
- Loading CSV with pd.read_csv()
- Inspecting DataFrames (head, shape, columns, dtypes)
- Importance of data inspection
- Best practices for CSV loading

Duration: ~2 minutes
Date: March 6, 2026
```

---

## Example Transcript

**Full Example (~2 minutes):**

> "Hello! Today I'm demonstrating how to load CSV files into Pandas DataFrames. CSV files contain tabular data—rows and columns—separated by commas, similar to spreadsheets.
>
> Let me show you. First, I import pandas. [Type and run] Then I use read_csv with the file path. [Type and run] That's it—one line loads the entire file into a DataFrame.
>
> Now let's inspect what we loaded. Using head(), I see the first five rows. [Show output] The columns are 'id' and 'value', and I have three rows of data. 
>
> The shape method tells me exactly: three rows, two columns. [Show output] The column names are confirmed here, [Show columns] and dtypes shows both are integers. [Show dtypes]
>
> Why does inspection matter? Because issues like wrong file paths, incorrect delimiters, or missing headers can cause silent errors. If you don't check immediately, you might analyze wrong data and get incorrect results. Always verify your structure right after loading.
>
> To summarize: import pandas, use read_csv, and inspect with head, shape, columns, and dtypes. This foundation ensures your analysis starts correctly. Thanks for watching!"

---

## Tips for Success

### Presentation Tips
1. **Practice First** - Do a test run before recording
2. **Speak Naturally** - Don't read a script word-for-word
3. **Show Enthusiasm** - Let your interest in the topic show
4. **Point Things Out** - Use your cursor to highlight important parts
5. **Pause Briefly** - Give viewers time to read output

### Content Tips
1. **Keep It Simple** - Don't overexplain
2. **Focus on Essentials** - Stick to the core concepts
3. **Use Real Data** - Demonstrate with actual CSV files
4. **Explain the "Why"** - Not just "how" but "why it matters"
5. **End Strong** - Clear summary reinforces learning

### Technical Tips
1. **Test Audio** - Record a sample first
2. **Check Visibility** - Can text be read easily?
3. **Minimize Distractions** - Close unnecessary windows
4. **Have a Backup** - Save multiple takes if needed
5. **Watch It Back** - Review before submitting

---

## Resources

### Recording Software Options
- **Free:** OBS Studio, QuickTime (Mac), Game Bar (Windows)
- **Paid:** Camtasia, ScreenFlow, Loom
- **Online:** Loom, Screencast-O-Matic

### Video Editing (Optional)
- Trim beginning/end
- Add title screen
- Enhance audio
- Add captions

### Upload Platforms
- YouTube (most common)
- Vimeo
- Google Drive
- Loom

---

## Final Notes

Remember: The goal is to demonstrate understanding, not perfection. Your video should show that you can:
1. Load a CSV file successfully
2. Inspect the loaded data
3. Explain the structure (rows and columns)
4. Articulate why inspection is important

Keep it clear, concise, and confident. Good luck!

---

**Video Walkthrough Status:** 📹 Ready to Record

**Next Action:** Record your 2-minute screen-capture video following this guide.
