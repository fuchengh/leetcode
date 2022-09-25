class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.q = [None for _ in range(k)]
        self.front = self.rear = -1

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.rear = (self.rear + 1) % self.size
        self.q[self.rear] = value
        if self.front == -1:
            self.front = 0
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.q[self.front] = None
        if self.front == self.rear: # only one element in q
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        return True

    def Front(self) -> int:
        return self.q[self.front] if self.front >= 0 else -1

    def Rear(self) -> int:
        return self.q[self.rear] if self.rear >= 0 else -1

    def isEmpty(self) -> bool:
        return self.front == -1

    def isFull(self) -> bool:
        return (self.front == self.rear + 1) or (self.front == 0 and self.rear == self.size-1)


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()