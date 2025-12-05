import sys
def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
sys.set_int_max_str_digits(100000000000000)


num = int(input("Enter a non-negative integer: "))
print("Factorial of", num, "is", factorial(num))