class Solution(object):
    def search(self, nums, target):
        return self.modified_binary_search(nums, target, 0, len(nums) - 1)

    def modified_binary_search(self, nums, target, left, right):
        if left>right:
            return -1
        mid=(left+right) // 2
        if nums[mid]==target:
            return mid


        if nums[mid] >= nums[left]:
            if target >= nums[left] and target <= nums[mid]:
                return self.modified_binary_search(nums, target, left, mid - 1)
            else:
                return self.modified_binary_search(nums,target,mid+1,right)
        else:
            if target >= nums[mid] and target <= nums[right]:
                return self.modified_binary_search(nums, target,mid+1,right)
            else:
                return self.modified_binary_search(nums, target,left,mid-1)
            