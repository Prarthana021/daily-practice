class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        j=1
        while j < len(nums):
            if(nums[j]!=nums[i]):
                i+=1 #next place for unique element
                nums[i]=nums[j] #move unique element j is pointing to i 
                
            j+=1
        return i+1
        