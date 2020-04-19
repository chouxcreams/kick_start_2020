T = int(input())
for case in range(1, T + 1):
    N, D = map(int, input().split())
    buses = list(map(int, input().split()))
    ans = 0
    for bus in reversed(buses):
        D -= D % bus

    print("Case #{0}: {1}".format(case, D))