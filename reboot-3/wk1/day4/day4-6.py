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
    
    # 반쪽을 만들고, 중앙 문자를 넣고, 반쪽을 뒤집어서 붙임
    half_str = "".join(half)
    palindrome = half_str + midchr + half_str[::-1]
    print(palindrome)
else:
    print("I'm Sorry Hansoo")