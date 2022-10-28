# Find the GCD of two numbers using recursion.
# GCD is the largest positive integer that divides the numbers without a remainder.
# Euclidean algorithm can be used, where num1/num2 with remainder -> num2/remainder with rem2 -> (num2/rem1)/rem2 until remainder =0

def gcd(num1, num2):
    #Constraints
    assert int(num1) == num1 and int(num2) == num2, 'Both numbers must be nonzero integers'
    #Fix return value since mathematically GCD is the same for positive/negative/positive and negative combos
    # Base case where remainder is 0
    if num2 == 0:
        return abs(num1)
    else:
    #Recursive case where remainder is not 0
        return gcd(num2, num1%num2)

print(gcd(-18, 48))