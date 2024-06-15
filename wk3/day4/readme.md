# 4일차 알고리즘 문제해결

### 1️⃣17202번: 핸드폰 번호 궁합

난이도: 브론즈

분류:  DP

링크: [핸드폰 번호 궁합](https://www.acmicpc.net/problem/17202)


```python
#40ms
def findcomp(num1, num2):
    combined = []
    for i in range(len(num1)):
        combined.append(int(num1[i]))
        combined.append(int(num2[i]))

    dp = [combined]

    while len(dp[-1]) > 2:
        current = dp[-1]
        next = []
        for i in range(len(current) - 1):
            next.append((current[i] + current[i + 1]) % 10)
        dp.append(next)

    final = dp[-1]
    return f"{final[0]}{final[1]}"

num1 = input().strip()
num2 = input().strip()

result = findcomp(num1, num2)
print(result)

```

--------
### 2️⃣2775번: 부녀회장이 될테야

난이도: 브론즈

분류: DP

링크: [부녀회장이 될테야](https://www.acmicpc.net/problem/2775)


```python
#56ms
def countpeople(k, n):
    dp = [[0] * (n + 1) for _ in range(k + 1)]
    
    for i in range(1, n + 1):
        dp[0][i] = i
    
    for i in range(1, k + 1):
        for j in range(1, n + 1):
            dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
    
    return dp[k][n]

T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())
    print(countpeople(k, n))
```

--------
### 3️⃣ 11722번 - 가장 긴 감소하는 부분 수열

난이도: 실버

분류: DP

링크: [11722번: 가장 긴 감소하는 부분 수열](https://www.acmicpc.net/problem/11722)


```python
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
```

--------

### 4️⃣9095번: 1, 2, 3 더하기

난이도: 실버

분류: DP

링크: [9095번: 1, 2, 3 더하기](https://www.acmicpc.net/problem/9095)

```python
#40ms
def countway(n):
    if n == 0:
        return 0
    dp = [0] * (n+1)
    
    dp[0] = 1
    if n >= 1: dp[1] = 1
    if n >= 2: dp[2] = 2
    if n >= 3: dp[3] = 4
    
    for i in range(4, n+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    
    return dp[n]

casecnt = int(input())
testcases = [int(input()) for _ in range(casecnt)]

for n in testcases:
    print(countway(n))
```

--------

### 5️⃣ 9655번: 돌게임

난이도: 실버

분류: DP

링크 : [9655번: 돌게임](https://www.acmicpc.net/problem/9655)


```python
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
```
--------

### 6️⃣ 2839번 - 설탕 배달

난이도: 실버

분류: DP

링크: [2839번 - 설탕 배달](https://www.acmicpc.net/problem/2839)


```python
#40ms
num = int(input())

def bags(num):
    for bags in range(num//5, -1, -1):
        sugar = num - (bags*5)
        if sugar % 3 == 0:
            newbags = sugar//3
            return bags + newbags
    return -1

print(bags(num))
```

--------

### 7️⃣ 11726번 - 2×n 타일링

난이도: 실버

분류: DP

링크: [2×n 타일링](https://www.acmicpc.net/problem/11726)


```python
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
```

--------

### 8️⃣ 1149번 - RGB 거리

난이도: 실버

분류: DP

링크: [1149번: RGB거리](https://www.acmicpc.net/problem/1149)

```python
#80ms
def findmincost(n, costs):
    #dp 배열 초기화: 각 집을 R, G, B로 칠할 때의 비용을 저장
    dp = [[0] * 3 for _ in range(n)]
    
    #첫 번째 집의 비용 초기화
    dp[0][0] = costs[0][0]  # R
    dp[0][1] = costs[0][1]  # G
    dp[0][2] = costs[0][2]  # B
    
    #각 집을 R, G, B로 칠할 때의 최소 비용 계산
    #처음 인덱스는 이미 정의를 했기 때문에 1부터 
    for i in range(1, n):
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + costs[i][0]  # R로 칠하는 경우
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + costs[i][1]  # G로 칠하는 경우
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + costs[i][2]  # B로 칠하는 경우
    
    #마지막 집까지 칠한 후, 최소 비용 선택
    return min(dp[n-1][0], dp[n-1][1], dp[n-1][2])

n = int(input())
costs = [list(map(int, input().split())) for _ in range(n)]

# 결과 출력
print(findmincost(n, costs))

```

-----
