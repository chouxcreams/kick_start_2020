import sys
input = sys.stdin.readline

T = int(input())

def ans(case, val):
    answer = "".join(("Case #", str(case + 1), ": ", str(val)))
    print(answer)

for case in range(T):
    N, K, P = map(int, input().split())
    stacks = []
    for _ in range(N):  # each stacks
        plates = list(map(int, input().split()))
        stack = [0] * (K + 1)
        for i in range(K):  # each plate in the stack
            stack[i + 1] = stack[i] + plates[i]
        stacks.append(stack)

    dp = [[-1] * (P + 1) for _ in range(N+1)]
    dp[0][0] = 0
    for n in range(1, N+1):
        stack = stacks[n-1]
        dp[n][0] = 0
        for k in range(1, K+1):
            val = stack[k]
            for p in range(k, P+1):
                if dp[n-1][p-k] == -1:
                    continue
                dp[n][p] = max(dp[n-1][p-k] + val, dp[n-1][p], dp[n][p])
    ans(case, dp[N][P])
