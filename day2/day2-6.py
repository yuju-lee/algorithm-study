n = int(input())

dic = dict()

for i in range(n):
    name, flag = input().split()
    dic[name] = flag

employee = list([k for k, v in dic.items() if v == 'enter'])

srt = sorted(employee, reverse=True)

for i in range(len(srt)): 
    print(srt[i])

