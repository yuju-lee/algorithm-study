#80ms
def findmincost(n, costs):
    #dp 배열 초기화: 각 집을 R, G, B로 칠할 때의 비용을 저장
    dp = [[0] * 3 for _ in range(n)]
    
    #첫 번째 집의 비용 초기화
    dp[0][0] = costs[0][0]  # R
    dp[0][1] = costs[0][1]  # G
    dp[0][2] = costs[0][2]  # B
    
    #각 집을 R, G, B로 칠할 때의 최소 비용 계산
    #처음 인덱스는 이미 정의를 했기 때문에 1부터 
    for i in range(1, n):
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + costs[i][0]  # R로 칠하는 경우
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + costs[i][1]  # G로 칠하는 경우
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + costs[i][2]  # B로 칠하는 경우
    
    #마지막 집까지 칠한 후, 최소 비용 선택
    return min(dp[n-1][0], dp[n-1][1], dp[n-1][2])

n = int(input())
costs = [list(map(int, input().split())) for _ in range(n)]

# 결과 출력
print(findmincost(n, costs))
