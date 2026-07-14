# Using counter
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # store the total length of students
        res = len(students)
        # count the number of students who prefer 0 vs 1
        hashmap = Counter(students)

        # loop through each sandwiches
        for sandwich in sandwiches:
            # if there exists student who wants that sandwich?
            # decrease the number of students that want that sandwich
            # decrease the result by 1
            if hashmap[sandwich] > 0:
                hashmap[sandwich] -= 1
                res -= 1
            # if no student exist who want sandwich, exit and return the 
            # left out students
            else:
                return res
        
        return res