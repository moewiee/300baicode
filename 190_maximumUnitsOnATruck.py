class Solution:
    def maximumUnits(self, boxTypes: list, truckSize: int) -> int:
        boxes = []
        for box in boxTypes:
            for _ in range(box[0]): boxes.append(box[1])
        boxes.sort()
        return sum(boxes[-truckSize:])