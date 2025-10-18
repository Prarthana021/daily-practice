class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans= [0] * len(nums) # this creates array called [0,0,0,0]
        
        for i in range(len(nums)):
            product=1
            for j in range(len(nums)):
                if i==j:
                    continue
                product *= nums[j]
            ans[i]=product 
        return ans


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [0]*n
        suffix = [0]*n
        
        prefix[0]=nums[0]
        for i in range(1,n):
            prefix[i]=prefix[i-1]*nums[i]
        suffix[n-1]=nums[n-1]
        for j in range(n-2):  # Changed: was range(n-1), should be range(n-2)
            index = n-j-2  # Changed: was n-j-1, should be n-j-2
            suffix[index] = suffix[index+1] * nums[index]
        ans = []  # Changed: start with empty list since you're using append
        for i in range(n):
            if i==0:
                ans.append(suffix[i+1])
            elif i==n-1:  # Changed: was 'if', should be 'elif'
                ans.append(prefix[i-1])
            else:
                ans.append(prefix[i-1]*suffix[i+1])
        return ans
# array   1 2 3 4  
# prefix: 1 2 6 24     precomputed products till that point.....
# suffix: 24 24 12 4
        

