# 1일차 알고리즘 문제해결

### 1️⃣ 2798번: 블랙잭

난이도: 브론즈

분류: 브루트포스

링크: [2798번: 블랙잭](https://www.acmicpc.net/problem/2798)


```python
#144ms
from itertools import combinations

cardnum, limit = map(int, input().split())
cards = list(map(int, input().split()))

cardcombi = list(combinations(cards, 3))

sumls = []

for card in cardcombi:
    deck = list(card)
    if sum(deck) <= limit:
        sumls.append(sum(deck))

print(max(sumls))

```

--------
### 2️⃣ 1440번: 타임머신

난이도: 브론즈

분류: 브루트 포스

링크 : [1440번: 타임머신](https://www.acmicpc.net/problem/1440)


```python
#44ms
from itertools import permutations

time = str(input())
intime = time.split(":")

timeperm = list(permutations(intime, 3))
cnt = 0
for times in timeperm:
    currtime = list(map(int, times))

    hour = currtime[0]
    min = currtime[1]
    sec = currtime[2]
    
    if 0 < hour < 13:
        if min < 60:
            if sec < 60:
                cnt += 1

print(cnt)

```

--------


### 3️⃣ 2061번: 좋은 암호

난이도: 브론즈

분류: 브루트 포스

링크 : [2061번: 좋은 암호](https://www.acmicpc.net/problem/2061)


```python
#이렇게 썼더니 시간초과나서
k, l = map(int, input().split())
cnt = 0

#l이 소수인지 확인
#l이 소수가 아닐 경우
i = 1
while i < k/l:
    i += 1
    if i*l == k:
        cnt += 1
        break
    

if 0 < cnt:
    print("GOOD")
else:
    print(f"BAD {i}")

#기능 쪼갬
#1600ms
def checkprime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

#기능쪼개기
def smallestprime(k, limit):
    for i in range(2, limit):
        if checkprime(i) and k % i == 0:
            return i
    return None

k, limit = map(int, input().split())

smallest = smallestprime(k, limit)

if smallest is None:
    print("GOOD")
else:
    print(f"BAD {smallest}")

```

--------

### 4️⃣ 10419번: 지각

난이도: 브론즈

분류: 브루트 포스

링크 : [10419번: 지각](https://www.acmicpc.net/problem/10419)


```python
#36ms
testcase = int(input())

for _ in range(testcase):
    candidate = []
    late = 0
    time = int(input())
    while late < time:
        if late + (late * late) <= time:
            candidate.append(late)
        late += 1

    print(max(candidate))
```

--------


### 5️⃣ 1251번: 단어 나누기

난이도: 실버

분류: 브루트 포스

링크: [1251번: 단어 나누기](https://www.acmicpc.net/problem/1251)


```python
#32ms
from itertools import combinations

word = list(str(input()))
ans = ''

#인덱스 조합 생성해서 그 조합으로 단어 자르기
for i, j in combinations(range(1, len(word)), 2): 
    p1 = word[:i]
    p2 = word[i:j]
    p3 = word[j:]

    #단어 뒤집어서 합치기
    rword = p1[::-1] + p2[::-1] + p3[::-1]

    #각 조합 중 사전상 제일 앞 단어 넣기
    if ans == '' or rword < ans:
        ans = rword

anstr = ''.join(ans)

print(anstr)
```
--------

### 6️⃣ 4673번: 셀프 넘버

난이도: 실버

분류: 브루트포스

링크: [4673번: 셀프 넘버](https://www.acmicpc.net/problem/4673)


```python
#48ms
def findnum(n):
    total = n
    while n > 0:
        total += n%10
        n //= 10
    return total

num = set()

for i in range(1, 10001):
    num.add(findnum(i))

for i in range(1, 10001):
    if i not in num:
        print(i)
```

--------

### 7️⃣ 1063번: 킹

난이도: 실버

분류: 시뮬레이션

링크: [1063번: 킹](https://www.acmicpc.net/problem/1063)


```python
#36ms
def pos2xy(pos):
    return ord(pos[0]) - 65, int(pos[1]) - 1

def xy2pos(x, y):
    return chr(x + 65) + str(y + 1)

dic = {
    'R': [1, 0],
    'L': [-1, 0],
    'B': [0, -1],
    'T': [0, 1],
    'RT': [1, 1],
    'LT': [-1, 1],
    'RB': [1, -1],
    'LB': [-1, -1]
}

kingpos, rockpos, movecnt = input().split()
movecnt = int(movecnt)

# 초기위치 > 좌표변경
kx, ky = pos2xy(kingpos)
rx, ry = pos2xy(rockpos)

for _ in range(movecnt):
    move = input().strip()
    dx, dy = dic[move]
    
    #킹의 새 위치
    finalkx, finalky = kx + dx, ky + dy
    
    #킹이 체스판을 벗어나지 않을 때
    if 0 <= finalkx < 8 and 0 <= finalky < 8:
        #돌의 위치와 같아지면 돌도 이동
        if finalkx == rx and finalky == ry:
            finalrx, finalry = rx + dx, ry + dy
            #돌이 체스판을 벗어나지 않으면
            if 0 <= finalrx < 8 and 0 <= finalry < 8:
                kx, ky = finalkx, finalky
                rx, ry = finalrx, finalry
        else:
            kx, ky = finalkx, finalky

print(xy2pos(kx, ky))
print(xy2pos(rx, ry))

```

--------

### 8️⃣ 1182번 - 부분수열의 합

난이도: 실버

분류: 브루트포스

링크: [1182번: 부분수열의 합](https://www.acmicpc.net/problem/1182)


```python
#504ms
from itertools import combinations 

count, sumnum = map(int, input().split())
numbers = list(map(int, input().split()))
ans = 0
for i in range(1, count+1):
    tmp = list(combinations(numbers, i))
    for j in tmp:
        if sum(j) == sumnum:
            ans += 1
print(ans)

```


-----
