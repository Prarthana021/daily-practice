class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hass={}
        lst=[]
        for i in range(len(nums)):
            hass[nums[i]]=1+hass.get(nums[i],0)

        for key,v in hass.items():
            lst.append([v,key])
        lst.sort(reverse=True)

        res=[]
        for i in range(k):
            res.append(lst[i][1])
        
        return res
        

            
            




        