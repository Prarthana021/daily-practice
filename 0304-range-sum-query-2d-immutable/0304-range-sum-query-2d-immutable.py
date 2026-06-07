class NumMatrix:

    def __init__(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])

        # Step 1: Create prefix matrix full of 0s
        # It has one extra row and one extra column
        self.prefix = []

        for r in range(rows + 1):
            row = []

            for c in range(cols + 1):
                row.append(0)

            self.prefix.append(row)

        # Step 2: Fill the prefix matrix
        for r in range(rows):
            for c in range(cols):
                current_value = matrix[r][c]

                prefix_row = r + 1
                prefix_col = c + 1

                above = self.prefix[prefix_row - 1][prefix_col]
                left = self.prefix[prefix_row][prefix_col - 1]
                overlap = self.prefix[prefix_row - 1][prefix_col - 1]

                self.prefix[prefix_row][prefix_col] = (
                    current_value + above + left - overlap
                )

    def sumRegion(self, row1, col1, row2, col2):
        # Shift original matrix indexes to prefix matrix indexes
        row1 = row1 + 1
        col1 = col1 + 1
        row2 = row2 + 1
        col2 = col2 + 1

        total = self.prefix[row2][col2]

        above_area = self.prefix[row1 - 1][col2]
        left_area = self.prefix[row2][col1 - 1]
        overlap_area = self.prefix[row1 - 1][col1 - 1]

        return total - above_area - left_area + overlap_area