#84ms
citycount = int(input())
budgets = list(map(int, input().split()))
total = int(input())

#모든 도시의 예산 총합이 총 예산보다 작거나 같을 경우 최대 예산 출력
if sum(budgets) <= total:    
    print(max(budgets))

else:
    budgets.sort()
    left = 0
    right = max(budgets)

    while left <= right:
        mid = (left + right) // 2 
        find = 0
        
        #현재 중간 값(mid)으로 모든 도시의 예산을 계산하여 합산
        for budget in budgets:
            find += min(budget, mid)
            
        #합산한 예산이 총 예산 이하일 경우
        if find <= total:
            left = mid + 1
        else:
            #합산한 예산이 총 예산을 초과할 경우, right 값 감소
            right = mid - 1

    print(right)