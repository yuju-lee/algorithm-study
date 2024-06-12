# 4일차 알고리즘 문제해결

### 1️⃣ 2441번: 별 찍기 - 4

난이도: 브론즈

분류: 구현

링크:

[2441번: 별 찍기 - 4](https://www.acmicpc.net/problem/2441)


```python
#44ms
cnt = int(input())
j = 0
for i in range(cnt, 0, -1):
    print(" "*j+"*"*i)
    j+=1


```

--------

### 2️⃣ 1292번: 쉽게 푸는 문제

난이도: 브론즈

분류: 구현

링크: 

[1292번: 쉽게 푸는 문제](https://www.acmicpc.net/problem/1292)


```python
#80ms
first, last = map(int, input().split())

ls = []
for num in range(1, last+1):
    for _ in range(num):
        ls.append(num)

print(sum(ls[first-1:last]))
```

--------


### 3️⃣ 28417번: 스케이트보드

난이도: 브론즈

분류: 정렬

링크: 

[28417번: 스케이트보드](https://www.acmicpc.net/problem/28417)


```python
#3028ms
def findrunscore(ls): 
    newls = max(ls[0:2])
    return newls

def findtrickscore(ls):
    newls = ls[2:]
    newls.sort(reverse=True)
    return newls[0:2]


playercnt = int(input())
maxscore = 0
    
for _ in range(playercnt):
    score = list(map(int, input().split()))

    runscore = findrunscore(score)
    trickscore = findtrickscore(score)
    
    if maxscore < runscore + sum(trickscore):
        maxscore = runscore + sum(trickscore)

print(maxscore)

```

--------


### 4️⃣ 11899번: 괄호 끼워넣기

난이도: 실버

분류: 문자열, 스택

링크: 

[](https://www.acmicpc.net/problem/11899)



```python
#40ms
s = str(input())

def checkVPS(s):
    stack = []
    for i in range(len(s)):
        if len(stack):
            if s[i]==")" and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(s[i])
        else:
            stack.append(s[i])

    return len(stack)

print(checkVPS(s))

```

--------


 

### 5️⃣ 11561번: 징검다리

난이도: 실버

분류: 이분 탐색

링크: 

[11561번: 징검다리](https://www.acmicpc.net/problem/11561)


```python
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
```
--------

### 6️⃣ 1417번: 국회의원 선거

난이도: 실버

분류: 정렬, 힙

링크: 

[](https://www.acmicpc.net/problem/1417)


```python
import heapq

population = int(input())

ls = []

for _ in range(population):
    votecnt = int(input())
    ls.append(votecnt)

dasom = ls[0]
candidate = ls[1:]

#후보자 표를 최대 힙으로 변환
candidate = [-x for x in candidate]
heapq.heapify(candidate) #??
cnt = 0

#유일한 후보자일 경우
if population == 1:
    print(0)
else:
    while candidate and dasom <= -candidate[0]:
        #최대 힙에서 가장 큰 값을 가져와 1 감소시키기
        maxvote = -heapq.heappop(candidate)
        maxvote -= 1
        dasom += 1
        cnt += 1
        #수정된 값을 다시 힙에 삽입
        heapq.heappush(candidate, -maxvote)

    print(cnt)
```

--------

### 7️⃣ 1072번: 게임

난이도: 실버

분류: 이분 탐색

링크: 

[1072번: 게임](https://www.acmicpc.net/problem/1072)


```python
#44ms
def findratio(x, y):
    left = 1
    right = x

    ratio = int((100*y)//x)
    ans = 0
    if 99 <= ratio:
        return -1
    else:
        while left <= right:
            mid = (left+right)//2
            newratio = (y+mid) * 100 // (x+mid)
            if  ratio < newratio:
                ans = mid
                right = mid-1
            else: 
                left = mid+1
                
        
    return ans

x, y = map(int, input().split())
print(findratio(x, y))
```

--------

### 8️⃣ 2304번: 창고 다각형

난이도: 실버

분류: 스택

링크: 

[2304번: 창고 다각형](https://www.acmicpc.net/problem/2304)


```python
#80ms
max_height = 0
max_index = 0

# 기둥의 위치와 높이를 저장할 딕셔너리
pillars = {}

# 입력 처리 및 가장 높은 기둥 찾기
for _ in range(int(input())):
    x, height = map(int, input().split())
    pillars[x] = height

    if max_height < height:
        max_index = x
        max_height = height

curr = 0
area = 0

# 왼쪽 부분의 면적 계산
for i in range(max_index + 1):
    if i in pillars:ㄴ
        curr = max(curr, pillars[i])
    area += curr

curr = 0

# 오른쪽 부분의 면적 계산
for i in range(1000, max_index, -1):
    if i in pillars:
        curr = max(curr, pillars[i])
    area += curr

print(area)


```


-----
