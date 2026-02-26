# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return [True,0]

            left=dfs(root.left)
            right=dfs(root.right)

            balanced= left[0] and right[0] and abs(left[1]-right[1]) <= 1
            return[balanced, 1+max(left[1],right[1])]

        return dfs(root)[0]
        # def dfs(root):
        #     if not root: #node is root in function definition so same thing
        #         return [True, 0]

        #     left, right = dfs(root.left), dfs(root.right)
        #     balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1 #whichever node you are at that node's right sub tree left sub tree and from that as root node check height difference
        #     return [balanced, 1 + max(left[1], right[1])] #whichever node you are calculating by keeping it root that node's height value 

        # return dfs(root)[0]