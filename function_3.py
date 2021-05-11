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
