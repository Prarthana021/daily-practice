class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=[0]*len(nums)
        postfix=[0]*len(nums)
        ans=[0]*len(nums)
        length=len(nums)
        prefix[0]=1
        postfix[length-1]=1
        for i in range(1,length):
            prefix[i]=prefix[i-1]*nums[i-1]
        for i in range(length-2,-1,-1):
            postfix[i]=postfix[i+1]*nums[i+1]

        for i in range(len(nums)):
            ans[i]=prefix[i]*postfix[i]

        return ans
