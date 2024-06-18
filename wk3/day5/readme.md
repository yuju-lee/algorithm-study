# 5일차 알고리즘 문제해결

### 1️⃣1145번: 적어도 대부분의 배수

난이도: 브론즈

분류:  완전탐색

링크: [1145번: 적어도 대부분의 배수](https://www.acmicpc.net/problem/1145)


```python
#256ms
def findnumber(arr):
    minnum = min(arr)
    
    while minnum:
        cnt = 0
        for num in arr:
            if minnum % num == 0:
                cnt += 1
        if cnt >= 3:
            return minnum
        minnum += 1

arr = list(map(int, input().split()))
result = findnumber(arr)
print(result)

```

--------
### 2️⃣1292번: 쉽게 푸는 문제

난이도: 브론즈

분류: 완전 탐색

링크: [1292번: 쉽게 푸는 문제](https://www.acmicpc.net/problem/1292)


```python
first, last = map(int, input().split())

ls = []
for num in range(1, last+1):
    for _ in range(num):
        ls.append(num)

print(sum(ls[first-1:last]))
```

--------

### 3️⃣21313번: 문어

난이도: 브론즈

분류: 그리디 알고리즘

링크: [21313번: 문어](https://www.acmicpc.net/problem/21313)


```python
octopus = int(input())

if octopus % 2 == 0:
    ans = '12'*(octopus//2)
    print(' '.join(ans))
else:
    ans = '12'*(octopus//2) +'3' 
    print(' '.join(ans))
```

--------

### 4️⃣17202번: 핸드폰 번호 궁합

난이도: 브론즈

분류: DP

링크: [17202번: 핸드폰 번호 궁합](https://www.acmicpc.net/problem/17202)


```python
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

### 5️⃣ 11047번 - 동전 0

난이도: 실버

분류: 그리디

링크: [11047번 - 동전 0](https://www.acmicpc.net/problem/11047)


```python
#40ms
count, balance = map(int,input().split())
arr = []
for _ in range(count):
    score = int(input())
    arr.append(score)

arr.reverse()

cnt = 0

for price in arr:
    if balance // price > 0:
        cnt = cnt+(balance//price)
        balance = balance - price*(balance//price)
        
print(cnt)

```
--------


### 6️⃣ 2512번 - 예산

난이도: 실버

분류: 이분 탐색

링크: [2512번 - 예산](https://www.acmicpc.net/problem/2512)


```python
#84ms
citycount = int(input())
budgets = list(map(int, input().split()))
total = int(input())

#모든 도시의 예산 총합이 총 예산보다 작거나 같을 경우 최대 예산 출력
if sum(budgets) <= total:    
    print(max(budgets))

else:
    budgets.sort()
    left = 0
    right = max(budgets)

    while left <= right:
        mid = (left + right) // 2 
        find = 0
        
        #현재 중간 값(mid)으로 모든 도시의 예산을 계산하여 합산
        for budget in budgets:
            find += min(budget, mid)
            
        #합산한 예산이 총 예산 이하일 경우
        if find <= total:
            left = mid + 1
        else:
            #합산한 예산이 총 예산을 초과할 경우, right 값 감소
            right = mid - 1

    print(right)
```

--------

### 7️⃣ 13305번 - 주유소

난이도: 실버

분류: 그리디

링크: [13305번: 주유소](https://www.acmicpc.net/problem/13305)


```python
#100ms
def findcost(citycount, lengths, prices):
    total = 0
    minprice = prices[0]
    
    for i in range(citycount-1):
        # 현재 도로를 지나기 위한 기름 비용 추가
        total += minprice * lengths[i]
        
        # 만약 현재 주유소의 가격이 더 싸다면 갱신
        if prices[i+1] < minprice:
            minprice = prices[i+1]
    
    return total

citycount = int(input())
lengths = list(map(int, input().split()))
prices = list(map(int, input().split()))

# 최소 비용 계산 및 출력
print(findcost(citycount, lengths, prices))
```

--------

### 8️⃣ 1713번 - 후보 추천하기

난이도: 실버

분류: 시뮬레이션

링크: [1713번: 후보 추천하기](https://www.acmicpc.net/problem/1713)


```python
from collections import defaultdict, deque

def findbest(N, recom):
    frame = deque(maxlen=N)
    studentcount = defaultdict(int)
    stamp = defaultdict(int)

    current = 0
    for student in recom:
        current += 1
        if student in studentcount:
            studentcount[student] += 1
        else:
            if len(frame) >= N:
                #가장 적은 추천 찾기
                mincount = min(studentcount[stu] for stu in frame)
                #가장 오래된 사람
                oldest = min(
                    (stu for stu in frame if studentcount[stu] == mincount),
                    key=lambda stu: stamp[stu]
                )
                #사진 제거
                frame.remove(oldest)
                del studentcount[oldest]
                del stamp[oldest]
            #새로운 학생 추가
            frame.append(student)
            studentcount[student] = 1
            stamp[student] = current

    final = sorted(frame)
    return final

n = int(input())
total = int(input())
recom = list(map(int, input().split()))

result = findbest(n, recom)
print(' '.join(map(str, result)))
```

-----
