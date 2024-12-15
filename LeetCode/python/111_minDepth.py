# Definition for a binary tree node.

from collections import deque
import sys
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        
        q = deque()
        ans = sys.maxsize

        q.append((root, False, 1))

        while q:
            cur_node, is_leaf, cur_level = q.popleft()
            if cur_node.left == None and cur_node.right == None:
                ans = min(ans, cur_level)
            if cur_node.left != None:
                q.append((cur_node.left, False, cur_level+1)) 
            if cur_node.right != None:
                q.append((cur_node.right,False, cur_level+1))

        return ans     