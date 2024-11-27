#4224ms

n = int(input())

dic = {
    'STRAWBERRY':0, 
    'BANANA':0, 
    'LIME':0, 
    'PLUM':0
    }

for i in range(n):
    card, cnt = input().split()
    dic[card] = dic[card]+int(cnt)

if 5 in dic.values(): 
    print('YES')
else: 
    print('NO')