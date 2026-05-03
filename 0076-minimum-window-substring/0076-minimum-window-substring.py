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

            while self.contains(mapT,mapS):
                if res=="" or right-left+1 < len(res):
                    res=s[left:right+1]
                mapS[s[left]]-=1
                left+=1
        return res

    
    def contains(self,mapT,mapS):
        for ch in mapT:
            if mapT.get(ch,0)>mapS.get(ch,0):
                return False
        return True
        













    #     mapT={}
    #     mapS={}

    #     left=0
    #     res=""
    #     for ch in t:
    #         mapT[ch] = mapT.get(ch, 0) + 1

    #     for right in range(len(s)):
    #         mapS[s[right]]=mapS.get(s[right],0)+1
    #         while self.contains(mapS,mapT):
    #             mapS[s[left]]-=1
    #             left+=1
    #             if res=="" or right-left+1 < len(res):
    #                 res=s[left:right+1]
              
    #     return res
    
    # def contains(self, mapS, mapT):
    #     for ch in mapT:
    #         if mapT.get(ch,0)>mapS.get(ch,0):
    #             return False
    #     return True

                

        
 

            
            



        