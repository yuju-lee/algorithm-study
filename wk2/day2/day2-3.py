#216ms

n, m = map(int, input().split()) #아는노래개수 n / 맞히려는 노래 개수 m
dic = dict()

for i in range(n):
    parts = str(input()).split()
    name = parts[1]
    notes = ''.join(parts[2:])

    dic.setdefault(name, notes[0:3])

for j in range(m):
    q = str(input()).replace(' ', '') #ex. CCC
    ansls = [k for k, v in dic.items() if v == q]
    if len(ansls) == 0:
        print("!")
    elif len(ansls) ==1:
        print(ansls[0])
    else:
        print("?")