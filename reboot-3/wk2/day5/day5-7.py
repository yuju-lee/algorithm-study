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