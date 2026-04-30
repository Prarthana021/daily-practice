class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlength=0
        length=0
        left=0
        right=0
        win=set()
        while right<len(s):
            if s[right] not in win:
                win.add(s[right])
                right+=1
                length=right-left
                maxlength=max(maxlength,length)
            else:
                
                while s[right] in win:
         
                    win.remove(s[left])
                    left+=1
        return maxlength
                    

        