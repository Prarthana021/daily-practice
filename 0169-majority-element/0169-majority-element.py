class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        has={}
        for num in nums:
            has[num]=has.get(num,0)+1
        
        for key,value in has.items():
            if has.get(key) >= n/2:
                return key

        