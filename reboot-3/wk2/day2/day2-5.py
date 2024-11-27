#40ms / 50점
dic = {}
cnt = 0
for j in range(97, 123): #소문자
    dic.setdefault(chr(j), cnt+1)
    cnt += 1

n = int(input())
s = str(input())
sum = 0

for i in range(n):
    value = dic[s[i]]
    sum += value * 31**i

print(sum % 1234567891)
