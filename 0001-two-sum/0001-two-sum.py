class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        A=[]
        for i, num in enumerate(nums):

            A.append([num,i])
    
        A.sort()
        i,j= 0, len(nums)-1

        while(i<j):
            current= A[i][0]+A[j][0]
            if(current==target):
                return[min(A[i][1],A[j][1]),max (A[i][1],A[j][1])]

            elif current<target:
                i+=1
            else:
                j-=1
        return []
            


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1={}
        for i, num in enumerate(nums):
            dict1[num]=i
        for i, num in enumerate(nums):
            diff=target-num
            if diff in dict1 and dict1[diff]!=i:
                return [i, dict1[diff]]
                

        
    





         


    

      
