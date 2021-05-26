"""Write a list comprehension to find factorial of each numbers in a given list L if and only
if the numbers are even. For Example: If L = [1,2,3,4] then output should be [2, 24]."""

def factorial(x):
    fact = 1
    for y in range(1,x + 1):
       fact = fact*y
    return fact
      

def factofeven(num):
    evenList = [i for i in num if i%2==0]
    factList = [factorial(j) for j in evenList]
    return factList
        

num = list(map(int, input().split()))
print(factofeven(num))
