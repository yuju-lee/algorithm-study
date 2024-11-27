#점수가 최소가 되려면, 같은 수 사이에 다른 수가 없어야함
#11223344 이렇게 되어야 함
#즉, 2N 개의 수열에서 4개의 수를 일렬로 나열하는 경우의 수
#40ms
num = int(input())
cnt = 1

for i in range(1, num+1):
  cnt *= i

print(cnt)
