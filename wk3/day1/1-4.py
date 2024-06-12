#36ms
testcase = int(input())

for _ in range(testcase):
    candidate = []
    late = 0
    time = int(input())
    while late < time:
        if late + (late * late) <= time:
            candidate.append(late)
        late += 1

    print(max(candidate))