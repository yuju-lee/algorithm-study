#192ms
n = int(input())
a = set((map(int, input().split())))
m = int(input())
b = list(map(int, input().split())) #여기 값이 a에 있는지 확인

for i in range(m):
    if b[i] in a:
        print(1, end=" ")
    else:
        print(0, end=" ")
