#40ms
def fill2x(n):
    if n == 1: return 1
    elif n == 2: return 2
    #dp[i]: 2×i 크기의 직사각형을 1×2 타일과 2×1 타일로 채우는 방법의 수를 의미
    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 2
    
    for i in range(3, n+1):
        dp[i] = (dp[i-1] + dp[i-2]) % 10007
    
    return dp[n]

n = int(input())

print(fill2x(n))