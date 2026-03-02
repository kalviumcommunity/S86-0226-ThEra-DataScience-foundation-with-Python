"""
Loops Milestone: For and While Loops in Python
================================================
This script demonstrates:
- for loops for iterating over sequences
- while loops for condition-based repetition
- break and continue for loop control
- Avoiding infinite loops
"""

# 1. For Loops: Iterating over a range and a list
print("=" * 50)
print("1. FOR LOOPS")
print("=" * 50)

# Iterate over a range of numbers
print("Numbers from 1 to 5:")
for i in range(1, 6):
    print(f"  {i}")

# Iterate over a list
fruits = ["Apple", "Banana", "Cherry"]
print("\nFruits:")
for fruit in fruits:
    print(f"  {fruit}")

# Using the loop variable
print("\nFruit lengths:")
for fruit in fruits:
    print(f"  {fruit}: {len(fruit)} characters")

# 2. While Loops: Condition-based repetition
print("\n" + "=" * 50)
print("2. WHILE LOOPS")
print("=" * 50)

count = 0
while count < 3:
    print(f"Count is {count}")
    count += 1
print("Loop ended when count reached 3.")

# 3. Controlling Loop Flow: break and continue
print("\n" + "=" * 50)
print("3. BREAK AND CONTINUE")
print("=" * 50)

print("Break example (stop at 3):")
for i in range(1, 6):
    if i == 4:
        print("  Breaking loop at 4!")
        break
    print(f"  {i}")

print("\nContinue example (skip 3):")
for i in range(1, 6):
    if i == 3:
        print("  Skipping 3!")
        continue
    print(f"  {i}")

# 4. Avoiding Infinite Loops
print("\n" + "=" * 50)
print("4. AVOIDING INFINITE LOOPS")
print("=" * 50)

# Example of a safe while loop
max_attempts = 5
attempt = 0
while attempt < max_attempts:
    print(f"Attempt {attempt+1} of {max_attempts}")
    attempt += 1
print("Loop finished safely.")

# Example of a potential infinite loop (commented out)
# Uncommenting the following lines would cause an infinite loop:
# while True:
#     print("This would run forever!")
#     # break  # Only a break would stop it

print("\nAlways ensure your loop condition will eventually become False!")