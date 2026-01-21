class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        for i,a in enumerate(nums):
            if a > 0:
                break
            if i>0 and nums[i]==nums[i-1]: #check if from second element if it  is same as its left neighour if yes then skip  
                continue
            l=i+1
            r=len(nums)-1
            while(l<r):
                threesum = a + nums[l] + nums[r]
                if threesum > 0:
                    r -=1
                elif threesum < 0:
                    l += 1
                else:
                    res.append([a,nums[l],nums[r]])
                    #if solution is found then move both pointers since moving
                    #only one pointer can never yeild a same result i.e 0
                    l+=1
                    r-=1
                    # if we have already found 1 solution then we check for 
                    #duplicates of l to avoid same result
                    while(l<r and nums[l]==nums[l-1]):
                        l+=1
        return res              

        