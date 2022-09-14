class Solution:
    def highFive(self, items: list) -> list:
        d ={}
        for item in items:
            if item[0] in d.keys():
                d[item[0]] += [item[1]]
            else:
                d[item[0]] = [item[1]]
        ret = []
        for student in range(1, 1001):
            if student in d.keys():
                ret.append([student, int(sum(sorted(d[student])[-5:]) / 5)])
        
        return ret