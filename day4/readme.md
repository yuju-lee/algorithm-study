# 4일차 알고리즘 문제해결



```python
print(len(input().split()))
```

--------


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



```python
x, y = map(str, input().split())

xr = x[::-1]
yr = y[::-1]

if int(xr) < int(yr): print(int(yr))
else: print(int(xr))
```

--------



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
