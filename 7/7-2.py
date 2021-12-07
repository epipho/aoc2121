pos = [int(v) for v in open("7.input").read().split(",")]

# find extents
start = min(pos)
end = max(pos)

best = 9999999999999
for t in range(start, end+1):
    fuel = 0
    for p in pos:
        n = abs(p - t)
        fuel += (n*n + n) / 2
    if fuel < best:
        best = fuel


print(best)
