class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.deq = deque([])
        self.table = defaultdict(lambda: None)

    def get(self, key: int) -> int:
        if self.table[key] is not None:
            # move elem to the front of q
            idx = self.deq.index(key)
            del self.deq[idx]
            self.deq.appendleft(key)
            return self.table[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        
        # check if key is already in the table
        if self.table[key] is not None:
            # do not need to evict key, since the size doesnt changed
            self.get(key)
        # otherwise, insert key to the front of q
        else:
            # check if should evict key
            if len(self.deq)+1 > self.cap:
                rm_key = self.deq.pop()
                self.table[rm_key] = None
            self.deq.appendleft(key)
        
        self.table[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)