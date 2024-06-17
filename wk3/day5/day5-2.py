first, last = map(int, input().split())

ls = []
for num in range(1, last+1):
    for _ in range(num):
        ls.append(num)

print(sum(ls[first-1:last]))