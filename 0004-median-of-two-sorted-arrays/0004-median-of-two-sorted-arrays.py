class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n,m =len(nums1),len(nums2)
        total=n+m
        # If total is odd, mid1 == mid2
        mid1= (total -1)//2
        mid2= total //2

        i,j=0,0 #tracks in first and second array
        counter=0
        prev,curr=0,0

        while(counter <=mid2):
            prev=curr
            if i<n and(j>=m or nums1[i]<=nums2[j]):
                curr = nums1[i]
                i+=1
            else:
                curr = nums2[j]
                j+=1
            counter+=1
        if total % 2 == 0:
            # Even total: average of two middle elements
            return (prev + curr) / 2
        else:
            # Odd total: just the middle element
            return curr