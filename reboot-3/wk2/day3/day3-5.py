#40ms
first = []
second = []
for _ in range(3):
    rate, year, lastname = map(str,input().split())
    
    first.append(int(year)%100)
    second.append([int(rate), lastname[0]])
    
    first.sort(key=lambda x: x)
    second.sort(key=lambda x: (x, x), reverse=True)

print(''.join(map(str, first)))

for i in range(len(second)):
    print(second[i][1], end="")