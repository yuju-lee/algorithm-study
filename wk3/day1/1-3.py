#이렇게 썼더니 시간초과나서
k, l = map(int, input().split())
cnt = 0

#l이 소수인지 확인
#l이 소수가 아닐 경우
i = 1
while i < k/l:
    i += 1
    if i*l == k:
        cnt += 1
        break
    

if 0 < cnt:
    print("GOOD")
else:
    print(f"BAD {i}")

#기능 쪼갬
#1600ms
def checkprime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

#기능쪼개기
def smallestprime(k, limit):
    for i in range(2, limit):
        if checkprime(i) and k % i == 0:
            return i
    return None

k, limit = map(int, input().split())

smallest = smallestprime(k, limit)

if smallest is None:
    print("GOOD")
else:
    print(f"BAD {smallest}")