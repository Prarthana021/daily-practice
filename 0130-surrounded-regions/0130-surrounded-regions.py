class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])
        queue = []

        # STEP 1: find all O's on the border, add to queue
        for j in range(cols):                          # top row
            if board[0][j] == 'O':
                queue.append((0, j))
                board[0][j] = 'S'                      # mark as safe
        for j in range(cols):                          # bottom row
            if board[rows - 1][j] == 'O':
                queue.append((rows - 1, j))
                board[rows - 1][j] = 'S'
        for i in range(rows):                          # left column
            if board[i][0] == 'O':
                queue.append((i, 0))
                board[i][0] = 'S'
        for i in range(rows):                          # right column
            if board[i][cols - 1] == 'O':
                queue.append((i, cols - 1))
                board[i][cols - 1] = 'S'

        # STEP 2: BFS from all border O's, mark connected O's as safe
        while queue:
            i, j = queue.pop(0)

            # DOWN
            ni = i + 1
            nj = j
            if ni >= 0 and ni < rows and nj >= 0 and nj < cols and board[ni][nj] == 'O':
                board[ni][nj] = 'S'
                queue.append((ni, nj))

            # UP
            ni = i - 1
            nj = j
            if ni >= 0 and ni < rows and nj >= 0 and nj < cols and board[ni][nj] == 'O':
                board[ni][nj] = 'S'
                queue.append((ni, nj))

            # RIGHT
            ni = i
            nj = j + 1
            if ni >= 0 and ni < rows and nj >= 0 and nj < cols and board[ni][nj] == 'O':
                board[ni][nj] = 'S'
                queue.append((ni, nj))

            # LEFT
            ni = i
            nj = j - 1
            if ni >= 0 and ni < rows and nj >= 0 and nj < cols and board[ni][nj] == 'O':
                board[ni][nj] = 'S'
                queue.append((ni, nj))

        # STEP 3: final scan
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':                 # not reached from border = surrounded
                    board[i][j] = 'X'                  # flip to X
                elif board[i][j] == 'S':               # was connected to border = safe
                    board[i][j] = 'O'                  # flip back to O