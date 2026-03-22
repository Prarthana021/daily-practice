class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(grid,i,j):
            if i<0 or i>=len(grid):
                return 0
            if j<0 or j>=len(grid[0]):
                return 0
            if grid[i][j]==0:
                return 0

            grid[i][j]=0
            area=1

            area+=dfs(grid,i-1,j)
            area+=dfs(grid,i+1,j)
            area+=dfs(grid,i,j+1)
            area+=dfs(grid,i,j-1)

            return area
        
        max_area=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:

                    island_area=dfs(grid,i,j)
                    max_area=max(max_area,island_area)

        return max_area
            

            

        