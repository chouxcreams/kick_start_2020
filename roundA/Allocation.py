import sys
input = sys.stdin.readline
T = int(input())
for case in range(T):
    N, B = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    val = 0
    for i in range(N):
        val += A[i]
        if val > B:
            answer = "".join(("Case #", str(case + 1), ": ", str(i)))
            print(answer)
            break
    else:
        answer = "".join(("Case #", str(case + 1), ": ", str(N)))
        print(answer)

