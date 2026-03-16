class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        res=[]

        def dfs(i,cur,total):
            if (total==target):
                res.append(cur.copy())
                return
            if(i>=len(candidates) or total > target):
                return

            cur.append(candidates[i])
            dfs(i,cur,total+candidates[i]) #stay at the same element so i

            cur.pop()
            dfs(i+1,cur,total)  #move to different element so its i+1

        dfs(0,[],0)
        return res
            
        