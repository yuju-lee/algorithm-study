#100ms
import sys

input = sys.stdin.readline

n = int(input())
h = []
stack = []
cnt = 0

for i in range(n):
    s = int(input())
    h.append(s)

hr = list(reversed(h))

#마지막으로 들어오는 숫자를 기준
last = h[-1]
highest = 0

for j in hr:
    if last <= j and highest < j:
        cnt += 1
        highest = j

print(cnt)