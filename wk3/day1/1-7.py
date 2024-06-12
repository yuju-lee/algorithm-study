#36ms
def pos2xy(pos):
    return ord(pos[0]) - 65, int(pos[1]) - 1

def xy2pos(x, y):
    return chr(x + 65) + str(y + 1)

dic = {
    'R': [1, 0],
    'L': [-1, 0],
    'B': [0, -1],
    'T': [0, 1],
    'RT': [1, 1],
    'LT': [-1, 1],
    'RB': [1, -1],
    'LB': [-1, -1]
}

kingpos, rockpos, movecnt = input().split()
movecnt = int(movecnt)

# 초기위치 > 좌표변경
kx, ky = pos2xy(kingpos)
rx, ry = pos2xy(rockpos)

for _ in range(movecnt):
    move = input().strip()
    dx, dy = dic[move]
    
    #킹의 새 위치
    finalkx, finalky = kx + dx, ky + dy
    
    #킹이 체스판을 벗어나지 않을 때
    if 0 <= finalkx < 8 and 0 <= finalky < 8:
        #돌의 위치와 같아지면 돌도 이동
        if finalkx == rx and finalky == ry:
            finalrx, finalry = rx + dx, ry + dy
            #돌이 체스판을 벗어나지 않으면
            if 0 <= finalrx < 8 and 0 <= finalry < 8:
                kx, ky = finalkx, finalky
                rx, ry = finalrx, finalry
        else:
            kx, ky = finalkx, finalky

print(xy2pos(kx, ky))
print(xy2pos(rx, ry))
