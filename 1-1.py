values = [int(ln) for ln in open("1.input").readlines()]

inc = 0
for i in range(1, len(values)):
    if values[i] > values[i-1]:
        inc += 1

print(inc)
