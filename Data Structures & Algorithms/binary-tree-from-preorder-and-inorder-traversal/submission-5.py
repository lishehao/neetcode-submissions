
class Solution:
    def buildTree(self, preorder: List[int],
                  inorder: List[int]) -> Optional[TreeNode]:

        indexMap = {
            val: i for i, val in enumerate(inorder)
        }

        preIndex = 0

        def build(left, right):
            nonlocal preIndex

            if left > right:
                return None

            rootVal = preorder[preIndex]
            preIndex += 1

            root = TreeNode(rootVal)

            mid = indexMap[rootVal]

            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)

            return root

        return build(0, len(inorder) - 1)
