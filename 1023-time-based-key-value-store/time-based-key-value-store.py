import bisect
class TimeMap:

    def __init__(self):
        self.d = defaultdict(list)
        self.d1 = defaultdict(list)


    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append(value)
        self.d1[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        idx = bisect.bisect_right(self.d1[key],timestamp)-1
        if idx < 0:
            return ""
        return self.d[key][idx]



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)