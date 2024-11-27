#44ms
from itertools import combinations

minimi = []

for _ in range(9):
    height = int(input())
    minimi.append(height)

minimi.sort()

#9개 입력 중 7개의 조합 (중복없이)
perm = list(combinations(minimi, 7))

for combination in perm:
    if sum(combination) == 100:
        for height in combination:
            print(height)
        break