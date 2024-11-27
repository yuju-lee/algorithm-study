#144ms
from itertools import combinations

cardnum, limit = map(int, input().split())
cards = list(map(int, input().split()))

cardcombi = list(combinations(cards, 3))

sumls = []

for card in cardcombi:
    deck = list(card)
    if sum(deck) <= limit:
        sumls.append(sum(deck))

print(max(sumls))