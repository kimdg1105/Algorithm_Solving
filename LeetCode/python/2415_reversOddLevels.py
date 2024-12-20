# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque()

        if root == None:
            return None

        lv = 0
        q.append((root, lv))
        lv_val_list = []
        lv_node_list = []

        while q:
            cur_node, cur_lv = q.popleft()
            next_lv = cur_lv + 1

            if next_lv % 2 != 0:
                if cur_node.left != None:
                    lv_val_list.append(cur_node.left.val)
                    lv_node_list.append(cur_node.left)
                if cur_node.right != None:
                    lv_val_list.append(cur_node.right.val)
                    lv_node_list.append(cur_node.right)

            if cur_node.left != None:
                q.append((cur_node.left, next_lv))
            if cur_node.right != None:
                q.append((cur_node.right, next_lv))

            if 2**next_lv == len(lv_val_list):
                for idx, node in enumerate(lv_node_list):
                    node.val = lv_val_list[len(lv_val_list) - 1 - idx]

                lv_val_list = []
                lv_node_list = []

        return root
