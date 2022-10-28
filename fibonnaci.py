# fib
# Sequence of numbers in which each number is the sum of the two preceding ones and the sequence starts from 0 and 1

fib_memo = {}

def fib(num):
    # Prevent unintentional edge case
    assert num >=0 and int(num) == num, 'Input must be a positive integer number'
    # Establish base case
    if num in [0,1]:
        return num
    else:
    # Recursive case
        if num not in fib_memo:
            fib_memo[num] = fib(num-1) + fib(num-2)
        return fib_memo[num]

print(fib(35))