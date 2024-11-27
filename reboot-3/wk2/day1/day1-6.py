from collections import deque

n, m = map(int, input().split())
pos = list(map(int, input().split())) #뽑아내려는 원소의 위치

#큐의 크기는 n, 뽑는 갯수는 m 
leftcnt = 0
rightcnt = 0
cnt = 0

#큐 만들기
queue = deque(range(1, n+1))

#원소뽑기
for p in pos:
    #현재 큐의 원소 p 위치 (index 사용해서)
    index = queue.index(p)
    #왼쪽으로 움직일때
    left = index
    #오른쪽으로 움직일 때
    right = len(queue)-index

    #왼쪽으로 움직이는게 오른쪽으로 움직이는것보다 적으면 왼쪽으로
    if left <= right:
        queue.rotate(-left) #음수면 왼쪽으로 움직임
        cnt += left
    else: #아니면 오른쪽
        queue.rotate(right)
        cnt += right

    #첫번째 제거
    queue.popleft()

print(cnt)