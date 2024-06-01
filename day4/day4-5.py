#40ms

s = str(input())

dic = ["c=","c-","dz=","d-","lj","nj","s=","z="]

cnt = 0

for i in range(len(s)):
    if s[i:(i+1)+1] in dic:
        cnt = cnt+1
    elif s[i:(i+1)+2] in dic:
         cnt= cnt+1


print(len(s)-cnt)