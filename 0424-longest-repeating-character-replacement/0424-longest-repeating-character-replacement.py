class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hasmap={}
        maxfreq=0
        left=0
        res=0
        winsize=0
        for right in range(len(s)):
            hasmap[s[right]]=hasmap.get(s[right],0)+1
            maxfreq=max(hasmap.values())
            winsize=right-left+1
            replacement=winsize-maxfreq

            while replacement>k:
                hasmap[s[left]]-=1
                left+=1

               # recompute after shrinking
                winsize-=1
                maxfreq=max(hasmap.values())
                replacement=winsize-maxfreq
            res=max(res,winsize)
        return res
            

                

                


            


        