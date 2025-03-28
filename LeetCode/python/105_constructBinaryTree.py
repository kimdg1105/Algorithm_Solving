# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List, Optional


class Solution:
    def divideOrder(self, order:List[int], pivot):
        l_order = order[:order.index(pivot)]
        r_order = order[order.index(pivot)+1:]
        return l_order, r_order

    def addLeft(self,rootNode:TreeNode, order:List[int]):
        v=order.pop(0)
        rootNode.left = TreeNode(v)
        return v
    
    def addRight(self, rootNode: TreeNode, order:List[int]):
        v=order.pop(0)
        rootNode.right= TreeNode(v)
        return v


    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return None

        root = TreeNode(preorder.pop(0))
        l_inorder, r_inorder = self.divideOrder(inorder, root.val)
        # print(l_inorder, r_inorder)

        root.left = self.buildTree(preorder, l_inorder)
        root.right = self.buildTree(preorder, r_inorder)

        return root
    

Solution().buildTree([3,9,20,15,7], [9,3,15,20,7])