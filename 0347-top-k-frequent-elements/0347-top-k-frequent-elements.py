class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mydict={}
        for n in nums:
            mydict[n]=1+mydict.get(n,0)
        
        colls = []
        for key,val in mydict.items():
            colls.append((key,val))
    
        colls.sort(key=lambda coll:coll[1],reverse=True)

        ans = []
        for a,b in colls[:k]:
            ans.append(a)
        return ans
