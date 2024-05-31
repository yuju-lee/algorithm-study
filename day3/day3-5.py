a1, a0 = map(int,input().split())
c = int(input())
n0 = int(input())

f=(a1*n0)+a0
g = n0 * c

#a1, a0이 음수일 경우를 필터링하기 위해 a1 <= c 조건 추가
if f<=g and a1<=c : print(1)
else: print(0)