class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])

        pacific_set = set()
        atlantic_set = set()
        pacific_queue = []
        atlantic_queue = []

        # add all Pacific edge cells (top row + left column)
        for j in range(cols):
            pacific_queue.append((0, j))
            pacific_set.add((0, j))
        for i in range(rows):
            pacific_queue.append((i, 0))
            pacific_set.add((i, 0))

        # add all Atlantic edge cells (bottom row + right column)
        for j in range(cols):
            atlantic_queue.append((rows - 1, j))
            atlantic_set.add((rows - 1, j))
        for i in range(rows):
            atlantic_queue.append((i, cols - 1))
            atlantic_set.add((i, cols - 1))

        # BFS helper — same logic for both oceans
        def bfs(queue, visited):
            while queue:
                i, j = queue.pop(0)

                # DOWN
                ni = i + 1
                nj = j
                if ni >= 0 and ni < rows and nj >= 0 and nj < cols:
                    if (ni, nj) not in visited and heights[ni][nj] >= heights[i][j]:
                        visited.add((ni, nj))
                        queue.append((ni, nj))

                # UP
                ni = i - 1
                nj = j
                if ni >= 0 and ni < rows and nj >= 0 and nj < cols:
                    if (ni, nj) not in visited and heights[ni][nj] >= heights[i][j]:
                        visited.add((ni, nj))
                        queue.append((ni, nj))

                # RIGHT
                ni = i
                nj = j + 1
                if ni >= 0 and ni < rows and nj >= 0 and nj < cols:
                    if (ni, nj) not in visited and heights[ni][nj] >= heights[i][j]:
                        visited.add((ni, nj))
                        queue.append((ni, nj))

                # LEFT
                ni = i
                nj = j - 1
                if ni >= 0 and ni < rows and nj >= 0 and nj < cols:
                    if (ni, nj) not in visited and heights[ni][nj] >= heights[i][j]:
                        visited.add((ni, nj))
                        queue.append((ni, nj))

        bfs(pacific_queue, pacific_set)             # run BFS for Pacific
        bfs(atlantic_queue, atlantic_set)           # run BFS for Atlantic

        # find cells in BOTH sets
        result = []
        for i in range(rows):
            for j in range(cols):
                if (i, j) in pacific_set and (i, j) in atlantic_set:
                    result.append([i, j])

        return result