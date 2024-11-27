#44ms
matrix = []
maxcharcnt = 0 #최대글자수

# 입력 받기
for i in range(5):
    s = input()
    matrix.append(s)
    if len(s) > maxcharcnt:
        maxcharcnt = len(s)

# 세로로 읽어서 출력하기
for i in range(maxcharcnt):
    for j in range(5):
        if i < len(matrix[j]):
            print(matrix[j][i], end="")