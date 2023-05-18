"""
This program will reverse any type of number you passed!
Use reverse_num() function
"""

def reverse_num(number):
    return number[::-1]


if __name__ == '__main__':
    num = str(input("Enter the number:"))
    print(f'Reversed Number of {num} is {reverse_num(num)}')
