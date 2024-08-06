# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        longest_diameter = [0]

        def dfs(node):
            if node is None:
                return 0
            
            left_dfs = dfs(node.left)
            right_dfs = dfs(node.right)
            diameter = left_dfs + right_dfs

            longest_diameter[0] = max(longest_diameter[0], diameter)

            return 1 + max(left_dfs, right_dfs)

        dfs(root)

        return longest_diameter[0]
