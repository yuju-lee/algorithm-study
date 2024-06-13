#76ms
from collections import deque

n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]

#상하좌우 및 대각선 이동을 위한 배열
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

#BFS 탐색을 위한 큐 초기화
q = deque([(i, j) for i in range(n) for j in range(m) if maps[i][j]])

#가장 먼 거리 초기화
longest = 0  

while q: 
    #큐에서 현재 위치를 꺼내고
    x, y = q.popleft()
    #8방향 탐색  
    for i in range(8):  
        nx = dx[i] + x
        ny = dy[i] + y
        
        #유효한 좌표인지 확인
        if 0 <= nx < n and 0 <= ny < m:
            #상어가 없는 위치인 경우
            if not maps[nx][ny]:
                #현재 거리 + 1로 갱신  
                maps[nx][ny] = maps[x][y] + 1  
                #가장 먼 거리 갱신
                longest = maps[nx][ny]  
                #큐에 새 위치 추가
                q.append((nx, ny))  

#상어가 있는 1부터 값을 더하여 주었으므로 마지막에 저장된 값에 1을 뺀 값을 출력
print(longest - 1)