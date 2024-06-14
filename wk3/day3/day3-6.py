#508ms
from sys import stdin
input = stdin.readline
n = int(input())

tier = []

for _ in range(n):
    rank = int(input())
    tier.append(rank)

tier.sort()

score = 0
for i in range(n):
    score += abs(tier[i] - (i + 1))

print(score)