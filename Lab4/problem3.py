val = input("Enter a word: ")
def checkpalindrome(val):
    pal = ""
    for i in range(len(val) - 1, -1, -1):
        pal += val[i]
    if pal == val:
        return "The word is a palindrome"
    else:
        return "The word is not a palindrome"

print(checkpalindrome(val))