#Find the sum of digits of a positive integer number using recursion.

def sum_digits(n):
    #Constraints
    assert n >=0 and int(n) == n, 'The number must be a positive integer.'
    if n ==0:
        #Base case where n can no longer be reduced and the final 2 digits can be added.
        return 0
    else:
        # Recursive case where n/10 is not less than 100 and must be divided again. 
        return int(n%10) + sum_digits(int(n/10))

print(sum_digits(2929))