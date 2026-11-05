# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inOrder(self, node, ordered):
        if node == None:
            return 

        self.inOrder(node.left, ordered)

        ordered.append(node.val)

        self.inOrder(node.right, ordered)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ordered = []
        self.inOrder(root, ordered)

        return ordered[k-1]