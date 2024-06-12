#32ms
from itertools import combinations

word = list(str(input()))
ans = ''

#인덱스 조합 생성해서 그 조합으로 단어 자르기
for i, j in combinations(range(1, len(word)), 2): 
    p1 = word[:i]
    p2 = word[i:j]
    p3 = word[j:]

    #단어 뒤집어서 합치기
    rword = p1[::-1] + p2[::-1] + p3[::-1]

    #각 조합 중 사전상 제일 앞 단어 넣기
    if ans == '' or rword < ans:
        ans = rword

anstr = ''.join(ans)

print(anstr)