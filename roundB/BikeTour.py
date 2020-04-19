T = int(input())
for case in range(1, T + 1):
    N = int(input())
    H = list(map(int, input().split()))
    peaks = 0
    for i in range(1, N-1):
        if H[i] > H[i-1] and H[i] > H[i+1]:
            peaks += 1
    print("Case #{0}: {1}".format(case, peaks))