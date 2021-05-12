"""
John would like to create a function to check whether given number is
positive or negative or neutral. Help him to write an independent function
and pass different inputs to the function and check its behaviour
"""
def numCheck(n):
    if(n<0):
        return "Negative"
    elif(n>0):
        return "Positive"
    else:
        return "Neutral"

n= eval(input(""))
result = numCheck(n)
print(result)
    
