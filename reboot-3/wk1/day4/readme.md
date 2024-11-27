# 4일차 알고리즘 문제해결

### 1️⃣ 2902번: KMP는 왜 KMP일까?

난이도: 브론즈

분류: 문자열

링크: [2902번: KMP는 왜 KMP일까?](https://www.acmicpc.net/problem/2902)

```python
# 44ms

inp = input().split("-")
output = ""

for s in range(len(inp)):
    output += inp[s][0]

print(output)
```

--------

### 2️⃣ 11721번: 열 개씩 끊어 출력하기

난이도: 브론즈

분류: 문자열

링크: [11721번: 열 개씩 끊어 출력하기](https://www.acmicpc.net/problem/11721)


```python
#36ms
s = str(input())
cnt = 0

#10으로 나눈 몫만큼 슬라이싱
for i in range(len(s)//10):
    print(s[cnt:cnt+10])
    cnt = cnt+10

#나머지가 있다면 나머지만큼만 뒤에서 잘라 출력
if 0 < (len(s)%10):
    print(s[-(len(s)%10):])
else:
    pass
```

--------

### 3️⃣ 2745번: 진법 변환

난이도: 브론즈

분류: 구현, 문자열

링크: [2745번: 진법 변환](https://www.acmicpc.net/problem/2745)


```python
#40ms
b, n = list(map(str, input().split()))
n = int(n)
#int(string, 진법) > 특정 n진법인 string을 10진법으로 변환
print(int(b,n))
```

--------

### 4️⃣ 28432번: 끝말잇기

난이도: 실버

분류: 구현, 문자열

링크: [28432번: 끝말잇기](https://www.acmicpc.net/problem/28432)



```python
# 56ms

#리스트 만드는 함수 정의
def setList(n):
    ls = []

    for i in range(n): 
        ls.append(str(input()))
    
    return ls

n = int(input()) #입력갯수
word = setList(n)

m = int(input()) #후보입력갯수
temp = setList(m)

#후보단어의 리스트에서 입력 단어와의 중복 제거 (set으로 변환 후 list 반환)
wordset = set(word)
candidate = [item for item in temp if item not in wordset]

if 1 < len(word): #입력단어가 2개 이상일 경우에만 앞뒤 단어 검사
    for i in range(len(word)):
        if word[i] == "?":
        
		        #?가 첫 단어일 경우 다음 글자의 첫 번째 글자만 확인
            if i == 0: 
                lastchr = '' #이전 글자는 없으므로 비워둠
                nextchr = word[i+1][0:1] #다음 단어의 첫 번째 글자 저장

            #?가 마지막 단어일 경우 이전 글자의 마지막 글자만 확인
            elif i == (len(word)-1): 
                lastchr = word[i-1][-1:] #이전 단어의 마지막 글자 저장
                nextchr = ''
                
            else:
                lastchr = word[i-1][-1:] #이전 단어의 마지막 글자 저장
                nextchr = word[i+1][0:1] #다음 단어의 첫 번째 글자 저장
        else:
            pass
else:
    pass

if 1 < len(candidate): #후보 단어가 2개 이상일 경우에만 조건 확인
    for j in range(len(candidate)):
        if 1 < len(candidate):
            if lastchr == '' and candidate[j][-1:] == nextchr:
                print(candidate[j])
                break
            elif nextchr == '' and candidate[j][0:1] == lastchr:
                print(candidate[j])
                break
            elif candidate[j][0:1] == lastchr and candidate[j][-1:] == nextchr:
                print(candidate[j])
                break
        else:
            print(candidate[j])
            break
#입력 단어가 1개일 경우 무조건 "?" 입력
#이 경우는 후보 단어도 무조건 1개 (후보 단어는 문제의 답이 정확히 하나인 경우만 입력 받음) 
#후보 단어 1개를 답으로 출력
else: 
    print(candidate[0])
```

--------

### 5️⃣ 2941번: 크로아티아 알파벳

난이도: 실버

분류: 문자열

링크: [크로아티아 알파벳](https://www.acmicpc.net/problem/2941)


```python
#40ms

s = str(input())

#최대 3글자까지 한 단어로 취급
dic = ["c=","c-","dz=","d-","lj","nj","s=","z="]

cnt = 0

for i in range(len(s)):
		#i부터 2글자로 자른 슬라이스에서 dic 단어가 있을 경우 카운트 +1
    if s[i:(i+1)+1] in dic:
        cnt = cnt+1
		#i부터 3글자로 자른 슬라이스에서 dic 단어가 있을 경우 카운트 +1
    elif s[i:(i+1)+2] in dic:
         cnt= cnt+1

#전체 글자수 - 크로아티아 단어 수
print(len(s)-cnt)
```
--------

### 6️⃣ 1213번: 팰린드롬 만들기

난이도: 실버

분류: 문자열

링크: [1213번: 팰린드롬 만들기](https://www.acmicpc.net/problem/1213)


```python
#68ms

# 글자수가 짝수일 때 모든 문자가 짝수 빈도를 가져야 하고,
# 글자수가 홀수일 때 홀수 빈도를 가지는 문자는 딱 하나여야 함
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
    
    # 반쪽 + 중앙 문자(짝수인경우 없음) + 반쪽
    half_str = "".join(half)
    palindrome = half_str + midchr + half_str[::-1]
    print(palindrome)
else:
    print("I'm Sorry Hansoo")
```

--------

### 7️⃣ 2002번: 추월

난이도: 실버

분류: 문자열, 해시 맵 (딕셔너리)

링크: [2002번: 추월](https://www.acmicpc.net/problem/2002)


```python
#124ms
n = int(input())

carin = dict()
cnt = 0
fastcar = 0
carout = []

#터널에 들어간 차 번호대로 index 부여 (숫자가 낮을수록 빨리들어간 순)
for i in range(n):
    car = str(input())
    carin.setdefault(car, cnt+1)
    cnt = cnt+1

carindex = list(carin.values())


for j in range(n):
    car = str(input())
    carout.append(carin[car])

carcnt = 0

for k in range(len(carout)-1):

    minindex = min(carout[k+1:len(carout)])

    if carout[k] > minindex:
        carcnt = carcnt + 1

print(carcnt)
```

--------

### 8️⃣ 5525번: IOIOI

난이도: 실버

분류: 문자열

링크: [5525번: IOIOI](https://www.acmicpc.net/problem/5525)


```python
#44ms 50점
def makeIOI(n):
    if n == 1:
        ioi = "IOI"
    else:
        ioi = "IOI"+ "OI"*(n-1)
    return ioi

n = int(input())
s = makeIOI(n)
wordcnt = int(input())
word = str(input())

cnt = 0
for i in range(wordcnt-n):
    if s == word[i:len(s)+i]:
        cnt = cnt+1
print(cnt)

#############################################################
#488ms 100점
def makeIOI(n):
    if n == 1:
        return "IOI"
    else:
        return "IOI" + "OI" * (n - 1)

def computeLPSArray(pattern):
    M = len(pattern)
    lps = [0] * M # LPS 배열 초기화
    length = 0  # 접두사와 접미사가 일치하는 최대 길이
    i = 1  # 패턴의 두 번째 문자부터 시작

    #i가 패턴의 길이보다 작을 때까지 반복
    while i < M:
        #패턴의 현재 문자가 현재 접두사-접미사 최대 길이 다음 문자와 일치하는 경우
        if pattern[i] == pattern[length]:
            length += 1
            #패턴의 i번째 위치까지의 접두사와 접미사가 일치하는 최대 길이를 기록
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            #패턴의 i번째 위치까지의 접두사와 접미사가 일치하지 않음
            else: 
                lps[i] = 0
                i += 1
    return lps

def KMPSearch(pattern, text):
    M = len(pattern)
    N = len(text)
    lps = computeLPSArray(pattern)
    i = 0 #텍스트에서 현재 검사 중인 인덱스
    j = 0 #패턴에서 현재 검사 중인 인덱스
    count = 0

    while i < N:
        # 텍스트와 패턴의 현재 문자(text[i]와 pattern[j])가 일치하면 i와 j를 모두 증가
        if pattern[j] == text[i]:
            i += 1
            j += 1
        #패턴이 발견될 경우 cnt 1 증가
        if j == M:
            count += 1
            #패턴의 다음 검색을 위해 j를 LPS 배열의 이전 값으로 설정
            #(부분 일치한 부분까지 돌아가서 다시 검사)
            j = lps[j - 1]
        elif i < N and pattern[j] != text[i]:
            #j가 0이 아니면 j를 LPS 배열의 이전 값으로 설정
            #부분 일치한 부분까지 돌아가서 다시 검사
            if j != 0:
                j = lps[j - 1]
            else:
                #j가 0이면 i를 증가시켜 텍스트의 다음 문자를 검사
                i += 1
    
    return count

n = int(input())
s = makeIOI(n)
wordcnt = int(input())
word = str(input())

# KMP 알고리즘
result = KMPSearch(s, word)
print(result)
```

-----

- KMP(Knuth-Morris-Pratt) 알고리즘
    - **KMP 알고리즘**이란: 문자열 검색 알고리즘 중 하나로, 주어진 텍스트에서 패턴을 효율적으로 찾기 위해 사용된다. 이 알고리즘은 패턴을 텍스트에서 빠르게 검색하기 위해 미리 패턴에 대한 정보를 계산하고 활용할 수 있다. 시간 복잡도는 **`O(n + m)`**으로, 여기서 **`n`**은 텍스트의 길이, **`m`**은 패턴의 길이이다.
    - **KMP 알고리즘**은 두 가지 주요 단계로 구성:
        1. **전처리 단계**: 패턴에 대해 LPS(Longest Prefix which is also Suffix) 배열을 계산
        2. **검색 단계**: LPS 배열을 사용하여 패턴을 텍스트에서 효율적으로 검색
    - **KMP 알고리즘의 장점**
        - **효율성**: LPS 배열을 사용하여 중복된 비교를 피하고, 불필요한 텍스트 비교를 줄일 수 있다
        - **선형 시간 복잡도**: KMP 알고리즘의 시간 복잡도는 **`O(n + m)`**으로, 텍스트와 패턴의 길이에 선형적으로 비례함