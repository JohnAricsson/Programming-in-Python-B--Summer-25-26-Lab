num = int(input("Enter a number : "))

def checkEven(num):
    return num%2==0
if(checkEven(num)): print("Even")
else: print("Odd")