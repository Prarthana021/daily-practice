# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        q=collections.deque()
        q.append(root)
        res=[]

        while q:
            level_size=len(q)
            level=[]
            for i in range(level_size):
                node=q.popleft()  #pop from first to last so left
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
             res.append(level)

        return res

        
                


                
                

                


        