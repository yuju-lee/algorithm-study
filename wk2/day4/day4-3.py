#3028ms
def findrunscore(ls): 
    newls = max(ls[0:2])
    return newls

def findtrickscore(ls):
    newls = ls[2:]
    newls.sort(reverse=True)
    return newls[0:2]


playercnt = int(input())
maxscore = 0
    
for _ in range(playercnt):
    score = list(map(int, input().split()))

    runscore = findrunscore(score)
    trickscore = findtrickscore(score)
    
    if maxscore < runscore + sum(trickscore):
        maxscore = runscore + sum(trickscore)

print(maxscore)