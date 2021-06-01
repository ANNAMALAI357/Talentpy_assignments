"""
Write a simple generator which can give prime numbers from range 1 to 5000.
"""
def generator_func():
    for num in range(1,5001):
        result=True
        for y in range(2,num):
            if num%y==0:
                result = False
        if result==True:
            yield num

for i in generator_func():
    print(i)
    
