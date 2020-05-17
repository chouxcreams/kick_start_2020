T = int(input())
for case in range(1, T + 1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    flag = False
    prev = -1
    cnt = 0
    for n in arr:
        if n == prev - 1:
            if n == 1:
                cnt += 1
                prev = -1
                continue
            prev -= 1
        else:
            prev = -1
        if n == K:
            prev = K

    print("Case #{0}: {1}".format(case, cnt))