# 3일차 알고리즘 문제해결

### 1️⃣ 24263번: **알고리즘 수업 - 알고리즘의 수행 시간 2**

난이도: 브론즈

분류: 구현

링크: [24263번: 알고리즘 수업 - 알고리즘의 수행 시간 2](https://www.acmicpc.net/problem/24263)

```python
print(len(input().split()))
```

--------

### 2️⃣ 24265번: **알고리즘 수업 - 알고리즘의 수행 시간 4**

난이도: 브론즈

분류: 구현

링크: [24265번: 알고리즘 수업 - 알고리즘의 수행 시간 4](https://www.acmicpc.net/problem/24265)


```python
# 총 시행횟수: 1+2+3+4+...+(n-1) > 가우스덧셈
# 시간복잡도: O(n^2)
n = int(input())
#가우스덧셈 출력
print(int(n*(n-1)/2))
#n*n = n^2, 최고차항 2
print(3)
```

--------


### 3️⃣ 24267번: **알고리즘 수업 - 알고리즘의 수행 시간 6**

난이도: 브론즈

분류: 구현

링크: [24267번: 알고리즘 수업 - 알고리즘의 수행 시간 6](https://www.acmicpc.net/problem/24267)


```python
n = int(input())
print((n*(n-1)*(n-2))/6)
print(3)
```

--------

### 4️⃣ 24416번: 알고리즘 수업 - 피보나치 수 1

난이도: 브론즈

분류: 구현

링크: [24416번: 알고리즘 수업 - 피보나치 수 1](https://www.acmicpc.net/problem/24416)


```python
n = int(input())
#다이나믹 프로그래밍으로 피보나치 구현
dp = [0]*100 
dp[1], dp[2]=1, 1 # fibo(1) fibo(2) = 0
# 피보나치 수열을 반복문으로 구현 (bottom up)
for i in range(3, n+1):
    dp[i] = dp[i-1]+dp[i-2]
    
print(dp[n], n-2)
```

--------

### 5️⃣ 24313번: 알고리즘 수업 - 점근적 표기 1

난이도: 실버

분류: 수학

링크: [24313번: 알고리즘 수업 - 점근적 표기 1](https://www.acmicpc.net/problem/24313)


```python
a1, a0 = map(int,input().split())
c = int(input())
n0 = int(input())

f=(a1*n0)+a0
g = n0 * c

#a1, a0이 음수일 경우를 필터링하기 위해 a1 <= c 조건 추가
if f<=g and a1<=c : print(1)
else: print(0)
```
--------

### 6️⃣ 10816번: **N과 M (2)**

난이도: 실버

분류: 해시 맵 (딕셔너리)

링크: [15650번: N과 M (2)](https://www.acmicpc.net/problem/15650)


```python
from itertools import combinations

n, m = map(int, input().split())

# [1, 2, 3, 4]
numList = [i for i in range(1, n+1)]

for seq in combinations(numList, m):
    print(*seq)
```

--------


### 7️⃣ 25192번: 인사성 밝은 곰곰이

난이도: 실버

분류: 문자열, 해시 맵 (딕셔너리)

링크: [25192번: 인사성 밝은 곰곰이](https://www.acmicpc.net/problem/25192)



```python
n= int(input())

emoticon = set()
cnt = 0

for i in range(n):
    name = str(input())
    if name != 'ENTER': #enter가 아닐경우
        if name not in emoticon: 
            cnt += 1
            emoticon.add(name)
    else:
        emoticon.clear()

print(cnt)
```

--------

### 8️⃣ 1764번: 듣보잡

난이도: 실버

분류: 문자열, 해시 맵 (딕셔너리)

링크: [1764번: 듣보잡](https://www.acmicpc.net/problem/1764)


```python
n, m = map(int, input().split())

d = set()
for i in range(n):
    name = str(input())
    d.add(name)

b = set()
for i in range(m):
    name = str(input())
    b.add(name)

s = sorted(d.intersection(b))
print(len(s))
for i in range(len(s)):
    print(s[i])
```


-----

- 다이나믹 프로그래밍에 대해
    - 다이나믹 프로그래밍?
        - 필요한 **계산 값을 저장해두었다가 재사용**하는 알고리즘 설계 기법
        - 큰 문제를 한번에 해결하기 어려울 때, 여러개의 작은 문제로 나누어 푸는 '분할 정복' 알고리즘이 있다. 이때 **동일한 작은 문제**들이 **반복적으로 계산**되는 경우가 생길 수 있다. **그 문제를 매번 재계산 하지 않고 값을 저장했다가 재사용하는 기법이 바로 다이나믹 프로그래밍**이다. 메모리 공간을 약간 더 사용하여 시간을 획기적으로 줄일 수 있는 방법이다.
    - 다음 조건 만족 시 사용할 수 있음:
        - 최적 부분 구조
        - 중복 하위 문제
    - **Topdown (하향식)**
        - 메모이제이션(memoiztion)을 사용하여 다이나믹 프로그래밍을 구현하는 방식
        - **메모이제이션**(memoiztion)?
            - 한번 구한 계산 결과를 메모리 공간에 메모해두고, 같은 식을 다시 호출하면 메모한 결과 그대로 가져오는 기법
        - 탑다운 방식은 큰 문제를 해결하기 위해 작은 문제를 호출한다고 하여 **하향식**이라고도 불린다.
        - 탑다운방식은 **재귀함수**를 이용하여 구현할 수 있다.
    - **Bottom-Up (상향식)**
        - 타블레이션(tabulation)을 사용하여 다이나믹 프로그래밍을 구현하는 방식
        - **타블레이션**(tabulation)?
            - 하위 문제부터 천천히 해결하면서 더 큰 문제를 해결하는 기법
        - 하위 문제부터 시작해서 더 큰 문제를 해결해 나가기 때문에 **상향식**이라고도 한다.
        - 바텀업방식은 **반복문**을 이용하여 구현할 수 있다.