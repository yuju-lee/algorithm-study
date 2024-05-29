# 1일차 알고리즘 문제해결

### 1️⃣ 2438번: 별 찍기 - 1

난이도: 브론즈

분류: 구현

링크: [2438번: 별 찍기 - 1](https://www.acmicpc.net/problem/2438)

```python
# 줄이 늘어날수록 별을 1개씩 더함 
# 1번 줄 1개, 2번 줄 2개 ... n번 줄은 n+1개

n = int(input("")) #input
for i in range(n):
    print("*"*(i+1)) #i+1만큼 출력
```

--------

### 2️⃣ 2480번: 주사위 세개

난이도: 브론즈

분류: 구현

링크: [2480번: 주사위 세개](https://www.acmicpc.net/problem/2480)

```python
# 규칙
# 같은 눈이 3개가 나오면 10,000원+(같은 눈)×1,000원의 상금을 받게 된다.
# 같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)×100원의 상금을 받게 된다.
# 모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)×100원의 상금을 받게 된다.

# 각 규칙마다 분기 두기
# 같은 눈이 나오는 경우를 가장 큰 분기로 두고 출력값(상금계산) 설정

while(1):
    a, b, c = map(int, input("").split())
    if 1<=a<=6 and 1<=b<=6 and 1<=c<=6: break #문제에서 제시한 조건을 입력 시 while문 탈출 후 다음 If구문 실행

if a==b==c: price = 10000+(a*1000) #3개가 같을 경우
elif a==b or b==c or a==c: #2개가 같을 경우
    if a==b or a==c: price = 1000+(a*100) #a를 기준으로 a / b,c 비교하기 (or: 두 조건 중 하나만 만족해도 됨)
    elif b==c: price = 1000+(b*100) #b를 기준으로 c와 비교
else: #값이 다 다를 경우
    if a > b and a > c: topnum = a #a가 가장 큰 값일 경우 topnum 변수에 a값 할당
    elif b > a and b > c: topnum = b #b가 가장 큰 값일 경우 topnum 변수에 b값 할당
    elif c > a and c > a: topnum = c #c가 가장 큰 값일 경우 topnum 변수에 c값 할당
    price = topnum*100

print(price) #최종 price 출력
```

--------

### 3️⃣ 2675번: 문자열 반복

난이도: 브론즈

분류: 구현

링크: [2675번: 문자열 반복](https://www.acmicpc.net/problem/2675)

```python
# 테스트케이스만큼 전체 반복 > 가장 바깥 for문
# 입력받는 R값만큼 print S
# S의 글자를 전부 list의 요소로 넣어 해당 요소를 for문으로 R회 반복 출력

t = int(input("")) #테스트 케이스 count

for i in range(t): #케이스 count 만큼 for문 반복
		result = '' #변수 초기화
    r, s = map(str, input("").split()) #반복횟수 int R, 문자열 S값 입력받음
    r = int(r)
    slist = list(map(str,s)) #string -> list 형변환 'add' -> ['a','d','d']
    
    for j in range(len(slist)): #글자수만큼 반복 (글자 하나하나를 전부 list element로 바꾸었기에 list length == 글자수)
        result += slist[j]*r # list 한 요소를 *r 만큼 반복하고 result 변수에 쌓기
    
    print(result)
    
    result='' #다음 테스트케이스를 위해 초기화
```

--------

### 4️⃣ 2445번: 별 찍기 - 8

난이도: 브론즈

분류: 구현

링크: [2445번: 별 찍기 - 8](https://www.acmicpc.net/problem/2445)

```python
# for문 2개 쓰기 싫어서...
# 한 문장의 총 글자수: n*2개
# 별의 개수는 첫줄에서부터 2개에서 시작해 배수로 올라가 n*2개까지 증가 후 배수로 감소
# 공백의 개수는 총 글자 수에서 별의 개수를 뺀 나머지
# for문 2개 쓰기 싫으니 i값으로 조건 걸어서 n+1번째 줄부터 else구문으로 빠지게 함
# else 구문에서는 별의 개수를 총 글자수에서 i+1값을 빼어 2개씩 빠지게 함
# 공백 count는 위와 같이 전체 줄에서 별의 개수를 뺀 값

n = int(input(""))
for i in range(0, n*2-1): #문제에서 제시한 조건 0~n*2-1번 순회
    if i < n: #0부터 n-1번 순회 (별 개수 증가)
        star = i+1 #회차별로 별 1개 증가
        space = n*2 - ((star)*2) #한 줄의 총 글자수 n*2 에서 별 갯수*2(양쪽이라 2개)를 뺀 나머지가 공백의 개수
        print("*"*(star)+" "*(space)+"*"*(star)) #양쪽에 별 넣기
    else: #n번부터 n*2-1까지 순회 (별 개수 감소)
        star = (n*2) - (i+1) #총 글자수에서 i+1만큼씩 감소 (2개씩 빠지니깐)
        space = (n*2) - ((star)*2) #한 줄의 총 글자수 n*2 에서 별 갯수*2(양쪽이라 2개)를 뺀 나머지가 공백의 개수
        print("*"*(star)+" "*(space)+"*"*(star))
        
# for문 2개 (위와 같은 로직)
# 이게 더 나을지도?
n = int(input(""))
for i in range(1,n+1):
    print("*"*i+" "*(2*(n-i))+"*"*i)
for j in range(1,n):
    print("*"*(n-j)+" "*(2*j)+"*"*(n-j))
```

--------

### 5️⃣ 1924번: 2007년

난이도: 브론즈

분류: 구현

링크: [1924번: 2007년](https://www.acmicpc.net/problem/1924)

```python
while(1):
    m, d = map(int,input("").split())
    if 1<=m<=12 and 1<=d<=31: break

endone = [1,3,5,7,8,10,12]
endzero = [4,6,9,11]
endeight = [2]
days = ['MON','TUE','WED','THU','FRI','SAT','SUN']
daynum = []*31
dic = {}
keys = []

def makekey(i, j):
    key = str(i)+"/"+str(j)
    return key

for i in range(1, 13): #1월부터 12월까지
    if i in endone: #31일로 끝나는 달
        for j in range(1, 32): keys.append(makekey(i, j))
    elif i in endzero: #30일로 끝나는 달
        for j in range(1, 31): keys.append(makekey(i, j))
    else: #28일로 끝나는 달
        for j in range(1, 29): keys.append(makekey(i, j))

for i in range(len(keys)):
    dic.setdefault(keys[i], days[i%7])

setData = str(m)+"/"+str(d)
print(dic[setData])
```
--------


### 6️⃣ 1193번: 분수찾기

난이도: 실버

분류: 구현

링크: [1193번: 분수찾기](https://www.acmicpc.net/problem/1193)

```python
x = int(input(""))
endnum = 0
box = 0
while(1):
    endnum = endnum+box
    if endnum >= x : 
        break
    box = box+1

prelastnum = endnum - box
xindex = x - prelastnum

if box%2 == 0:
    for i in range(1, box+1): 
        x = i
        y = (box+1)-i
        if i == xindex:
            print(str(x)+"/"+str(y))
            break
else: 
    for i in range(1, box+1): #박스번호
        y = i
        x = (box+1)-i
        if i == xindex:
            print(str(x)+"/"+str(y))
            break
```

--------


### 7️⃣ 25206번: 너의 평점은

난이도: 실버

분류: 구현

링크: [25206번: 너의 평점은](https://www.acmicpc.net/problem/25206)

```python
#(학점 × 과목평점)의 합을 학점의 총합으로 나눈 값
scoreData = []
for i in range(20):
    inpt = list(map(str,input("").split(" ")))    
    scoreData.append(inpt)

score = {
    "A+":4.5,
    "A0":4.0,
    "B+":3.5,
    "B0":3.0,
    "C+":2.5,
    "C0":2.0,
    "D+":1.5,
    "D0":1.0,
    "F":0.0     
         }
credit, sumscore, sumcredit = 0, 0, 0
for i in range(len(scoreData)):
    if scoreData[i][2] == "P":
        pass
    else:
        credit = float(scoreData[i][1]) #학점
        indscore = score[scoreData[i][2]] #평점
        sumscore = sumscore+(credit * indscore)
        sumcredit = sumcredit+credit

print("전공평점:", sumscore/sumcredit)
```

--------

### 8️⃣ 8979번: 올림픽

난이도: 실버

분류: 구현

링크: [8979번: 올림픽](https://www.acmicpc.net/problem/8979)

```python
import sys
while (1):
		#cn: 국가수 / sn: 등수를 알고 싶은 국가의 번호
    cn, sn = map(int,sys.stdin.readline().split()) 
    if 1<=cn<=1000 and 1<=sn<=cn: break

arr = []
for i in range(cn): #입력값을 2차원 배열로 만들기
    country, gold, silver, bronze = map(int,input("").split())
    temp = [country, gold, silver, bronze]
    arr.append(temp)

scoretemp = []
bestscore = 0
for i in range(len(arr)):
		#가중치 부여하여 점수 총합
    score = (arr[i][1]*20)+(arr[i][2]*10)+(arr[i][3]*5)
    arr[i].append(score)
    scoretemp.append(score)

#총합으로 순위 정하기
rank = []
for i in range(len(scoretemp)):
    rank.append(1)
    for j in range(len(scoretemp)):
        if scoretemp[i] < scoretemp[j]:
            rank[i] = rank[i]+1

for i in range(len(arr)): arr[i].append(rank[i])

for i in range(len(arr)):
    if arr[i][0] == sn:
        print(arr[i][5])
```


