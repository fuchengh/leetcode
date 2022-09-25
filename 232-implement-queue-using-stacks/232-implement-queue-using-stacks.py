class MyQueue:
    def __init__(self):
        self.q = []

    def push(self, x: int) -> None:
        aux = []
        while self.q:
            aux.append(self.q.pop())
        self.q.append(x)
        while aux:
            self.q.append(aux.pop())

    def pop(self) -> int:
        return self.q.pop()

    def peek(self) -> int:
        return self.q[-1]

    def empty(self) -> bool:
        return len(self.q) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()