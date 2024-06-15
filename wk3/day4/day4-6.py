#40ms
num = int(input())

def bags(num):
    for bags in range(num//5, -1, -1):
        sugar = num - (bags*5)
        if sugar % 3 == 0:
            newbags = sugar//3
            return bags + newbags
    return -1

print(bags(num))