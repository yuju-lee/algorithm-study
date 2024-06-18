from collections import defaultdict, deque

def findbest(N, recom):
    frame = deque(maxlen=N)
    studentcount = defaultdict(int)
    stamp = defaultdict(int)

    current = 0
    for student in recom:
        current += 1
        if student in studentcount:
            studentcount[student] += 1
        else:
            if len(frame) >= N:
                #가장 적은 추천 찾기
                mincount = min(studentcount[stu] for stu in frame)
                #가장 오래된 사람
                oldest = min(
                    (stu for stu in frame if studentcount[stu] == mincount),
                    key=lambda stu: stamp[stu]
                )
                #사진 제거
                frame.remove(oldest)
                del studentcount[oldest]
                del stamp[oldest]
            #새로운 학생 추가
            frame.append(student)
            studentcount[student] = 1
            stamp[student] = current

    final = sorted(frame)
    return final

n = int(input())
total = int(input())
recom = list(map(int, input().split()))

result = findbest(n, recom)
print(' '.join(map(str, result)))