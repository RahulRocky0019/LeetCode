# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def balanced(p, q):
            if not p and not q:
                return True
            
            if (p and not q) or (not p and q):
                return False
            
            if p.val != q.val:
                return False
            
            return balanced(p.left, q.right) and balanced(p.right, q.left)

        return balanced(root.left, root.right)
