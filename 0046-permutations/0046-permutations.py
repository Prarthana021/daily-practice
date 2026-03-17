class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        cur=[]
        def dfs(i):
            if len(cur)==len(nums):
                res.append(cur.copy())
                return
            
            
            for num in nums:
                if num in cur:
                    continue
                cur.append(num)
                dfs(cur)
                cur.pop()
        dfs(0)
        return res



            