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