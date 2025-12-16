import sys

sys.setrecursionlimit(10**6)


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


num_list = []
while True:
    try:
        num_list.append(int(input()))
    except:
        break


def build_bst(preorder):
    if not preorder:
        return None

    def build(min_val, max_val):
        if not preorder or preorder[0] < min_val or preorder[0] > max_val:
            return None

        val = preorder.pop(0)
        root = TreeNode(val)
        root.left = build(min_val, val)
        root.right = build(val, max_val)
        return root

    return build(float("-inf"), float("inf"))


# 후위순회
def postorder(root):
    if not root:
        return []

    result = []
    result.extend(postorder(root.left))
    result.extend(postorder(root.right))
    result.append(root.val)
    return result


# 실행
root = build_bst(num_list[:])  # 복사본 전달
result = postorder(root)

for val in result:
    print(val)
