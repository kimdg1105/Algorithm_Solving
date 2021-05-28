


def preorder(node):
    if node.data != '.':
        print(node.data, end ='')
        if node.left != '.':
            preorder(graph[node.left])
        if node.right != '.':
            preorder(graph[node.right])

def inorder(node):
    if node.data != '.':
        if node.left != '.':
            inorder(graph[node.left])
        print(node.data, end='')
        if node.right != '.':
            inorder(graph[node.right])

def postorder(node):
    if node.data != '.':
        if node.left != '.':
            postorder(graph[node.left])
        if node.right != '.':
            postorder(graph[node.right])
        print(node.data, end='')

class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right


if __name__ == "__main__":
    N = int(input())
    graph = {}
    for _ in range(N):
        cur,l,r = map(str, input().split())
        graph[cur] = Node(data=cur, left=l, right=r)

    preorder(graph['A'])
    print()
    inorder(graph['A'])
    print()
    postorder(graph['A'])



