# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def tree_depth(node):
            if not node:
                return 0

            left = tree_depth(node.left)
            right = tree_depth(node.right)

            return 1 + max(left, right)

        return tree_depth(root)

        # Also Works
        #
        # if not root:
        #     return 0

        # left = self.maxDepth(root.left)
        # right = self.maxDepth(root.right)

        # return 1 + max(left, right)
