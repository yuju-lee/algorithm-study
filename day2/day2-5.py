#과목 count
subject = int(input())

#점수를 스트링으로 입력받아 공백으로 자르고 리스트 생성
s = str(input()).split(" ")

#리스트를 int형으로 변환하여 score에 할당
score = list(map(int, s))

#최고 점수 추출
maxScore = max(score)

#총합 변수 초기화
sumScore = 0

#각각의 새로운 성적을 계산해 총합 변수에 할당
for i in range(subject):
    score[i] = (score[i]/maxScore)*100
    sumScore += score[i]

#해당 변수를 과목 수로 나누기
print(sumScore/subject)