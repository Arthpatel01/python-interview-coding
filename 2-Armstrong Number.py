"""
This program will return True/False based in Armstrong Number
"""

def is_arm_strong(number):
    if not number:
        return False

    sum = 0
    for row in str(number):
        sum += int(row)**3
    if sum == int(number):
        return True
    else:
        return False

if __name__ == "__main__":
    num = input("Enter Number:")
    print(is_arm_strong(num))