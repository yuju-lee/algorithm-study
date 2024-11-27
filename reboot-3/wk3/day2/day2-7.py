#길이가 2면 걸린 시간도 2로 계산
#큐로 앞+뒤가 최대하중보다 무거워질 때까지 pop
#건너가면 cnt+1
#다 건넌 시간은 길이+1

#68ms
from collections import deque

truckcount, length, weight = map(int, input().split())
trucks = list(map(int, input().split()))

def crossbridge(truckcount, length, weight, trucks):
    time = 0
    bridge = deque([0] * length)  # 다리의 상태를 나타내는 큐
    bridgeweight = 0  # 현재 다리 위의 트럭들의 무게 합
    truckindex = 0  # 현재 대기중인 트럭의 인덱스

    while truckindex < truckcount or bridgeweight > 0:
        time += 1
        # 다리에서 트럭을 한 칸씩 이동
        exitingtruck = bridge.popleft()
        bridgeweight -= exitingtruck

        if truckindex < truckcount:
            # 다음 트럭이 다리에 올라갈 수 있는지 확인
            nextruck = trucks[truckindex]
            if bridgeweight + nextruck <= weight:
                bridge.append(nextruck)
                bridgeweight += nextruck
                truckindex += 1
            else:
                bridge.append(0)  # 다음 트럭이 올라갈 수 없다면 빈 공간 유지

    return time

print(crossbridge(truckcount, length, weight, trucks))