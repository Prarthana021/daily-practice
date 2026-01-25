class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        while l<=r:
            m=(l+r)//2
            if nums[m]>=nums[r]:
                l=m+1
            else:
                r= m #not m-1 because m itself can be minimum so we cant discard it
        return nums[r]


        