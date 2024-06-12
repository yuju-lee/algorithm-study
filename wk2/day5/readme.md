# 5일차 알고리즘 문제해결

### 1️⃣ 24479번: 알고리즘 수업 - 깊이 우선 탐색 1

난이도: 실버

분류: DFS

링크: [24479번: 알고리즘 수업 - 깊이 우선 탐색 1](https://www.acmicpc.net/problem/24479)


```python
#576ms
import sys
input = sys.stdin.readline
from collections import defaultdict

#정점의 수 n, 간선의 수 line, 시작 정점 R
node, line, start = map(int, input().split())

def dfs(start):
    stack = [start]
    order = 1

    while stack:
        current = stack.pop()
        if not visited[current]:
            visited[current] = True
            visit_order[current] = order
            order += 1
            #인접 노드를 오름차순으로 방문하기 위해 sorted
            for adj in sorted(graph[current], reverse=True):
                if not visited[adj]:
                    stack.append(adj)

graph = defaultdict(list)
visited = [False] * (node + 1)
visit_order = [0] * (node + 1)

for _ in range(line):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

dfs(start)

for i in range(1, node + 1):
    print(visit_order[i])

```

--------

### 2️⃣ 24444번: 알고리즘 수업 - 너비 우선 탐색 1

난이도: 실버

분류: BFS

링크: [24444번: 알고리즘 수업 - 너비 우선 탐색 1](https://www.acmicpc.net/problem/24444)


```python
#596ms
import sys
from collections import defaultdict, deque

input = sys.stdin.readline

def bfs(start):
    visited = [False] * (node + 1)
    visit_order = [0] * (node + 1)
    queue = deque([start])
    order = 1

    while queue:
        vertex = queue.popleft()
        if not visited[vertex]:
            visited[vertex] = True
            visit_order[vertex] = order
            order += 1

            for neighbor in sorted(graph[vertex]):
                if not visited[neighbor]:
                    queue.append(neighbor)

    return visit_order

# 정점의 수 n, 간선의 수 line, 시작 정점 R
node, line, start = map(int, input().split())
graph = defaultdict(list)

visitorder = bfs(start)

for _ in range(line):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, node + 1):
    print(visitorder[i])

```

--------


### 3️⃣ 2644번: 촌수 계산

난이도: 실버

분류: DFS, BFS

링크: [2644번: 촌수 계산](https://www.acmicpc.net/problem/2644)


```python
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


```

--------



### 4️⃣ 7562번: 나이트의 이동

난이도: 실버

분류: BFS (최단 거리)

링크: [7562번: 나이트의 이동](https://www.acmicpc.net/problem/7562)


```python
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
```

--------
### 5️⃣ 18352번: 특정 거리의 도시 찾기

난이도: 실버

분류: BFS (최단 거리)

링크: [18352번: 특정 거리의 도시 찾기](https://www.acmicpc.net/problem/18352)


```python
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
```
--------


### 6️⃣ 2606번: 바이러스

난이도: 실버

분류: BFS, DFS

링크: [2606번: 바이러스](https://www.acmicpc.net/problem/2606)


```python
#44ms
def dfs(idx):
    global count
    if visited[idx]: # 방문한 노드는 다시 방문할 필요가 없어요
        return
    visited[idx] = True # 이 노드를 방문 처리할게요
    count += 1 #감염된 컴퓨터 수 카운트
    for i in graph[idx]: # 주변 노드들에 대해 하나씩 탐색을 시도해요
        dfs(i)

# 그래프 초기 설정
n = int(input())
graph = [[] for  _ in range(n + 1)]
visited = [False] * (n + 1)

cnt = int(input())

for _ in range(cnt):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x) #양방향연결추가

#여기서 변수 초기화
count = 0
#1번부터 DFS 시작
dfs(1)

print(count-1)
```

--------

### 7️⃣ 21937번: 작업

난이도: 실버

분류: DFS, BFS

링크: [21937번: 작업](https://www.acmicpc.net/problem/21937)


```python
#328ms
import sys
sys.setrecursionlimit(10**7)

input = sys.stdin.readline

def dfs(idx):
    global count
    if visited[idx]: # 방문한 노드는 다시 방문할 필요가 없어요
        return
    visited[idx] = True  #출발 노드 방문처리
    for i in graph[idx]: #그래프를 돌며
        if not visited[i]: # 주변 노드들에 대해 하나씩 탐색을 시도해요
            count+=1  # 값이 증가 
            dfs(i)

count = 0
n, m = map(int,input().split())
graph = [[] for _ in range(n+1)] 
visited = [False] * (n+1)

for i in range(m):
    u, v= map(int,input().split())
    graph[v].append(u)

x = int(input())
dfs(x)

print(count)
```

--------

### 8️⃣ 25195번: yes or yes

난이도: 골드

분류: BFS DFS 

링크: [25195번: yes or yes](https://www.acmicpc.net/problem/25195)


```python

```


-----


이 날 문제는 다시 풀어봐야 할 것 같다.