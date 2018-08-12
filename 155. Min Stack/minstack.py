#-*- coding: UTF-8 -*-

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.minVal = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.data.append(x)
        if len(self.minVal) == 0:
            self.minVal.append(x)
        else:
            if(x > self.minVal[-1]):
                x = self.minVal[-1]
            self.minVal.append(x)

    def pop(self):
        """
        :rtype: void
        """
        self.minVal.pop()
        self.data.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.data[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.minVal[-1]

if __name__ == '__main__':
    stack = MinStack()
    stack.push(1)
    stack.push(2)
    stack.push(0)
    stack.push(-1)
    stack.push(3)
    top = stack.top()
    print(top)
    stack.pop()
    stack.pop()
    min = stack.getMin()
    print(min)