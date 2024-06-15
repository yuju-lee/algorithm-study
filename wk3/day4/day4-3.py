#100ms
def longest_decreasing_subsequence(num):
    n = len(num)
    dp = [1] * n 

    for i in range(1, n):
        for j in range(i):
            if num[j] > num[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

n = int(input())
a = list(map(int, input().split()))

print(longest_decreasing_subsequence(a))