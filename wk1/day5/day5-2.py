# 36ms
matrix = []
for i in range(9):
    ls = list(map(int,input().split()))
    matrix.append(ls)

r, c, maxnum = 0, 0, 0

for i in range(9):
    for j in range(9):
        if maxnum <= matrix[i][j]:
            maxnum = matrix[i][j]
            r = i+1
            c = j+1
print(maxnum)
print(r, c)