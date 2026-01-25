class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
       l=1
       r=max(piles)
       res=r #because r cant exceed the max value in pile; kok cant eat more than max in the pile at once
       while l<=r:
        m=(l+r)//2
        time = 0 
        for i in piles:
            time+=math.ceil(float(i) / m)
        if time <= h:
            res=min(res,m)
            r=m-1
        else:
            l=m+1
       return res



        
        