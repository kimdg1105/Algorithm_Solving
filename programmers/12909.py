def solution(s):
    stack = []

    for char in s:
        if len(stack) > 0:
            if stack[-1] == "(" and char == ")":
                stack.pop(-1)
                continue

        stack.append(char)

    return len(stack) == 0


print(solution("()()"))
print(solution("(())()"))
print(solution(")()("))
print(solution("(()("))
