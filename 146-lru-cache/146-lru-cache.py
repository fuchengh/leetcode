class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.table = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.table.keys():
            # move elem to the end of q
            self.table.move_to_end(key)
            return self.table[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        
        # check if key is already in the table
        if key in self.table.keys():
            # do not need to evict key, since the size doesnt changed
            self.get(key)
        # otherwise, insert key to the front of q
        else:
            # check if should evict key
            if len(self.table)+1 > self.cap:
                self.table.popitem(last=False)
        
        self.table[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)