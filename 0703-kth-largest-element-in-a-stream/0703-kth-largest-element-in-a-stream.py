class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minheap, self.k=nums,k
        heapq.heapify(self.minheap)
        while len(self.minheap)>k:
            heapq.heappop(self.minHeap)

    def add(self, val:int)->int:
        heapq.heappush(self.minheal,val)
        while len(self.minheap)>self.k:
            heapq.heappop(self.minHeap)
        return self.minheap[0]
        