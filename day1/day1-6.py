x = int(input(""))
endnum = 0
box = 0
while(1):
    endnum = endnum+box
    if endnum >= x : 
        break
    box = box+1

prelastnum = endnum - box
xindex = x - prelastnum

if box%2 == 0:
    for i in range(1, box+1): 
        x = i
        y = (box+1)-i
        if i == xindex:
            print(str(x)+"/"+str(y))
            break
else: 
    for i in range(1, box+1): #박스번호
        y = i
        x = (box+1)-i
        if i == xindex:
            print(str(x)+"/"+str(y))
            break