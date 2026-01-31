class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mymap={}
        for i,n in enumerate(nums):
            if target-nums[i] in mymap and mymap[target-nums[i]]!=i:
                return i,mymap[target-nums[i]]
            mymap[n]=i
            
            

        