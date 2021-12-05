class Board:

    def __init__(self, f, sx, sy):
        self.sx = sx
        self.sy = sy
        self.vals = []
        for i in range(0, sy):
            self.vals.extend([int(v) for v in f.readline().split()])

        self.marks = [1]*len(self.vals)

    def mark(self, v):
        try:
            self.marks[self.vals.index(v)] = 0
        except:
            pass

    def check(self):
        # check rows
        for r in range(0, self.sy):
            sum = 0
            for c in range(0, self.sx):
                sum += self.marks[r*self.sx+c]
            if sum == 0:
                return True
        # check cols
        for c in range(0, self.sx):
            sum = 0
            for r in range(0, self.sy):
                sum += self.marks[r*self.sx+c]
            if sum == 0:
                return True

        return False

    def score(self, v):
        score = 0
        for i, m in enumerate(self.marks):
            score += m*self.vals[i]
        return score*v

with open("4.input") as f:
    draws = [int(i) for i in f.readline().split(',')]
    boards = []
    while len(f.readline()) > 0:
        boards.append(Board(f, 5, 5))

    for d in draws:
        for b in boards:
            b.mark(d)
            if b.check():
            # done!
                print(b.score(d))
                exit(1)
