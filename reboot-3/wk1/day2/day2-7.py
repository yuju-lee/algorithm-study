n = int(input())

data = dict()

for i in range(n):
    fname, ftype = input().split(".")
    #get()으로 불러와서 +1 / get() -> O(1)
    #get(x, y) = y는 디폴트값
    data[ftype] = data.get(ftype, 0) + 1

#소트 후 딕셔너리 key, value를 리스트로
sortdata = sorted(data.items())

#출력
for i in range(len(sortdata)):
    print(sortdata[i][0], sortdata[i][1])