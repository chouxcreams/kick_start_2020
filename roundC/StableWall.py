T = int(input())
c2i = lambda c: ord(c) - ord('A')
i2c = lambda i: chr(i + ord('A'))


class Polyominos:
    def __init__(self, name):
        self.name = name
        self.deps = set()
        self.exist = False


for case in range(1, T + 1):
    R, C = map(int, input().split())
    wall = [list(input()) for _ in range(R)]
    upper_row = wall[0]
    polys = {}
    for name in upper_row:
        polys[name] = Polyominos(name)
    for row in wall[1:]:
        for i in range(C):
            name = row[i]
            upper_tile = upper_row[i]
            if name not in polys:
                polys[name] = Polyominos(name)
            if upper_row[i] != row[i]:
                polys[upper_tile].deps.add(name)
        upper_row = row

    prev_put = None
    put = []
    while len(polys) > 0:
        now_put = None
        names = polys.keys()
        for name in names:
            poly = polys[name]
            if prev_put in poly.deps:
                poly.deps.remove(prev_put)
            if now_put is not None:
                continue
            if len(poly.deps) == 0:
                now_put = name
                put.append(name)

        if now_put is None:
            ans = "-1"
            break
        del polys[now_put]
        prev_put = now_put

    else:
        ans = ''.join(put)
    print("Case #{0}: {1}".format(case, ans))