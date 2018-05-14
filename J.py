import copy
def check(now,a,b ,minc ,cnt, flgs):
    minc += a[now]
    flgs[now] = True
    mincnt = 10000000000 * len(a) * len(b)
    cnt -= 1
    if cnt <= 0:
        flgs[now] = False
        return minc
    else:
        for i in range(n):
            if not flgs[i]:
                chek = check(i,a, b,minc + b[now][i],cnt, flgs)
                if mincnt > chek:
                    mincnt = chek
    flgs[now] = False
    return mincnt

for i in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    b =[]
    for j in range(n):
        b.append(list(map(int,input().split())))

    minclick = 10000000000 * len(a) * len(b)
    for now in range(n):
        #initpolace
        flgs = [False for x in range(len(a))]
        rtn = check(now, copy.deepcopy(a), b, 0, len(a),flgs)
        if minclick > rtn:
            minclick = rtn
    print('Case #{}:'.format(i + 1))
    print(minclick)
