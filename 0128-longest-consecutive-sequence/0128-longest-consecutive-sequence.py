# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         store=set(nums)
#         res=0
#         for num in nums:    
           
#             curr=num
#             streak=0
#             while curr in store:
                
#                 streak+=1
#                 curr+=1
#             res=max(res,streak)
#         return res


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest

