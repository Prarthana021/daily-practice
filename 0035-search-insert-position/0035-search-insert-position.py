class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1

        while left<=right:
            mid = (left + right) // 2

            if nums[mid]<target:
                left+=1
            elif nums[mid]>target:
                right-=1
            else:
                return mid
        return left #when loop ends left is exactly where target should go
            
        