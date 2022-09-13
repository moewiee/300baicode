class Solution:
    def allSame(self, students):
        if len(set(students)) == 1:
            return True
        return False
    
    def countStudents(self, students: list, sandwiches: list) -> int:        
        while students[0] == sandwiches[0]:
            students.pop(0)
            sandwiches.pop(0)

        while not self.allSame(students):
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
            else:
                students.append(students[0])
                students.pop(0)
        
        while len(students) and students[0] == sandwiches[0]:
            students.pop(0)
            sandwiches.pop(0)

        return len(students)


if __name__ == "__main__":
    s = Solution()

    assert s.countStudents([1,1,0,0], [0,1,0,1]) == 0
    assert s.countStudents([1,1,1,0,0,1], [1,0,0,0,1,1]) == 3

    print("TEST PASSED!")