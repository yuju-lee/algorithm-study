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