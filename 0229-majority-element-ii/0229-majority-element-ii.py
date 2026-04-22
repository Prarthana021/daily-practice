class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        has={}
        ans=[]

        for num in nums:
            has[num]=has.get(num,0)+1

        for key,value in has.items():
            if value >(n/3):
                ans.append(key)
        return ans
                
        