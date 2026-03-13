class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        sub=[]

        def dfs(j):
            if j>=len(nums):
                res.append(sub.copy())
                return
            
            sub.append(nums[j])
            dfs(j+1)

            sub.pop()
            dfs(j+1)
        dfs(0)
        return res



   



        