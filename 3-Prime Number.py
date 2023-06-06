"""
This program will return True if the passed number is Prime Number.
"""


def check_prime_number(number):
    number = int(number)
    if number > 1:
        for i in range(2, number // 2):
            if number % i == 0:
                """Is Not Prime Number"""
                return False
            else:
                """Is Prime Number"""
                return True
    else:
        """Not A Prime Number"""
        return False


if __name__ == '__main__':
    num = input("Enter the Number:")
    print(check_prime_number(num))
