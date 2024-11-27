s = str(input()).upper()

ls = list(s)
dic = {} 

#key: 아스키코드, value: 0인 dic 생성
for i in range(65,91): 
    dic.setdefault(i, 0)

#입력받은 글자수대로 카운트
for i in range(len(ls)):
    a = ord(ls[i])
    dic[a] = dic[a] + 1

#dic의 value만 리스트 생성
dicvalues = list(dic.values())

#최대값 구하기
maxdata = max(dicvalues)

#최대값을 가지는 모든 인덱스를 maxindex 리스트로 저장
maxindex = list(filter(lambda x: dicvalues[x] == maxdata, range(len(dicvalues))))

#maxindex의 length값으로 중복 계산해 2개 이상이면 ? 출력
if  1 < len(maxindex):
    print("?")
else:
    print(chr(maxindex[0]+65))