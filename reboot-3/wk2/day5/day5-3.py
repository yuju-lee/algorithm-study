#56ms
#최단거리 계산을 위해 BFS 사용
import sys
from collections import defaultdict, deque

input = sys.stdin.readline
#start에서 end까지의 촌수를 계산
def bfs(start, end):
    queue = deque([start])
    #노드의 방문 여부
    visited[start] = True
    #거리
    distance[start] = 0
    
    while queue:
        current = queue.popleft()
        if current == end:
            return distance[current]
        
        for neighbor in graph[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                distance[neighbor] = distance[current] + 1
                queue.append(neighbor)
    #촌수를 계산할 수 없으면 -1 리턴
    return -1

total = int(input())
person1, person2 = map(int, input().split())
m = int(input())

graph = defaultdict(list)
visited = [False] * (total + 1)
distance = [-1] * (total + 1)

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

print(bfs(person1, person2))
