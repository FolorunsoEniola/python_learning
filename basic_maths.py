#  use_advanced_math.py
# use_advanced_math.py

from advanced_math import square_root, power
from advanced_math import sin as sine, cos as cosine

x = 16
y = 2
angle = 30

print(f"Square root of {x}: {square_root(x)}")
print(f"{x} to the power of {y}: {power(x, y)}")
print(f"Sine of {angle} degrees: {sine(angle):.2f}")
print(f"Cosine of {angle} degrees: {cosine(angle)}")

#another math operations file
import math_operations

result_add = math_operations.add(5, 3)
result_subtract = math_operations.subtract(10, 4)
result_multiply = math_operations.multiply(2, 6)
result_divide = math_operations.divide(15, 3)

print(f"Addition: {result_add}")
print(f"Subtraction: {result_subtract}")
print(f"Multiplication: {result_multiply}")
print(f"Division: {result_divide}")
print(f"Value of PI: {math_operations.PI}")
