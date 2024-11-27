#40ms
count, balance = map(int,input().split())
arr = []
for _ in range(count):
    score = int(input())
    arr.append(score)

arr.reverse()

cnt = 0

for price in arr:
    if balance // price > 0:
        cnt = cnt+(balance//price)
        balance = balance - price*(balance//price)
        
print(cnt)
