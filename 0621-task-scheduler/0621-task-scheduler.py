#always try to run the task with the highest remaining frequency among the tasks that are currently allowed
#1 increase time
#2 run task from heap
#3 add to queue
#4 THEN check queue and move cooled tasks back to heap

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count=Counter(tasks)
        maxheap= [-cnt for cnt in count.values()]

        heapq.heapify(maxheap)

        time=0
        q=deque()

        while maxheap or q:
            time +=1
            if not maxheap:
                time= q[0][1]
            else:
                cnt= 1 + heapq.heappop(maxheap)

                if cnt:
                    q.append([cnt,time+n])
            if q and q[0][1]==time:
                heapq.heappush(maxheap,q.popleft()[0])

        return time

                



        
        