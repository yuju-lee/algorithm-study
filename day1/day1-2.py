# 규칙
# 같은 눈이 3개가 나오면 10,000원+(같은 눈)×1,000원의 상금을 받게 된다.
# 같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)×100원의 상금을 받게 된다.
# 모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)×100원의 상금을 받게 된다.

# 각 규칙마다 분기 두기
# 같은 눈이 나오는 경우를 가장 큰 분기로 두고 출력값(상금계산) 설정

while(1):
    a, b, c = map(int, input().split())
    if 1<=a<=6 and 1<=b<=6 and 1<=c<=6: break #문제에서 제시한 조건을 입력 시 while문 탈출 후 다음 If구문 실행

if a==b==c: price = 10000+(a*1000) #3개가 같을 경우
elif a==b or b==c or a==c: #2개가 같을 경우
    if a==b or a==c: price = 1000+(a*100) #a를 기준으로 a / b,c 비교하기 (or: 두 조건 중 하나만 만족해도 됨)
    elif b==c: price = 1000+(b*100) #b를 기준으로 c와 비교
else: #값이 다 다를 경우
    if a > b and a > c: topnum = a #a가 가장 큰 값일 경우 topnum 변수에 a값 할당
    elif b > a and b > c: topnum = b #b가 가장 큰 값일 경우 topnum 변수에 b값 할당
    elif c > a and c > a: topnum = c #c가 가장 큰 값일 경우 topnum 변수에 c값 할당
    price = topnum*100

print(price) #최종 price 출력