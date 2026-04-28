class Solution:
    def validPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s) - 1

        while start < end:
            if s[start] == s[end]:
                start += 1
                end -= 1
            else:
                return self.palindrome(s, start + 1, end) or self.palindrome(s, start, end - 1)

        return True #if its a palindrom and we never enter else blcok 

    def palindrome(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1

        return True



        


        