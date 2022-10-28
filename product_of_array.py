def productOfArray(arr: list):
    
    if len(arr) == 0:
        return 1
    else:
        num = arr[-1]
        del arr[-1]
        return num * productOfArray(arr)

print(productOfArray([1,2,3,10]))
