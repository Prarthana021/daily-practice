# class Solution:
#     def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 if nums[j]==nums[i] and j-i<=k:
#                     return True
#         return False



# The problem says abs(i - j) ≤ k, so once an element is more than k positions behind, it can never form a valid pair again — it's dead weight, so we slide the window
#sliding window means deleting the old invalid and adding the new pair 
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window=set()

        for i,j in enumerate(nums):
            if j in window:
                return True
            window.add(j)
            if len(window)>k:
                window.remove(nums[i-k])
        return False

        