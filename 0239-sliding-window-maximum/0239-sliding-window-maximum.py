class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q=deque()
        left=0
        res=[]

        for right in range(len(nums)):
            while q and nums[right]>= nums[q[-1]]:
                q.pop()
            q.append(right)

            if q[0]<left:
                q.popleft()
            
            if right-left+1 == k:
                res.append(nums[q[0]])

           # move left to slide window
                left += 1 
        return res