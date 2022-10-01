# Fibonnaci
# Sequence of numbers in which each number is the sum of the two preceding ones and the sequence starts from 0 and 1

#Naive Recursive

def fibonnaci(n):
    # Prevent unintentional edge case
    assert n >=0 and int(n) == n, 'Input must be a positive integer number'
    # Establish base case
    if n in [0,1]:
        return n
    else:
    # Recursive case
        return fibonnaci(n-1) + fibonnaci(n-2)

print(fibonnaci(8))