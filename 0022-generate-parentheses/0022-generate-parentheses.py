class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        cur=[]
        def dfs(open,close,cur):
            if len(cur)==2*n:
                res.append(cur)
                return

            if open < n:
                dfs(open+1, close, cur + "(")
            if close<open:
                dfs(open,close+1,cur + ")")
        dfs(0,0,"")
        return res


        