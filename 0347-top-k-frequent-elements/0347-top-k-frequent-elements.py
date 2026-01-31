class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mymap={}
        arr=[]
        for i,n in enumerate(nums):
            mymap[n]=mymap.get(n,0)+1
        
        for n,i in mymap.items():
            arr.append([i,n])
        arr.sort()

        res=[]
        while len(res)<k:
            res.append(arr.pop()[1])
        return res





        
