def countseat(n, ls):
    cnt = 0
    for i in range(len(ls)):
        #각 행별로 X 개수 세기
        cntX = ls[i].count('X')
        #누울 자리가 하나라도 있는 경우
        if cntX <= n-2:
            #리스트를 문자열로
            s = ''.join(ls[i])
            #만든 문자열을 X 기준으로 잘라서 리스트로
            tmp = s.split('X') 
            #만든 리스트만큼 반복
            for j in range(len(tmp)): 
                if 1 < len(tmp[j]): #2개 이상 연속일 경우
                    cnt = cnt + 1
    return cnt

n = int(input())
ls = []

for i in range(n):
    ls.append(list(str(input())))

#세로 배열 만들기
vls = [list(row) for row in zip(*ls)]

print(countseat(n, ls), countseat(n, vls))