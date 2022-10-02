class TimeMap:
    def __init__(self):
        self.table = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.table:
            self.table[key] = []
        self.table[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key in self.table:
            # binary search for largest timestamp <= target timestamp
            idx = bisect_left(self.table[key], timestamp, key=lambda x: x[0])
            if idx != len(self.table[key]) and self.table[key][idx][0] == timestamp:
                # same as target, return
                return self.table[key][idx][1]
            else:
                idx = max(0, idx-1)
                if self.table[key][idx][0] <= timestamp:
                    return self.table[key][idx][1]
        return ""

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)