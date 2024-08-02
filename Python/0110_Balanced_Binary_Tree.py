# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balance = [True]

        def height(node):
            if not node:
                return 0

            left = height(node.left)
            # if balance[0] == False:
            #     return 0
            right = height(node.right)

            if abs(left - right) > 1:
                balance[0] = False
                # return 0

            return 1 + max(left, right)

        height(root)

        return balance[0]
