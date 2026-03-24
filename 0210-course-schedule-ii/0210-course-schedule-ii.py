class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list={}
        in_degree=[0]*numCourses

        for i in range(numCourses):
            adj_list[i] = []

        for course,prereq in prerequisites:
            in_degree[course]+=1 #[1:1,2:1,3:2] 
            adj_list[prereq].append(course)   #0->1,2 , 1->3, 2->3, 3->[]
        #make list and ajd list and then put value in queue then pop then append
        queue=[]
       
        for i in range(numCourses):
            if in_degree[i]==0:
                queue.append(i)     #[0]
        taken=0
        res=[]
        while queue:
            current=queue.pop(0)
            taken+=1
            res.append(current)


            for next_course in adj_list[current]: #(1 & 2)so for 3 in 1 and for 3 in 2 
                in_degree[next_course]-=1
                if in_degree[next_course] == 0:
                    queue.append(next_course)
        return res if taken == numCourses else[]              
        