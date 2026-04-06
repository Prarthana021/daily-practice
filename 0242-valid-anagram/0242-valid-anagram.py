class Solution:
    def isAnagram(self, s:str,t:str)-> bool:
        map1={}
        map2={}

        if len(s)!=len(t):
            return False

        for i in s:
            map1[i]= 1+ map1.get(i,0)
        for i in t:
            map2[i]= 1+map2.get(i,0)

        for i in s:
            if map1.get(i)!=map2.get(i):
                return False
        return True
            

       