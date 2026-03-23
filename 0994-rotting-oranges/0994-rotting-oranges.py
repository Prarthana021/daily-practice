class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        queue=[]

        fresh=0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==2:
                    queue.append((i,j))
                if grid[i][j]==1:
                    fresh+=1

        if fresh == 0:
            return 0

        minutes=0 
        while queue:
            n=len(queue)
       

            for k in range(n):
                i,j=queue.pop(0)

                #DOWN
                ni=i+1
                nj=j

                if ni>=0 and ni<rows and nj>=0 and nj<cols and grid[ni][nj]==1:
                    grid[ni][nj]=2
                    fresh-=1
                    queue.append((ni,nj))
                
                # UP
                ni = i - 1
                nj = j
                if ni >= 0 and ni < rows and nj >= 0 and nj < cols and grid[ni][nj] == 1:
                    grid[ni][nj] = 2
                    fresh -= 1
                    queue.append((ni, nj))

                # RIGHT
                ni = i
                nj = j + 1
                if ni >= 0 and ni < rows and nj >= 0 and nj < cols and grid[ni][nj] == 1:
                    grid[ni][nj] = 2
                    fresh -= 1
                    queue.append((ni, nj))

                # LEFT
                ni = i
                nj = j - 1
                if ni >= 0 and ni < rows and nj >= 0 and nj < cols and grid[ni][nj] == 1:
                    grid[ni][nj] = 2
                    fresh -= 1
                    queue.append((ni, nj))
                
            minutes+=1
        if fresh == 0:
            return minutes - 1
        else:
            return -1

    