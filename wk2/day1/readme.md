# 1일차 알고리즘 문제해결

### 1️⃣ 1152번: 단어의 갯수

난이도: 브론즈

분류: 문자열

링크: [1152번: 단어의 개수](https://www.acmicpc.net/problem/1152)

```python
print(len(input().split()))
```

--------

### 2️⃣ 27160번: 할리갈리

난이도: 브론즈

분류: 문자열, 해시 맵 (딕셔너리)

링크: [27160번: 할리갈리](https://www.acmicpc.net/problem/27160)


```python
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

### 3️⃣ 2908번: 상수

난이도: 브론즈

분류: 문자열

링크: [2908번: 상수](https://www.acmicpc.net/problem/2908)


```python
x, y = map(str, input().split())

xr = x[::-1]
yr = y[::-1]

if int(xr) < int(yr): print(int(yr))
else: print(int(xr))
```

--------

### 4️⃣ 1157번: 단어 공부

난이도: 브론즈

분류: 구현

링크: [1157번: 단어 공부](https://www.acmicpc.net/problem/1157)



```python
s = str(input()).upper()

ls = list(s)
dic = {} 

#key: 아스키코드, value: 0인 dic 생성
for i in range(65,91): 
    dic.setdefault(i, 0)

#입력받은 글자수대로 카운트
for i in range(len(ls)):
    a = ord(ls[i])
    dic[a] = dic[a] + 1

#dic의 value만 리스트 생성
dicvalues = list(dic.values())

#최대값 구하기
maxdata = max(dicvalues)

#최대값을 가지는 모든 인덱스를 maxindex 리스트로 저장
maxindex = list(filter(lambda x: dicvalues[x] == maxdata, range(len(dicvalues))))

#maxindex의 length값으로 중복 계산해 2개 이상이면 ? 출력
if  1 < len(maxindex):
    print("?")
else:
    print(chr(maxindex[0]+65))
```

--------

### 5️⃣ 1546번: 평균

난이도: 브론즈

분류: 구현

링크: [1546번: 평균](https://www.acmicpc.net/problem/1546)


```python
#과목 count
subject = int(input())

#점수를 스트링으로 입력받아 공백으로 자르고 리스트 생성
s = str(input()).split(" ")

#리스트를 int형으로 변환하여 score에 할당
score = list(map(int, s))

#최고 점수 추출
maxScore = max(score)

#총합 변수 초기화
sumScore = 0

#각각의 새로운 성적을 계산해 총합 변수에 할당
for i in range(subject):
    score[i] = (score[i]/maxScore)*100
    sumScore += score[i]

#해당 변수를 과목 수로 나누기
print(sumScore/subject)
```
--------

### 6️⃣ 7785번: 회사에 있는 사람

난이도: 실버

분류: 문자열, 해시 맵 (딕셔너리)

링크: [7785번: 회사에 있는 사람](https://www.acmicpc.net/problem/7785)


```python
n = int(input())

dic = dict()

for i in range(n):
    name, flag = input().split()
    dic[name] = flag

employee = list([k for k, v in dic.items() if v == 'enter'])

srt = sorted(employee, reverse=True)

for i in range(len(srt)): 
    print(srt[i])


```

--------

### 7️⃣ 20291번: 파일 정리

난이도: 실버

분류: 문자열

링크: [20291번: 파일 정리](https://www.acmicpc.net/problem/20291)


```python
n = int(input())

data = dict()

for i in range(n):
    fname, ftype = input().split(".")
    #get()으로 불러와서 +1 / get() -> O(1)
    #get(x, y) = y는 디폴트값
    data[ftype] = data.get(ftype, 0) + 1

#소트 후 딕셔너리 key, value를 리스트로
sortdata = sorted(data.items())

#출력
for i in range(len(sortdata)):
    print(sortdata[i][0], sortdata[i][1])
```

--------

### 8️⃣ 11478번: 서로 다른 부분 문자열의 개수

난이도: 실버

분류: 문자열, 해시 맵 (딕셔너리)

링크: [11478번: 서로 다른 부분 문자열의 개수](https://www.acmicpc.net/problem/11478)


```python
s = str(input())
ls = []

#string 슬라이싱
for i in range(0, len(s)+1):
    for j in range(len(s)+1,0,-1):
        ls.append(s[i:j])

#중복값 제거 및 공백 제거
ls = set(list(filter(None, ls)))
print(len(ls))

```


-----
