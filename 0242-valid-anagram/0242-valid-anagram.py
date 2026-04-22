class Solution:
    def isAnagram(self, s:str,t:str)-> bool:
        str_s={}
        str_t={}

        for str in s:
            str_s[str]=str_s.get(str,0)+1
        for str in t:
            str_t[str]=str_t.get(str,0)+1
        
        return str_s==str_t




       