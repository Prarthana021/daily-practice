class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=[]
        postfix=[]

        result = 1
        for i in range(len(nums)):
            result *= nums[i]
            prefix.append(result)
        
        result =1
        for i  in range(len(nums)-1,-1,-1):
            result *= nums[i]
            postfix.append(result)  #this will be in reverse order so
        postfix.reverse()

        res=[]
        for i in range(len(nums)):
            left = prefix[i-1] if i > 0 else 1
            right = postfix[i+1] if i < len(nums)-1 else 1
            res.append(left * right)
        
        return res
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

