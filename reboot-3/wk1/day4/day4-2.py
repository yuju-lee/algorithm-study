#36ms
s = str(input())
cnt = 0
for i in range(len(s)//10):
    print(s[cnt:cnt+10])
    cnt = cnt+10

if 0 < (len(s)%10):
    print(s[-(len(s)%10):])
else:
    pass