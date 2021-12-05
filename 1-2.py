values = [int(ln) for ln in open("1.input").readlines()]

sums = []
for i in range(0, len(values)-2):
    sums.append(values[i] + values[i+1] + values[i+2])

inc = 0
for i in range(1, len(sums)):
    if sums[i] > sums[i-1]:
        inc += 1


print(inc)
