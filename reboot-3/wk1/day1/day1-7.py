#(학점 × 과목평점)의 합을 학점의 총합으로 나눈 값
scoreData = []
for i in range(20):
    inpt = list(map(str,input().split(" ")))    
    scoreData.append(inpt)

score = {
    "A+":4.5,
    "A0":4.0,
    "B+":3.5,
    "B0":3.0,
    "C+":2.5,
    "C0":2.0,
    "D+":1.5,
    "D0":1.0,
    "F":0.0     
         }
credit, sumscore, sumcredit = 0, 0, 0
for i in range(len(scoreData)):
    if scoreData[i][2] == "P":
        pass
    else:
        credit = float(scoreData[i][1]) #학점
        indscore = score[scoreData[i][2]] #평점
        sumscore = sumscore+(credit * indscore)
        sumcredit = sumcredit+credit

print("전공평점:", sumscore/sumcredit)