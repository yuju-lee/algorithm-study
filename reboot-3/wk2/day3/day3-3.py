#376ms
fticketcnt = int(input())
ticket = sorted(list(map(int, input().split())))

ans = 0

for i in range(1, fticketcnt+1):
    if i != ticket[i-1]:
        ans = i
        break

if ans:
    print(ans)
else:
    print(fticketcnt+1)