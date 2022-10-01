# Calculate the power of a number using recursion.

def power(base, exp):
    assert int(exp) == exp and exp>=0, 'Exponent must be a positive integer'
    if exp == 0:
        return 1
    return base*power(base, exp-1)

print(power(3.2, 3))