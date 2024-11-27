#44ms
from itertools import permutations

cardcnt = int(input())
k = int(input())
cards = []
for _ in range(cardcnt):
    card = int(input())
    cards.append(card)

strset = set()

for deck in permutations(cards, k):
    strdeck = "".join(map(str, deck))
    strset.add(strdeck)

print(len(strset))
