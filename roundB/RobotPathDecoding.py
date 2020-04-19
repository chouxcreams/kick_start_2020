T = int(input())
for case in range(1, T + 1):
    commands = input()
    w, h = 1, 1
    coefs = []
    times = 1
    for s in commands:
        if s == 'N':
            h -= times
        elif s == 'S':
            h += times
        elif s == 'W':
            w -= times
        elif s == 'E':
            w += times
        elif s == '(':
            pass
        elif s == ')':
            times //= coefs.pop()
        else:
            coef = int(s)
            times *= coef
            coefs.append(coef)
    w %= 10 ** 9
    h %= 10 ** 9
    if w == 0:
        w = 10 ** 9
    if h == 0:
        h = 10 ** 9
    print("Case #{0}: {1} {2}".format(case, w, h))