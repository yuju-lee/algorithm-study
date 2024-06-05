#40ms
b, n = list(map(str, input().split()))
n = int(n)
#int(string, 진법) > 특정 n진법인 string을 10진법으로 변환
print(int(b,n))
