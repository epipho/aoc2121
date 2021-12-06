import re

s = re.compile(r'\s+->\s+|,')

coords = [list(map(int, s.split(c))) for c in open("5.input").readlines()]
# filter out non-straight
coords = [c for c in coords if c[0] == c[2] or c[1] == c[3]]

vals = {}
for ln in coords:
    xs = 1 if ln[0] < ln[2] else -1
    ys = 1 if ln[1] < ln[3] else -1
    for x in range(ln[0], ln[2]+xs, xs):
        for y in range(ln[1], ln[3]+ys, ys):
            if (x, y) not in vals:
                vals[(x, y)] = 0
            vals[(x, y)] += 1

ans = 0
for v in vals.values():
    if v > 1:
        ans += 1

for k, v in vals.items():
    print(k, v)

print(ans)
