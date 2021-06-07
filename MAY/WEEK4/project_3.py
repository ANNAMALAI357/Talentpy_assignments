"""
Create a class Printer with a default constructor and a method called print_me(data), which
returns the data that comes as argument.
Example: Let’s say obj is the object for Printer class.
	 	 	 res = obj.print_me(“Welcome”)
	 	 	 print(result)
Output: Welcome
"""
class Printer:
    def print_me(data):
        return data

obj = Printer
result = obj.print_me("Welcome")
print(result)
