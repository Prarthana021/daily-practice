class Solution:
    def minWindow(self, s: str, t: str) -> str:
        mapT={}
        mapS={}
        res=""
        for ch in t:
            mapT[ch]=mapT.get(ch,0)+1
        
        left=0
        for right in range(len(s)):
            mapS[s[right]]=mapS.get(s[right],0)+1

            while self.contains(mapT,mapS): #for valid window
                if res=="" or right-left+1 < len(res): #check and record minimum valid
                    res=s[left:right+1]. #if min valid is available 
                mapS[s[left]]-=1 # even if not if t in s then we shrink window and check again 
                left+=1
        return res

    
    def contains(self,mapT,mapS):
        for ch in mapT:
            if mapT.get(ch,0)>mapS.get(ch,0):
                return False
        return True
    
            
            



        