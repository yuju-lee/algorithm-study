#40ms
s = str(input())
ls = s.split("-")

for i in range((len(s))):
    if 65 <= ord(s[i][0:1]) <= 90:
        print(s[i][0:1], end="")
    else: pass