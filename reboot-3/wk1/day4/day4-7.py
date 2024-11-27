#124ms
n = int(input())

carin = dict()
cnt = 0
fastcar = 0
carout = []

#터널에 들어간 차 번호대로 index 부여 (숫자가 낮을수록 빨리들어간 순)
for i in range(n):
    car = str(input())
    carin.setdefault(car, cnt+1)
    cnt = cnt+1

carindex = list(carin.values())


for j in range(n):
    car = str(input())
    carout.append(carin[car])

carcnt = 0

for k in range(len(carout)-1):

    minindex = min(carout[k+1:len(carout)])

    if carout[k] > minindex:
        carcnt = carcnt + 1

print(carcnt)

    
