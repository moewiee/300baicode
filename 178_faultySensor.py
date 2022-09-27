class Solution:
    def badSensor(self, sensor1: list, sensor2: list) -> int:
        while sensor1 and sensor1[0] == sensor2[0]:
            sensor1.pop(0)
            sensor2.pop(0)
        if len(sensor1) == 0: return -1
        if sensor1[:-1] == sensor2[1:] and sensor2[:-1] != sensor1[1:]: return 1
        if sensor2[:-1] == sensor1[1:] and sensor1[:-1] != sensor2[1:]: return 2
        return -1