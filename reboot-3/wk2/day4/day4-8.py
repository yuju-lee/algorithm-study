#80ms
max_height = 0
max_index = 0

# 기둥의 위치와 높이를 저장할 딕셔너리
pillars = {}

# 입력 처리 및 가장 높은 기둥 찾기
for _ in range(int(input())):
    x, height = map(int, input().split())
    pillars[x] = height

    if max_height < height:
        max_index = x
        max_height = height

curr = 0
area = 0

# 왼쪽 부분의 면적 계산
for i in range(max_index + 1):
    if i in pillars:
        curr = max(curr, pillars[i])
    area += curr

curr = 0

# 오른쪽 부분의 면적 계산
for i in range(1000, max_index, -1):
    if i in pillars:
        curr = max(curr, pillars[i])
    area += curr

print(area)
