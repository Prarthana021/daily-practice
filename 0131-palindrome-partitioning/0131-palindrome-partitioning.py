class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res = []
        cur = []

        def backtrack(i):
            # base case: we've used up the entire string
            if i == len(s):
                res.append(cur.copy())
                return

            # try every possible substring starting from i
            for j in range(i, len(s)):
                substring = s[i:j+1]

                # only continue if this substring is a palindrome
                if substring == substring[::-1]:
                    cur.append(substring)      # make choice
                    backtrack(j + 1)           # explore (j+1 because we used chars up to j)
                    cur.pop()                  # undo choice

        backtrack(0)
        return res