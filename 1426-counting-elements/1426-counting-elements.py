class Solution:
    def countElements(self, arr: List[int]) -> int:
        res = 0
        counter = Counter(arr)

        for num, freq in counter.items():
            if num + 1 in counter:
                res += freq


        return res
