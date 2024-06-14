#784ms
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

testcase = int(input())
results = []

for _ in range(testcase):
    #컴퓨터 개수, 의존성 개수, 해킹당한 컴퓨터 번호
    n, d, c = map(int, input().split())  
    graph = [[] for _ in range(n + 1)]

    for _ in range(d):
        a, b, s = map(int, input().split())
        graph[b].append((a, s))  #b > a로 의존성 추가
    
    #해킹당한 컴퓨터부터 최단 시간을 계산
    dist = dijkstra(c, n, graph)
    
    #감염된 컴퓨터 수 및 최대 감염 시간 계산
    infect = 0
    maxtime = 0
    
    for i in range(1, n + 1):
        if dist[i] != INF:
            infect += 1
            maxtime = max(maxtime, dist[i])
    
    results.append((infect, maxtime))

#결과 출력
for result in results:
    print(result[0], result[1])