#4188ms
def findmaxmeeting(meetinglist):
    #끝나는 시간 순서로 정렬하고 시작 시간을 정의
    meetinglist.sort(key= lambda x: (x[1], x[0]))
    #결과저장배열 초기화
    finish = 0
    cnt = 0
    for start, end in meetinglist:
        if start >= finish:
            cnt += 1
            finish = end

    return cnt

meetingcnt = int(input())
meetinglist = []

for _ in range(meetingcnt):
    start, end = map(int, input().split())
    meetinglist.append((start, end))

print(findmaxmeeting(meetinglist))