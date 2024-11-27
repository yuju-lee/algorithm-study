from itertools import combinations

n, m = map(int, input().split())

# [1, 2, 3, 4]
numList = [i for i in range(1, n+1)]

for seq in combinations(numList, m):
    print(*seq)