"""
Create a python class DateOperations with following methods Hint: Use Datetime module
1. get_current_date() -> This function should return today’s date in format DD/MM/
YYYY. Example: 18/03/1994.
 Create a python class MathOperations with following methods Hint: Use math module
1. get_square_root(no) -> This function should return square root of given number 
2. get_power_val(x,y) -> The function should return X power Y as output. (Example: 
X=3, Y=2 , then 3 power 2 => 3 * 3 = 9)
Create another file runner.py and import DateOperations and MathOperations classes and 
call the methods get_current_date, get_square_root and get_power_val.
"""
from datetime import date
import math

class DateOperations:
    def __init__(self):
        pass
    def get_current_date(self):
        return date.today().strftime('%d/%m/%Y')

class MathOperations:
    def __init__(self):
        pass
    def get_square_root(self,number):
        return math.sqrt(number)
    def get_power_val(self,x,y):
        return math.pow(x,y)

