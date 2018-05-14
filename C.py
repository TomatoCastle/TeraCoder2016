for i in range(int(input())):
    w, h=map(int,input().split())
    townmap =[]
    hppy_point = -9
    mhy = -1
    mhx = -1

    for j in range(h):
        townmap.append(list(map(int, input().split())))


    for a in range (h):
        for b in range(w):
            if townmap[a][b] == 0:
                nowp = 0
                #such
                for c in range(a - 1, a + 2):
                    for d in range(b - 1, b + 2):
                        if not(c < 0) and not (d < 0) and (c < h) and (d < w):
                            nowp += townmap[c][d]
                if nowp > hppy_point:
                    hppy_point = nowp
                    mhy = a
                    mhx = b


    print('Case #{}:'.format(i + 1))
    if hppy_point > 0:
        print('{} {}'.format(mhx, mhy))
    else:
        print('NG')