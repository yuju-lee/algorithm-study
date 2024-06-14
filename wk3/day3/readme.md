# 3일차 알고리즘 문제해결

### 1️⃣5585번: 거스름돈

난이도: 브론즈

분류: 그리디 알고리

링크: [5585번: 거스름돈](https://www.acmicpc.net/problem/5585)


```python
#40ms
def countcoin(price):
    paid = 1000
    cnt = 0

    change = paid - price

    if change == 0:
        return cnt
    
    if change // 500:
        cnt += change // 500
        change = change - (500*(change//500))
    
    if change // 100:
        cnt += change // 100
        change = change - (100*(change//100))
    
    if change // 50:
        cnt += change // 50
        change = change - (50*(change//50))

    if change // 10:
        cnt += change // 10
        change = change - (10*(change//10))

    if change // 5:
        cnt += change // 5
        change = change - (5*(change//5))
    
    if change // 1:
        cnt += change // 1
        change = change - ((change//1))

    return cnt


price = int(input())
print(countcoin(price))
```

--------
### 2️⃣14659번: 한조 서열정리하고옴ㅋㅋ

난이도: 브론즈

분류: 그리디 알고리즘

링크: [14659번: 한조 서열정리하고옴ㅋㅋ](https://www.acmicpc.net/problem/14659)


```python
#44ms
def findbesthanjo(hanjos):
    maxhanjo = 0
    cnt = 0  # 초기 cnt 설정
    total = []
    for hanjo in hanjos:

        if maxhanjo < hanjo:
            maxhanjo = hanjo
            cnt = 0  
        else:
            cnt += 1
        total.append(cnt)

    return max(total)

n = int(input())
hanjos = list(map(int, input().split()))

print(findbesthanjo(hanjos))
```

--------


### 3️⃣14720번: 우유 축제

난이도: 브론즈

분류: 그리디 알고리

링크: [14720번: 우유 축제](https://www.acmicpc.net/problem/14720)


```python
#이렇게 썼는데 틀렸음... 왜지? 로직은 비슷한 것 같은데 ㅠㅠ
milkcount = int(input())
storemilk = list(map(int, input().split()))

#0, 1, 2
order = [0, 1, 2]
cnt = 0
for i in range(len(storemilk)):
    if storemilk[i] - order[i%3] == 0:
        cnt+= 1

print(cnt)

#40ms
milkcount = int(input())
storemilk = list(map(int, input().split()))

cnt = 0
for i in range(len(storemilk)):
    if storemilk[i] == cnt % 3:
        cnt+= 1

print(cnt)
```

--------

### 4️⃣1504번: 특정한 최단경로

난이도: 실버

분류: 다익스트라

링크: [1504번: 특정한 최단경로](https://www.acmicpc.net/problem/1504)


```python
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
```

--------
### 5️⃣ 10282번: 해킹

난이도: 실버

분류: 다익스트라

링크: [10282번: 해킹](https://www.acmicpc.net/problem/10282)


```python
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
```
--------

### 6️⃣ 2012번 - 등수 매기기

난이도: 실버

분류: 그리디

링크: [2012번 - 등수 매기기](https://www.acmicpc.net/problem/2012)


```python
#508ms
from sys import stdin
input = stdin.readline
n = int(input())

tier = []

for _ in range(n):
    rank = int(input())
    tier.append(rank)

tier.sort()

score = 0
for i in range(n):
    score += abs(tier[i] - (i + 1))

print(score)
```

--------

### 7️⃣ 1931번 - 회의실 배정

난이도: 실버

분류: 그리디

링크: [1931번: 회의실 배정](https://www.acmicpc.net/problem/1931)


```python
#4188ms
def findmaxmeeting(meetinglist):
    #끝나는 시간 순서로 정렬하고 시작 시간을 정의
    meetinglist.sort(key= lambda x: (x[1], x[0]))
    #결과저장배열 초기화
    finish = 0
    cnt = 0
    for start, end in meetinglist:
        if start >= finish:
            cnt += 1
            finish = end

    return cnt

meetingcnt = int(input())
meetinglist = []

for _ in range(meetingcnt):
    start, end = map(int, input().split())
    meetinglist.append((start, end))

print(findmaxmeeting(meetinglist))
```

--------

### 8️⃣ 1916번 - 최소비용 구하기

난이도: 골드

분류: 다익스트라

링크: [1916번: 최소비용 구하기](https://www.acmicpc.net/problem/1916)

```python
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
```


-----
