from collections import deque

#테스트 케이스의 수
cnt = int(input())

for i in range(cnt):
    #문서의 개수 N / 궁금한 문서의 현재 위치 M
    n, m = map(int, input().split())
    #중요도 리스트 입력
    priorities = list(map(int, input().split()))
    
    #문서의 중요도와 인덱스를 함께 큐에 저장
    queue = deque((priority, idx) for idx, priority in enumerate(priorities))
    order = 0

    while queue:
        #현재 문서의 중요도와 인덱스 추출
        current = queue.popleft()
        #현재 문서보다 높은 중요도의 문서가 있는지 확인
        if any(current[0] < priority for priority, _ in queue):
            #현재 문서를 큐의 끝에 다시 추가
            queue.append(current)
        else:
            order += 1 #현재 문서를 인쇄
            if current[1] == m: #처리된 문서가 처음 요청된 문서인지 확인
                print(order)
                break