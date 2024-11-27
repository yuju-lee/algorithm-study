#1056ms
from collections import deque

def bfs(l, start, end):
    if start == end:
        return 0

    #나이트의 이동 방향 정의
    directions = [(-2, -1), (-1, -2), (1, -2), (2, -1), 
                  (2, 1), (1, 2), (-1, 2), (-2, 1)]
    
    queue = deque([start])
    visited = [[False] * l for _ in range(l)]
    visited[start[0]][start[1]] = True
    steps = 0

    while queue:
        steps += 1
        for _ in range(len(queue)):
            x, y = queue.popleft()
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < l and 0 <= ny < l and not visited[nx][ny]:
                    if (nx, ny) == end:
                        return steps
                    visited[nx][ny] = True
                    queue.append((nx, ny))
    
    #도달할 수 없는 경우?
    return -1  

t = int(input().strip())
results = []

for _ in range(t):
    length = int(input().strip())
    start = tuple(map(int, input().strip().split()))
    end = tuple(map(int, input().strip().split()))
    results.append(bfs(length, start, end))

for result in results:
    print(result)