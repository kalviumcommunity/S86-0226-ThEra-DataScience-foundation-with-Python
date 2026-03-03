"""
Functions milestone demonstration script.

Defines simple functions accepting parameters and returning results.
Shows how to call them, store outputs, and compose results.
"""

def add(a, b):
    """Return the sum of a and b."""
    return a + b


def multiply(a, b):
    """Return the product of two numbers."""
    return a * b


def greet(name):
    """Return a greeting message for the given name."""
    return f"Hello, {name}!"


def area_rectangle(width, height):
    """Return the area of a rectangle with given dimensions."""
    return width * height


def no_return_example(x):
    """Demonstrate a function that prints but does not return.

    This is a common beginner mistake; the caller receives None.
    """
    print(f"inside no_return_example: x={x}, but not returning")
    # intentionally no return statement


def run_examples():
    print("\n--- Functions Milestone Demo ---\n")

    # 1. call simple functions and print returned results directly
    print("add(3, 4):", add(3, 4))
    print("multiply(2, 5):", multiply(2, 5))
    print("greet('Alice'):", greet("Alice"))

    # 2. store return values in variables for reuse
    sum_result = add(10, 20)
    product_result = multiply(sum_result, 3)
    area = area_rectangle(width=5, height=6)
    message = greet("Bob")

    print(f"stored sum_result: {sum_result}")
    print(f"product using sum_result: {product_result}")
    print(f"area of rectangle 5x6: {area}")
    print(f"message stored: {message}")

    # 3. compose functions by feeding return values into others
    double_area = multiply(area, 2)
    print(f"double area: {double_area}")

    # 4. use returned value in further computation
    final_value = add(product_result, double_area)
    print(f"final_value (product + double_area): {final_value}")

    # 5. show example of function that doesn't return (returns None)
    result = no_return_example(5)
    print(f"result of no_return_example stored in variable: {result!r}")

    # 6. call functions with a loop and different arguments
    for pair in [(1, 2), (5, 7), (0, 0)]:
        print(f"add{pair} = {add(*pair)}")


if __name__ == "__main__":
    run_examples()
