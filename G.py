import itertools

def chek(j, k, laund):


for i in range(int(input())):
    n = int(input())
    lis=[]
    for j in range(n):
        sublis = []
        sublis.append('1')
        for x in range(1,j-1):
            sublis.append(combi(x))
        sublis.append('1')
        lis.append(sublis)
    for j in range(n):
        for x in range(j):
            if lis[j][x] % 2 == 0:
                if not (j-1 < 0) and not (x-1 < 0) and (j-1 < n) and (x-1 < j) and (lis[j][x] % 2 == 0):
                    cnt = chek(j-1, x-1, 2)

    print()
    list.extend()