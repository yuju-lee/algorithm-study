n= int(input())

emoticon = set()
cnt = 0

for i in range(n):
    name = str(input())
    if name != 'ENTER': #enter가 아닐경우
        if name not in emoticon: 
            cnt += 1
            emoticon.add(name)
    else:
        emoticon.clear()

print(cnt)