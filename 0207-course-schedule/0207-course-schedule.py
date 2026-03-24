class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list={}
        in_degree=[0]*numCourses

        for i in range(numCourses):
            adj_list[i] = []

        for course,prereq in prerequisites:
            in_degree[course]+=1 #[1:1,2:1,3:2] 
            adj_list[prereq].append(course)   #0->1,2 , 1->3, 2->3, 3->[]
        
        queue=[]
       
        for i in range(numCourses):
            if in_degree[i]==0:
                queue.append(i)     #[0]
        taken=0
        while queue:
            current=queue.pop(0)
            taken+=1

            for next_course in adj_list[current]:
                in_degree[next_course]-=1
                if in_degree[next_course] == 0:
                    queue.append(next_course)
        return taken == numCourses               