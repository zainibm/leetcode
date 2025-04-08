'''
Min Stack
https://leetcode.com/problems/min-stack
https://neetcode.io/problems/minimum-stack
'''
class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        min_val = self.stack[-1]
        temp = []
        while len(self.stack):
            val = self.stack.pop()
            min_val = min(min_val, val)
            temp.append(val)
        while len(temp):
            self.stack.append(temp.pop())
        return min_val