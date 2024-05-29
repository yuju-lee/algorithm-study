# 테스트케이스만큼 전체 반복 > 가장 바깥 for문
# 입력받는 R값만큼 print S
# S의 글자를 전부 list의 요소로 넣어 해당 요소를 for문으로 R회 반복 출력

t = int(input("")) #테스트 케이스 count

for i in range(t): #케이스 count 만큼 for문 반복
    result = '' #변수 초기화
    r, s = map(str, input("").split()) #반복횟수 int R, 문자열 S값 입력받음
    r = int(r)
    slist = list(map(str,s)) #string -> list 형변환 'add' -> ['a','d','d']
    
    for j in range(len(slist)): #글자수만큼 반복 (글자 하나하나를 전부 list element로 바꾸었기에 list length == 글자수)
        result += slist[j]*r # list 한 요소를 *r 만큼 반복하고 result 변수에 쌓기
    
    print(result)
    
    result='' #다음 테스트케이스를 위해 초기화