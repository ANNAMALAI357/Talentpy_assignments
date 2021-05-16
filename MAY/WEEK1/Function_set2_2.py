"""
You are going to design a magical calculator with the following functions.
• Function that takes input and calculates it’s factorial. (A)
• Function that takes input and calculate it’s sum of digits. (B)
• Function that takes input and find’s the largest digit in the input. (C)
- Implement all the above functions.
- Get input and pass the input to factorial function (A), get the output from
factorial function and pass it as input to sum of digits function (B). Get the output
from sum of digits function, add the output with random 5 digit number and pass
the outcome to largest digit function (C) and print the output that you receive from
function C.
Sample I/O:
• Input 5
• Output of A = 120
• Output of B(120) = 1+2+0 = 3
• Output of C(3 + 10000 = 10003) = 3 (Here 10000 is the random number)
• Hence output is 3 , where 3 is the largest digit of 10003.
"""
import random
def  A():
    fact = 1
    for i in range(1,num+1):
        fact = fact*i
    return fact
def B(fact):
    tot = 0
    while(fact>0):
        dig=fact%10
        tot=tot+dig
        fact=fact//10
    return tot
        
def C(tot):
    larNum = tot+rand
    larNum = str(larNum)
    larlist = [int(x) for x in larNum]
    return max(larlist)
    
    
num = int(input("Enter the Number : "))
rand = random.randint(10000,99999)
print(C(B(A())))



