from heapq import heappush, heappop, heapify

T = int(input())
for case in range(T):
    N, K = map(int, input().split())
    M = list(map(int, input().split()))
    diffs = []
    heapify(diffs)
    for i in range(1, N):
        heappush(diffs, M[i-1] - M[i])

    for _ in range(K):
        diff = heappop(diffs)
        if diff == -1:
            answer = "".join(("Case #", str(case + 1), ": 1"))
            print(answer)
            break
        a = diff // 2
        b = diff - a
        if a < b:
            a += 1
        else:
            b += 1
        heappush(diffs, a)
        heappush(diffs, b)
    else:
        answer = "".join(("Case #", str(case + 1), ": ", str(-heappop(diffs))))
        print(answer)