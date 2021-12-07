fish = [int(v) for v in open("6.input").read().split(",")]

counts = [0]*9
for f in fish:
    counts[f] += 1

for d in range(0, 256):
    # number to duplicate
    new = counts[0]
    # shift all
    for i in range(1, 9):
        counts[i-1] = counts[i]
    # add new
    counts[6] += new
    counts[8] = new

    total = sum(counts)
    print(f"Day {d}: {total}")
