class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hasmap={}
        
        for i in range(len(nums)):
            if target-nums[i] in hasmap:
                return ([i,hasmap.get(target-nums[i])])
            else:
                hasmap[nums[i]]=i
        

        return [0,0]


                

        