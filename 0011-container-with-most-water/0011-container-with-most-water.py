class Solution:
    def maxArea(self, height: List[int]) -> int:
        i=0
        j=len(height)-1
        maxarea=0
        area=0
        while i<j:
            

            area=(j-i)*min(height[i],height[j])
            maxarea=max(maxarea,area)

            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return maxarea
            

 

            

        