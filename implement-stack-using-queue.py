from collections import deque

class MyList:
    def __init__(self):
        self.list = deque()
    
    def push(self, x):
        return self.list.append(x)
        

    def pop(self):
        return self.list.pop()
        

    def top(self):
        return self.list[-1]
        

    def empty(self):
        return len(self.list) == 0
