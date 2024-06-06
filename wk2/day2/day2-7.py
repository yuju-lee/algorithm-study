# #메모리초과

# from itertools import *
# t = int(input())

# def makecom(t):
#     cnt = int(input())
#     dic = {}
#     count = 0

#     for i in range(cnt):
#         name, cate = input().split()
#         if cate not in dic:
#             dic[cate] = []
#         dic[cate].append(name)

#     catelist = dic.values()

#     anset = []
    
#     for j in range(1, len(catelist)+1):
#         for com in combinations(catelist, j):
#             productcnt = 1
#             for group in com:
#                 productcnt *= len(group)
#             count += productcnt

#     return count

# for i in range(t):
#     print(makecom(i))
import sys

t = int(input())

for _ in range(t):
    cloth = {}
    result = 1
    n = int(input())
    for _ in range(n):
        name, type = sys.stdin.readline().rstrip().split()

        if not type in cloth:
            cloth[type] = 1
        else:
            cloth[type] += 1

    for i in cloth:
        result *= (cloth[i] + 1)

    print(result - 1)