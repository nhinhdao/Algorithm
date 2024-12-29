
from collections import deque


class Node:
    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next

class Solution(object):
    def countStudents(self, students, sandwiches):
        count = 0
        top = 0

        while len(students) > count:
            student = students.pop(0)
            
            if student == sandwiches[top]:
                top += 1
                count = 0
            else:
                students.append(student)
                count += 1
        
        return count

    def countStudentsUsingQueue(self, students, sandwiches):
        count = 0
        sandwichTop = 0
        queue = deque(students)

        while len(queue) > count:
            topStudent = queue.popleft()
            if topStudent == sandwiches[sandwichTop]:
                count = 0
                sandwichTop += 1
            else:
                count += 1
                queue.append(topStudent)

        return count

    def countStudentsUsingLinkedList(self, students, sandwiches):
        head = tail = Node(students[0], None)
        count = 0
        sandwichTop = 0
        lenQueue = len(students)
        for i in range(1, len(students)):
            node = Node(students[i], None)
            tail.next = node
            tail = tail.next
    
        while lenQueue > count:
            if head.val == sandwiches[sandwichTop]:
                count = 0
                sandwichTop += 1
                node = head.next
                head.next = None
                head = node
                lenQueue -= 1
            else:
                count += 1
                node = head.next
                tail.next = head
                tail = tail.next
                head.next = None
                head = node


        return count


def countStudentsUsingList(students, sandwiches):
    """
    [1,1,1,0,0,1] 6
    [1,0,0,0,1,1]

    count 6
    6 [1,1,0,0,1] [0,0,0,1,1]
    5 [1,0,0,1,1] [0,0,0,1,1]
    4 [0,0,1,1,1] [0,0,0,1,1]
    3 [0,1,1,1] [0,0,1,1]
    2 [1,1,1] [0,1,1]
    1
    """
    # [1,1,1] [0,1,1] [1,1] [1,1]
    

    while students:
        student = students.pop(0)
        
        if student == sandwiches[0]:
            sandwiches.pop(0)
        else:
            students.append(student)
        
        if len(set(students)) == 1 and students[0] != sandwiches[0]:
            break
    
    return len(students)
        


students = [0,0,0,1,1,1,1,1,1,0,1,1,1,1,0,1,1,1,1,0,0,1,1,1,0,1,0,1,1,0,0,0,0,0,1,1,1,1,0,0,0,0,0,1,1,1]
sandwiches = [1,0,0,0,0,0,0,1,1,0,1,1,0,1,1,1,0,0,0,1,1,0,1,1,1,1,1,1,1,0,0,1,0,0,1,0,1,0,1,0,1,1,1,0,1,0]
# test = Solution()
# print(test.countStudentsUsingLinkedList(students, sandwiches))

print(countStudentsUsingList([1,1,1,0,0,1], [1,0,0,0,1,1]))
# print(len(set([1,1,1])))