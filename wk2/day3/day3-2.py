#40ms
testcase = int(input())

schls = []
for _ in range(testcase):
    schoolcnt = int(input())
    for _ in range(schoolcnt):
        school, drink = map(str, input().split())
        schls.append([int(drink), school])
    #drink를 오름차순으로
    schls.sort(key=lambda x: (x))
    #스쿨리스트의 마지막 > 두번째 인덱스 출력
    print(schls[-1][1])

