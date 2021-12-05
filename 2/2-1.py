inp = [ln.split() for ln in open("2.input").readlines()]

depth = 0
pos = 0

for cmd, amt in inp:
    if cmd == 'forward':
        pos += int(amt)
    elif cmd == 'down':
        depth += int(amt)
    elif cmd == 'up':
        depth -= int(amt)

print(f"POST: {pos}, DEPTH: {depth}, {pos*depth}")
