#48ms
def findnum(n):
    total = n
    while n > 0:
        total += n%10
        n //= 10
    return total

num = set()

for i in range(1, 10001):
    num.add(findnum(i))

for i in range(1, 10001):
    if i not in num:
        print(i)