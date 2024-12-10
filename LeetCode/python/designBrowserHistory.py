class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next


class BrowserHistory:
    head, tail = None, None
    current = None

    def __init__(self, homepage: str):
        newNode = ListNode(homepage)
        self.head, self.tail = newNode, newNode
        self.current = newNode

    def visit(self, url: str) -> None:
        newNode = ListNode(url)
        self.current.next = newNode
        newNode.prev = self.current
        self.current = newNode
        return None

    def back(self, steps: int) -> str:
        for _ in range(steps):
            if self.current.prev is None:
                break
            self.current = self.current.prev
        return self.current.value

    def forward(self, steps: int) -> str:
        for _ in range(steps):
            if self.current.next is None:
                break
            self.current = self.current.next
        return self.current.value


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)