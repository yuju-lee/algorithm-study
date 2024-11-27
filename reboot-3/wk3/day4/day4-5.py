#40ms
def rockgame(num):
    dp = [False] * (num+1)
    
    if num >= 1: dp[1] = True
    if num >= 2: dp[2] = False
    if num >= 3: dp[3] = True
    
    for i in range(4, num+1):
        if not dp[i-1] or not dp[i-3]: dp[i] = True
        else: dp[i] = False
    
    return "SK" if dp[num] else "CY"


num = int(input())

print(rockgame(num))