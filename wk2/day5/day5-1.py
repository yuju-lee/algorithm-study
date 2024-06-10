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