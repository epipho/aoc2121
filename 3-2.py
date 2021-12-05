def mcv(inp, pos):
    z = 0
    for i in inp:
        if i[pos] == '0':
            z += 1
    return '0' if z > len(inp) / 2 else '1'

def todec(val):
    ret = 0
    for i, v in enumerate(reversed(val)):
        ret += int(v) * 2**i
    return ret


oxy = [ln.strip() for ln in open("3.input").readlines()]
co2 = oxy.copy()

pos = 0
while len(oxy) > 1:
    v = mcv(oxy, pos)
    oxy = list(filter(lambda x: x[pos] == v, oxy))
    pos += 1

pos = 0
while len(co2) > 1:
    v = mcv(co2, pos)
    co2 = list(filter(lambda x: x[pos] != v, co2))
    pos += 1

oxyv = todec(oxy[0])
co2v = todec(co2[0])

print(oxyv * co2v)
