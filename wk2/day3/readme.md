# 3일차 알고리즘 문제해결

### 1️⃣ 2309번: 일곱 난쟁이

난이도: 브론즈

분류: 정렬

링크:

[일곱 난쟁이](https://www.acmicpc.net/problem/2309)


```python
#44ms
from itertools import combinations

minimi = []

for _ in range(9):
    height = int(input())
    minimi.append(height)

minimi.sort()

#9개 입력 중 7개의 조합 (중복없이)
perm = list(combinations(minimi, 7))

for combination in perm:
    if sum(combination) == 100:
        for height in combination:
            print(height)
        break

```

--------

### 2️⃣ 11557번: Yangjojang of The Year

난이도: 브론즈

분류: 정렬

링크: 

[Yangjojang of The Year](https://www.acmicpc.net/problem/11557)


```python
#40ms
testcase = int(input())

schls = []
for _ in range(testcase):
    schoolcnt = int(input())
    for _ in range(schoolcnt):
        school, drink = map(str, input().split())
        schls.append([int(drink), school])
    #drink를 오름차순으로
    schls.sort(key=lambda x: (x))
    #스쿨리스트의 마지막 > 두번째 인덱스 출력
    print(schls[-1][1])


```

--------


### 3️⃣ 16466번: 콘서트

난이도: 브론즈

분류: 정렬

링크: 

[16466번: 콘서트](https://www.acmicpc.net/problem/16466)


```python
#376ms
fticketcnt = int(input())
ticket = sorted(list(map(int, input().split())))

ans = 0

for i in range(1, fticketcnt+1):
    if i != ticket[i-1]:
        ans = i
        break

if ans:
    print(ans)
else:
    print(fticketcnt+1)

```

--------


### 4️⃣ 2805번: 나무 자르기

난이도: 실버

분류: 이분 탐색

링크: 

[2805번: 나무 자르기](https://www.acmicpc.net/problem/2805)


```python
#4368ms
treecnt, take = map(int, input().split())
trees = list(map(int, input().split()))

trees.sort()
ans = 0
left = 1
right = max(trees)

while left <= right:
    mid = (left+right)//2
    cnt = 0
    for tree in trees:
        if tree > mid:
            cnt += tree - mid
    
    if cnt >= take:
        ans = mid
        left = mid+1
    else:
        right = mid-1
    
print(ans)
```

--------


 

### 5️⃣ 28114번: 팀명 정하기

난이도: 브론즈

분류: 정렬 

링크: 

[28114번: 팀명 정하기](https://www.acmicpc.net/problem/28114)


```python
#40ms
first = []
second = []
for _ in range(3):
    rate, year, lastname = map(str,input().split())
    
    first.append(int(year)%100)
    second.append([int(rate), lastname[0]])
    
    first.sort(key=lambda x: x)
    second.sort(key=lambda x: (x, x), reverse=True)

print(''.join(map(str, first)))

for i in range(len(second)):
    print(second[i][1], end="")
```
--------

### 6️⃣ 11399번: ATM

난이도: 실버

분류: 정렬

링크: 

[11399번: ATM](https://www.acmicpc.net/problem/11399)


```python
#44ms
personcnt = int(input())
time = list(map(int, input().split()))

time.sort()

for i in range(1, personcnt):
    time[i] += time[i-1]

print(sum(time))


```

--------

### 7️⃣ 18870번: 좌표 압축

난이도: 실버

분류: 정렬

링크: 

[18870번: 좌표 압축](https://www.acmicpc.net/problem/18870)


```python
cnt = int(input())

coordinate = list(map(int, input().split()))
sortls = sorted(list(set(coordinate)))

dic = {}

for i in range(len(sortls)):
    dic[sortls[i]] = i

for i in coordinate:
    print(dic[i], end=" ")
```

--------

### 8️⃣ 10815번: 숫자카드

난이도: 실버

분류: 이분 탐색

링크: 

[10815번: 숫자카드](https://www.acmicpc.net/problem/10815)


```python
#772ms
cardcnt = int(input()) #숫자카드 갯수
card = list(map(int, input().split()))

numcnt = int(input())
number = list(map(int, input().split()))

dic = {}

for i in range(cardcnt):
    dic.setdefault(card[i], 1)

for j in range(numcnt):
    print(dic.get(number[j], 0), end=" ")
               
```


-----
