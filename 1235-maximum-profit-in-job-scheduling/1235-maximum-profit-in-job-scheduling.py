class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        '''
        sort by start time, then endTime
        0, 1, 2,  3, 4
        1, 2, 3,  4, 6
        3, 5, 10, 6, 9
        20,20,100,70,60
        
        create an array of next job with startTime[j] >= endTime[i]
        
        T(i) = max profit for jobs with index >= i
        T(i) = max{
           1. take this job
                profit[i] + T(j), j is the next job with startTime[j] >= endTime[i]
            2. skip this job
                T(i + 1)
        }
        T(i) = 0 if i >= n
            = profit[i] if i == n - 1
        cache = {
            4: 60,
            3: 130
        }
        
        T(0) = max{
            20 + T(2) = 20 + 130 = 150
            T(1) = 130
        }
        T(2) = max{
            100 + T(5) = 100  ==> notice here when do for loop cuz 5 is out of bound
            T(3) = 130
        }
        T(3) = max{
            70 + T(4)  = 130
            T(4)
        }
        T(4) = 60
        T(1) = max{
            20 + T(4) = 60
            T(2) = 130
        }
        '''
        
        n = len(startTime)
        jobs = [(startTime[i], endTime[i], profit[i], i) for i in range(n)]
        jobs = sorted(jobs, key = lambda x:(x[0]))
        cache = dict()
        
        def findNextJob():
            def binSearch(i):
                left, right = i + 1, n - 1
                end = jobs[i][1]
                while left <= right:
                    mid = left + (right - left) // 2
                    if end > jobs[mid][0]:
                        left = mid + 1
                    elif mid - 1 >= 0 and end > jobs[mid - 1][0]:
                        return mid
                    else:
                        right = mid - 1
                return left
            
            nextJob = [n for _ in range(n)]
            for i in range(n - 1):
                # binary search
                nextJob[i] = binSearch(i)
                
            return nextJob
        
        nextJob = findNextJob()
        
        def rec(i):
            if i == n:
                return 0
            if i == n - 1:
                return jobs[i][2]
            if i in cache:
                return cache[i]
            res = max(jobs[i][2] + rec(nextJob[i]), rec(i + 1))
            cache[i] = res
            return res
        
        return rec(0)
            
        