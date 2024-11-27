import heapq
import sys

input = sys.stdin.readline

def findmincost(queue):
    total = 0
    #힙으로 만들기
    heapq.heapify(queue)
    #힙에 있는 게 없을 때까지
    while len(queue) > 1:
        #처음이랑 두번째 값 꺼내기
        first = heapq.heappop(queue)
        second = heapq.heappop(queue)
        #두개 합쳐서
        sumcost = first + second
        #토탈에 넣고
        total += sumcost
        #합친값 푸쉬
        heapq.heappush(queue, sumcost)
    #토탈 리턴
    return total

t = int(input())
ans = []

for _ in range(t):
    cnt = int(input())
    queue = list(map(int, input().split()))
    ans.append(findmincost(queue))

print(*ans, sep='\n')