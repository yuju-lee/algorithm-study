#4368ms
treecnt, take = map(int, input().split())
trees = list(map(int, input().split()))

trees.sort()
ans = 0
left = 1
right = max(trees)

while left <= right:
    mid = (left+right)//2
    cnt = 0
    for tree in trees:
        if tree > mid:
            cnt += tree - mid
    
    if cnt >= take:
        ans = mid
        left = mid+1
    else:
        right = mid-1
    
print(ans)