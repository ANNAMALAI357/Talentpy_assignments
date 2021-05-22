"""project 1
1 or 89 application.
Mr.Talentpy would like to create a func,on one_or_eight which takes an integer input (no) and
performs following opera,on.
1. Square the number if it is single digit. (Eg: 3, then 3 * 3 = 9)
2. If it is not single digit, square each digits and add. (Eg: 12, then (1*1) + (2*2) = 1+4 = 5
You have to repeat step (1) and (2) un,l you reach 1 or 89. Note that, always your result will reach
1 or 89 for sure. Input must be a positive number.
If the operation reaches at the end, 89 return True, if operation reaches 1 at the end return False.
Sample Input/Output: 1
• Input: 3
• Output : 3 *3 = 9 => 9 * 9 => 81 => (64+1) = 65 => (36+25) = 61 => (36+1) => 37 = (9+49) => 58
=> (25+64) => 89.
• Explanation : True
Sample Input/Output: 2
• Input: 10
• Output : 1 square + 0 square = 1+0 = 1
• Explanation : False 
"""
def one_or_eight(n):
  # for one digit numbers 
  if(n<10):
    result = n*n
    if(result == 1):
        return False
    elif(result == 89):
        return True
    else:
        return one_or_eight(result)
# for two digit numbers
  else:
    a = [int(x) for x in str(n)]
    result = sum(map(lambda i : i * i, a))
    if(result == 1):
        return  False
    elif(result==89):
        return True
    else:
        return one_or_eight(result)
    




n = int(input(""))
value = one_or_eight(n)
print(value)

