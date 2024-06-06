#116ms
from heapq import *
from sys import stdin

input = stdin.readline

n = int(input()) 
heap = []

for _ in range(n):
    a = int(input())
    if a:
        heappush(heap, a)
    else:
        if heap:
            print(heappop(heap))
        else:
            print(0)
