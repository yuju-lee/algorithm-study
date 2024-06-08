import heapq

population = int(input())

ls = []

for _ in range(population):
    votecnt = int(input())
    ls.append(votecnt)

dasom = ls[0]
candidate = ls[1:]

#후보자 표를 최대 힙으로 변환
candidate = [-x for x in candidate]
heapq.heapify(candidate) #??
cnt = 0

#유일한 후보자일 경우
if population == 1:
    print(0)
else:
    while candidate and dasom <= -candidate[0]:
        #최대 힙에서 가장 큰 값을 가져와 1 감소시키기
        maxvote = -heapq.heappop(candidate)
        maxvote -= 1
        dasom += 1
        cnt += 1
        #수정된 값을 다시 힙에 삽입
        heapq.heappush(candidate, -maxvote)

    print(cnt)