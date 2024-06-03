# pattern1 = [] #흰색으로 시작함
# pattern2 = [] #검은색으로 시작함

# sorted(patter1, )


# from math import sqrt


# k = 2
# d = 4

# sqrt(k)

# y축을 포함한 총 점의 갯수 = x의 길이를 k로 나눈 몫 + 1 (y축은 0, 0 이므로 1 더해줘야 함)

# n = 2
# s = 8
# maxmul = 0
# maxls = []
# ls = []

# if 1 < s:
#     for i in range(1, s+1//2):
#         for j in range(s//2, 0, -1):
#             if i+j == s:
#                 ls.append([i, j])

#     for i in range(len(ls)):
        
#         if maxmul < ls[i][0] * ls[i][1]:
#             maxmul = ls[i][0] * ls[i][1]
#             maxls.append([ls[i][1], ls[i][0]])
# else:
#     maxls.append([-1])

# print(maxls[0])


from math import sqrt

def solution(k, d):
    answer = 0
    for i in range(0, d+1, k):
        y = sqrt(d**2 - i**2)
        answer = answer + y//k+1
    return int(answer)

print(solution(2, 5))