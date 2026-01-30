class Solution:
    def containsDuplicate(self, nums:List[int])->bool:
        myset=set()
        for i in range(len(nums)):
            if nums[i] in myset:
                return True
            myset.add(nums[i])
        return False
            
#Or even compare the length of array and length of set by converting it to set
#len(set(nums))==len(nums)




            