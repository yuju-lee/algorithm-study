#이렇게 썼는데 틀렸음... 왜지? 로직은 비슷한 것 같은데 ㅠㅠ
milkcount = int(input())
storemilk = list(map(int, input().split()))

#0, 1, 2
order = [0, 1, 2]
cnt = 0
for i in range(len(storemilk)):
    if storemilk[i] - order[i%3] == 0:
        cnt+= 1

print(cnt)

#40ms
milkcount = int(input())
storemilk = list(map(int, input().split()))

cnt = 0
for i in range(len(storemilk)):
    if storemilk[i] == cnt % 3:
        cnt+= 1

print(cnt)