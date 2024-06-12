#44ms
from itertools import permutations

time = str(input())
intime = time.split(":")

timeperm = list(permutations(intime, 3))
cnt = 0
for times in timeperm:
    currtime = list(map(int, times))

    hour = currtime[0]
    min = currtime[1]
    sec = currtime[2]
    
    if 0 < hour < 13:
        if min < 60:
            if sec < 60:
                cnt += 1

print(cnt)
