class TimeMap:

    def __init__(self):
        self.map = dict()        

    def set(self, key: str, value: str, timestamp: int) -> None:
        arr = self.map.get(key, [])
        arr.append((timestamp, value))
        self.map[key] = arr

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""
        arr = self.map[key]
        i, j = 0, len(arr) - 1
        while i <= j:
            mid = i + (j - i) // 2
            tup = arr[mid]
            time, val = tup[0], tup[1]
            if time > timestamp:
                j = mid - 1
            elif mid == len(arr) - 1 or (mid + 1 < len(arr) and arr[mid + 1][0] > timestamp):
                return val
            else:
                i = mid + 1
        return ""
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)