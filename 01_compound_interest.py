"""
Exercise 1.1 – Compound Interest

Objective:
Calculate the final amount using the compound interest formula:
A = C * (1 + r)^n
Where:
- C = initial capital
- r = annual interest rate (as decimal)
- n = number of years
"""

# Input from the user
C = float(input("Initial capital: "))
r = float(input("Annual interest rate (as decimal, e.g., 0.05): "))
n = int(input("Number of years: "))

# Compound interest formula
A = C * (1 + r) ** n

# Output
print(f"Final amount after {n} years: {A:.2f}")
