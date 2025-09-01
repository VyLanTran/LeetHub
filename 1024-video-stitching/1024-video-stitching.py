class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        '''
        Time: O(nlog(n))
        Space: O(n) - sorting in python takes O(n) space
        '''

        clips.sort(key=lambda clip: (clip[0], clip[1]))

        if clips[0][0] > 0:
            return -1

        res = 0
        cur_end = 0
        i = 0
        n = len(clips)

        while i in range(n):
            if clips[i][0] > cur_end:
                return -1

            max_end = cur_end

            while i in range(n) and clips[i][0] <= cur_end:
                max_end = max(max_end, clips[i][-1])
                i += 1

            if max_end > cur_end:
                cur_end = max_end
                res += 1
            
            if cur_end >= time:
                return res

        return res if cur_end >= time else -1
     


