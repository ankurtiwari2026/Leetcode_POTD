# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        queue = [root]
        level = 0
        while queue:
            prev = float('-inf') if level % 2 == 0 else float('inf')
            for _ in range(len(queue)):
                node = queue.pop(0)
                if (level % 2 == 0 and (node.val % 2 == 0 or node.val <= prev)) or (level % 2 != 0 and (node.val % 2 != 0 or node.val >= prev)):
                    return False
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                prev = node.val
            level += 1
        return True
