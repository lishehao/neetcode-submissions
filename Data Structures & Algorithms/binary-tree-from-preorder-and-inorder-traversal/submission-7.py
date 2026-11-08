# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indexMap = {val: index for index, val in enumerate(inorder)}
        preIndex = 0

        def build(left, right):
            if left > right:
                return None

            nonlocal preIndex
            midVal = preorder[preIndex]
            preIndex += 1

            midIndex = indexMap[midVal]

            leftNode = build(left, midIndex - 1)
            rightNode = build(midIndex + 1, right)

            node = TreeNode(midVal, leftNode, rightNode)

            return node

        return build(0, len(inorder) - 1)