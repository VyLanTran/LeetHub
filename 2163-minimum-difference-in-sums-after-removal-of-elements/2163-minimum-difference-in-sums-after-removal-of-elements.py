class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        '''
        first, find n


        n = 2
        0,1 ,2 ,3 ,4,5
        7,9 ,5 ,8 ,1,3
        _,16,12,12,6,4
        _,1 ,2 , 2,4,5

        for each i, find min sum_first
        maintaing a max heap containing the n min numbers
        heap = [  3, 1]
        i = 0: -1 (not possible)
        i = 1: 16, (last index used = 1)
        i = 2: 12 (2)
        i = 3: 12 (2)
        i = 4: 6 (4)
        i = 5: 4 (5)

        min_heap = [8, 9]
        i = 5: -1
        i = 4: 4   
            if last_used[i] < i, use sum_first[i]
            else, use sum_first[i-1] (if None, then break)
            12 - 4 = 8
        i = 3: 11
            12 - 11 = 1
        i = 2: 13
            16-13=3
        i = 1: 17


        '''

        size = len(nums)
        n = size // 3
        max_heap = []
        sum_first, last_used = [None] * size, [None] * size
        cur_sum = 0
        # print(n)

        for i, num in enumerate(nums):
            if len(max_heap) < n:
                heappush(max_heap, -num)
                cur_sum += num
                # last_used[i] = i
            elif -max_heap[0] > num:
                # print(i, num, max_heap)
                removed_num = -heappop(max_heap)
                heappush(max_heap, -num)
                cur_sum += num - removed_num
                # last_used[i] = i
            # else:
            #     last_used[i] = last_used[i - 1]

            if len(max_heap) >= n:
                sum_first[i] = cur_sum
        # print(sum_first)
        cur_sum = 0
        min_heap = []
        res = float('inf')

        for i in range(size - 1, -1, -1):
            j = i + 1
            # print(f"i={i}, j={j}")
            if j + n <= size:
                if i >= n - 1:
                    # print(f"right_start={j}, left_end={i}, cur_right_sum={cur_sum}")
                    res = min(res, sum_first[i] - cur_sum)
            num = nums[i]
            if len(min_heap) < n:
                heappush(min_heap, num)
                cur_sum += num
            elif num > min_heap[0]:
                removed_num = heappop(min_heap)
                heappush(min_heap, num)
                cur_sum += num - removed_num

        return res


            
            

