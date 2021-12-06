import re

def get_step(c0, c1):
    if c0 == c1:
        return 0
    if c0 > c1:
        return -1
    return 1

s = re.compile(r'\s+->\s+|,')

coords = [list(map(int, s.split(c))) for c in open("5.input").readlines()]

vals = {}
for ln in coords:
    print(ln)
    xs = get_step(ln[0], ln[2])
    ys = get_step(ln[1], ln[3])
    x = ln[0]
    y = ln[1]
    while x != ln[2]+xs or y != ln[3]+ys:
        print(x, y)
        if (x, y) not in vals:
            vals[(x, y)] = 0
        vals[(x, y)] += 1
        x += xs
        y += ys

ans = 0
for v in vals.values():
    if v > 1:
        ans += 1

for k, v in vals.items():
    print(k, v)

print(ans)
