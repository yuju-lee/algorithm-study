#772ms
cardcnt = int(input()) #숫자카드 갯수
card = list(map(int, input().split()))

numcnt = int(input())
number = list(map(int, input().split()))

dic = {}

for i in range(cardcnt):
    dic.setdefault(card[i], 1)

for j in range(numcnt):
    print(dic.get(number[j], 0), end=" ")
               