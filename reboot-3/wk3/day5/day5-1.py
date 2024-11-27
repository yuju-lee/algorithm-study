#256ms
def findnumber(arr):
    minnum = min(arr)
    
    while minnum:
        cnt = 0
        for num in arr:
            if minnum % num == 0:
                cnt += 1
        if cnt >= 3:
            return minnum
        minnum += 1

arr = list(map(int, input().split()))
result = findnumber(arr)
print(result)