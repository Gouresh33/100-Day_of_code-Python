enemies = 1


def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")


# def is_prime_trial_division(n):
#
#     if n <= 1:
#         return False
#
#     for i in range(2, int(n**0.5) + 1):
#
#         if n % i == 0:
#             return False
#
#     return True

""""Refer the following for prime number program"""

def is_prime(num):
    if num == 2:
        return True
    if num == 1:
        return False

    # Loop through all the numbers between 2 and the number
    for i in range(2, num):
        # Check if the number (num) can be divided by the potential prime number
        if num % i == 0:
            return False

    # this return is outside the for loop which will only run once the loop finishes and none of the numbers are divisible. Therefore it is prime.
    return True
