cnt = int(input())

coordinate = list(map(int, input().split()))
sortls = sorted(list(set(coordinate)))

dic = {}

for i in range(len(sortls)):
    dic[sortls[i]] = i

for i in coordinate:
    print(dic[i], end=" ")