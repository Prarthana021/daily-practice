class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset=set(nums)

        longest=0
        cnt=0
        for num in numset:
            if num-1 not in numset:
                cnt=1
                while num+cnt in numset:
                    cnt+=1
                longest = max(longest,cnt)
        return longest

            
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset=set(nums)
        count=0
        longest=0

        for num in numset:
            if num-1 not in numset:
                count=1
                while(num+count) in numset:
                    count+=1
                longest=max(longest,count)
        return longest
            
      
        
        
  

                
        