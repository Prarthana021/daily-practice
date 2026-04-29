# Original:         [1, 2, 3, 4, 5, 6, 7]
# Reverse all:      [7, 6, 5, 4, 3, 2, 1]
# Reverse first k:  [5, 6, 7, 4, 3, 2, 1]
# Reverse rest:     [5, 6, 7, 1, 2, 3, 4] 

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n=len(nums)
        k= k % n #if k > n then use modulo

        nums.reverse()
        nums[:k]=reversed(nums[:k])
        nums[k:]=reversed(nums[k:])




