class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        left, right = 0, n - 1
        
        def canReach(lastBuilding):
            arr = []
            for i in range(lastBuilding):
                diff = heights[i + 1] - heights[i]
                if diff > 0:
                    arr.append(diff)
            # print("before", arr)
            arr.sort(reverse = True)
            # print("after", arr)
            sum = 0
            for i in range(ladders, len(arr)):
                sum += arr[i]
                if sum > bricks:
                    return False
            return True
        
        # print(canReach(3))
                
        while left <= right:
            mid = left + (right - left) // 2
            if not canReach(mid):
                right = mid - 1
            elif mid == n - 1 or not canReach(mid + 1):
                return mid
            else:
                left = mid + 1
                
        return n - 1
    
    '''
    0, 1, 2, 3
          l  r
    m = 2
    '''
            