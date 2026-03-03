"""
Milestone: Writing Readable Variable Names and Comments (PEP8 Basics)

This script demonstrates best practices for writing readable Python code,
focusing on variable naming conventions and meaningful comments following PEP 8.

Author: Your Name
Date: March 3, 2026
"""


# ============================================================================
# SECTION 1: Variable Naming - Good vs Bad Examples
# ============================================================================

def demonstrate_variable_naming():
    """
    Shows the difference between poor and well-named variables.
    Good variable names are self-documenting and reduce the need for comments.
    """
    
    print("=" * 60)
    print("SECTION 1: Variable Naming Examples")
    print("=" * 60)
    
    # BAD EXAMPLE: Cryptic, single-letter, vague names
    print("\n❌ BAD EXAMPLE - Unclear variable names:")
    x = 25  # What does x represent?
    y = 30  # What does y represent?
    z = x * y  # What is z?
    print(f"Result: {z}")
    
    # GOOD EXAMPLE: Clear, descriptive names using snake_case
    print("\n✅ GOOD EXAMPLE - Clear variable names:")
    student_age = 25
    course_duration_hours = 30
    total_study_hours = student_age * course_duration_hours
    print(f"Total study capacity: {total_study_hours} hours")
    
    print("\nKey Takeaway: Descriptive names eliminate ambiguity.")


# ============================================================================
# SECTION 2: PEP 8 Naming Conventions
# ============================================================================

def demonstrate_pep8_naming():
    """
    Demonstrates proper PEP 8 naming conventions for different types of variables.
    
    PEP 8 Rules:
    - Variables and functions: lowercase_with_underscores (snake_case)
    - Constants: UPPERCASE_WITH_UNDERSCORES
    - Classes: CapitalizedWords (PascalCase)
    """
    
    print("\n" + "=" * 60)
    print("SECTION 2: PEP 8 Naming Conventions")
    print("=" * 60)
    
    # Constants (values that don't change)
    MAX_STUDENTS_PER_CLASS = 50
    DEFAULT_PASSING_GRADE = 60
    COURSE_NAME = "Data Science Foundation"
    
    # Regular variables (snake_case)
    current_student_count = 45
    average_grade = 75.5
    is_class_full = current_student_count >= MAX_STUDENTS_PER_CLASS
    
    print("\n✅ Constants (UPPERCASE_WITH_UNDERSCORES):")
    print(f"  MAX_STUDENTS_PER_CLASS = {MAX_STUDENTS_PER_CLASS}")
    print(f"  DEFAULT_PASSING_GRADE = {DEFAULT_PASSING_GRADE}")
    print(f"  COURSE_NAME = '{COURSE_NAME}'")
    
    print("\n✅ Variables (lowercase_with_underscores):")
    print(f"  current_student_count = {current_student_count}")
    print(f"  average_grade = {average_grade}")
    print(f"  is_class_full = {is_class_full}")
    
    # BAD EXAMPLES to avoid
    print("\n❌ AVOID These Naming Styles:")
    print("  studentCount (camelCase - not Python convention)")
    print("  StudentCount (PascalCase - reserved for classes)")
    print("  student_Count (inconsistent capitalization)")
    print("  s, cnt, tmp (too abbreviated)")


# ============================================================================
# SECTION 3: Writing Useful Comments
# ============================================================================

def demonstrate_effective_comments():
    """
    Shows the difference between useful and unnecessary comments.
    Good comments explain WHY, not WHAT (the code shows what).
    """
    
    print("\n" + "=" * 60)
    print("SECTION 3: Effective Commenting")
    print("=" * 60)
    
    print("\n❌ BAD EXAMPLE - Over-commenting obvious code:")
    print("Code: grade = 85  # Assign 85 to grade")
    print("Problem: This comment states the obvious!")
    
    print("\n✅ GOOD EXAMPLE - Explaining intent:")
    # Using 60 as the threshold because university policy requires
    # a minimum of 60% for course completion certification
    passing_threshold = 60
    print(f"Code: passing_threshold = {passing_threshold}")
    print("Comment explains WHY 60 was chosen, not WHAT the code does.")
    
    # Example with student grades
    student_grades = [85, 92, 78, 45, 88, 73]
    
    # Filter out failing grades to calculate class success rate
    # This helps identify if intervention programs are needed
    passing_grades = [grade for grade in student_grades if grade >= passing_threshold]
    
    success_rate = (len(passing_grades) / len(student_grades)) * 100
    
    print(f"\nTotal students: {len(student_grades)}")
    print(f"Passing students: {len(passing_grades)}")
    print(f"Success rate: {success_rate:.1f}%")


# ============================================================================
# SECTION 4: Avoiding Common Readability Mistakes
# ============================================================================

def demonstrate_readability_mistakes():
    """
    Highlights common mistakes that reduce code readability.
    Professional code should be clean and self-explanatory.
    """
    
    print("\n" + "=" * 60)
    print("SECTION 4: Common Readability Mistakes")
    print("=" * 60)
    
    print("\n❌ MISTAKE 1: Misleading Comments")
    print("Code: total_price = base_price * 1.18  # Add 15% tax")
    print("Problem: Comment says 15% but code uses 18%!")
    
    print("\n✅ CORRECT: Keep comments and code aligned")
    base_price = 100
    # Apply 18% GST (Goods and Services Tax) as per regional law
    total_price = base_price * 1.18
    print(f"Code: total_price = {total_price}")
    
    print("\n❌ MISTAKE 2: Commented-out Code")
    print("# old_calculation = price * 0.9")
    print("# result = old_calculation + tax")
    print("Problem: Dead code clutters the file. Use version control instead!")
    
    print("\n❌ MISTAKE 3: Vague Variable Names")
    print("temp, data, val, x, result")
    print("Problem: These names provide no context!")
    
    print("\n✅ CORRECT: Descriptive Names")
    print("student_average_score, processed_dataset, maximum_value")
    print("temperature_celsius, sales_data")


# ============================================================================
# SECTION 5: Real-World Data Science Example
# ============================================================================

def analyze_student_performance():
    """
    A realistic example combining all readability best practices.
    This function analyzes student performance data with clear naming and comments.
    """
    
    print("\n" + "=" * 60)
    print("SECTION 5: Real-World Example - Student Performance Analysis")
    print("=" * 60)
    
    # Student performance data (name, score)
    student_data = [
        ("Alice", 92),
        ("Bob", 78),
        ("Charlie", 85),
        ("Diana", 45),
        ("Eve", 88),
        ("Frank", 73)
    ]
    
    # University requires 60% for passing
    MINIMUM_PASSING_SCORE = 60
    
    # Initialize counters for analysis
    total_students = len(student_data)
    passing_students_count = 0
    total_score_sum = 0
    highest_score = 0
    top_performer_name = ""
    
    print("\nStudent Performance Report:")
    print("-" * 40)
    
    for student_name, exam_score in student_data:
        total_score_sum += exam_score
        
        # Track passing students for success rate calculation
        if exam_score >= MINIMUM_PASSING_SCORE:
            passing_students_count += 1
            status = "PASS"
        else:
            status = "FAIL"
        
        # Identify top performer for recognition
        if exam_score > highest_score:
            highest_score = exam_score
            top_performer_name = student_name
        
        print(f"{student_name:10} | Score: {exam_score:3} | {status}")
    
    # Calculate class statistics
    average_class_score = total_score_sum / total_students
    success_rate_percentage = (passing_students_count / total_students) * 100
    
    print("-" * 40)
    print(f"\nClass Statistics:")
    print(f"  Total Students: {total_students}")
    print(f"  Passing Students: {passing_students_count}")
    print(f"  Success Rate: {success_rate_percentage:.1f}%")
    print(f"  Class Average: {average_class_score:.1f}")
    print(f"  Top Performer: {top_performer_name} ({highest_score} points)")
    
    # Alert if success rate is concerning
    # Management wants to know if less than 70% of students are passing
    if success_rate_percentage < 70:
        print(f"\n⚠️  ALERT: Success rate below 70% - intervention may be needed")


# ============================================================================
# SECTION 6: Before and After Refactoring
# ============================================================================

def show_before_after_refactoring():
    """
    Demonstrates the impact of applying readability best practices
    by comparing messy code vs clean code.
    """
    
    print("\n" + "=" * 60)
    print("SECTION 6: Before & After Refactoring")
    print("=" * 60)
    
    print("\n❌ BEFORE: Poor Readability")
    print("=" * 40)
    print("""
def calc(d):
    x=0  # counter
    for i in d:
        if i>60:  # check
            x+=1
    return (x/len(d))*100  # pct
    """)
    
    print("\n✅ AFTER: Improved Readability")
    print("=" * 40)
    print("""
def calculate_success_rate(exam_scores):
    \"\"\"
    Calculate the percentage of students who passed the exam.
    
    Args:
        exam_scores: List of numerical exam scores
    
    Returns:
        float: Success rate as a percentage
    \"\"\"
    PASSING_THRESHOLD = 60
    
    passing_students_count = 0
    
    for score in exam_scores:
        if score > PASSING_THRESHOLD:
            passing_students_count += 1
    
    total_students = len(exam_scores)
    success_rate = (passing_students_count / total_students) * 100
    
    return success_rate
    """)
    
    print("\n✨ Key Improvements:")
    print("  1. Descriptive function and variable names")
    print("  2. Proper spacing and formatting")
    print("  3. Meaningful comments explaining intent")
    print("  4. Docstring documenting function purpose")
    print("  5. Named constant instead of magic number")


# ============================================================================
# SECTION 7: Key Takeaways and Best Practices
# ============================================================================

def display_key_takeaways():
    """
    Summarizes the essential readability principles covered in this milestone.
    """
    
    print("\n" + "=" * 60)
    print("KEY TAKEAWAYS - PEP 8 READABILITY")
    print("=" * 60)
    
    takeaways = [
        "✅ Use snake_case for variables and functions",
        "✅ Use UPPERCASE for constants",
        "✅ Choose descriptive, meaningful names",
        "✅ Explain WHY, not WHAT in comments",
        "✅ Avoid over-commenting obvious code",
        "✅ Keep code and comments synchronized",
        "✅ Remove commented-out code",
        "✅ Be consistent throughout your codebase",
        "✅ Write code for humans first, computers second",
        "✅ Readable code is maintainable code"
    ]
    
    print()
    for takeaway in takeaways:
        print(f"  {takeaway}")
    
    print("\n" + "=" * 60)
    print("Remember: Code is read far more often than it is written!")
    print("=" * 60)


# ============================================================================
# MAIN EXECUTION
# ============================================================================

def main():
    """
    Main function to run all demonstrations.
    Executes each section sequentially to show readability concepts.
    """
    
    print("\n")
    print("╔" + "=" * 58 + "╗")
    print("║  PEP 8 READABILITY MILESTONE - COMPLETE DEMONSTRATION  ║")
    print("╚" + "=" * 58 + "╝")
    
    # Execute all demonstration sections
    demonstrate_variable_naming()
    demonstrate_pep8_naming()
    demonstrate_effective_comments()
    demonstrate_readability_mistakes()
    analyze_student_performance()
    show_before_after_refactoring()
    display_key_takeaways()
    
    print("\n✨ Milestone Complete! You now understand PEP 8 readability basics.\n")


# Run the program when script is executed directly
if __name__ == "__main__":
    main()
