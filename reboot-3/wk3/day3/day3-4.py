#432ms
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

def findshortest(n, graph, v1, v2):
    #1번 정점에서 모든 정점까지의 최단 거리 계산
    distfrom1 = dijkstra(1, n, graph)
    
    #v1에서 모든 정점까지의 최단 거리 계산
    distv1 = dijkstra(v1, n, graph)
    
    #v2에서 모든 정점까지의 최단 거리 계산
    distv2 = dijkstra(v2, n, graph)
    
    minlen = INF
    
    #시작점(1) -> v1 -> v2 -> 목적지(N) 의 최단 거리 계산
    if distfrom1[v1] != INF and distv1[v2] != INF and distv2[n] != INF:
        path1 = distfrom1[v1] + distv1[v2] + distv2[n]
        minlen = min(minlen, path1)
    
    #시작점(1) -> v2 -> v1 -> 목적지(N) 의 최단 거리 계산
    if distfrom1[v2] != INF and distv2[v1] != INF and distv1[n] != INF:
        path2 = distfrom1[v2] + distv2[v1] + distv1[n]
        minlen = min(minlen, path2)
    
    #최단 경로 길이가 INF일 경우 경로가 없으므로 -1
    if minlen == INF:
        return -1
    else:
        return minlen

n, e = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

result = findshortest(n, graph, v1, v2)
print(result)
