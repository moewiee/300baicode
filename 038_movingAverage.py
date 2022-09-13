class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.list = []

    def next(self, val: int) -> float:
        self.list.append(val)
        if len(self.list) == (self.size + 1):
            self.list.pop(0)
        return sum(self.list) / len(self.list)