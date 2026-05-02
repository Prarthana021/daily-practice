class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sum=0
        minwindow=float("inf")
        left=0
        winlen=0
        for right in range(len(nums)):
            sum+=nums[right]
 
            while sum >= target:
                winlen=right-left+1 #only calclulate window lengeth when we get valid answer 
                minwindow=min(minwindow,winlen)
                sum-=nums[left]
                left+=1
                winlen-=1
            
           
          
        return 0 if minwindow == float("inf") else minwindow





             
        