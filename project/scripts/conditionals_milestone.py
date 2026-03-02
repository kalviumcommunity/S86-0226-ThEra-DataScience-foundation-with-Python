"""
Conditionals milestone demonstration script

Demonstrates:
- basic if
- if-else
- if-elif-else
- logical operators (and, or, not)

Run this file to see printed decision paths for several sample values.
"""

def basic_if(x):
    print(f"basic_if: input={x}")
    if x > 0:
        print("  -> x is positive")
    print()


def if_else(n):
    print(f"if_else: input={n}")
    if n % 2 == 0:
        print("  -> n is even")
    else:
        print("  -> n is odd")
    print()


def if_elif_else(score):
    print(f"if_elif_else: score={score}")
    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    elif score >= 60:
        grade = 'D'
    else:
        grade = 'F'
    print(f"  -> grade = {grade}")
    print()


def logical_operators_examples(age, has_permission, is_member):
    print(f"logical_operators: age={age}, has_permission={has_permission}, is_member={is_member}")
    # and: both conditions must be true
    if age >= 18 and has_permission:
        print("  -> allowed (age >= 18 AND has_permission)")
    else:
        print("  -> not allowed (failed AND check)")

    # or: either condition suffices
    if is_member or has_permission:
        print("  -> access granted (is_member OR has_permission)")
    else:
        print("  -> access denied (failed OR check)")

    # not: invert a boolean
    if not has_permission:
        print("  -> warning: permission missing (NOT has_permission)")
    print()


def run_examples():
    print('\n--- Conditional Statements Milestone Demo ---\n')

    # 1. Basic if
    basic_if(5)
    basic_if(-2)

    # 2. if-else
    if_else(4)
    if_else(7)

    # 3. if-elif-else
    for s in (95, 82, 76, 63, 50):
        if_elif_else(s)

    # 4. logical operators
    logical_operators_examples(age=20, has_permission=True, is_member=False)
    logical_operators_examples(age=16, has_permission=False, is_member=True)
    logical_operators_examples(age=15, has_permission=False, is_member=False)


if __name__ == '__main__':
    run_examples()
