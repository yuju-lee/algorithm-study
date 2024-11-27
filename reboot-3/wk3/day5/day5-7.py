#100ms
def findcost(citycount, lengths, prices):
    total = 0
    minprice = prices[0]
    
    for i in range(citycount-1):
        # 현재 도로를 지나기 위한 기름 비용 추가
        total += minprice * lengths[i]
        
        # 만약 현재 주유소의 가격이 더 싸다면 갱신
        if prices[i+1] < minprice:
            minprice = prices[i+1]
    
    return total

citycount = int(input())
lengths = list(map(int, input().split()))
prices = list(map(int, input().split()))

# 최소 비용 계산 및 출력
print(findcost(citycount, lengths, prices))