sensorcnt = int(input())
pointcnt = int(input())

sensors = list(map(int, input().split()))

sensors.sort()
arr = []
for i in range(0, len(sensors)-1):
    dis = sensors[i+1]-sensors[i]
    arr.append(dis)

arr.sort()

print(sum(arr[0:sensorcnt-pointcnt]))
