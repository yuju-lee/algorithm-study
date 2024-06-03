#92ms
n, m = map(int, input().split())

ls = []
for i in range(n):
    s = str(input())
    ls.append(s)

pattern1 = ['WB'*4,'BW'*4]*4 #흰색으로 시작함
pattern2 = ['BW'*4,'WB'*4]*4 #검은색으로 시작함
mincnt = float('inf')
for i in range(n-7):
    for j in range(m-7): #전체 순회
        cnt1, cnt2 = 0, 0
        for x in range(8): #패턴이랑 8개씩 나눈거랑 맞는지 확인
            for y in range(8):
                if ls[i+x][j+y] != pattern1[x][y]:
                    cnt1 += 1
                if ls[i+x][j+y] != pattern2[x][y]:
                    cnt2 += 1
        
        if min(cnt1, cnt2) < mincnt:
            mincnt = min(cnt1, cnt2)

print(mincnt)