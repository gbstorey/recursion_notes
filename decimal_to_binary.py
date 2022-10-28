# Convert a decimal number to binary using recursion


def d_to_b(n):
    assert int(n) == n, 'The parameter must be an integer only!'
    #Base case where quotient is 0
    if n == 0:
        return n%2
    # Recursive case where quotient is > 0
    # Multiplies previous result by order of magnitude, effectively shifting digits left, so the next remainder can be added to the end
    return (n%2) + 10*(d_to_b(int(n/2)))

print(d_to_b(10))