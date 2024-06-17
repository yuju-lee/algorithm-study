octopus = int(input())

if octopus % 2 == 0:
    ans = '12'*(octopus//2)
    print(' '.join(ans))
else:
    ans = '12'*(octopus//2) +'3' 
    print(' '.join(ans))