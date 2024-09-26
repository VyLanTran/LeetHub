class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:

        res = 0

        def rec(i, mydict):
            nonlocal res
            if i >= len(nums):
                if mydict:
                    res += 1
                return
            # print(f"i = {i}, val = {nums[i]}, prev = {nums[i] - k}, after = {nums[i] + k}, myset = {uniqueNums}")
            # print("is true: ", nums[i] - k not in uniqueNums and nums[i] + k not in uniqueNums)
            rec(i + 1, mydict)
            if nums[i] - k not in mydict and nums[i] + k not in mydict:
                
                # uniqueNums.add(nums[i])
                mydict[nums[i]] = mydict.get(nums[i], 0) + 1
                rec(i + 1, mydict)
                # uniqueNums.remove(nums[i])
                mydict[nums[i]] -= 1
                if mydict[nums[i]] == 0:
                    del mydict[nums[i]]
                
        rec(0, {})
        return res

            