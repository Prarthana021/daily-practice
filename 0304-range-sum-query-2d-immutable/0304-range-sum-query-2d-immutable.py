class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows = len(matrix)
        cols = len(matrix[0])

        # We are creating a prefix matrix where we store sums.
        # Size is +1 row and +1 column to make the math easier.
        # This creates (rows + 1) rows.
        # Each row has (cols + 1) columns.
        # All values are initialized to 0.
        self.prefixSum = [[0] * (cols + 1) for _ in range(rows + 1)]

        # Build the prefix sum matrix
        for r in range(rows):
            for c in range(cols):
                current = matrix[r][c]

                # sum above current cell in prefix matrix
                top = self.prefixSum[r][c + 1]

                # sum left of current cell in prefix matrix
                left = self.prefixSum[r + 1][c]

                # overlap area counted twice, so subtract it
                topLeft = self.prefixSum[r][c]

                # Store sum from original matrix (0,0) to (r,c)
                # We use r+1 and c+1 because prefixSum has extra row and col
                self.prefixSum[r + 1][c + 1] = current + top + left - topLeft
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # Convert original matrix indexes to prefixSum indexes
        # because prefixSum is shifted by +1 row and +1 column
        row1 += 1
        col1 += 1
        row2 += 1
        col2 += 1

        # Big rectangle from (0,0) to bottom-right
        total = self.prefixSum[row2][col2]

        # Remove area above the required rectangle
        top = self.prefixSum[row1 - 1][col2]

        # Remove area left of the required rectangle
        left = self.prefixSum[row2][col1 - 1]

        # Add back overlap because it was removed twice
        topLeft = self.prefixSum[row1 - 1][col1 - 1]

        return total - top - left + topLeft