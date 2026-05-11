class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left=0
        right=len(nums)-1

        while left < right: #[not <= bcuz we ain't doing if xyz= target we dont know it yet]
            mid = (left+right)//2
            if nums[mid] > nums[right]: #meaning we take unsroted array
                left = mid+1
            else:
                right=mid
        return nums[right]
