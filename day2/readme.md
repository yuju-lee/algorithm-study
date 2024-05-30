# 2일차 알고리즘 문제해결

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

## 시간복잡도의 문제해결 단계
- O(1): 상수 시간 : 문제를 해결하는데 오직 한 단계만 처리함.
- O(log n): 로그 시간 : 문제를 해결하는데 필요한 단계들이 연산마다 특정 요인에 의해 줄어듬.
- O(n): 직선적 시간 : 문제를 해결하기 위한 단계의 수와 입력값 n이 1:1 관계를 가짐.
- O(n log n): 문제를 해결하기 위한 단계의 수가 N*(log2N) 번만큼의 수행시간을 가진다. (선형로그형)
- O(n^2): 2차 시간 : 문제를 해결하기 위한 단계의 수는 입력값 n의 제곱.
- O(C^n): 지수 시간 : 문제를 해결하기 위한 단계의 수는 주어진 상수값 C 의 n 제곱.


## 시간복잡도 구하기

- 하나의 루프를 사용하여 단일 요소 집합을 반복 하는 경우: O (n)
- 컬렉션의 절반 이상 을 반복 하는 경우: O (n / 2) -> O (n)
- 두 개의 다른 루프를 사용하여 두 개의 개별 콜렉션을 반복 할 경우: O (n + m) -> O (n)
- 두 개의 중첩 루프를 사용하여 단일 컬렉션을 반복하는 경우: O (n²)
- 두 개의 중첩 루프를 사용하여 두 개의 다른 콜렉션을 반복 할 경우: O (n * m) -> O (n²)
- 컬렉션 정렬을 사용하는 경우: O(n*log(n))

## 정렬 알고리즘 비교

<table style="border-collapse: collapse; width: 100%;" border="1" data-ke-align="alignLeft">
<tbody>
<tr>
<td style="width: 28.7209%;"><b>Sorting Algorithms</b></td>
<td style="width: 16.9767%;"><b>공간 복잡도</b></td>
<td style="width: 54.0698%;" colspan="3"><b>시간 복잡도</b></td>
</tr>
<tr>
<td style="width: 28.7209%;">&nbsp;</td>
<td style="width: 16.9767%;"><b>최악</b></td>
<td style="width: 16.8605%;"><b>최선</b></td>
<td style="width: 18.6047%;"><b>평균</b></td>
<td style="width: 18.6047%;"><b>최악</b></td>
</tr>
<tr>
<td style="width: 28.7209%;">Bubble Sort</td>
<td style="width: 16.9767%;" data-text="1">O(1)</td>
<td style="width: 16.8605%;" data-text="3">O(n)</td>
<td style="width: 18.6047%;" data-text="5">O(n2)</td>
<td style="width: 18.6047%;" data-text="5">O(n2)</td>
</tr>
<tr>
<td style="width: 28.7209%;">Heapsort</td>
<td style="width: 16.9767%;" data-text="1">O(1)</td>
<td style="width: 16.8605%;" data-text="4">O(n log n)</td>
<td style="width: 18.6047%;" data-text="4">O(n log n)</td>
<td style="width: 18.6047%;" data-text="4">O(n log n)</td>
</tr>
<tr>
<td style="width: 28.7209%;">Insertion Sort</td>
<td style="width: 16.9767%;" data-text="1">O(1)</td>
<td style="width: 16.8605%;" data-text="3">O(n)</td>
<td style="width: 18.6047%;" data-text="5">O(n2)</td>
<td style="width: 18.6047%;" data-text="5">O(n2)</td>
</tr>
<tr>
<td style="width: 28.7209%;">Mergesort</td>
<td style="width: 16.9767%;" data-text="3">O(n)</td>
<td style="width: 16.8605%;" data-text="4">O(n log n)</td>
<td style="width: 18.6047%;" data-text="4">O(n log n)</td>
<td style="width: 18.6047%;" data-text="4">O(n log n)</td>
</tr>
<tr>
<td style="width: 28.7209%;">Quicksort</td>
<td style="width: 16.9767%;" data-text="2">O(log n)</td>
<td style="width: 16.8605%;" data-text="4">O(n log n)</td>
<td style="width: 18.6047%;" data-text="4">O(n log n)</td>
<td style="width: 18.6047%;" data-text="4">O(n2)</td>
</tr>
<tr>
<td style="width: 28.7209%;">Selection Sort</td>
<td style="width: 16.9767%;" data-text="1">O(1)</td>
<td style="width: 16.8605%;" data-text="5">O(n2)</td>
<td style="width: 18.6047%;" data-text="5">O(n2)</td>
<td style="width: 18.6047%;" data-text="5">O(n2)</td>
</tr>
<tr>
<td style="width: 28.7209%;">Shell Sort</td>
<td style="width: 16.9767%;" data-text="1">O(1)</td>
<td style="width: 16.8605%;" data-text="3">O(n)</td>
<td style="width: 18.6047%;" data-text="6">O(n log n2)</td>
<td style="width: 18.6047%;" data-text="6">O(n log n2)</td>
</tr>
<tr>
<td style="width: 28.7209%;">Smooth Sort</td>
<td style="width: 16.9767%;" data-text="1">O(1)</td>
<td style="width: 16.8605%;" data-text="3">O(n)</td>
<td style="width: 18.6047%;" data-text="4">O(n log n)</td>
<td style="width: 18.6047%;" data-text="4">O(n log n)</td>
</tr>
</tbody>
</table>


## 자료구조 비교
<table style="border-collapse: collapse; width: 100%;" border="1" data-ke-align="alignLeft">
<tbody>
<tr>
<td style="width: 24.0698%;"><b>Data Structures</b></td>
<td style="width: 35.9301%;" colspan="3"><b>Average Case</b></td>
<td style="width: 39.7674%;" colspan="3"><b>Worst Case</b></td>
</tr>
<tr>
<td style="width: 24.0698%;">&nbsp;</td>
<td style="width: 11.9767%;"><b><span>Search</span></b></td>
<td style="width: 11.9767%;"><b>Insert</b></td>
<td style="width: 11.9767%;"><b>Delete</b></td>
<td style="width: 15.814%;"><b><span>Search</span></b></td>
<td style="width: 11.9767%;"><b>Insert</b></td>
<td style="width: 11.9767%;"><b>Delete</b></td>
</tr>
<tr>
<td style="width: 24.0698%;">Array</td>
<td style="width: 11.9767%;">O(n)</td>
<td style="width: 11.9767%;">N/A</td>
<td style="width: 11.9767%;">N/A</td>
<td style="width: 15.814%;">O(n)</td>
<td style="width: 11.9767%;">N/A</td>
<td style="width: 11.9767%;">N/A</td>
</tr>
<tr>
<td style="width: 24.0698%;">Sorted Array</td>
<td style="width: 11.9767%;">O(log n)</td>
<td style="width: 11.9767%;">O(n)</td>
<td style="width: 11.9767%;">O(n)</td>
<td style="width: 15.814%;">O(log n)</td>
<td style="width: 11.9767%;">O(n)</td>
<td style="width: 11.9767%;">O(n)</td>
</tr>
<tr>
<td style="width: 24.0698%;">Linked List</td>
<td style="width: 11.9767%;">O(n)</td>
<td style="width: 11.9767%;">O(1)</td>
<td style="width: 11.9767%;">O(1)</td>
<td style="width: 15.814%;">O(n)</td>
<td style="width: 11.9767%;">O(1)</td>
<td style="width: 11.9767%;">O(1)</td>
</tr>
<tr>
<td style="width: 24.0698%;">Doubly Linked List</td>
<td style="width: 11.9767%;">O(n)</td>
<td style="width: 11.9767%;">O(1)</td>
<td style="width: 11.9767%;">O(1)</td>
<td style="width: 15.814%;">O(n)</td>
<td style="width: 11.9767%;">O(1)</td>
<td style="width: 11.9767%;">O(1)</td>
</tr>
<tr>
<td style="width: 24.0698%;">Stack</td>
<td style="width: 11.9767%;">O(n)</td>
<td style="width: 11.9767%;">O(1)</td>
<td style="width: 11.9767%;">O(1)</td>
<td style="width: 15.814%;">O(n)</td>
<td style="width: 11.9767%;">O(1)</td>
<td style="width: 11.9767%;">O(1)</td>
</tr>
<tr>
<td style="width: 24.0698%;">Hash table</td>
<td style="width: 11.9767%;">O(1)</td>
<td style="width: 11.9767%;">O(1)</td>
<td style="width: 11.9767%;">O(1)</td>
<td style="width: 15.814%;">O(n)</td>
<td style="width: 11.9767%;">O(n)</td>
<td style="width: 11.9767%;">O(n)</td>
</tr>
<tr>
<td style="width: 24.0698%;">Binary Search Tree</td>
<td style="width: 11.9767%;">O(log n)</td>
<td style="width: 11.9767%;">O(log n)</td>
<td style="width: 11.9767%;">O(log n)</td>
<td style="width: 15.814%;">O(n)</td>
<td style="width: 11.9767%;">O(n)</td>
<td style="width: 11.9767%;">O(n)</td>
</tr>
<tr>
<td style="width: 24.0698%;">B-Tree</td>
<td style="width: 11.9767%;">O(log n)</td>
<td style="width: 11.9767%;">O(log n)</td>
<td style="width: 11.9767%;">O(log n)</td>
<td style="width: 15.814%;">O(log n)</td>
<td style="width: 11.9767%;">O(log n)</td>
<td style="width: 11.9767%;">O(log n)</td>
</tr>
<tr>
<td style="width: 24.0698%;">Red-Black tree</td>
<td style="width: 11.9767%;">O(log n)</td>
<td style="width: 11.9767%;">O(log n)</td>
<td style="width: 11.9767%;">O(log n)</td>
<td style="width: 15.814%;">O(log n)</td>
<td style="width: 11.9767%;">O(log n)</td>
<td style="width: 11.9767%;">O(log n)</td>
</tr>
<tr>
<td style="width: 24.0698%;">AVL Tree</td>
<td style="width: 11.9767%;">O(log n)</td>
<td style="width: 11.9767%;">O(log n)</td>
<td style="width: 11.9767%;">O(log n)</td>
<td style="width: 15.814%;">O(log n)</td>
<td style="width: 11.9767%;">O(log n)</td>
<td style="width: 11.9767%;">O(log n)</td>
</tr>
</tbody>
</table>

## 자료형 별 함수의 시간복잡도
<table style="border-collapse: collapse; width: 100%;" border="1" data-ke-align="alignLeft">
<tbody>
<tr>
<td>리스트(List)</td>
<td>- 순서 O, 수정 가능(mutable)</td>
<td>list = [v1, v2, …]</td>
</tr>
<tr>
<td>세트(Set)</td>
<td>- 순서 X, unique, mutable</td>
<td>set = {v1, v2, …}</td>
</tr>
<tr>
<td>딕셔너리(Dictionary)</td>
<td>- 순서 X, 키(immutable), 값(mutable)이 맵핑</td>
<td>dict = {k1:v1, k2:v2, …}</td>
</tr>
</tbody>
</table>

## list 메소드 별 시간복잡도
<table style="border-collapse: collapse; width: 100%;" border="1" data-ke-align="alignLeft">
<tbody>
<tr>
<td style="width: 23.2558%;"><b>&nbsp;Operation</b></td>
<td style="width: 22.907%;"><b>Example</b></td>
<td style="width: 18.4884%;"><b>Big-O</b></td>
<td style="width: 35.2326%;"><b>Notes</b></td>
</tr>
<tr>
<td style="width: 23.2558%;">Index</td>
<td style="width: 22.907%;">l[i]</td>
<td style="width: 18.4884%;">O(1)</td>
<td style="width: 35.2326%;">인덱스로 값 찾기</td>
</tr>
<tr>
<td style="width: 23.2558%;">Store</td>
<td style="width: 22.907%;">l[i] = val</td>
<td style="width: 18.4884%;">O(1)</td>
<td style="width: 35.2326%;">인덱스로 데이터 저장</td>
</tr>
<tr>
<td style="width: 23.2558%;">Length</td>
<td style="width: 22.907%;">len(l)</td>
<td style="width: 18.4884%;">O(1)</td>
<td style="width: 35.2326%;">리스트 길이</td>
</tr>
<tr>
<td style="width: 23.2558%;">Append</td>
<td style="width: 22.907%;">l.append(val)</td>
<td style="width: 18.4884%;">O(1)</td>
<td style="width: 35.2326%;">리스트 뒤에 데이터 추가</td>
</tr>
<tr>
<td style="width: 23.2558%;">Pop</td>
<td style="width: 22.907%;">l.pop()</td>
<td style="width: 18.4884%;">O(1)</td>
<td style="width: 35.2326%;">리스트 마지막 데이터 pop</td>
</tr>
<tr>
<td style="width: 23.2558%;">Clear</td>
<td style="width: 22.907%;">l.clear()</td>
<td style="width: 18.4884%;">O(1)</td>
<td style="width: 35.2326%;">빈 리스트로 만듬</td>
</tr>
<tr>
<td style="width: 23.2558%;">Slice</td>
<td style="width: 22.907%;">l[a:b]</td>
<td style="width: 18.4884%;">O(b-a)</td>
<td style="width: 35.2326%;">슬라이싱</td>
</tr>
<tr>
<td style="width: 23.2558%;">Extend</td>
<td style="width: 22.907%;">l.extend(l2)</td>
<td style="width: 18.4884%;">O(len(l2))</td>
<td style="width: 35.2326%;">리스트 확장</td>
</tr>
<tr>
<td style="width: 23.2558%;">Construction</td>
<td style="width: 22.907%;">list(…)</td>
<td style="width: 18.4884%;">O(len(…))</td>
<td style="width: 35.2326%;">리스트 생성</td>
</tr>
<tr>
<td style="width: 23.2558%;">check ==, !=</td>
<td style="width: 22.907%;">l1 == l2</td>
<td style="width: 18.4884%;">O(N)</td>
<td style="width: 35.2326%;">&nbsp;</td>
</tr>
<tr>
<td style="width: 23.2558%;">Insert</td>
<td style="width: 22.907%;">l[a:b] = …</td>
<td style="width: 18.4884%;">O(N)</td>
<td style="width: 35.2326%;">데이터 삽입</td>
</tr>
<tr>
<td style="width: 23.2558%;">Delete</td>
<td style="width: 22.907%;">del l[i]</td>
<td style="width: 18.4884%;">O(N)</td>
<td style="width: 35.2326%;">데이터 삭제</td>
</tr>
<tr>
<td style="width: 23.2558%;">Containment</td>
<td style="width: 22.907%;">x in/not in l</td>
<td style="width: 18.4884%;">O(N)</td>
<td style="width: 35.2326%;">x값 포함 여부 확인</td>
</tr>
<tr>
<td style="width: 23.2558%;">Copy</td>
<td style="width: 22.907%;">l.copy()</td>
<td style="width: 18.4884%;">O(N)</td>
<td style="width: 35.2326%;">리스트 복제</td>
</tr>
<tr>
<td style="width: 23.2558%;">Remove</td>
<td style="width: 22.907%;">l.remove(val)</td>
<td style="width: 18.4884%;">O(N)</td>
<td style="width: 35.2326%;">리스트에서 val값 제거</td>
</tr>
<tr>
<td style="width: 23.2558%;">Pop 2</td>
<td style="width: 22.907%;">l.pop(i)</td>
<td style="width: 18.4884%;">O(N)</td>
<td style="width: 35.2326%;">i번째 인덱스 값 pop</td>
</tr>
<tr>
<td style="width: 23.2558%;">Extreme value</td>
<td style="width: 22.907%;">min(l) / max(l)</td>
<td style="width: 18.4884%;">O(N)</td>
<td style="width: 35.2326%;">전체 데이터를 체크해야함</td>
</tr>
<tr>
<td style="width: 23.2558%;">Reverse</td>
<td style="width: 22.907%;">l.reverse()</td>
<td style="width: 18.4884%;">O(N)</td>
<td style="width: 35.2326%;">뒤집기</td>
</tr>
<tr>
<td style="width: 23.2558%;">Iteration</td>
<td style="width: 22.907%;">for v in l:</td>
<td style="width: 18.4884%;">O(N)</td>
<td style="width: 35.2326%;">&nbsp;</td>
</tr>
<tr>
<td style="width: 23.2558%;">Sort</td>
<td style="width: 22.907%;">l.sort()</td>
<td style="width: 18.4884%;">O(N log N)</td>
<td style="width: 35.2326%;">파이썬 기본 정렬</td>
</tr>
<tr>
<td style="width: 23.2558%;">Multiply</td>
<td style="width: 22.907%;">k*l</td>
<td style="width: 18.4884%;">O(k N)</td>
<td style="width: 35.2326%;">&nbsp;</td>
</tr>
</tbody>
</table>


## set 메소드 별 시간복잡도
<table style="border-collapse: collapse; width: 100%;" border="1" data-ke-align="alignLeft">
<tbody>
<tr>
<td style="width: 23.1395%;"><b>&nbsp;Operation</b></td>
<td style="width: 21.3953%;"><b>Example</b></td>
<td style="width: 24.186%;"><b>Big-O</b></td>
<td style="width: 31.1628%;"><b>Notes</b></td>
</tr>
<tr>
<td style="width: 23.1395%;">Add</td>
<td style="width: 21.3953%;">s.add(val)</td>
<td style="width: 24.186%;">O(1)</td>
<td style="width: 31.1628%;">집합 요소 추가</td>
</tr>
<tr>
<td style="width: 23.1395%;">Containment</td>
<td style="width: 21.3953%;">x in/not in s</td>
<td style="width: 24.186%;">O(1)</td>
<td style="width: 31.1628%;">포함 여부 확인</td>
</tr>
<tr>
<td style="width: 23.1395%;">Remove</td>
<td style="width: 21.3953%;">s.remove(val)</td>
<td style="width: 24.186%;">O(1)</td>
<td style="width: 31.1628%;">요소 제거(없으면 에러)</td>
</tr>
<tr>
<td style="width: 23.1395%;">Discard</td>
<td style="width: 21.3953%;">s.discard(val)</td>
<td style="width: 24.186%;">O(1)</td>
<td style="width: 31.1628%;">요소 제거(없어도 에러x)</td>
</tr>
<tr>
<td style="width: 23.1395%;">Pop</td>
<td style="width: 21.3953%;">s.pop()</td>
<td style="width: 24.186%;">O(1)</td>
<td style="width: 31.1628%;">랜덤하게 하나 pop</td>
</tr>
<tr>
<td style="width: 23.1395%;">Clear</td>
<td style="width: 21.3953%;">s.clear()</td>
<td style="width: 24.186%;">O(1)</td>
<td style="width: 31.1628%;">&nbsp;</td>
</tr>
<tr>
<td style="width: 23.1395%;">Construction</td>
<td style="width: 21.3953%;">set(…)</td>
<td style="width: 24.186%;">O(len(…))</td>
<td style="width: 31.1628%;">길이만큼</td>
</tr>
<tr>
<td style="width: 23.1395%;">check ==, !=</td>
<td style="width: 21.3953%;">s != t</td>
<td style="width: 24.186%;">O(len(s))</td>
<td style="width: 31.1628%;">&nbsp;</td>
</tr>
<tr>
<td style="width: 23.1395%;">&lt;= or &lt;</td>
<td style="width: 21.3953%;">s &lt;= t</td>
<td style="width: 24.186%;">O(len(s))</td>
<td style="width: 31.1628%;">부분집합 여부</td>
</tr>
<tr>
<td style="width: 23.1395%;">Union</td>
<td style="width: 21.3953%;">s, t</td>
<td style="width: 24.186%;">O(len(s)+len(t))</td>
<td style="width: 31.1628%;">합집합</td>
</tr>
<tr>
<td style="width: 23.1395%;">Intersection</td>
<td style="width: 21.3953%;">s &amp; t</td>
<td style="width: 24.186%;">O(len(s)+len(t))</td>
<td style="width: 31.1628%;">교집합</td>
</tr>
<tr>
<td style="width: 23.1395%;">Difference</td>
<td style="width: 21.3953%;">s - t</td>
<td style="width: 24.186%;">O(len(s)+len(t))</td>
<td style="width: 31.1628%;">차집합</td>
</tr>
<tr>
<td style="width: 23.1395%;">Symmetric Diff</td>
<td style="width: 21.3953%;">s ^ t</td>
<td style="width: 24.186%;">O(len(s)+len(t))</td>
<td style="width: 31.1628%;">여집합</td>
</tr>
<tr>
<td style="width: 23.1395%;">Iteration</td>
<td style="width: 21.3953%;">for v in s:</td>
<td style="width: 24.186%;">O(N)</td>
<td style="width: 31.1628%;">전체 요소 순회</td>
</tr>
<tr>
<td style="width: 23.1395%;">Copy</td>
<td style="width: 21.3953%;">s.copy()</td>
<td style="width: 24.186%;">O(N)</td>
<td style="width: 31.1628%;">&nbsp;</td>
</tr>
</tbody>
</table>


## dict 메소드 별 시간복잡도

<table style="border-collapse: collapse; width: 100%;" border="1" data-ke-align="alignLeft">
<tbody>
<tr>
<td style="width: 23.2558%;"><b>&nbsp;Operation</b></td>
<td style="width: 20.1163%;"><b>Example</b></td>
<td style="width: 17.093%;"><b>Big-O</b></td>
<td style="width: 39.5349%;"><b>Notes</b></td>
</tr>
<tr>
<td style="width: 23.2558%;">Store</td>
<td style="width: 20.1163%;">d[k] = v</td>
<td style="width: 17.093%;">O(1)</td>
<td style="width: 39.5349%;">집합 요소 추가</td>
</tr>
<tr>
<td style="width: 23.2558%;">Length</td>
<td style="width: 20.1163%;">len(d)</td>
<td style="width: 17.093%;">O(1)</td>
<td style="width: 39.5349%;">&nbsp;</td>
</tr>
<tr>
<td style="width: 23.2558%;">Delete</td>
<td style="width: 20.1163%;">del d[k]</td>
<td style="width: 17.093%;">O(1)</td>
<td style="width: 39.5349%;">해당 key 제거</td>
</tr>
<tr>
<td style="width: 23.2558%;">get/setdefault</td>
<td style="width: 20.1163%;">d.get(k)</td>
<td style="width: 17.093%;">O(1)</td>
<td style="width: 39.5349%;">key에 따른 value 확인</td>
</tr>
<tr>
<td style="width: 23.2558%;">Pop</td>
<td style="width: 20.1163%;">d.pop(k)</td>
<td style="width: 17.093%;">O(1)</td>
<td style="width: 39.5349%;">pop</td>
</tr>
<tr>
<td style="width: 23.2558%;">Pop item</td>
<td style="width: 20.1163%;">d.popitem()</td>
<td style="width: 17.093%;">O(1)</td>
<td style="width: 39.5349%;">랜덤 데이터(key:value) pop</td>
</tr>
<tr>
<td style="width: 23.2558%;">Clear</td>
<td style="width: 20.1163%;">d.clear()</td>
<td style="width: 17.093%;">O(1)</td>
<td style="width: 39.5349%;">&nbsp;</td>
</tr>
<tr>
<td style="width: 23.2558%;">View</td>
<td style="width: 20.1163%;">d.keys()</td>
<td style="width: 17.093%;">O(1)</td>
<td style="width: 39.5349%;">key 전체 확인</td>
</tr>
<tr>
<td style="width: 23.2558%;">Values</td>
<td style="width: 20.1163%;">d.values()</td>
<td style="width: 17.093%;">O(1)</td>
<td style="width: 39.5349%;">value 전체 확인</td>
</tr>
<tr>
<td style="width: 23.2558%;">Construction</td>
<td style="width: 20.1163%;">dict(…)</td>
<td style="width: 17.093%;">O(len(…))</td>
<td style="width: 39.5349%;">(key, value) tuple 갯수만큼</td>
</tr>
<tr>
<td style="width: 23.2558%;">Iteration</td>
<td style="width: 20.1163%;">for k in d:</td>
<td style="width: 17.093%;">O(N)</td>
<td style="width: 39.5349%;">딕셔너리 전체 순회</td>
</tr>
</tbody>
</table>