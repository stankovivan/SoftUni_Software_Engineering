from collections import deque

parent = input()
stack = []

result = True
for que in parent:
    if que in ["{", "[", "("]:
        stack.append(que)
    elif que == "}":
        if stack and stack[-1] == "{":
            if stack:
                stack.pop()
        else:
            result = False
            break
    elif que == "]":
        if stack and stack[-1] == "[":
            if stack:
                stack.pop()
        else:
            result = False
            break
    elif que == ")":
        if stack and stack[-1] == "(":
            if stack:
                stack.pop()
        else:
            result = False
            break
print(f"YES" if result else "NO")
