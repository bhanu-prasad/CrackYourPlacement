
#https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def solve(root):
            if root is None:
                return 0
            l=solve(root.left)
            r=solve(root.right)
            return 1+max(l,r)
        return solve(root)