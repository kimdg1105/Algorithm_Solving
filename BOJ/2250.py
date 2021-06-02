import sys


class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right
        self.depth = -1
        self.idx = -1


def inorder(node, d):
    global index
    if node.data != -1:
        node.depth = d
        d += 1
        if node.left != -1:
            inorder(tree[node.left], d)
        print(node.data, " ", end='')
        node.idx = index
        index += 1
        if node.right != -1:
            inorder(tree[node.right], d)


N = int(input())
parent = -1
pl = [-1 for _ in range(N + 1)]
tree = {}
d = 1
index = 1
for _ in range(N):
    a, b, c = map(int, input().split())
    tree[a] = Node(data=a, left=b, right=c)
    if b != -1:
        pl[b] = a
    if c != -1:
        pl[c] = a

# 뿌리 찾기
for i in range(1, N + 1):
    if pl[i] == -1:
        parent = i

print("parent is ", parent)
inorder(tree[parent], d)

# 최대 깊이 찾기
level = 1
for i in range(1, N + 1):
    if tree[i].depth > level:
        level = tree[i].depth

# 각 레벨 별 원소 정리
lv_list = [[] for _ in range(level + 1)]
for i in range(1, level + 1):
    for j in range(1, N + 1):
        if tree[j].depth == i:
            lv_list[i].append(j)

# cal
ret = 0
lv = 0
for i in range(1, len(lv_list)):
    min_idx = sys.maxsize
    max_idx = -1

    for j in lv_list[i]:
        if tree[j].idx >= max_idx:
            max_idx = tree[j].idx
        if tree[j].idx <= min_idx:
            min_idx = tree[j].idx

    tmp = max_idx - min_idx + 1
    print("Tmp is", tmp)
    if tmp > ret:
        ret = tmp
        lv = i

print(lv, ret)
