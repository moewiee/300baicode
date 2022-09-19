class Solution:
    def destCity(self, paths: list) -> str:
        allCity = set()
        startCity = set()
        for p in paths:
            allCity.add(p[0])
            allCity.add(p[1])
            startCity.add(p[0])
        for ac in allCity:
            if ac not in startCity:
                return ac