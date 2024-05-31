n, m = map(int, input().split())

d = set()
for i in range(n):
    name = str(input())
    d.add(name)

b = set()
for i in range(m):
    name = str(input())
    b.add(name)

s = sorted(d.intersection(b))
print(len(s))
for i in range(len(s)):
    print(s[i])