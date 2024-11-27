#40ms
def countcoin(price):
    paid = 1000
    cnt = 0

    change = paid - price

    if change == 0:
        return cnt
    
    if change // 500:
        cnt += change // 500
        change = change - (500*(change//500))
    
    if change // 100:
        cnt += change // 100
        change = change - (100*(change//100))
    
    if change // 50:
        cnt += change // 50
        change = change - (50*(change//50))

    if change // 10:
        cnt += change // 10
        change = change - (10*(change//10))

    if change // 5:
        cnt += change // 5
        change = change - (5*(change//5))
    
    if change // 1:
        cnt += change // 1
        change = change - ((change//1))

    return cnt


price = int(input())
print(countcoin(price))


