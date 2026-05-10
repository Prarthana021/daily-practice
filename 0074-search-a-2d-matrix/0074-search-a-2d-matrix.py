class Solution(object):
    def searchMatrix(self, matrix, target):
        row_index = self.searchRow(matrix, target)

        if row_index != -1:
            return self.binarySearchRow(matrix, row_index, target)

        return False


    def searchRow(self, matrix, target):
        low = 0
        high = len(matrix) - 1
        last_col = len(matrix[0]) - 1

        while low <= high:
            mid = (low + high) // 2

            first = matrix[mid][0]
            last = matrix[mid][last_col]

            if first <= target and target <= last:
                return mid

            elif target > last:
                low = mid + 1

            else:
                high = mid - 1

        return -1


    def binarySearchRow(self, matrix, row_index, target):
        low = 0
        high = len(matrix[row_index]) - 1

        while low <= high:
            mid = (low + high) // 2

            value = matrix[row_index][mid]

            if value == target:
                return True

            elif value > target:
                high = mid - 1

            else:
                low = mid + 1

        return False