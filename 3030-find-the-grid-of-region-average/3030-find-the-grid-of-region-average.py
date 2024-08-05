class Solution:
    def resultGrid(self, image: List[List[int]], threshold: int) -> List[List[int]]:
        
        dirs = [[-1,0], [1,0], [0,-1], [0,1]]
        
        def isRegion(top, left):
            bot, right = top + 2, left + 2
            sumIntensity = 0
            for i in range(top, bot + 1):
                for j in range(left, right + 1):
                    val = image[i][j]
                    sumIntensity += val
                    for di, dj in dirs:
                        newI, newJ = i + di, j + dj
                        if newI >= top and newJ >= left and newI <= bot and newJ <= right:
                            if abs(val - image[newI][newJ]) > threshold:
                                # print(i, j, newI, newJ, abs(val - image[newI][newJ]))
                                return False, None
            return True, sumIntensity // 9
        
        rows, cols = len(image), len(image[0])
        intensityGrid = [[[] for _ in range(cols)] for _ in range(rows)]
        res = [[image[i][j] for j in range(cols)] for i in range(rows)]
        
        for i in range(rows):
            for j in range(cols):
                if not (i + 2 < rows and j + 2 < cols):
                    continue
                regionBool, avgIntensity = isRegion(i, j)
                # print(regionBool, avgIntensity)
                if not regionBool:
                    continue
                for x in range(i, i + 3):
                    for y in range(j, j + 3):
                        intensityGrid[x][y].append(avgIntensity)
        for i in range(rows):
            for j in range(cols):
                if intensityGrid[i][j]:
                    res[i][j] = sum(intensityGrid[i][j]) // len(intensityGrid[i][j])
                    
        return res
        

        # arr = [1, 2, 3]
        # print(sum(arr)  // len(arr))
                                
            