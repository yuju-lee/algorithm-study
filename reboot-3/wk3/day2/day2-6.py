#2852ms
def moveturtle(commandline):
    #방향에 따른 x, y 이동 정의
    directions = {
        0: (0, 1),   #북쪽
        1: (1, 0),   #동쪽
        2: (0, -1),  #남쪽
        3: (-1, 0)   #서쪽
    }

    #초기 위치와 방향 (북쪽)
    x, y = 0, 0
    direction = 0

    #이동한 모든 좌표를 저장
    minx = maxx = x
    miny = maxy = y

    for command in commandline:
        if command == 'F':
            x += directions[direction][0]
            y += directions[direction][1]

        elif command == 'B':
            x -= directions[direction][0]
            y -= directions[direction][1]

        elif command == 'L':
            direction = (direction-1) % 4

        elif command == 'R':
            direction = (direction+1) % 4
        
        #최소, 최대 좌표 갱신
        minx = min(minx, x)
        maxx = max(maxx, x)
        miny = min(miny, y)
        maxy = max(maxy, y)
    
    #직사각형의 넓이 계산
    width = maxx - minx
    height = maxy - miny

    return width * height


testcase = int(input())
for _ in range(testcase):
    commandline = input().strip()
    print(moveturtle(commandline))
