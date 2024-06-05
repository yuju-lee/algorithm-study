ls = list(str(input()))
stack = []
score = 0

for i in range(len(ls)):
    #첫번째는 무조건 10점+스택에 저장
    if i == 0:
        score += 10
        stack.append(ls[i])
    
    #현재 글자와 스택의 마지막 값이 다른 경우
    elif stack[-1] !=ls[i]: 
        #스택이 비어있지 않을 경우에만 pop (첫번째에 ')'가 들어오면 안 되니깐)
        if 0 < len(stack): 
            stack.pop()
        score += 10
        #스택 비우고 현재글자(새글자) 추가
        stack.append(ls[i])
    
    #현재 글자와 스택 글자가 같으며 스택에 값이 있는 경우
    elif 0 < len(stack) and stack[-1] == ls[i]:
        score += 5
        stack.append(ls[i])
            
print(score)