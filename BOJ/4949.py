while True:
    s = input()

    if s == ".":
        break

    else:
        stack = []
        for char in s:
            if len(stack) == 0 and (char == ")" or char == "]"):
                stack.append(char)
                break

            if char == ".":
                break
            if char == "(" or char == "[":
                stack.append(char)
            if char == ")":
                if stack[-1] != "(":
                    break
                else:
                    stack.pop()
            if char == "]":
                if stack[-1] != "[":
                    break
                else:
                    stack.pop()

        if len(stack) == 0:
            print("yes")
        else:
            print("no")
