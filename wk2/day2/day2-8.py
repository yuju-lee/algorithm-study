#148ms
import heapq
from sys import stdin

input = stdin.readline
heap = []

count = int(input())

for i in range(1, count + 1):
    try:
        num = int(input())
        if num != 0:
            # (절대값, 실제값) 형태로 저장
            heapq.heappush(heap, (abs(num), num))
        else: # 0일 경우 배열에서 절대값이 가장 작은 값을 출력하고 제거
            if len(heap):
                print(heapq.heappop(heap)[1])
            else:
                print(0)
    except:
        print(0)