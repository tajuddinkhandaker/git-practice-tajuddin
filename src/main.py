from datetime import date
from utils import add, subtract, multiply, divide

# Print name
print("Khandaker Saleh Mohammad Tajuddin")

# Print today's date
today = date.today()
print(today)

# Calculator operations with error handling
operations = [
    ("add", add, 10, 4),
    ("subtract", subtract, 10, 4),
    ("multiply", multiply, 3, 5),
    ("divide", divide, 20, 4),
    ("divide by zero", divide, 10, 0),  # This will trigger error handling
    ("invalid input", add, "hello", 5),   # This will trigger error handling
]

for name, func, a, b in operations:
    try:
        result = func(a, b)
        print(f"{func.__name__}({a}, {b}) = {result}")
    except (ValueError, TypeError) as e:
        print(f"Error in {name}: {e}")
