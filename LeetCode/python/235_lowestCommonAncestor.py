class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        if root == None:
            return None

        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)

        if root == p or root == q:
            return root
        elif l and r:
            return root
        else:
            return l or r


root = TreeNode(6)
root.left = TreeNode(2)
root.right = TreeNode(8)

sol = Solution()
print(sol.lowestCommonAncestor(root, 2, 8))
