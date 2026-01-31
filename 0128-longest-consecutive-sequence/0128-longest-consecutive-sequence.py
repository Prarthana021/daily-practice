#find if a number is start of a sequence , if yes find if num+1 exists in the set until it doesnt, in the meantime update the length counter accordingly; we will find until num+length not num+1 since length updates and again we need to check for next in the sequence 
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset=set(nums)
        longest=0

        for num in numset:
            if num-1 not in numset:
                counter=1
                while num+counter in numset:
                    counter+=1
                longest=max(longest,counter)
        return longest


         