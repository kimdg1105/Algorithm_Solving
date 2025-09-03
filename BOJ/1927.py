import sys

input = sys.stdin.readline


class MyHeap:
    def __init__(self):
        self.heap = []

    def size(self):
        return len(self.heap)

    def parent_idx(self, node_idx: int):
        return (node_idx - 1) // 2

    def left_child_idx(self, node_idx: int):
        return 2 * node_idx + 1

    def right_child_idx(self, node_idx: int):
        return 2 * node_idx + 2

    def switch(self, from_idx: int, to_idx: int):
        self.heap[from_idx], self.heap[to_idx] = self.heap[to_idx], self.heap[from_idx]

    def insert(self, value: int):
        self.heap.append(value)
        inserted_idx = self.size() - 1
        while inserted_idx > 0:
            parent = self.parent_idx(inserted_idx)
            if self.heap[inserted_idx] < self.heap[parent]:
                self.switch(inserted_idx, parent)
                inserted_idx = parent
            else:
                break

    def pop(self):
        if self.size() == 0:
            return 0
        result = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()

        cur_idx = 0
        while True:
            left = self.left_child_idx(cur_idx)
            right = self.right_child_idx(cur_idx)
            smallest = cur_idx

            if left < self.size() and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < self.size() and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest != cur_idx:
                self.switch(cur_idx, smallest)
                cur_idx = smallest
            else:
                break

        return result


heap = MyHeap()

n = int(input())

for _ in range(n):
    num = int(input())
    if num == 0:
        print(heap.pop())
    else:
        heap.insert(num)
