inp = [ln.strip() for ln in open("3.input").readlines()]

mcb = []
for p in range(0, len(inp[0])):
    z = 0
    for i in inp:
        if i[p] == '0':
            z += 1
    mcb.append(0 if z > len(inp) / 2 else 1)

gamma = 0
epsilon = 0

mcb.reverse()
for i, v in enumerate(mcb):
    gamma += v * 2**i
    epsilon += (0 if v == 1 else 1) * 2**i

print(gamma*epsilon)
