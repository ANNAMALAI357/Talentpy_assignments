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
    
