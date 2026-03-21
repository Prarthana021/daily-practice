class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res = []
        cur = []

        def backtrack(i):
            # base case: we've used up the entire string
            if i==len(s):
                res.append(cur.copy())
                return

            for j in range(i,len(s)):
                substring = s[i:j+1]
                if substring == substring[::-1]:
                    cur.append(substring)
                    backtrack(j+1)
                    cur.pop()
        backtrack(0)
        return res
           