class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()
        res=[]
        def dfs(i, cur, total):
            if total==target:
                res.append(cur.copy())
                return
            if total>target or i>=len(candidates):
                return

            cur.append(candidates[i])
            dfs(i+1,cur,total + candidates[i])

            cur.pop()
            while( i+1 < len(candidates) and candidates[i] == candidates[i + 1] ):
                i +=1
            dfs(i+1,cur, total) # The second call just passes the ball to the next candidate. THAT candidate will add to total if it gets taken inside its own call.

        
        dfs(0,[],0)
        return res

        