#44ms
n = int(input())
dic=[] #리스트

for cnt in range(n):
    s = str(input())
    dic.append(s)

for i in range(len(dic)):
    rev = dic[i]
    if rev[::-1] in dic:
        ans = dic[i]
        break

print(len(ans), ans[(len(ans)//2)])
