"""
 Create a function to compute sum of digits. Call this sum of digits function
to find the sum of digits of numbers ranges from 1001 to 22000.
"""
def numChecker(n):
    if((1001<=n) and (n<=22000)):
        sumDigit(n)
    else:
        print("number out of range")
def sumDigit(n):
    tot = 0
    while(n>0):
        dig=n%10
        tot=tot+dig
        n=n//10
    print("The total sum of digits is:",tot)

n = int(input(""))
numChecker(n)
