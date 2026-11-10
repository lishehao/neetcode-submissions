# Definition for a binary tree node.
from io import RawIOBase
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def swap(parentNode: Optional[TreeNode]):
            if not parentNode:
                return None

            left = parentNode.left
            right = parentNode.right
            parentNode.left = swap(right)
            parentNode.right = swap(left)

            return parentNode

        return swap(root)

