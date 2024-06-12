#504ms
from itertools import combinations 

count, sumnum = map(int, input().split())
numbers = list(map(int, input().split()))
ans = 0
for i in range(1, count+1):
    tmp = list(combinations(numbers, i))
    for j in tmp:
        if sum(j) == sumnum:
            ans += 1
print(ans)
