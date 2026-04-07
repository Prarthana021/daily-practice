class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset=set(nums)
        length=0
        maxlen=0

        for i in range(len(nums)):
            if i not in numset:
                length=1
            while nums[i]+length in numset:
                length+=1
                maxlen=max(maxlen,length)
        return maxlen


                
        