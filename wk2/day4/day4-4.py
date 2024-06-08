#40ms
s = str(input())

def checkVPS(s):
    stack = []
    for i in range(len(s)):
        if len(stack):
            if s[i]==")" and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(s[i])
        else:
            stack.append(s[i])

    return len(stack)

print(checkVPS(s))
