# 2일차 알고리즘 문제해결

### 1️⃣ 9933번: 민균이의 비밀번호

난이도: 브론즈

분류: 해시 테이블 (딕셔너리)

링크: [9933번: 민균이의 비밀번호](https://www.acmicpc.net/problem/9933)


```python
#44ms
n = int(input())
dic=[] #리스트

for cnt in range(n):
    s = str(input())
    dic.append(s)

for i in range(len(dic)):
    rev = dic[i]
    if rev[::-1] in dic:
        ans = dic[i]
        break

print(len(ans), ans[(len(ans)//2)])

```

--------

### 2️⃣ 27160번: 할리갈리

난이도: 브론즈

분류: 해시

링크: [27160번: 할리갈리](https://www.acmicpc.net/problem/27160)


```python
#4224ms

n = int(input())

dic = {
    'STRAWBERRY':0, 
    'BANANA':0, 
    'LIME':0, 
    'PLUM':0
    }

for i in range(n):
    card, cnt = input().split()
    dic[card] = dic[card]+int(cnt)

if 5 in dic.values(): 
    print('YES')
else: 
    print('NO')
```

--------

### 3️⃣ 31562번: 전주 듣고 노래 맞추기

난이도: 브론즈

분류: 해시 

링크: [31562번: 전주 듣고 노래 맞추기](https://www.acmicpc.net/problem/31562)


```python
#216ms

n, m = map(int, input().split()) #아는노래개수 n / 맞히려는 노래 개수 m
dic = dict()

for i in range(n):
    parts = str(input()).split()
    name = parts[1]
    notes = ''.join(parts[2:])

    dic.setdefault(name, notes[0:3])

for j in range(m):
    q = str(input()).replace(' ', '') #ex. CCC
    ansls = [k for k, v in dic.items() if v == q]
    if len(ansls) == 0:
        print("!")
    elif len(ansls) ==1:
        print(ansls[0])
    else:
        print("?")

```

--------


### 4️⃣ 1927번: 최소 힙

난이도: 실버 

분류: 힙

링크: [1927번: 최소 힙](https://www.acmicpc.net/problem/1927)


```python
#116ms
from heapq import *
from sys import stdin

input = stdin.readline

n = int(input()) 
heap = []

for _ in range(n):
    a = int(input())
    if a:
        heappush(heap, a)
    else:
        if heap:
            print(heappop(heap))
        else:
            print(0)

```

--------

### 5️⃣ 15829번: hashing

난이도: 브론즈

분류: 해시 

링크: [15829번: hashing](https://www.acmicpc.net/problem/15829)


```python
#40ms / 50점
dic = {}
cnt = 0
for j in range(97, 123): #소문자
    dic.setdefault(chr(j), cnt+1)
    cnt += 1

n = int(input())
s = str(input())
sum = 0

for i in range(n):
    value = dic[s[i]]
    sum += value * 31**i

print(sum % 1234567891)

```
--------

### 6️⃣ 1920번: 수 찾기

난이도: 실버

분류: 해시 테이블 (딕셔너리)

링크: [1920번: 수 찾기](https://www.acmicpc.net/problem/1920)


```python
#192ms
n = int(input())
a = set((map(int, input().split())))
m = int(input())
b = list(map(int, input().split())) #여기 값이 a에 있는지 확인

for i in range(m):
    if b[i] in a:
        print(1, end=" ")
    else:
        print(0, end=" ")

```

--------

### 7️⃣ 9375번: 패션왕 신해빈

난이도: 실버

분류: 해시 테이블 (딕셔너리)

링크: [9375번: 패션왕 신해빈](https://www.acmicpc.net/problem/9375)


```python
import sys

t = int(input())

for _ in range(t):
    cloth = {}
    result = 1
    n = int(input())
    for _ in range(n):
        name, type = sys.stdin.readline().rstrip().split()

        if not type in cloth:
            cloth[type] = 1
        else:
            cloth[type] += 1

    for i in cloth:
        result *= (cloth[i] + 1)

    print(result - 1)

```

--------

### 8️⃣ 11286번: 절댓값 힙

난이도: 실버

분류: 힙

링크: [11286번: 절댓값 힙](https://www.acmicpc.net/problem/11286)


```python
#148ms
import heapq
from sys import stdin

input = stdin.readline
heap = []

count = int(input())

for i in range(1, count + 1):
    try:
        num = int(input())
        if num != 0:
            # (절대값, 실제값) 형태로 저장
            heapq.heappush(heap, (abs(num), num))
        else: # 0일 경우 배열에서 절대값이 가장 작은 값을 출력하고 제거
            if len(heap):
                print(heapq.heappop(heap)[1])
            else:
                print(0)
    except:
        print(0)
```


-----
