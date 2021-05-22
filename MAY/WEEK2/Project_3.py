def diff(S,K):
    list1 = list(S)
    list2 = []
    for i in range(len(S)):
        if S[i] == K:
            k = int(i)
            list2.append(k)
    first = list2[0]
    last = list2[-1]
    a = (last-first)-1
    return a
S = str(input().lower())
K = str(input().lower())
print(diff(S,K))
