for i in range(int(input())):
    n, l=map(int,input().split())
    mas = 0
    for j in range(n):
        cnt = 0
        s, m = map(list,input().split())
        for z in range(len(s)):
            if s[z] == m[z]:
                cnt +=1

        mas += len(s) - cnt
    print('Case #{}:'.format(i + 1))
    if l > mas : print('NG')
    else: print('OK')
