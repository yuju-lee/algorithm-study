#시간초과
# from itertools import combinations
# vertex = int(input())
# verties = []
# for i in range(1, vertex+1):
#     verties.append(i)

# ans = list(combinations(verties, 5))

# print(len(ans))

#40ms
from math import comb

vertex = int(input().strip())
result = comb(vertex, 5)

print(result)