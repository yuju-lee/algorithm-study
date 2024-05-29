import sys
while (1):
		#cn: 국가수 / sn: 등수를 알고 싶은 국가의 번호
    cn, sn = map(int,sys.stdin.readline().split()) 
    if 1<=cn<=1000 and 1<=sn<=cn: break

arr = []
for i in range(cn): #입력값을 2차원 배열로 만들기
    country, gold, silver, bronze = map(int,input("").split())
    temp = [country, gold, silver, bronze]
    arr.append(temp)

scoretemp = []
bestscore = 0
for i in range(len(arr)):
		#가중치 부여하여 점수 총합
    score = (arr[i][1]*20)+(arr[i][2]*10)+(arr[i][3]*5)
    arr[i].append(score)
    scoretemp.append(score)

#총합으로 순위 정하기
rank = []
for i in range(len(scoretemp)):
    rank.append(1)
    for j in range(len(scoretemp)):
        if scoretemp[i] < scoretemp[j]:
            rank[i] = rank[i]+1

for i in range(len(arr)): arr[i].append(rank[i])

for i in range(len(arr)):
    if arr[i][0] == sn:
        print(arr[i][5])