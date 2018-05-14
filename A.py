for i in range(int(input())):
    m, n = map(int, input().split())
    b = m
    for j in range(int(n)):
        b += int(str(input()))
    print('Case #{}:'.format(i + 1))
    if b < 0: print('NG')
    else: print('OK')