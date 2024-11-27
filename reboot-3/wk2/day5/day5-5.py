#1872ms
import sys
from collections import defaultdict, deque

input = sys.stdin.readline

def bfs(start):
    queue = deque([start])
    distance[start] = 0  #시작점의 거리는 0
    
    while queue:
        current = queue.popleft()
        
        for neighbor in graph[current]:
            if distance[neighbor] == -1:  #아직 방문하지 않은 경우
                distance[neighbor] = distance[current] + 1
                queue.append(neighbor)

city, road, length, start = map(int, input().split())
graph = defaultdict(list)

for _ in range(road):
    u, v = map(int, input().split())
    graph[u].append(v)

distance = [-1] * (city + 1)  #모든 도시에 대한 거리를 -1로 초기화

bfs(start)

#최단 거리가 K인 도시들을 찾아 오름차순으로 정렬
result = [i for i in range(1, city + 1) if distance[i] == length]

if result:
    for city in sorted(result):
        print(city)
else:
    print(-1)