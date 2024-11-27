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
