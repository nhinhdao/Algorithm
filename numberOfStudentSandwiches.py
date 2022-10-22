
from collections import deque


class Node:
    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next

class Solution(object):
    def countStudents(self, students, sandwiches):
        count = 0
        while len(students) > count:
            if students[0] == sandwiches[0]:
                count = 0
                students = students[1:len(students)]
                sandwiches = sandwiches[1:len(sandwiches)]
            else:
                count += 1
                students.append(students[0])
                students = students[1:len(students)]
        
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




student = [0,0,0,1,1,1,1,1,1,0,1,1,1,1,0,1,1,1,1,0,0,1,1,1,0,1,0,1,1,0,0,0,0,0,1,1,1,1,0,0,0,0,0,1,1,1]
sandwich = [1,0,0,0,0,0,0,1,1,0,1,1,0,1,1,1,0,0,0,1,1,0,1,1,1,1,1,1,1,0,0,1,0,0,1,0,1,0,1,0,1,1,1,0,1,0]
test = Solution()
print(test.countStudentsUsingLinkedList(student, sandwich))