#56ms
def checkVPS(s):
    stack = []
    for i in range(len(s)):
        #첫 글자가 닫는 괄호면 무조건 no
        if i == 0:
            if s[i] == '(':
                stack.append(s[i])
            else:
                stack.append(s[i])
                break

        else: #2번째부터
            # (는 넣고, )이 들어올 때마다 하나씩 pop
            if s[i] == '(':
                stack.append(s[i])
            else: #닫는 괄호가 들어오면
                if 0 < len(stack):
                    stack.pop()
                else:
                    stack.append(s[i])
                    break
                    
    if len(stack) == 0: return "YES"
    else: return "NO"

cnt = int(input())
ans = []
for i in range(cnt):
    s = str(input())
    ans.append(checkVPS(s))

for j in range(len(ans)):
    print(ans[j])
    