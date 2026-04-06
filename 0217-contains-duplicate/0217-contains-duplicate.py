class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hasmap={}
        for i in range(len(nums)):
            hasmap[nums[i]]= 1+ hasmap.get(nums[i],0)
           
        for j in hasmap.values():
            if j>=2:
                return True
            
        return False
            

       




        

        