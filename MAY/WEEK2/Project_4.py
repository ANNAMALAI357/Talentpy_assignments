"""
Be Positive!  Create a function to sum up all positive argument inputs. Inputs ranges from 0 to N,
where N can be any positive number.
"""
def sumof(*a):
    k = []
    for ele in list1:
        if ele > 0:
            k.append(ele)
        else:
            continue
    return sum(k)
#Enter inputs with space
N = input().split()
list1 = []
for i in N:
    a = int(i)
    list1.append(a)
print(sumof(list1))
