x, y = map(str, input().split())

xr = x[::-1]
yr = y[::-1]

if int(xr) < int(yr): print(int(yr))
else: print(int(xr))