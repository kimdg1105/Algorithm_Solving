class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for e in s:
            if e == "(":
                stack.append(")")
            elif e == "{":
                stack.append("}")
            elif e == "[":
                stack.append("]")
            elif not stack or stack.pop() != e:
                return False
        return not stack
