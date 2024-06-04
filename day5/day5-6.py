def findsize(n, m, ls):
    #작은것부터 큰 정사각형까지 구하기
    size = 1
    #정사각형사이즈를 키워가면서 배열 순회하고 max 크기 설정
    for i in range(n):
        for j in range(m):
            curr = ls[i][j] #현재값(비교대상)
            for x in range(1, min(n-i, m-j)):
                if curr == ls[i][j+x] and curr == ls[i+x][j] and curr == ls[i+x][j+x]:
                        size = max(size, x+1)
    return size*size
                        
                        
n, m = map(int, input().split())
ls = []
for i in range(n):
    s = str(input())
    ls.append(s)
print(findsize(n, m, ls))
