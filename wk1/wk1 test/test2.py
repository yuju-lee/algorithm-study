adr = str(input())
temp = []
tempcnt = 0

def makeadr(adr):
    for i in range(len(adr)):
        if len(adr[i]) != 4:
            new = "0"*(4-len(adr[i]))+adr[i]
            adr[i] = new
    newadr = ":".join(adr)
    return newadr

if '::' in adr:
    ls = adr.split("::")

    for part in ls:
        if part: temp.append(part.split(":"))
        else: temp.append([])
    
    for part in temp:
        tempcnt += len(part)
    
    skipstr = ["0"*4]*(8-tempcnt)
    
    newadr = (":".join(temp[0])+":"+":".join(skipstr)+":"+":".join(temp[1])).strip(":")
    newadr = makeadr(newadr.split(":"))

else:
    newadr = makeadr(adr.split(":"))

print(newadr)
