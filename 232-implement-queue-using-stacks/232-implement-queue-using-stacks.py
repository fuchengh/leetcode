class MyQueue:
    def __init__(self):
        self.q = []
        self.aux = []

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        self.peek()
        return self.aux.pop()

    def peek(self) -> int:
        if not self.aux: # push to aux only if aux is empty (keep the order)
            while self.q:
                self.aux.append(self.q.pop())
        return self.aux[-1]

    def empty(self) -> bool:
        return len(self.q) == 0 and len(self.aux) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()