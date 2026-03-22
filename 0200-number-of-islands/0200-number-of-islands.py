class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def dfs(grid,i,j):
            if i < 0 or i >= len(grid):            # row is out of bounds (above or below grid)
                return
            if j < 0 or j >= len(grid[0]):      # col is out of bounds (left or right of grid)
                return
            if grid[i][j] == '0':                  # this cell is water OR already visited
                return    
            
            grid[i][j]=0

            dfs(grid,i-1,j)
            dfs(grid,i+1,j)
            dfs(grid, i,j-1)
            dfs(grid, i,j+1)   

        count=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1':
                    count+=1
                    dfs(grid,i,j)
                    
                        

        return count 
        