# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def height(node):
            if not node:
                return 0
            return 1 +max(height(node.left),height(node.right))
        def diameter(node):
            if not node:
                return 0
            #calculating height of left node and right node
            left_height=height(node.left)

            right_height=height(node.right)
            #calculating diameter of left and right node of thr tree
            left_diameter=diameter(node.left)
            right_diameter=diameter(node.right)
            return max(left_height+right_height,max(left_diameter,right_diameter))
        return diameter(root)                
        