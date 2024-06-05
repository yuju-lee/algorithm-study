adr = str(input())
temp=[]
tempcnt = 0
if '::' in adr:
    ls = adr.split("::")

    for i in range(len(ls)):
        if ':' in ls[i]:
            temp.append(ls[i].split(":"))
        else:
            temp.append(ls[i])

    for j in range(len(temp)):
        tempcnt = len(temp[j]) + tempcnt
    
    skipcnt = 8-tempcnt
    
    skipstr = ("0"*4+":")*skipcnt

    newadr = (":").join(temp[0])+":"+skipstr+(":").join(temp[1])
    
    if newadr[0:1] == ":":
        newadr = newadr[1:]
    if newadr[-1] == ":":
        newadr = newadr[:-1]

    tempadr = newadr.split(":")
    for i in range(len(tempadr)):
        if len(tempadr[i]) != 4:
            new = "0"*(4-len(tempadr[i]))+tempadr[i]
            tempadr[i] = new
    newadr = ":".join(tempadr)


        
else:
    ls = adr.split(":")
    for i in range(len(ls)):
        if len(ls[i]) != 4:
            new = "0"*(4-len(ls[i]))+ls[i]
            ls[i] = new
    newadr = ":".join(ls)

print(newadr)

        
adr = str(input())
temp = []
tempcnt = 0

if '::' in adr:
    ls = adr.split("::")
    
    for part in ls:
        if part:
            temp.append(part.split(":"))
        else:
            temp.append([])
    
    for part in temp:
        tempcnt += len(part)
    
    skipcnt = 8 - tempcnt
    skipstr = ["0"*4] * skipcnt
    newadr = (":".join(temp[0])+":"+":".join(skipstr)+":"+":".join(temp[1])).strip(":")

else:
    ls = adr.split(":")
    for i in range(len(ls)):
        if len(ls[i]) != 4:
            new = "0" * (4 - len(ls[i])) + ls[i]
            ls[i] = new
    newadr = ":".join(ls)

tempadr = newadr.split(":")

for i in range(len(tempadr)):
    if len(tempadr[i]) != 4:
        new = "0" * (4-len(tempadr[i])) + tempadr[i]
        tempadr[i] = new
newadr = ":".join(tempadr)

print(newadr)
