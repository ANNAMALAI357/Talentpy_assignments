def A(string):
    return string[::-1]

def B(string):
    count = 0
    strlist = list(string)
    for ele in strlist:
        if ele in["a","A"]:
            count+=1
    return count

def C(string,index):
    return string[index]

def D(string,index):
    if (index == 0):
        return "complete without multiply"
    else:
        return string*5

string = input()
print(D(C(A(string),(B(A(string)))),(B(A(string)))))
        



