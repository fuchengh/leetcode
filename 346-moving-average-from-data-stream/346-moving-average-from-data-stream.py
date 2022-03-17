class MovingAverage:

    def __init__(self, size: int):
        self.size = 0
        self.max_size = size
        self.nums = deque([])

    def next(self, val: int) -> float:
        if self.size + 1 > self.max_size:
            # pop left and insert new val
            self.nums.popleft()
            self.nums.append(val)
        else:
            self.size += 1
            self.nums.append(val)
        return sum(self.nums) / self.size

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)