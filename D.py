for i in range(int(input())):
    max=0
    n = int(input())
    p = sorted(list(map(int,input().split())))
    e = list(map(int,input().split()))
    for j in range(len(p)):
        min = 10000
        en = -1
        for m in range(len(e)):
            if e[m] >= p[j] or e[m] == 10000:
                continue
            if min > (p[j] - e[m]):
                min = p[j] - e[m]
                en = m
        if en != -1:
            max+=1
            e[en] = 10000

    print('Case #{}:'.format(i + 1))
    print(max)
