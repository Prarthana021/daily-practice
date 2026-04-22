class Solution(object):
    def twoSum(self, nums, target):
        hasmap={}
        for i in range(len(nums)):
            complement=target-nums[i]
            if complement not in hasmap:
                hasmap[nums[i]]=i
            else:
                return [hasmap.get(complement),i]


     
        
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
    
                                                        