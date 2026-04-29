class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
# i = slow pointer (tracks where to place the next unique element)
# j = fast pointer (scans through the array)
        i=0
        j=1

        for j in range(len(nums)):
            if nums[i]!=nums[j]:
                i+=1
                nums[i]=nums[j] #nums[0] in untouched now 1st posn is nums[j] if unique
            j+=1
        return i+1






