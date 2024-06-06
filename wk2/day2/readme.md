# 1일차 알고리즘 문제해결

### 1️⃣ 17608번: 막대기

난이도: 브론즈

분류: 스택

링크:

[17608번: 막대기](https://www.acmicpc.net/problem/17608)


```python
#100ms
import sys

input = sys.stdin.readline

n = int(input())
h = []
stack = []
cnt = 0

for i in range(n):
    s = int(input())
    h.append(s)

hr = list(reversed(h))

#마지막으로 들어오는 숫자를 기준
last = h[-1]
highest = 0

for j in hr:
    if last <= j and highest < j:
        cnt += 1
        highest = j

print(cnt)
```

--------

### 2️⃣ 12605번: 단어순서 뒤집기

난이도: 브론즈 

분류: 스택 문자열 

링크: 

[12605번: 단어순서 뒤집기](https://acmicpc.net/problem/12605)


```python
#32ms
import sys

input = sys.stdin.readline
cnt = int(input())
ls = []

for i in range(cnt):
    n = list(map(str, input().split()))

    for j in range(len(n)):
        rev = list(reversed(n))
        result = " ".join(rev)

    print(f"Case #{i+1}: {result}")
```

--------

### 3️⃣ 2153번: 소수 단어

난이도 : 브론즈

분류 : 문자열 구현

링크 

[2153번: 소수 단어](https://www.acmicpc.net/problem/2153)


```python
from math import sqrt
s = str(input())

dic = dict()
#dic 만들기
cnt = 0
for j in range(97, 123): #소문자
    dic.setdefault(chr(j), cnt+1)
    cnt += 1
for i in range(65, 91): #대문자
    dic.setdefault(chr(i), cnt+1)
    cnt += 1

#알파벳을 숫자로 바꾸고 그 숫자를 담을 변수
sn = 0

#알파벳을 숫자로 바꾸기
for k in range(len(s)):
    c = s[k]
    sn = dic[c]+sn

def prime(n):
    #1도 소수라는 조건(?)
    if n <= 1: return print("It is a prime word.")
    #2부터 n의 제곱근까지 h로 나눴을 때 나머지가 0인 게 하나라도 있으면 소수 아님 
    for h in range(2, int(sqrt(n)) + 1):
        if n % h == 0:
            return print("It is not a prime word.")
    return print("It is a prime word.")

prime(sn)
```

--------

### 4️⃣ 7567번: 그릇

난이도: 브론즈

분류: 문자열 구현

링크

[7567 번: 그릇](https://www.acmicpc.net/problem/7567)


```python
ls = list(str(input()))
stack = []
score = 0

for i in range(len(ls)):
    #첫번째는 무조건 10점+스택에 저장
    if i == 0:
        score += 10
        stack.append(ls[i])
    
    #현재 글자와 스택의 마지막 값이 다른 경우
    elif stack[-1] !=ls[i]: 
        #스택이 비어있지 않을 경우에만 pop (첫번째에 ')'가 들어오면 안 되니깐)
        if 0 < len(stack): 
            stack.pop()
        score += 10
        #스택 비우고 현재글자(새글자) 추가
        stack.append(ls[i])
    
    #현재 글자와 스택 글자가 같으며 스택에 값이 있는 경우
    elif 0 < len(stack) and stack[-1] == ls[i]:
        score += 5
        stack.append(ls[i])
            
print(score)
```

--------

### 5️⃣ 1966번: 프린터 큐

난이도: 실버

분류: 큐 (덱)

링크: 

[1966번: 프린터 큐](https://www.acmicpc.net/problem/1966)


```python
from collections import deque

#테스트 케이스의 수
cnt = int(input())

for i in range(cnt):
    #문서의 개수 N / 궁금한 문서의 현재 위치 M
    n, m = map(int, input().split())
    #중요도 리스트 입력
    priorities = list(map(int, input().split()))
    
    #문서의 중요도와 인덱스를 함께 큐에 저장
    queue = deque((priority, idx) for idx, priority in enumerate(priorities))
    order = 0

    while queue:
        #현재 문서의 중요도와 인덱스 추출
        current = queue.popleft()
        #현재 문서보다 높은 중요도의 문서가 있는지 확인
        if any(current[0] < priority for priority, _ in queue):
            #현재 문서를 큐의 끝에 다시 추가
            queue.append(current)
        else:
            #현재 문서를 인쇄
            order += 1
            #처리된 문서가 처음 요청된 문서인지 확인
            if current[1] == m:
                print(order)
                break
```
--------

### 6️⃣ 1021번: 회전하는 큐

난이도: 실버

분류: 덱

링크: 

[1021번: 회전하는 큐](https://www.acmicpc.net/problem/1021)


```python
from collections import deque

n, m = map(int, input().split())
pos = list(map(int, input().split())) #뽑아내려는 원소의 위치

#큐의 크기는 n, 뽑는 갯수는 m 
leftcnt = 0
rightcnt = 0
cnt = 0

#큐 만들기
queue = deque(range(1, n+1))

#원소뽑기
for p in pos:
    #현재 큐의 원소 p 위치 (index 사용해서)
    index = queue.index(p)
    #왼쪽으로 움직일때
    left = index
    #오른쪽으로 움직일 때
    right = len(queue)-index

    #왼쪽으로 움직이는게 오른쪽으로 움직이는것보다 적으면 왼쪽으로
    if left <= right:
        queue.rotate(-left) #음수면 왼쪽으로 움직임
        cnt += left
    else: #아니면 오른쪽
        queue.rotate(right)
        cnt += right

    #첫번째 제거
    queue.popleft()

print(cnt)
```

--------

### 7️⃣ 9012번: 괄호

난이도: 실버

분류: 스택

링크: 

[9012번: 괄호](https://www.acmicpc.net/problem/9012)


```python
#56ms
def checkVPS(s):
    stack = []
    for i in range(len(s)):
        #첫 글자가 닫는 괄호면 무조건 no
        if i == 0:
            if s[i] == '(':
                stack.append(s[i])
            else:
                stack.append(s[i])
                break

        else: #2번째부터
            # (는 넣고, )이 들어올 때마다 하나씩 pop
            if s[i] == '(':
                stack.append(s[i])
            else: #닫는 괄호가 들어오면
                if 0 < len(stack):
                    stack.pop()
                else:
                    stack.append(s[i])
                    break
                    
    if len(stack) == 0: return "YES"
    else: return "NO"

cnt = int(input())
ans = []
for i in range(cnt):
    s = str(input())
    ans.append(checkVPS(s))

for j in range(len(ans)):
    print(ans[j])
```

--------

### 8️⃣ 2346번: 풍선 터뜨리기

난이도: 실버

분류: 덱

링크: 

[2346번: 풍선 터뜨리기](https://www.acmicpc.net/problem/2346)


```python
#64ms
from collections import deque

cnt = int(input())
balloon = list(map(int, input().split())) #풍선에 적힌 이름

result = []
#풍선번호, 인덱스를 큐로 / 인덱스 시작은 1로 시작
queue = deque((number, idx) for idx, number in enumerate(balloon, start=1))

while queue:
    #현재 풍선
    #queue[0]: 풍선번호
    #queue[1]: 풍선인덱스
    n, idx = queue.popleft()
    #터진 풍선의 인덱스 넣기
    result.append(idx)
    
    if n > 0: #양수일경우 -(풍선번호-1) / 왼쪽
        queue.rotate(-(n-1))
    else: #음수일경우 -(-풍선번호) / 오른쪽
        queue.rotate(-n)
    
for i in range(len(result)):
    print(result[i], end=" ")
```


-----
