# 56ms
def setList(n):
    ls = []

    for i in range(n): 
        ls.append(str(input()))
    
    return ls

n = int(input()) #입력갯수
word = setList(n)

m = int(input()) #후보입력갯수
temp = setList(m)

#후보단어의 리스트에서 입력 단어와의 중복 제거
wordset = set(word)
candidate = [item for item in temp if item not in wordset]

if 1 < len(word):
    for i in range(len(word)):
        if word[i] == "?":
            if i == 0: #?가 처음이면 다음글자의 첫번째만 글자가 들어감
                lastchr = ''
                nextchr = word[i+1][0:1] #다음단어의 첫번째글자

            elif i == (len(word)-1): #?가 마지막이면 이전글자의 마지막만 글자가 들어감
                lastchr = word[i-1][-1:] #이전단어의 마지막글자
                nextchr = ''
            else:
                lastchr = word[i-1][-1:] #이전단어의 마지막글자
                nextchr = word[i+1][0:1] #다음단어의 첫번째글자
        else:
            pass
else:
    pass

if 1 < len(candidate):
    for j in range(len(candidate)):
        if 1 < len(candidate):
            if lastchr == '' and candidate[j][-1:] == nextchr:
                print(candidate[j])
                break
            elif nextchr == '' and candidate[j][0:1] == lastchr:
                print(candidate[j])
                break
            elif candidate[j][0:1] == lastchr and candidate[j][-1:] == nextchr:
                print(candidate[j])
                break
        else:
            print(candidate[j])
            break
else:
    print(candidate[0])