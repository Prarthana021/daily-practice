# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:


#there are 2 steps to tis solution first is calculate height and next is calculate diameter using height 

        res=[0]
        def height(root):
            if not root:
                return 0
            left_height= height(root.left)
            right_height=height(root.right)
            dia= left_height + right_height

            res[0]= max(res[0],dia)
            
            return 1+ max(left_height,right_height)

        height(root)
        return res[0]


        
       
        