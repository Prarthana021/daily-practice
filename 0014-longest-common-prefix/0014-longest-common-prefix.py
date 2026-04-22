class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        basic=strs[0]
        p=""
        for i in range(len(basic)):
            ch=basic[i]
            for j in strs:
                if i >= (len(j)) or ch != j[i]:
                   return p
        
            p+=ch
        return p
                    






        