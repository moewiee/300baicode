class TwoSum:

    def __init__(self):
        self.data = {}

    def add(self, number: int) -> None:
        if number in self.data.keys():
            self.data[number] += 1 
        else:
            self.data[number] = 1
        

    def find(self, value: int) -> bool:
        for s in self.data.keys():
            if value - s in self.data.keys(): 
                if s == value - s:
                    if self.data[s] > 1:
                        return True
                else:
                    return True
        return False