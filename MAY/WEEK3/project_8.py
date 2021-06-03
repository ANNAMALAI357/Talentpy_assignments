"""
Write python recursive function to perform multiplication of all elements of list L.
"""
def product(l):
  mul = 1
  for x in l:
    mul = mul * x
  return mul
l = input().split()
l = [int(i) for i in l ]
print(product(l))

"""
input:
11 22 33
output:
7986

"""
