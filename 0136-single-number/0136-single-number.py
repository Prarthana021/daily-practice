class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        cnt=0
        my_map={}
        for num in nums:
            my_map[num]=my_map.get(num,0)+1

        for num in nums:
            if my_map[num]==1:
                return num

        