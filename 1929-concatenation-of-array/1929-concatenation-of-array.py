class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        size=len(nums)
        res=[0]*2*size

        for i in range(len(res)):
            if i < size:
                res[i]=nums[i]
            else:
                res[i]=nums[i-size]

        return res


  

        
            
        

        