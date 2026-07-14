# O(n^2) solution
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        total_students = len(students)
        student_queue = deque(students)
        
        res = total_students

        for sandwich in sandwiches:
            count = 0
            
            while count < total_students and student_queue[0] != sandwich:
                student_queue.append(student_queue.popleft())
                count += 1
            
            if student_queue[0] == sandwich:
                student_queue.popleft()
                res -= 1
            else:
                break
        
        return res