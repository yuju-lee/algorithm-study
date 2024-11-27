# 5일차 알고리즘 문제해결

### 1️⃣ 2738번: 행렬 덧셈

난이도: 브론즈

분류: 구현 (2차원 배열)

링크: [2738번: 행렬 덧셈](https://www.acmicpc.net/problem/2738)


```python
#48ms
def setMatrix(n):
    outls = []
    for i in range(n):
        matrix = list(map(str,input().split()))
        outls.append(matrix)

    return outls

n, m = list(map(int,input().split()))
aMatrix = setMatrix(n)
bMatrix = setMatrix(n)

for i in range(len(aMatrix)):
    for j in range(len(aMatrix[i])):
        print(int(aMatrix[i][j])+int(bMatrix[i][j]), end=" ")
    print()
```

--------

### 2️⃣ 2556번: 최댓값

난이도: 브론즈

분류: 구현 (2차원 배열)

링크: [2566번: 최댓값](https://www.acmicpc.net/problem/2566)


```python
# 36ms
matrix = []
for i in range(9):
    ls = list(map(int,input().split()))
    matrix.append(ls)

r, c, maxnum = 0, 0, 0

for i in range(9):
    for j in range(9):
        if maxnum <= matrix[i][j]:
            maxnum = matrix[i][j]
            r = i+1
            c = j+1
print(maxnum)
print(r, c)
```

--------


### 3️⃣ 10798번: 세로읽기

난이도: 브론즈

분류: 구현

링크: [10798번: 세로읽기](https://www.acmicpc.net/problem/10798)


```python
#44ms
matrix = []
maxcharcnt = 0 #최대글자수

# 입력 받기
for i in range(5):
    s = input()
    matrix.append(s)
    if len(s) > maxcharcnt:
        maxcharcnt = len(s)

# 세로로 읽어서 출력하기
for i in range(maxcharcnt):
    for j in range(5):
        if i < len(matrix[j]):
            print(matrix[j][i], end="")
```

--------

### 4️⃣ 1652번: 누울 자리를 찾아라

난이도: 실버

분류: 구현 (2차원 배열)

링크: [1652번: 누울 자리를 찾아라](https://www.acmicpc.net/problem/1652)


```python
def countseat(n, ls):
    cnt = 0
    for i in range(len(ls)):
        #각 행별로 X 개수 세기
        cntX = ls[i].count('X')
        #누울 자리가 하나라도 있는 경우
        if cntX <= n-2:
            #리스트를 문자열로
            s = ''.join(ls[i])
            #만든 문자열을 X 기준으로 잘라서 리스트로
            tmp = s.split('X') 
            #만든 리스트만큼 반복
            for j in range(len(tmp)): 
                if 1 < len(tmp[j]): #2개 이상 연속일 경우
                    cnt = cnt + 1
    return cnt

n = int(input())
ls = []

for i in range(n):
    ls.append(list(str(input())))

#세로 배열 만들기
vls = [list(row) for row in zip(*ls)]

print(countseat(n, ls), countseat(n, vls))
```

--------

### 5️⃣ 1018번: 체스판 다시 칠하기

난이도: 실버

분류: 구현 (2차원 배열)

링크: [1018번: 체스판 다시 칠하기](https://www.acmicpc.net/problem/1018)


```python
#92ms
n, m = map(int, input().split())

ls = []
for i in range(n):
    s = str(input())
    ls.append(s)

pattern1 = ['WB'*4,'BW'*4]*4 #흰색으로 시작함
pattern2 = ['BW'*4,'WB'*4]*4 #검은색으로 시작함
mincnt = float('inf')
for i in range(n-7):
    for j in range(m-7): #전체 순회
        cnt1, cnt2 = 0, 0
        for x in range(8): #패턴이랑 8개씩 나눈거랑 맞는지 확인
            for y in range(8):
                if ls[i+x][j+y] != pattern1[x][y]:
                    cnt1 += 1
                if ls[i+x][j+y] != pattern2[x][y]:
                    cnt2 += 1
        
        if min(cnt1, cnt2) < mincnt:
            mincnt = min(cnt1, cnt2)

print(mincnt)

```
--------

### 6️⃣ 1051번: 숫자 정사각형

난이도: 실버

분류: 구현 (2차원 배열)

링크: [1051번: 숫자 정사각형](https://www.acmicpc.net/problem/1051)


```python
def findsize(n, m, ls):
    #작은것부터 큰 정사각형까지 구하기
    size = 1
    #정사각형사이즈를 키워가면서 배열 순회하고 max 크기 설정
    for i in range(n):
        for j in range(m):
            curr = ls[i][j] #현재값(비교대상)
            for x in range(1, min(n-i, m-j)):
                if curr == ls[i][j+x] and curr == ls[i+x][j] and curr == ls[i+x][j+x]:
                        size = max(size, x+1)
    return size*size
                        
                        
n, m = map(int, input().split())
ls = []
for i in range(n):
    s = str(input())
    ls.append(s)
print(findsize(n, m, ls))

```

--------

### 7️⃣ 2477번: 참외밭

난이도: 실버

분류: 구현

링크: [2477번: 참외밭](https://www.acmicpc.net/problem/2477)


```python

```

--------

### 8️⃣ 16926번: 배열 돌리기 1

난이도: 골드

분류: 구현 (2차원 배열)

링크: [16926번: 배열 돌리기 1](https://www.acmicpc.net/problem/16926)


```python

```

-----
