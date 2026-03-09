#always try to run the task with the highest remaining frequency among the tasks that are currently allowed
#1 increase time
#2 run task from heap
#3 add to queue
#4 THEN check queue and move cooled tasks back to heap

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        # We need to know how many times each task appears,
        # because the task with the highest count is the hardest to schedule.

        maxHeap = [-cnt for cnt in count.values()]
        # We need a max heap so we can always pick the task
        # with the highest remaining count.
        # Python only has min heap, so we store negative counts.

        heapq.heapify(maxHeap)
        # Now this list becomes a heap,
        # so we can quickly remove the largest remaining task.

        time = 0
        # We need to count total CPU intervals,
        # so we keep a variable called time.

        q = deque()
        # We need a place to keep tasks that are cooling down,
        # so we use a queue.
        # Each queue item will look like:
        # [remaining_count, time_when_it_can_return]

        while maxHeap or q:
            # We need to keep going until:
            # 1. no task is left in heap
            # 2. no task is left cooling in queue

            time += 1
            # One CPU interval passes,
            # so we increase time by 1.

            if not maxHeap:
                # If heap is empty, it means there is no task
                # available to run right now.

                time = q[0][1]
                # Since we cannot do anything until the earliest cooling task returns,
                # we jump time directly to that return time.
                # q[0] = first task in queue
                # q[0][1] = return time of that task

            else:
                # If heap is not empty, it means at least one task
                # is ready to run now.

                cnt = 1 + heapq.heappop(maxHeap)
                # We run the task with highest remaining count.
                # Example: if we pop -3, after running it once,
                # remaining count becomes -2.
                # That is why we do 1 + popped_value.

                if cnt:
                    # If cnt is not 0, that means this task still has
                    # some executions left.

                    q.append([cnt, time + n])
                    # Since we just used this task,
                    # we cannot use it again immediately.
                    # So we put it into cooldown queue.
                    # We store:
                    # cnt = how many of this task are still left
                    # time + n = when cooldown finishes

            if q and q[0][1] == time:
                # Now we check:
                # do we have any task in queue?
                # and has the first cooling task finished waiting?

                heapq.heappush(maxHeap, q.popleft()[0])
                # If yes, we move that task back to heap,
                # because now it is allowed to be used again.
                # q.popleft() removes the first queue item
                # [0] takes its remaining count
                # then we push that count back into heap

        return time
        # After all tasks are done, total time is the answer.