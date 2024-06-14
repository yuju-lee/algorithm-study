#276ms
import heapq
import sys

input = sys.stdin.readline
INF = sys.maxsize

def dijkstra(start, n, graph):
    dist = [INF] * (n+1) #시작 정점에서 각 정점까지의 최단 거리를 저장
    dist[start] = 0  #시작 정점의 최단 거리: 0으로 초기화
    pq = [(0, start)]  #우선순위 큐에 (거리, 정점)을 넣음 (초기 거리는 0, 시작 정점)

    while pq:
        currdist, currnode = heapq.heappop(pq)
        
        #우선순위 큐에서 꺼낸 거리가 현재까지 계산된 거리보다 크면 무시
        if currdist > dist[currnode]:
            continue
        
        #현재 정점에서 인접한 정점 순회
        for nextnode, weight in graph[currnode]:
            distance = currdist + weight
            
            #새로 계산한 거리가 기존 최단 거리보다 짧으면 업데이트하고 우선순위 큐에 넣음
            if distance < dist[nextnode]:
                dist[nextnode] = distance
                heapq.heappush(pq, (distance, nextnode))
    
    return dist

n = int(input().strip())  # 도시의 개수
m = int(input().strip())  # 버스의 개수

graph = [[] for _ in range(n+1)]  # 그래프 초기화

for _ in range(m):
    u, v, w = map(int, input().strip().split())
    graph[u].append((v, w))

start, end = map(int, input().strip().split())

dist = dijkstra(start, n, graph)

# 도착 도시까지의 최단 거리를 출력, 도달 불가능한 경우 -1 출력
print(dist[end] if dist[end] != INF else -1)
