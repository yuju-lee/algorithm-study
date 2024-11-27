#44ms
def findbesthanjo(hanjos):
    maxhanjo = 0
    cnt = 0  # 초기 cnt 설정
    total = []
    for hanjo in hanjos:

        if maxhanjo < hanjo:
            maxhanjo = hanjo
            cnt = 0  
        else:
            cnt += 1
        total.append(cnt)

    return max(total)

n = int(input())
hanjos = list(map(int, input().split()))

print(findbesthanjo(hanjos))
