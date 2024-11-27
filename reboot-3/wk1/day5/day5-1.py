#48ms
def setMatrix(n):
    outls = []
    for i in range(n):
        matrix = list(map(str,input().split()))
        outls.append(matrix)

    return outls

n, m = list(map(int,input().split()))
aMatrix = setMatrix(n)
bMatrix = setMatrix(n)

for i in range(len(aMatrix)):
    for j in range(len(aMatrix[i])):
        print(int(aMatrix[i][j])+int(bMatrix[i][j]), end=" ")
    print()