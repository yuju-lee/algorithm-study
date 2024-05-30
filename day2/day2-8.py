s = str(input())
ls = []

#string 슬라이싱
for i in range(0, len(s)+1):
    for j in range(len(s)+1,0,-1):
        ls.append(s[i:j])

#중복값 제거 및 공백 제거
ls = set(list(filter(None, ls)))
print(len(ls))