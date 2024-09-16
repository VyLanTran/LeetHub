class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        '''
        00:00 --> hour * 60 + min = 0
        12:00 --> 12 * 60 + 0 = 720
        23:59 --> 1439 --> rem = 719 or 719 - 720 = -1


        MOD = 720

        0, 1, 2, ..., 719
        '''
        MOD = 1440
        minuteSet = set()
        minDiff = float('inf')

        def convertTimeToMin(timePoint):
            timePoint = timePoint.split(":")
            hourStr, minStr = timePoint
            hour, min = int(hourStr), int(minStr)
            return (hour * 60 + min) % MOD

        for timePoint in timePoints:
            convertedTime = convertTimeToMin(timePoint)
            if convertedTime in minuteSet:
                return 0
            minuteSet.add(convertedTime)
        
        minuteSet = list(minuteSet)
        minuteSet.sort()
        for i in range(len(minuteSet) - 1):
            minDiff = min(minDiff, minuteSet[i + 1] - minuteSet[i])
        minDiff = min(minDiff, minuteSet[0] - minuteSet[-1] + MOD)

        return minDiff
        