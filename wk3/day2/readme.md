# 2일차 알고리즘 문제해결

### 1️⃣ 2851번 - 슈퍼 마리오

난이도: 브론즈

분류: 브루트포스

링크: [2851번: 슈퍼 마리오](https://www.acmicpc.net/problem/2851)


```python
#40ms
score = 0
mushrooms = []
beforescore = 0
for i in range(10):
    num = input()
    mushrooms.append(int(num))

for mushroom in mushrooms:
    beforescore = score
    score += mushroom
    if score >= 100:
        break

if abs(100 - score) == abs(100 - beforescore):
    print(max(score, beforescore))
elif abs(100 - score) < abs(100 - beforescore):
    print(score)
else:
    print(beforescore)
```

--------

### 2️⃣25176번: 청정수열

난이도: 브론즈

분류: 조합

링크: [25176번: 청정수열](https://www.acmicpc.net/problem/25176)


```python
#40ms
num = int(input())
cnt = 1

for i in range(1, num+1):
  cnt *= i

print(cnt)

```

--------

### 3️⃣30821번: 별자리가 될 수 있다면

난이도: 브론즈

분류: 조합

링크: [30821번: 별자리가 될 수 있다면](https://www.acmicpc.net/problem/30821)


```python
#40ms
from math import comb

vertex = int(input().strip())
result = comb(vertex, 5)

print(result)
```

--------

### 4️⃣5568번: 카드놓기

난이도: 실버

분류: 백트래킹

링크: [5568번: 카드놓기](https://www.acmicpc.net/problem/5568)


```python
#44ms
from itertools import permutations

cardcnt = int(input())
k = int(input())
cards = []
for _ in range(cardcnt):
    card = int(input())
    cards.append(card)

strset = set()

for deck in permutations(cards, k):
    strdeck = "".join(map(str, deck))
    strset.add(strdeck)

print(len(strset))

```

--------

### 5️⃣ 1213번: 팰린드롬 만들기

난이도: 실버

분류: 완전 탐색

링크: [1213번: 팰린드롬 만들기](https://www.acmicpc.net/problem/1213)

```python
from collections import Counter

s = list(str(input()))

cntls = Counter(s)
oddcnt = 0

# 홀수 빈도의 문자가 몇 개인지 세기
for i in cntls.values():
    if i % 2 == 1:
        oddcnt += 1

if (len(s) % 2 == 0 and oddcnt == 0) or (len(s) % 2 == 1 and oddcnt == 1):
    half = []
    midchr = ""
    
    for char, count in sorted(cntls.items()):
        if count % 2 == 1:
            midchr = char
        half.extend(char * (count // 2))
    
    # 반쪽을 만들고, 중앙 문자를 넣고, 반쪽을 뒤집어서 붙임
    half_str = "".join(half)
    palindrome = half_str + midchr + half_str[::-1]
    print(palindrome)
else:
    print("I'm Sorry Hansoo")
```
--------

### 6️⃣ 8911번 - 거북이

난이도: 실버

분류: 시뮬레이션

링크: [8911번: 거북이](https://www.acmicpc.net/problem/8911)


```python
#2852ms
def moveturtle(commandline):
    #방향에 따른 x, y 이동 정의
    directions = {
        0: (0, 1),   #북쪽
        1: (1, 0),   #동쪽
        2: (0, -1),  #남쪽
        3: (-1, 0)   #서쪽
    }

    #초기 위치와 방향 (북쪽)
    x, y = 0, 0
    direction = 0

    #이동한 모든 좌표를 저장
    minx = maxx = x
    miny = maxy = y

    for command in commandline:
        if command == 'F':
            x += directions[direction][0]
            y += directions[direction][1]

        elif command == 'B':
            x -= directions[direction][0]
            y -= directions[direction][1]

        elif command == 'L':
            direction = (direction-1) % 4

        elif command == 'R':
            direction = (direction+1) % 4
        
        #최소, 최대 좌표 갱신
        minx = min(minx, x)
        maxx = max(maxx, x)
        miny = min(miny, y)
        maxy = max(maxy, y)
    
    #직사각형의 넓이 계산
    width = maxx - minx
    height = maxy - miny

    return width * height


testcase = int(input())
for _ in range(testcase):
    commandline = input().strip()
    print(moveturtle(commandline))

```

--------

### 7️⃣ 13335번 - 트럭

난이도: 실버

분류: 시뮬레이션, 큐 (덱)

링크: [13335번 - 트럭](https://www.acmicpc.net/problem/13335)


```python
#68ms
from collections import deque

truckcount, length, weight = map(int, input().split())
trucks = list(map(int, input().split()))

def crossbridge(truckcount, length, weight, trucks):
    time = 0
    bridge = deque([0] * length)  # 다리의 상태를 나타내는 큐
    bridgeweight = 0  # 현재 다리 위의 트럭들의 무게 합
    truckindex = 0  # 현재 대기중인 트럭의 인덱스

    while truckindex < truckcount or bridgeweight > 0:
        time += 1
        # 다리에서 트럭을 한 칸씩 이동
        exitingtruck = bridge.popleft()
        bridgeweight -= exitingtruck

        if truckindex < truckcount:
            # 다음 트럭이 다리에 올라갈 수 있는지 확인
            nextruck = trucks[truckindex]
            if bridgeweight + nextruck <= weight:
                bridge.append(nextruck)
                bridgeweight += nextruck
                truckindex += 1
            else:
                bridge.append(0)  # 다음 트럭이 올라갈 수 없다면 빈 공간 유지

    return time

print(crossbridge(truckcount, length, weight, trucks))
```

--------

### 8️⃣ 17086번 - 아기 상어 2

난이도: 실버

분류: 브루트포스, BFS

링크: [17086번: 아기 상어 2](https://www.acmicpc.net/problem/17086)


```python
#76ms
from collections import deque

n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]

#상하좌우 및 대각선 이동을 위한 배열
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

#BFS 탐색을 위한 큐 초기화
q = deque([(i, j) for i in range(n) for j in range(m) if maps[i][j]])

#가장 먼 거리 초기화
longest = 0  

while q: 
    #큐에서 현재 위치를 꺼내고
    x, y = q.popleft()
    #8방향 탐색  
    for i in range(8):  
        nx = dx[i] + x
        ny = dy[i] + y
        
        #유효한 좌표인지 확인
        if 0 <= nx < n and 0 <= ny < m:
            #상어가 없는 위치인 경우
            if not maps[nx][ny]:
                #현재 거리 + 1로 갱신  
                maps[nx][ny] = maps[x][y] + 1  
                #가장 먼 거리 갱신
                longest = maps[nx][ny]  
                #큐에 새 위치 추가
                q.append((nx, ny))  

#상어가 있는 1부터 값을 더하여 주었으므로 마지막에 저장된 값에 1을 뺀 값을 출력
print(longest - 1)
```


-----
