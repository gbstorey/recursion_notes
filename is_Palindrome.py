def isPalindrome(string):
    #Base case: if we have reached the middle of the word, then the word is symmetric and all the letters match. Additionally, a blank string would technically be a palindrome, so return True.
    if string == "":
        return True
    #Failed case: if the word is not symmetric, it cannot be a palindrome, so return False.
    if string[0] != string[-1]:
        return False
    #Recursive case: if all the letters have matched and there are letters remaining, continue to the next set of symmetric positions.
    else:
        new_string = string[1:-1]
        return isPalindrome(new_string)

#Complexity: Working from the end of the string to the middle, we have O(n) time complexity. We only use constant assignment operations so space complexity is O(1).

tests = [
    {
        "string": "awesome",
        "isPalindrome": False
    },
    {
        "string": "foobar",
        "isPalindrome": False
    },
    {
        "string": "tacocat",
        "isPalindrome": True
    },
    {
        "string": "amanaplanacanalpanama",
        "isPalindrome": True
    },
    {
        "string": "amanaplanacanalpandemonium",
        "isPalindrome": False
    },
]
success = True
for test in tests:
    if isPalindrome(test['string']) != test['isPalindrome']:
        print(f"Sorry, the test case for {test['string']} failed.")
        success=False

if success:
    print("Congrats, all test cases passed.")
