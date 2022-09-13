class Solution:
    def canAttendMeetings(self, intervals) -> bool:
        timeslot = [0] * 1000000
        for interval in intervals:
            if sum(timeslot[interval[0]:interval[1]]):
                return False
            timeslot[interval[0]:interval[1]] = [1 for _ in range(interval[1] - interval[0])]
        
        return True