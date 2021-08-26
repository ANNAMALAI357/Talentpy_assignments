from main import DateOperations as DO
from main import MathOperations as MO

class1 = DO()
class2 = MO()
print("Please the os operation you want to do:")
print("""1.Current date 
2.Square root the given number
3.value of the number x raised to the power of y""")
i = int(input())
if(i==1):
    print(class1.get_current_date())
elif(i==2):
    num = int(input("Enter the number"))
    print(class2.get_square_root(num))
elif(i==3):
    x = int(input("enter the value of x"))
    y = int(input("enter the value of y"))
    print(class2.get_power_val(x,y))
else:
    print("enter the correction option")
