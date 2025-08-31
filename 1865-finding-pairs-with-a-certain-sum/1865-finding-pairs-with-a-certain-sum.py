class FindSumPairs:
    '''
    Time: 
        init: O(n + m)
        add: O(1)
        count: O(n)
    Space: O(n + m)
    '''

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums2 = nums2
        self.counter1 = Counter(nums1)
        self.counter2 = Counter(nums2)
        

    def add(self, index: int, val: int) -> None:
        self.counter2[self.nums2[index]] -= 1
        self.nums2[index] += val
        self.counter2[self.nums2[index]] += 1

    def count(self, tot: int) -> int:
        res = 0
        for key1, value1 in self.counter1.items():
            res += value1 * self.counter2[tot - key1]
        return res


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)

