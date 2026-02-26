# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        if self.sameTree(root, subRoot):
            return True
        return (self.isSubtree(root.left,subRoot)or #We use OR because the subtree can exist in either the left side OR the right side. It only needs to be found once, not in both places.
        self.isSubtree(root.right,subRoot))

    def sameTree(self,root,subRoot):
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        if root.val!=subRoot.val:
            return False
        return (self.sameTree(root.left,subRoot.left) and 
        self.sameTree(root.right, subRoot.right))





        