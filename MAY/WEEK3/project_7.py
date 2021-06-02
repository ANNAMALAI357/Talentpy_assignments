"""
 Write python script to add elements of list L using reduce() function.
 """
import functools 
list1 = input().split()
L = [int(i) for i in list1]
print("The sum of the list elements is : ", end="")
func = lambda a, b: a+b
print(functools.reduce(func, L))

"""
output:
10 20 30 50
The sum of the list elements is : 110
"""
