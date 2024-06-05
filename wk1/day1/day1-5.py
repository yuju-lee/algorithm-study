while(1):
    m, d = map(int,input().split())
    if 1<=m<=12 and 1<=d<=31: break

endone = [1,3,5,7,8,10,12]
endzero = [4,6,9,11]
endeight = [2]
days = ['MON','TUE','WED','THU','FRI','SAT','SUN']
daynum = []*31
dic = {}
keys = []

def makekey(i, j):
    key = str(i)+"/"+str(j)
    return key

for i in range(1, 13): #1월부터 12월까지
    if i in endone: #31일로 끝나는 달
        for j in range(1, 32): keys.append(makekey(i, j))
    elif i in endzero: #30일로 끝나는 달
        for j in range(1, 31): keys.append(makekey(i, j))
    else: #28일로 끝나는 달
        for j in range(1, 29): keys.append(makekey(i, j))

for i in range(len(keys)):
    dic.setdefault(keys[i], days[i%7])

setData = str(m)+"/"+str(d)
print(dic[setData])