# A Basic Calculator Operation in Python

## Maintainer: Khandaker Saleh Mohammad Tajuddin

## What this project does

A basic calculator that performs addition, subtraction, multiplication, and division operations in Python.

## Features

| Operation | Description | Example |
|-----------|-------------|---------|
| `add(a, b)` | Returns the sum of a and b | `add(5, 3) → 8` |
| `subtract(a, b)` | Returns the difference of a and b | `subtract(10, 4) → 6` |
| `multiply(a, b)` | Returns the product of a and b | `multiply(3, 4) → 12` |

## Usage

```python
from src.utils import add, subtract, multiply

result = add(5, 3)       # Returns 8
result = subtract(10, 4) # Returns 6
result = multiply(3, 4)  # Returns 12
```

## Project Structure

```
├── README.md
├── src/
│   ├── main.py
│   └── utils.py
├── docs/
│   └── project-description.md
└── .gitignore
```
