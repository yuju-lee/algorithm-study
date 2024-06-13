#입력받고
#계속 더하면서 100이랑 가까워지는지 확인
#100 넘으면 거기서 멈추고 마지막 점수랑 이전 점수 비교 100에서 빼기 
#뺀 수가 더 작은 수 출력
#뺐는데 똑같으면 더 큰 점수 출력

#40ms
score = 0
mushrooms = []
beforescore = 0
for i in range(10):
    num = input()
    mushrooms.append(int(num))

for mushroom in mushrooms:
    beforescore = score
    score += mushroom
    if score >= 100:
        break

if abs(100 - score) == abs(100 - beforescore):
    print(max(score, beforescore))
elif abs(100 - score) < abs(100 - beforescore):
    print(score)
else:
    print(beforescore)