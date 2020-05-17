import sys
input = sys.stdin.readline

T = int(input())
for case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    max_val = 0
    for a in arr:
        max_val += max(a, 0)

    squares = set()
    i = 0
    while i ** 2 <= max_val:
        squares.add(i ** 2)
        i += 1
    cnt = 0
    for i in range(N):
        cum = 0
        for j in range(i, N):
            cum += arr[j]
            if cum in squares:
                cnt += 1
    print("Case #{0}: {1}".format(case, cnt))