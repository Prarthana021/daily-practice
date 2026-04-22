class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first=strs[0]
        p=""
        for i in range(len(first)):
            ch=first[i]
            for str in strs:
                if i>=len(str) or ch!=str[i]:
                    return p
            p+=ch
        return p






                    






        