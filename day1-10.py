from collections import deque

def solution(n, apples, directions):
    # 방향: 동(0), 남(1), 서(2), 북(3) -> 처음에 오른쪽을 향하니 동쪽이 0 이후 시계방향으로 1 2 3
    dx = [0, 1, 0, -1]  # x축 이동
    dy = [1, 0, -1, 0]  # y축 이동
    
    board = [[0] * (n + 1) for _ in range(n + 1)]
    # 사과 두기
    for x, y in apples:
        board[x][y] = 1
    
    # init
    x, y = 1, 1
    direction = 0 
    time = 0
    
    # 뱀의 몸 위치를 저장하는 큐
    snake = deque([(1, 1)])  # (x, y) 형식의 좌표값
    
    # 방향 변환 정보를 딕셔너리로 변환
    dir_changes = {t: d for t, d in directions}
    
    while True:
        time += 1
        
        # 다음 위치 계산하기
        nx = x + dx[direction]
        ny = y + dy[direction]
        
        # 벽이나 자기 자신과 부딪히는지 확인 로직
        if nx < 1 or nx > n or ny < 1 or ny > n or (nx, ny) in snake:
            break
            
        # 다음 위치로 머리 이동
        snake.append((nx, ny))
        
        # 사과가 있는지 확인
        if board[nx][ny] == 1:
            board[nx][ny] = 0  # 사과 먹기
        else:
            snake.popleft() # 사과가 없으면 꼬리 자르기
        
        # 업데이트
        x, y = nx, ny
        
        # 방향 전환 확인
        if time in dir_changes:
            if dir_changes[time] == 'L':
                direction = (direction - 1) % 4
            else:  # D
                direction = (direction + 1) % 4
    
    return time

N = int(input())  # 보드크기
K = int(input())  # 사과 수

apples = []
for _ in range(K):
    row, col = map(int, input().split())
    apples.append((row, col))

L = int(input())
directions = []
for _ in range(L):
    X, C = input().split()
    directions.append((int(X), C))

result = solution(N, apples, directions)
print(result)