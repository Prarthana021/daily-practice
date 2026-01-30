class Solution:
    def isAnagram(self, s:str,t:str)-> bool:
        map1={}
        map2={}

        for i,n in enumerate(s):
            map1[n]= 1+map1.get(n,0)
        for i,n in enumerate(t):
            map2[n]=1+map2.get(n,0)
        return map1==map2
            