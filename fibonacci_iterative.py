"""
In this program we will be print fibonacci series of given number using iterative method.
"""

n = input("Please Enter the Number:")

first = 0
second = 1
result = 0
for row in range(0, int(n)):
    if row <= 1:
        result = row
    else:
        result = first + second
        first = second
        second = result
    print(result)