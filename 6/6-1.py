class Fish:
    def __init__(self, timer):
        self.timer = timer

    # simulate 1 day
    def sim(self):
        self.timer -= 1
        if self.timer < 0:
            self.timer = 6
            return Fish(8)

fish = [Fish(int(v)) for v in open("6.input").read().split(",")]

for day in range(1, 81):
    new_fish = []
    for f in fish:
        n = f.sim()
        if n:
            new_fish.append(n)

    fish.extend(new_fish)
    print(f"Day {day}: {len(fish)}")
