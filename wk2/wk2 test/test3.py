import sys
input = sys.stdin.readline

n = int(input())
stack = []
ans = 0
#y값이 이전보다 낮으면 건물이 있다고 생각 (카운트 올리기)
for _ in range(n):
    x, height = map(int, input().split())
    #스택이 비어있지 않고 현재 높이가 스택의 마지막 높이보다 작으면 스택에서 빼고 건물 추가
    while stack and stack[-1] > height:
        stack.pop()
        ans += 1
    #스택이 비어있지 않고 현재 높이랑 스택 마지막 높이 같으면 지나감
    if stack and stack[-1] == height:
        continue
    #스택에 추가
    stack.append(height)

while stack:
    #0보다 높은 건 건물로 세기 
    if stack[-1] > 0: 
        ans += 1
    stack.pop()

print(ans)