# def fib(n):
#     if n==1 or n==2:
#         return 1
#     else:
#         return (fib(n-1)+fib(n-2))

n = int(input())
#다이나믹 프로그래밍으로 피보나치 구현
dp = [0]*100 
dp[1], dp[2]=1, 1 # fibo(1) fibo(2) = 0
# 피보나치 수열을 반복문으로 구현 (bottom up)
for i in range(3, n+1):
    dp[i] = dp[i-1]+dp[i-2]
    
print(dp[n], n-2)