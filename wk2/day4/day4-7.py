#44ms
def findratio(x, y):
    left = 1
    right = x

    ratio = int((100*y)//x)
    ans = 0
    if 99 <= ratio:
        return -1
    else:
        while left <= right:
            mid = (left+right)//2
            newratio = (y+mid) * 100 // (x+mid)
            if  ratio < newratio:
                ans = mid
                right = mid-1
            else: 
                left = mid+1
                
        
    return ans

x, y = map(int, input().split())
print(findratio(x, y))
