inp = [ln.split() for ln in open("2.input").readlines()]

depth = 0
pos = 0
aim = 0

for cmd, amt in inp:
    if cmd == 'forward':
        pos += int(amt)
        depth += int(amt) * aim

    elif cmd == 'down':
        aim += int(amt)
    elif cmd == 'up':
        aim -= int(amt)

print(f"POST: {pos}, DEPTH: {depth}, {pos*depth}")
