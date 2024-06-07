#44ms
personcnt = int(input())
time = list(map(int, input().split()))

time.sort()

for i in range(1, personcnt):
    time[i] += time[i-1]

print(sum(time))

