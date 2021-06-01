"""
Write a function called is_unique. This function should take a string and should check
whether all characters of the string is unique/not. Example: If the input string is
“abcd”, all characters are unique, hence it should return True. Another example, if the
string is “abaa”, then this function should return False.
1. Create a List L of size 10 with random strings of length > 1.
2. Write a python snippet to check is_unique nature for all elements of L. (Hint:
Use map function)
3. Apply filter function, to get only unique elements from L.
"""
import random
import string
# check if the element is unique and return true or false
def is_unique(L):
  if(len(set(L)) == len(L)):
    return True
  else:
    return False

List1 =[]
for i in range(0,10):
  n = ''.join(random.choices(string.ascii_uppercase,k=10))
  List1.append(n)

nature = lambda x: is_unique(x)
L = list(map(nature,List1))
print("STRING\t\tNATURE\n")
for i in range(0,len(L)):
  print(List1[i],"",L[i])
unique_elements = list(filter(nature,List1))
print("\nTHE UNIQUE ELEMENTS ARE :\t",unique_elements)
"""
output:

STRING      NATURE

RCJBRULJJU  False
YCDVLVRPRB  False
HOHWHMPCBQ  False
CBKOQRLUXI  True
FGPNZQYJFJ  False
BUINRJOGON  False
VBJGAEISRK  True
NKJULKGFUW  False
BDGSLPWWHF  False
IXPQCFNFXW  False

THE UNIQUE ELEMENTS ARE :    ['CBKOQRLUXI', 'VBJGAEISRK']
"""
