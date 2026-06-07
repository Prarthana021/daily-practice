class Solution(object):
    def twoSum(self, nums, target):
        # hashmap key -> number posn -> index
        # target-i is in the hashmap then return i and index of target-nums(i) 
        # else add nums(i) to hashmap 

        hmap={}
        for i in range(len(nums)):
            complement= target-nums[i]
            if complement in hmap:
                return([i,hmap.get(complement)])
            else:
                hmap[nums[i]]=i

            

        



        
