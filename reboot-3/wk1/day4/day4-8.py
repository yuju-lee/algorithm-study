#44ms 50점
def makeIOI(n):
    if n == 1:
        ioi = "IOI"
    else:
        ioi = "IOI"+ "OI"*(n-1)
    return ioi

n = int(input())
s = makeIOI(n)
wordcnt = int(input())
word = str(input())

cnt = 0
for i in range(wordcnt-n):
    if s == word[i:len(s)+i]:
        cnt = cnt+1
print(cnt)

#488ms 100점
def makeIOI(n):
    if n == 1:
        return "IOI"
    else:
        return "IOI" + "OI" * (n - 1)

def computeLPSArray(pattern):
    M = len(pattern)
    lps = [0] * M # LPS 배열 초기화
    length = 0  # 접두사와 접미사가 일치하는 최대 길이
    i = 1  # 패턴의 두 번째 문자부터 시작

    #i가 패턴의 길이보다 작을 때까지 반복
    while i < M:
        #패턴의 현재 문자가 현재 접두사-접미사 최대 길이 다음 문자와 일치하는 경우
        if pattern[i] == pattern[length]:
            length += 1
            #패턴의 i번째 위치까지의 접두사와 접미사가 일치하는 최대 길이를 기록
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            #패턴의 i번째 위치까지의 접두사와 접미사가 일치하지 않음
            else: 
                lps[i] = 0
                i += 1
    return lps

def KMPSearch(pattern, text):
    M = len(pattern)
    N = len(text)
    lps = computeLPSArray(pattern)
    i = 0 #텍스트에서 현재 검사 중인 인덱스
    j = 0 #패턴에서 현재 검사 중인 인덱스
    count = 0

    while i < N:
        # 텍스트와 패턴의 현재 문자(text[i]와 pattern[j])가 일치하면 i와 j를 모두 증가
        if pattern[j] == text[i]:
            i += 1
            j += 1
        #패턴이 발견될 경우 cnt 1 증가
        if j == M:
            count += 1
            #패턴의 다음 검색을 위해 j를 LPS 배열의 이전 값으로 설정
            #(부분 일치한 부분까지 돌아가서 다시 검사)
            j = lps[j - 1]
        elif i < N and pattern[j] != text[i]:
            #j가 0이 아니면 j를 LPS 배열의 이전 값으로 설정
            #부분 일치한 부분까지 돌아가서 다시 검사
            if j != 0:
                j = lps[j - 1]
            else:
                #j가 0이면 i를 증가시켜 텍스트의 다음 문자를 검사
                i += 1
    
    return count

n = int(input())
s = makeIOI(n)
wordcnt = int(input())
word = str(input())

# KMP 알고리즘
result = KMPSearch(s, word)
print(result)