'''
Number of Students Unable to Eat Lunch
https://leetcode.com/problems/number-of-students-unable-to-eat-lunch
'''
from collections import deque

def countStudents(students, sandwiches) -> int:
    q = deque(students)
    while q:
        if sandwiches[0] not in q:
            return len(q)
        else:
            student = q.popleft()
            if student == sandwiches[0]:
                sandwiches.pop(0)
            else:
                q.append(student)
    return len(q)

print(countStudents([1, 1, 0, 0], [0, 1, 0, 1])) # 0
print(countStudents([1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 1])) # 3