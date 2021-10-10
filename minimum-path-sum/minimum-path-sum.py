class Solution:
    def minPathSum(self, grid):
      
        if grid == []:
            return 0
        m = len(grid)
        n = len(grid[0])
        temp = [[0 for i in range(n)] for j in range(m)]
        temp[0][0] = grid[0][0]
        for i in range(1,m):
            temp[i][0] = temp[i-1][0] + grid[i][0]
        for j in range(1,n):
            temp[0][j] = temp[0][j-1] + grid[0][j]
            
        for i in range(1,m):
            for j in range(1,n):
                temp[i][j] = min(temp[i][j-1], temp[i-1][j]) + grid[i][j]
            
        return temp[-1][-1]