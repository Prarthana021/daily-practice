class Solution(object):
    def minEatingSpeed(self, piles, h):
        l=1
        r=max(piles)
         #because r cant exceed the max value in pile; koko cant eat more than that

        while l<r:
            mid=(l+r)//2

            totaltime=0
            for p in piles:
                totaltime+=math.ceil(float(p)/mid)
            if totaltime <=h:
                r=mid
            
            else:
                l = mid+1
        return r


        