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
            






         


    

      
