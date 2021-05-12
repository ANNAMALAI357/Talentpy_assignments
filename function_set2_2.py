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



