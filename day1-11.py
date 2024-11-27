def solution(n, heights) -> list:
    result = [0] * n
    stack = []
    
    for i in range(n):
        while stack and stack[-1][1] < heights[i]: # 스택이 비어있지 않고, 스택의 마지막 값이 현재 높이보다 작을 때
            stack.pop()
        
        if stack: # 스택이 비어있지 않다면
            result[i] = stack[-1][0] + 1  # 스택의 마지막 값의 인덱스 + 1
            
        stack.append((i, heights[i]))
    
    return result

n = int(input())

heights = list(map(int, input().split()))

result = solution(n, heights)
print(' '.join(map(str, result)))