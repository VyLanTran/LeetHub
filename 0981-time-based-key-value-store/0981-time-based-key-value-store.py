class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        arr = self.map[key]
        left, right = 0, len(arr) - 1
        res = ""

        while left <= right:
            mid = left + (right - left) // 2
            time, val = arr[mid]
            if time <= timestamp:
                res = val
                left = mid + 1
            else:
                right = mid - 1
        
        return res

        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

'''
{
    foo: [(1, bar)]
}
'''