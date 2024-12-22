class Solution(object):
    def countFishInComp(self, row, col, maxrow, maxcol, grid):
        fish = 0
        if  0 <= row < maxrow and 0 <= col < maxcol and grid[row][col] > 0:
            fish += grid[row][col]
            grid[row][col] = 0
            fish += self.countFishInComp(row+1, col, maxrow, maxcol, grid)
            fish += self.countFishInComp(row-1, col, maxrow, maxcol, grid)
            fish += self.countFishInComp(row, col+1, maxrow, maxcol, grid)
            fish += self.countFishInComp(row, col-1, maxrow, maxcol, grid)
        return fish

    def findMaxFish(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        mostfish, row, col, = 0, len(grid), len(grid[0])

        for i in range(row):
            for j in range(col):
                if grid[i][j] > 0:
                    curfish = self.countFishInComp(i, j, row, col, grid)
                    mostfish = max(mostfish, curfish)

        return mostfish



                    
                    

        
    
        