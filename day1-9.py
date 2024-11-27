from collections import deque

cnt = int(input())
balloon = list(map(int, input().split())) #풍선에 적힌 이름

result = []
#풍선번호, 인덱스를 큐로 / 인덱스 시작은 1로 시작
queue = deque((number, idx) for idx, number in enumerate(balloon, start=1))

while queue:
    #현재 풍선
    #queue[0]: 풍선번호
    #queue[1]: 풍선인덱스
    n, idx = queue.popleft()
    #터진 풍선의 인덱스 넣기
    result.append(idx)
    
    if n > 0: #양수일경우 -(풍선번호-1) / 왼쪽
        queue.rotate(-(n-1))
    else: #음수일경우 -(-풍선번호) / 오른쪽
        queue.rotate(-n)
    
for i in range(len(result)):
    print(result[i], end=" ")