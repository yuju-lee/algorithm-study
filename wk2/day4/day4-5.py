# def findrock(n):
#     ans = []
#     for i in range(n):
#         x = (i*(i+1))//2
#         if x < n:
#             ans.append(x)
#     if n == 1:
#         return 1 
#     else:
#         return len(ans)-1


def findrock(n):
    if n == 1:
        return 1
    
    left, right = 1, n
    while left < right:
        mid = (left + right + 1) // 2
        if mid * (mid + 1) // 2 <= n:
            left = mid
        else: 
            right = mid - 1
    
    return left

t = int(input())

for _ in range(t):
    n = int(input())
    print(findrock(n))
