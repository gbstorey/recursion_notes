# Factorial
# The product of all positive integers less than or equal to n.
# Only positive numbers.
# 0! = 1

def factorial(n):
    # Unintentional entry edge case
    assert n >=0 and int(n) == n, 'The number must be a positive integer only!'
    # Base cases
    if n in [0,1]:
        return 1
    else:
    #Recursive function call
        return n * factorial(n-1)

print(factorial(4))