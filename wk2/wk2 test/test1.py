#100ms
import sys
from collections import defaultdict, deque

input = sys.stdin.readline

def bfs(start, end):
    #수빈이랑 동생의 위치가 같으면 0
    if start == end:
        return 0
    #최댓값설정
    maxpos = 100000
    #-1: 방문안한위치
    visited = [-1]*(maxpos+1)
    #시작위치 큐에 추가하고
    queue = deque([start])
    #시작위치의 시간 0으로 초기화
    visited = [False] * (maxpos +1)
    #시간초과때문에 딕셔너리로 정의
    distance = {start: 0}
    #시작위치는 True로
    visited[start] = True

    while queue:
        current = queue.popleft()
        #가능한 이동위치
        for next in (current-1, current+1, current*2):
            #max 안에 있고 방문 안하면
            if 0 <= next <= maxpos and not visited[next]:
                visited[next] = True
                distance[next] = distance[current] + 1
                #도달하면
                if next == end:
                    #distance 리턴
                    return distance[next]
                #큐에 다음위치 추가
                queue.append(next)

start, end = map(int, input().split())

print(bfs(start, end))