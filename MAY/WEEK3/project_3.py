""" Write a generator to get even numbers from 1 to infinity"""

def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 2

for i in infinite_sequence():
  print(i, end=" ")
