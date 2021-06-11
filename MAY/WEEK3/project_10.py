"""
Write a generator which can give random values every time.
"""
import random
def randomNum():
  yield random.randint(0,100000000)

print(randomNum().__next__())
