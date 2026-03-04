"""
NumPy Array Arithmetic Operations - Practice Exercises & Solutions

This file contains practical exercises to help you master array arithmetic.
Each exercise includes the problem statement and a solution.

Difficulty Levels:
⭐ = Beginner (Basic operations)
⭐⭐ = Intermediate (Multiple operations combined)
⭐⭐⭐ = Advanced (Real-world scenarios)

Author: Data Science Foundation
Date: March 4, 2026
"""

import numpy as np


print("=" * 80)
print("NUMPY ARRAY ARITHMETIC - PRACTICE EXERCISES & SOLUTIONS")
print("=" * 80)

# ============================================================================
# BEGINNER EXERCISES (⭐)
# ============================================================================

print("\n" + "="*80)
print("BEGINNER EXERCISES (⭐)")
print("="*80)

# EXERCISE 1.1: Basic Array Creation and Addition
print("\n" + "-"*80)
print("EXERCISE 1.1: Basic Array Creation and Addition")
print("-"*80)

print("\n📝 PROBLEM:")
print("Create two arrays:")
print("  - array1 = [5, 10, 15, 20, 25]")
print("  - array2 = [1, 2, 3, 4, 5]")
print("Add them together and print the result.")

print("\n✅ SOLUTION:")
array1 = np.array([5, 10, 15, 20, 25])
array2 = np.array([1, 2, 3, 4, 5])
result = array1 + array2
print(f"array1: {array1}")
print(f"array2: {array2}")
print(f"array1 + array2 = {result}")
print(f"💡 Each corresponding pair is added: [5+1, 10+2, 15+3, 20+4, 25+5]")

# EXERCISE 1.2: Scalar Multiplication
print("\n" + "-"*80)
print("EXERCISE 1.2: Scalar Multiplication")
print("-"*80)

print("\n📝 PROBLEM:")
print("Given array = [2, 4, 6, 8, 10]")
print("Multiply all elements by 3")

print("\n✅ SOLUTION:")
array = np.array([2, 4, 6, 8, 10])
multiplied = array * 3
print(f"array: {array}")
print(f"array * 3 = {multiplied}")
print(f"💡 The scalar 3 is multiplied with each element")

# EXERCISE 1.3: Division Operation
print("\n" + "-"*80)
print("EXERCISE 1.3: Division Operation")
print("-"*80)

print("\n📝 PROBLEM:")
print("Given array = [100, 200, 300, 400, 500]")
print("Divide all elements by 10")

print("\n✅ SOLUTION:")
array = np.array([100, 200, 300, 400, 500])
divided = array / 10
print(f"array: {array}")
print(f"array / 10 = {divided}")
print(f"💡 Each element is divided by 10")

# EXERCISE 1.4: Element-Wise Subtraction
print("\n" + "-"*80)
print("EXERCISE 1.4: Element-wise Subtraction")
print("-"*80)

print("\n📝 PROBLEM:")
print("Given:")
print("  - prices_original = [100, 150, 200, 250]")
print("  - prices_sale = [80, 120, 160, 210]")
print("Calculate the difference (discount from original)")

print("\n✅ SOLUTION:")
prices_original = np.array([100, 150, 200, 250])
prices_sale = np.array([80, 120, 160, 210])
discount = prices_original - prices_sale
print(f"Original prices: {prices_original}")
print(f"Sale prices:     {prices_sale}")
print(f"Discount amount: {discount}")
print(f"💡 Subtraction shows how much was saved per item")

# ============================================================================
# INTERMEDIATE EXERCISES (⭐⭐)
# ============================================================================

print("\n" + "="*80)
print("INTERMEDIATE EXERCISES (⭐⭐)")
print("="*80)

# EXERCISE 2.1: Combined Operations (Order of Operations)
print("\n" + "-"*80)
print("EXERCISE 2.1: Combined Operations (Order of Operations)")
print("-"*80)

print("\n📝 PROBLEM:")
print("Given:")
print("  - base_salary = np.array([50000, 60000, 55000, 65000])")
print("  - bonus_multiplier = 1.1  (10% bonus)")
print("  - tax_rate = 0.2  (20% tax)")
print("Calculate: (salary * bonus_multiplier) - (salary * bonus_multiplier * tax_rate)")
print("In other words: salary with 10% bonus, minus 20% tax on bonus amount")

print("\n✅ SOLUTION:")
base_salary = np.array([50000, 60000, 55000, 65000])
bonus_multiplier = 1.1
tax_rate = 0.2

# Method 1: Step by step
salary_with_bonus = base_salary * bonus_multiplier
tax_on_salary = salary_with_bonus * tax_rate
take_home = salary_with_bonus - tax_on_salary

print(f"Base salary:        {base_salary}")
print(f"With 10% bonus:     {salary_with_bonus}")
print(f"Tax (20%):          {tax_on_salary}")
print(f"Take-home salary:   {take_home}")

# Method 2: Compact formula
take_home_compact = base_salary * bonus_multiplier * (1 - tax_rate)
print(f"\nCompact formula:    {take_home_compact}")
print(f"💡 Both methods give the same result!")

# EXERCISE 2.2: Working with 2D Arrays
print("\n" + "-"*80)
print("EXERCISE 2.2: Working with 2D Arrays")
print("-"*80)

print("\n📝 PROBLEM:")
print("Create a 3x3 array of test scores for 3 students and 3 subjects.")
print("Add 5 bonus points to everyone's score (optional extra credit)")

print("\n✅ SOLUTION:")
scores = np.array([[85, 90, 78],   # Student 1: Math, Science, English
                   [92, 88, 95],   # Student 2
                   [78, 85, 82]])  # Student 3

print(f"Original scores:\n{scores}\n")

scores_with_bonus = scores + 5
print(f"With 5 bonus points:\n{scores_with_bonus}")
print(f"💡 The scalar operation applies to every element in the 2D array!")

# EXERCISE 2.3: Element-wise Multiplication with Different Purposes
print("\n" + "-"*80)
print("EXERCISE 2.3: Element-wise Multiplication")
print("-"*80)

print("\n📝 PROBLEM:")
print("Given quantities and unit prices:")
print("  - quantities = [10, 20, 15, 8]  (units ordered)")
print("  - unit_prices = [5.99, 12.50, 8.75, 24.99]  (price per unit)")
print("Calculate total price for each item (quantity * unit_price)")

print("\n✅ SOLUTION:")
quantities = np.array([10, 20, 15, 8])
unit_prices = np.array([5.99, 12.50, 8.75, 24.99])

total_prices = quantities * unit_prices
print(f"Quantities:    {quantities}")
print(f"Unit prices:   {unit_prices}")
print(f"Total prices:  {total_prices}")
print(f"Grand total:   ${total_prices.sum():.2f}")
print(f"💡 Element-wise multiplication computes cost per item")

# EXERCISE 2.4: Combining Multiple Operations
print("\n" + "-"*80)
print("EXERCISE 2.4: Combining Multiple Operations")
print("-"*80)

print("\n📝 PROBLEM:")
print("Temperature conversion more complex:")
print("Convert Celsius to Fahrenheit AND apply a calibration offset")
print("Formula: F = (C × 9/5) + 32 + offset")
print("  - celsius = [0, 10, 20, 30, 40]")
print("  - offset = 0.5  (calibration adjustment)")

print("\n✅ SOLUTION:")
celsius = np.array([0, 10, 20, 30, 40])
offset = 0.5

fahrenheit = (celsius * 9/5) + 32 + offset
print(f"Celsius:       {celsius}")
print(f"Fahrenheit:    {fahrenheit}")
print(f"💡 Multiple operations in one formula maintains code clarity")

# ============================================================================
# ADVANCED EXERCISES (⭐⭐⭐)
# ============================================================================

print("\n" + "="*80)
print("ADVANCED EXERCISES (⭐⭐⭐)")
print("="*80)

# EXERCISE 3.1: Data Normalization
print("\n" + "-"*80)
print("EXERCISE 3.1: Data Normalization (Scale to 0-1)")
print("-"*80)

print("\n📝 PROBLEM:")
print("Normalize test scores to 0-1 range (min-max normalization)")
print("Formula: normalized = (value - min) / (max - min)")
print("  - scores = [45, 67, 89, 92, 78, 55, 88]")

print("\n✅ SOLUTION:")
scores = np.array([45, 67, 89, 92, 78, 55, 88])

min_score = scores.min()
max_score = scores.max()
normalized_scores = (scores - min_score) / (max_score - min_score)

print(f"Original scores:        {scores}")
print(f"Min: {min_score}, Max: {max_score}")
print(f"Normalized (0-1):       {normalized_scores}")
print(f"Normalized * 100 (%):   {(normalized_scores * 100).astype(int)}")
print(f"💡 Normalization scales values to a standard range for comparison")

# EXERCISE 3.2: Percentage Change Calculation
print("\n" + "-"*80)
print("EXERCISE 3.2: Percentage Change Calculation")
print("-"*80)

print("\n📝 PROBLEM:")
print("Calculate monthly sales growth percentage")
print("Formula: percent_change = (new - old) / old * 100")
print("  - jan_sales = [1000, 1500, 2000, 1200]")
print("  - feb_sales = [1100, 1650, 2200, 1100]")

print("\n✅ SOLUTION:")
jan_sales = np.array([1000, 1500, 2000, 1200])
feb_sales = np.array([1100, 1650, 2200, 1100])

percent_change = (feb_sales - jan_sales) / jan_sales * 100

print(f"January sales:         {jan_sales}")
print(f"February sales:        {feb_sales}")
print(f"Percent change:        {percent_change.astype(int)}%")
print(f"\nProduct performance:")
for i, change in enumerate(percent_change):
    direction = "📈 UP" if change > 0 else "📉 DOWN"
    print(f"  Product {i+1}: {change:+.1f}% {direction}")

# EXERCISE 3.3: Standardization (Z-score normalization)
print("\n" + "-"*80)
print("EXERCISE 3.3: Standardization (Z-score)")
print("-"*80)

print("\n📝 PROBLEM:")
print("Standardize data so it has mean=0 and std=1 (z-score normalization)")
print("Formula: z = (value - mean) / standard_deviation")
print("  - data = [10, 12, 14, 16, 18, 20]")

print("\n✅ SOLUTION:")
data = np.array([10, 12, 14, 16, 18, 20])

mean = data.mean()
std_dev = data.std()
z_scores = (data - mean) / std_dev

print(f"Original data:         {data}")
print(f"Mean: {mean:.2f}, Std Dev: {std_dev:.2f}")
print(f"Z-scores (standardized): {z_scores}")
print(f"New mean: {z_scores.mean():.6f} (should be ~0)")
print(f"New std:  {z_scores.std():.6f} (should be ~1)")
print(f"💡 Standardization makes it easy to compare different datasets")

# EXERCISE 3.4: Applying Discounts with Different Tiers
print("\n" + "-"*80)
print("EXERCISE 3.4: Tiered Discount Application")
print("-"*80)

print("\n📝 PROBLEM:")
print("Apply different discounts based on purchase amount:")
print("  - 0-100: 0% discount")
print("  - 100-500: 10% discount")
print("  - 500+: 20% discount")
print("\nOrders: [50, 150, 600, 75, 450, 800]")

print("\n✅ SOLUTION:")
orders = np.array([50, 150, 600, 75, 450, 800])

# Create discount array
discounts = np.zeros_like(orders, dtype=float)
discounts[orders < 100] = 0.00
discounts[(orders >= 100) & (orders < 500)] = 0.10
discounts[orders >= 500] = 0.20

discounted_prices = orders * (1 - discounts)

print(f"Order amounts:         {orders}")
print(f"Discount rates:        {(discounts*100).astype(int)}%")
print(f"After discount:        {discounted_prices.astype(int)}")

for i, (order, discount, price) in enumerate(zip(orders, discounts*100, discounted_prices)):
    print(f"  Order {i+1}: ${order:4} → {discount:2.0f}% off → ${price:6.2f}")

# EXERCISE 3.5: Real-world Portfolio Analysis
print("\n" + "-"*80)
print("EXERCISE 3.5: Investment Portfolio Analysis")
print("-"*80)

print("\n📝 PROBLEM:")
print("Analyze investment portfolio performance:")
print("  - initial_investment = [10000, 25000, 5000]  (3 stocks)")
print("  - current_value = [11000, 27500, 4500]")
print("Calculate returns per stock and overall portfolio")

print("\n✅ SOLUTION:")
initial_investment = np.array([10000, 25000, 5000])
current_value = np.array([11000, 27500, 4500])

# Calculate returns
returns = current_value - initial_investment
percent_returns = (returns / initial_investment) * 100

total_initial = initial_investment.sum()
total_current = current_value.sum()
total_return = total_current - total_initial
total_percent = (total_return / total_initial) * 100

print(f"\nInitial Investment:    {initial_investment}")
print(f"Current Value:         {current_value}")
print(f"Gain/Loss:             {returns}")
print(f"Percent Return:        {percent_returns.astype(int)}%")

print(f"\nPortfolio Summary:")
print(f"  Total invested:      ${total_initial:,.0f}")
print(f"  Current value:       ${total_current:,.0f}")
print(f"  Total gain:          ${total_return:,.0f}")
print(f"  Overall return:      {total_percent:.1f}%")

# ============================================================================
# CHALLENGE EXERCISE
# ============================================================================

print("\n" + "="*80)
print("CHALLENGE EXERCISE ⭐⭐⭐⭐")
print("="*80)

print("\n" + "-"*80)
print("CHALLENGE: Build A Sales Report Calculation System")
print("-"*80)

print("\n📝 PROBLEM:")
print("Create a complete sales calculation system that:")
print("1. Reads sales data (units and price per unit)")
print("2. Calculates revenue per product")
print("3. Applies tiered discounts (10% for orders > $1000)")
print("4. Calculates tax (8%)")
print("5. Determines final totals and commission (5%)")

print("\n✅ SOLUTION:")

# Sample data
products = ['Laptop', 'Mouse', 'Keyboard', 'Monitor']
units_sold = np.array([15, 120, 85, 30])
unit_prices = np.array([999.99, 24.99, 79.99, 349.99])

# Step 1: Calculate revenue
revenue = units_sold * unit_prices
print(f"\n1️⃣  REVENUE CALCULATION:")
print(f"Products:     {products}")
print(f"Units sold:   {units_sold}")
print(f"Unit price:   ${unit_prices}")
print(f"Revenue:      ${revenue}")

# Step 2: Apply discount
discount_rate = np.where(revenue > 1000, 0.10, 0)
discount_amount = revenue * discount_rate
revenue_after_discount = revenue - discount_amount

print(f"\n2️⃣  DISCOUNT APPLICATION (10% if revenue > $1000):")
print(f"Discount %:   {(discount_rate*100).astype(int)}%")
print(f"Discount $:   ${discount_amount}")
print(f"After discount: ${revenue_after_discount}")

# Step 3: Calculate tax
tax_rate = 0.08
tax_amount = revenue_after_discount * tax_rate
final_total = revenue_after_discount + tax_amount

print(f"\n3️⃣  TAX CALCULATION (8%):")
print(f"Tax amount:   ${tax_amount}")
print(f"Final total:  ${final_total}")

# Step 4: Calculate commission
commission_rate = 0.05
commission = revenue * commission_rate  # Commission on original revenue

print(f"\n4️⃣  COMMISSION (5% of original revenue):")
print(f"Commission:   ${commission}")

# Summary
print(f"\n📊 SUMMARY:")
print(f"{'Product':<15} {'Revenue':<12} {'After Tax':<12} {'Commission':<12}")
print("-" * 51)
for i, product in enumerate(products):
    print(f"{product:<15} ${revenue[i]:<11.2f} ${final_total[i]:<11.2f} ${commission[i]:<11.2f}")

print(f"\n{'TOTALS':<15} ${revenue.sum():<11.2f} ${final_total.sum():<11.2f} ${commission.sum():<11.2f}")

# ============================================================================
# TESTING YOUR UNDERSTANDING
# ============================================================================

print("\n" + "="*80)
print("TEST YOUR UNDERSTANDING")
print("="*80)

print(f"""
1. What's the difference between these two operations?
   a) list1 + list2       → Concatenates (joins) lists
   b) array1 + array2     → Adds element-wise

2. If array1.shape = (3, 4) and array2.shape = (3, 4),
   can you add them together?
   ✅ YES - Same shape, compatible

3. What does "broadcasting" mean in NumPy?
   → Applying a scalar operation to every element of an array

4. Why use NumPy for math instead of loops?
   → Much faster (100-1000x), cleaner code, more intuitive

5. If you multiply two arrays with *, is it a matrix multiplication?
   ❌ NO - It's element-wise. Use @ or np.dot() for matrix multiply
""")

print("\n" + "="*80)
print("PRACTICE TIPS")
print("="*80)

print(f"""
✅ DO:
   • Test code as you write it
   • Use .shape to check array dimensions
   • Use .dtype to check data types
   • Print intermediate results to debug
   • Start simple, then add complexity

❌ DON'T:
   • Assume output shape without checking
   • Mix arrays of incompatible shapes
   • Use loops for simple array operations
   • Forget that * is element-wise, not matrix multiply
   • Ignore data type changes

🎯 PRACTICE STRATEGY:
   1. Start with Beginner exercises (⭐)
   2. Make sure you understand each before moving on
   3. Try Intermediate exercises (⭐⭐)
   4. Tackle Advanced exercises (⭐⭐⭐)
   5. Complete the Challenge
   6. Create your own problems and solve them!
""")

print("\n" + "="*80)
print("EXERCISES COMPLETE!")
print("="*80)
print(f"""
You've now practiced:
✅ Basic array arithmetic with scalars and arrays
✅ Element-wise operations
✅ Real-world applications (pricing, conversions, etc.)
✅ Data normalization and standardization
✅ Complex calculations combining multiple operations

Ready for the next milestone? You now have the skills to:
• Build data analysis pipelines
• Manipulate numerical data efficiently
• Apply formulas to entire datasets
• Understand how NumPy works under the hood

Great job! Keep practicing and you'll master NumPy! 🚀
""")
